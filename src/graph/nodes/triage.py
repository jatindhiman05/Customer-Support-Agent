"""
Triage node — classifies the user's latest message into one of the
supported intents and decides which specialist node to route to next.

Uses the LLM (GPT-OSS-120B via Groq) with a prompt built from
data/taxonomy/intents.yaml.

Updates:
    state["intent"]
    state["intent_confidence"]
    state["intent_reasoning"]
    state["route"]
"""

from __future__ import annotations

import json
import re
from functools import lru_cache

import yaml
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from src.config import settings
from src.graph.state import AgentState, Intent, RouteName, latest_user_message


# =============================================================================
# LLM CLIENT
# =============================================================================

_triage_llm: ChatGroq | None = None


def _get_triage_llm() -> ChatGroq:
    global _triage_llm
    if _triage_llm is None:
        _triage_llm = ChatGroq(
            model=settings.triage_model,
            api_key=settings.groq_api_key,
            temperature=0,
            max_tokens=600,
            timeout=30.0,
            max_retries=2,
        )
    return _triage_llm


# =============================================================================
# CONFIG LOADING
# =============================================================================

@lru_cache(maxsize=1)
def _load_intents_config() -> dict:
    path = settings.taxonomy_dir / "intents.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@lru_cache(maxsize=1)
def _intents_list() -> list[dict]:
    """Return the list of intent dicts from intents.yaml."""
    return _load_intents_config().get("intents", [])


@lru_cache(maxsize=1)
def _intent_to_route() -> dict[str, str]:
    """Map intent name → route name (e.g., order_status → order_agent)."""
    return {i["name"]: i["routes_to"] for i in _intents_list()}


@lru_cache(maxsize=1)
def _priority_overrides() -> list[dict]:
    return _load_intents_config().get("priority_overrides", [])


# =============================================================================
# PRIORITY OVERRIDES (fast path before LLM)
# =============================================================================

def _check_priority_overrides(query: str) -> tuple[Intent | None, str]:
    """
    Check hardcoded override phrases (e.g., 'talk to a human').

    Returns (intent, matched_phrase) or (None, "").
    """
    lower = query.lower()
    for override in _priority_overrides():
        phrase = override["phrase"].lower()
        if phrase in lower:
            return override["intent"], phrase
    return None, ""


# =============================================================================
# PROMPT
# =============================================================================

_SYSTEM_PROMPT = """You are the triage classifier for a customer support AI at VoltNest (an e-commerce store).

Your job: classify the user's latest message into EXACTLY ONE of the supported intents.

Rules:
- Read the user message carefully.
- Choose the single most specific intent.
- If the message could fit multiple, prefer the more specific one.
- If nothing fits well, use `general`.
- If the user asks something unrelated to VoltNest (sports, coding, medical advice, etc.), use `out_of_scope`.
- If the user expresses strong anger/frustration OR asks for a human, use `escalation`.
- If the user mentions legal action (sue, lawyer, subpoena), use `sensitive_legal`.
- If the user mentions a safety incident (fire, injury, battery swelling, self-harm), use `sensitive_safety`.

You MUST return valid JSON with exactly these keys:
{
  "intent": "<one of the allowed intents>",
  "confidence": <float 0.0 to 1.0>,
  "reasoning": "<one short sentence>"
}

Do NOT include any text outside the JSON."""


def _build_intents_block() -> str:
    """Build the list of allowed intents for the prompt."""
    lines = ["Allowed intents:"]
    for i in _intents_list():
        lines.append(f"- {i['name']}: {i['description']}")
    return "\n".join(lines)


# =============================================================================
# PARSING
# =============================================================================

def _extract_json(raw: str) -> dict | None:
    """Extract the first JSON object from an LLM response."""
    raw = raw.strip()

    # Strip reasoning tags if present
    if "<final>" in raw:
        raw = raw.split("<final>")[-1].split("</final>")[0]
    elif "</reasoning>" in raw:
        raw = raw.split("</reasoning>")[-1]

    # Try code fences first
    fence_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if fence_match:
        try:
            return json.loads(fence_match.group(1))
        except json.JSONDecodeError:
            pass

    # Try first bare { ... }
    brace_match = re.search(r"\{.*\}", raw, re.DOTALL)
    if brace_match:
        try:
            return json.loads(brace_match.group(0))
        except json.JSONDecodeError:
            pass

    return None


