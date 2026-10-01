"""
LangGraph agent state schema.

This defines the shared state that flows through every node in the graph.
Each node reads fields it needs, updates fields it produces, and returns
its partial updates. LangGraph merges the updates.

Design:
    - Uses TypedDict for compatibility with LangGraph
    - `messages` uses add_messages so new messages append rather than replace
    - Every field has an explicit type and a default
    - Optional fields use None; required fields are populated by the entry node
"""

from __future__ import annotations

from typing import Annotated, Any, Literal

from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


# =============================================================================
# TYPE ALIASES
# =============================================================================

Intent = Literal[
    "order_status",
    "cancel_order",
    "modify_order",
    "delivery_issue",
    "product_question",
    "warranty_question",
    "tech_support",
    "payment_question",
    "payment_issue",
    "account_help",
    "policy_question",
    "general",
    "escalation",
    "sensitive_legal",
    "sensitive_safety",
    "out_of_scope",
]

RouteName = Literal[
    "order_agent",
    "rag_agent",
    "tech_agent",
    "billing_agent",
    "account_agent",
    "general_agent",
    "human_handoff",
    "sensitive_handler",
    "decline_handler",
]


# =============================================================================
# RETRIEVED DOCUMENT
# =============================================================================

class RetrievedDoc(TypedDict):
    """A single retrieved KB chunk used to ground a response."""
    doc_name: str
    category: str
    heading_path: str
    content: str
    semantic_score: float
    rerank_rank: int


# =============================================================================
# TOOL CALL RESULT
# =============================================================================

class ToolResult(TypedDict, total=False):
    """Result of a tool call (order lookup, refund, ticket)."""
    tool_name: str
    success: bool
    data: dict[str, Any] | None
    error: str | None


# =============================================================================
# AGENT STATE
# =============================================================================

class AgentState(TypedDict, total=False):
    """
    The shared state for the customer support agent.

    Fields:
        messages:            Conversation history (auto-appends)
        user_id:             Optional user identifier
        thread_id:           Conversation thread identifier

        intent:              Classified intent of the latest message
        intent_confidence:   0..1 confidence from the triage node
        intent_reasoning:    Short explanation of why this intent was chosen
        route:               Which specialist node to invoke next

        retrieved_docs:      KB chunks used to ground the response
        retrieval_scores:    Optional raw scores for debugging

        tool_calls:          Tools invoked during this turn
        tool_results:        Results of tool calls

        escalated:           Whether the conversation has been handed to a human
        escalation_reason:   Why escalation was triggered
        ticket_id:           Support ticket ID if one was created

        blocked:             Whether the guardrail blocked the input
        blocked_reason:      Why the input was blocked

        final_response:      The final user-facing response
        response_citations:  Source doc names cited in the response
    """

    # --- Identity -------------------------------------------------------------
    messages: Annotated[list[BaseMessage], add_messages]
    user_id: str | None
    thread_id: str | None

    # --- Triage --------------------------------------------------------------
    intent: Intent | None
    intent_confidence: float
    intent_reasoning: str
    route: RouteName | None

    # --- Retrieval -----------------------------------------------------------
    retrieved_docs: list[RetrievedDoc]
    retrieval_scores: list[float]

    # --- Tools ---------------------------------------------------------------
    tool_calls: list[str]
    tool_results: list[ToolResult]

    # --- Escalation ----------------------------------------------------------
    escalated: bool
    escalation_reason: str | None
    ticket_id: str | None

    # --- Guardrails ----------------------------------------------------------
    blocked: bool
    blocked_reason: str | None

    # --- Final output --------------------------------------------------------
    final_response: str | None
    response_citations: list[str]


# =============================================================================
# INITIAL STATE
# =============================================================================

def initial_state(
    user_message: str,
    user_id: str | None = None,
    thread_id: str | None = None,
) -> AgentState:
    """
    Build a fresh AgentState for a new user turn.

    Args:
        user_message: the raw user message
        user_id: optional user identifier
        thread_id: optional conversation thread identifier

    Returns:
        A fully-initialized AgentState.
    """
    from langchain_core.messages import HumanMessage

    return AgentState(
        messages=[HumanMessage(content=user_message)],
        user_id=user_id,
        thread_id=thread_id,

        intent=None,
        intent_confidence=0.0,
        intent_reasoning="",
        route=None,

        retrieved_docs=[],
        retrieval_scores=[],

        tool_calls=[],
        tool_results=[],

        escalated=False,
        escalation_reason=None,
        ticket_id=None,

        blocked=False,
        blocked_reason=None,

        final_response=None,
        response_citations=[],
    )


# =============================================================================
# HELPERS
# =============================================================================

def latest_user_message(state: AgentState) -> str:
    """Return the most recent user message content as a string."""
    for msg in reversed(state.get("messages", [])):
        if getattr(msg, "type", "") == "human":
            return msg.content if isinstance(msg.content, str) else str(msg.content)
    return ""


def latest_ai_message(state: AgentState) -> str | None:
    """Return the most recent AI message content as a string, if any."""
    for msg in reversed(state.get("messages", [])):
        if getattr(msg, "type", "") == "ai":
            return msg.content if isinstance(msg.content, str) else str(msg.content)
    return None


def add_ai_message(state: AgentState, content: str) -> AgentState:
    """Append an AI message to the state's history."""
    from langchain_core.messages import AIMessage
    return {"messages": [AIMessage(content=content)]}


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Agent State Test")
    print("=" * 70)
    print()

    state = initial_state(
        user_message="Where is my order ORD-100001?",
        user_id="U-5001",
        thread_id="thread-1",
    )

    print("Initial state:")
    for key, value in state.items():
        if key == "messages":
            print(f"  {key}: {[m.type for m in value]}")
        else:
            print(f"  {key}: {value!r}")
    print()

    print(f"Latest user message: {latest_user_message(state)!r}")
    print(f"Latest AI message:   {latest_ai_message(state)!r}")
    print()

    print(f"Fields defined: {len(AgentState.__annotations__)}")
    print()

    print("=" * 70)
    print("[OK] State schema works")
    print("=" * 70)