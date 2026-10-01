"""
Escalation node — handles all cases where the AI hands off to a human.

Triggered by:
    - intent == "escalation"          (user asked for a human)
    - intent == "sensitive_legal"     (legal threats)
    - intent == "sensitive_safety"    (safety incidents)
    - intent == "out_of_scope"        (unrelated requests)

Behavior:
    - Generates a support ticket ID
    - Sets state["escalated"] = True
    - Writes an empathetic handoff message to state["final_response"]
    - Records escalation reason and ticket ID

Updates:
    state["escalated"]
    state["escalation_reason"]
    state["ticket_id"]
    state["final_response"]
"""

from __future__ import annotations

import random
import string
from datetime import datetime, timezone

from src.config import settings
from src.graph.state import AgentState, latest_user_message


# =============================================================================
# TICKET ID GENERATION
# =============================================================================

def _generate_ticket_id() -> str:
    """Generate a support ticket ID like TCK-2026-A1B2C3."""
    year = datetime.now(timezone.utc).year
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"TCK-{year}-{suffix}"


# =============================================================================
# MESSAGE TEMPLATES
# =============================================================================

_MESSAGES = {
    "escalation": (
        "Of course — I'll connect you with a human agent right away. "
        "I've created ticket **{ticket_id}** so they can pick up right where "
        "we left off. A support specialist will reach out within **4 business hours** "
        "(Monday–Friday 9 AM–8 PM EST). "
        "If this is urgent, you can also email support@voltnest.com and mention "
        "your ticket number."
    ),
    "sensitive_legal": (
        "Thank you for letting me know. I've escalated your case to our support "
        "team with ticket **{ticket_id}**. A specialist will respond within "
        "**4 business hours**. Please keep any relevant documents or correspondence "
        "for reference."
    ),
    "sensitive_safety": (
        "Please stop using the product immediately and unplug it if it's safe to do so. "
        "I've escalated this as a priority case with ticket **{ticket_id}** — our safety "
        "team will reach out within **4 business hours**. Please keep the product and "
        "any packaging for inspection."
    ),
    "out_of_scope": (
        "I can only help with VoltNest product, order, and policy questions. "
        "If there's anything about your order or our products I can help with, "
        "just let me know."
    ),
}


# =============================================================================
# NODE
# =============================================================================

def escalation_node(state: AgentState) -> dict:
    """
    LangGraph node: hand off to a human agent.

    Returns partial state with:
        escalated, escalation_reason, ticket_id, final_response
    """
    question = latest_user_message(state)
    intent = state.get("intent") or "escalation"

    # Out-of-scope doesn't create a ticket — just declines
    if intent == "out_of_scope":
        return {
            "escalated": False,
            "escalation_reason": "out_of_scope",
            "ticket_id": None,
            "final_response": _MESSAGES["out_of_scope"],
        }

    # All other escalation types create a ticket
    ticket_id = _generate_ticket_id()

    template = _MESSAGES.get(intent, _MESSAGES["escalation"])
    message = template.format(ticket_id=ticket_id)

    return {
        "escalated": True,
        "escalation_reason": intent,
        "ticket_id": ticket_id,
        "final_response": message,
    }


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    from src.graph.state import initial_state

    print("=" * 70)
    print("Escalation Node Test")
    print("=" * 70)
    print()

    scenarios = [
        ("I want to talk to a human", "escalation"),
        ("My charger caught fire", "sensitive_safety"),
        ("I'm going to sue you", "sensitive_legal"),
        ("Who won the World Cup?", "out_of_scope"),
        ("You're useless, get me a manager", "escalation"),
    ]

    for q, intent in scenarios:
        print(f"Q: {q}  (intent: {intent})")
        state = initial_state(user_message=q)
        state["intent"] = intent
        update = escalation_node(state)
        print(f"   escalated: {update.get('escalated')}")
        print(f"   ticket:    {update.get('ticket_id')}")
        print(f"   answer:    {update.get('final_response', '')[:200]}")
        print()

    print("=" * 70)
    print("[OK] Escalation node works")
    print("=" * 70)