# =============================================================================
# VALIDATION
# =============================================================================

def _valid_intents() -> set[str]:
    return {i["name"] for i in _intents_list()}


# =============================================================================
# NODE
# =============================================================================

def triage_node(state: AgentState) -> dict:
    """
    LangGraph node: classify the user's message and set the route.

    Returns a partial state dict with:
        intent, intent_confidence, intent_reasoning, route
    """
    query = latest_user_message(state)
    if not query:
        # No user message? Default to general, don't call the LLM.
        return {
            "intent": "general",
            "intent_confidence": 0.0,
            "intent_reasoning": "No user message found.",
            "route": "general_agent",
        }

    # ---------- Fast path: priority overrides ----------
    override_intent, matched = _check_priority_overrides(query)
    if override_intent:
        route = _intent_to_route().get(override_intent, "general_agent")
        return {
            "intent": override_intent,
            "intent_confidence": 0.99,
            "intent_reasoning": f"Matched override phrase: '{matched}'",
            "route": route,
        }

    # ---------- LLM classification ----------
    llm = _get_triage_llm()
    intents_block = _build_intents_block()

    messages = [
        SystemMessage(content=_SYSTEM_PROMPT),
        HumanMessage(
            content=f"{intents_block}\n\nUser message:\n{query}\n\nReturn JSON only."
        ),
    ]

    try:
        response = llm.invoke(messages)
        raw = getattr(response, "content", str(response))
        parsed = _extract_json(raw)
    except Exception as e:
        # LLM error → safe fallback
        return {
            "intent": "general",
            "intent_confidence": 0.0,
            "intent_reasoning": f"LLM error: {type(e).__name__}",
            "route": "general_agent",
        }

    if not parsed:
        return {
            "intent": "general",
            "intent_confidence": 0.0,
            "intent_reasoning": "Could not parse LLM JSON.",
            "route": "general_agent",
        }

    intent = str(parsed.get("intent", "general")).strip()
    if intent not in _valid_intents():
        intent = "general"

    try:
        confidence = float(parsed.get("confidence", 0.5))
    except (TypeError, ValueError):
        confidence = 0.5

    confidence = max(0.0, min(1.0, confidence))
    reasoning = str(parsed.get("reasoning", ""))[:200]

    route = _intent_to_route().get(intent, "general_agent")

    return {
        "intent": intent,           # type: ignore[typeddict-item]
        "intent_confidence": confidence,
        "intent_reasoning": reasoning,
        "route": route,             # type: ignore[typeddict-item]
    }


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    from src.graph.state import initial_state

    print("=" * 70)
    print("Triage Node Test")
    print("=" * 70)
    print()

    test_queries = [
        "Where is my order ORD-100001?",
        "Can I return earbuds after 45 days?",
        "How do I reset my password?",
        "My VoltBuds won't connect to my phone",
        "I was charged twice for my order",
        "Can I use Klarna for a $40 order?",
        "Do you have student discounts?",
        "I want to talk to a human",
        "My charger caught fire",
        "What does IP67 mean?",
        "Where do you ship to?",
        "My speaker stopped working",
        "How do I change my email?",
        "Do you price match?",
        "The app keeps crashing",
    ]

    for q in test_queries:
        state = initial_state(user_message=q)
        update = triage_node(state)
        intent = update.get("intent", "?")
        route = update.get("route", "?")
        conf = update.get("confidence", update.get("intent_confidence", 0))
        print(f"Q: {q}")
        print(f"   intent:  {intent}  (conf={conf:.2f})")
        print(f"   route:   {route}")
        print(f"   why:     {update.get('intent_reasoning', '')}")
        print()

    print("=" * 70)
    print("[OK] Triage node works")
    print("=" * 70)