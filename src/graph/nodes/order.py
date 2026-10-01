"""
Order node — handles order-related queries by looking up structured data
in data/mock_data/orders.json (and shipments.json when relevant).

Handles these intents:
    order_status      — where is my order / tracking
    cancel_order      — cancel before shipping
    modify_order      — change address / items / shipping
    delivery_issue    — lost / delayed / damaged / not received

Approach:
    1. Extract an order ID from the user message (e.g., ORD-100001)
    2. If found, load the order + shipment and build a rich answer
    3. If not found, ask for the order ID
    4. If the query needs policy info ("can I cancel?"), fall back to RAG

Updates:
    state["final_response"]
    state["tool_results"]
    state["retrieved_docs"]  (if RAG fallback used)
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from src.config import settings
from src.graph.state import AgentState, latest_user_message


# =============================================================================
# DATA LOADING (cached)
# =============================================================================

@lru_cache(maxsize=1)
def _load_orders() -> dict[str, dict]:
    """Load orders keyed by order_id."""
    path: Path = settings.mock_data_dir / "orders.json"
    with open(path, "r", encoding="utf-8") as f:
        orders = json.load(f)
    return {o["order_id"]: o for o in orders}


@lru_cache(maxsize=1)
def _load_shipments() -> dict[str, dict]:
    """Load shipments keyed by tracking_number."""
    path: Path = settings.mock_data_dir / "shipments.json"
    with open(path, "r", encoding="utf-8") as f:
        shipments = json.load(f)
    return {s["tracking_number"]: s for s in shipments}


@lru_cache(maxsize=1)
def _load_users() -> dict[str, dict]:
    """Load users keyed by user_id."""
    path: Path = settings.mock_data_dir / "users.json"
    with open(path, "r", encoding="utf-8") as f:
        users = json.load(f)
    return {u["user_id"]: u for u in users}


# =============================================================================
# ORDER ID EXTRACTION
# =============================================================================

_ORDER_ID_RE = re.compile(r"\bORD-\d{6}\b", re.IGNORECASE)


def _extract_order_id(text: str) -> str | None:
    """Extract an order ID like ORD-100001 from a message."""
    match = _ORDER_ID_RE.search(text)
    return match.group(0).upper() if match else None


# =============================================================================
# FORMATTING
# =============================================================================

def _money(x: float) -> str:
    return f"${x:,.2f}"


def _format_order_response(order: dict, shipment: dict | None) -> str:
    """
    Build a user-friendly answer from the order + shipment records.

    Adapts the format to the order status.
    """
    oid = order["order_id"]
    status = order["status"]
    items = order.get("items", [])
    total = _money(order["total"])

    items_str = ", ".join(
        f"{i['quantity']}× {i['name']}" for i in items
    ) or "your items"

    lines: list[str] = []

    if status == "delivered":
        lines.append(f"**Order {oid} — Delivered**")
        lines.append(f"Items: {items_str}")
        lines.append(f"Total: {total}")
        if order.get("delivered_at"):
            lines.append(f"Delivered on {order['delivered_at'][:10]}")
        if shipment and shipment.get("delivered_to"):
            lines.append(f"Delivery location: {shipment['delivered_to']}")
        lines.append(
            "If anything is wrong with your order, you can request a return "
            "within 30 days of delivery. Need help with the return process?"
        )

    elif status == "in_transit":
        lines.append(f"**Order {oid} — In Transit**")
        lines.append(f"Items: {items_str}")
        lines.append(f"Total: {total}")
        if order.get("tracking_number"):
            lines.append(
                f"Tracking: {order['tracking_number']} "
                f"({order.get('carrier', 'carrier')})"
            )
        if shipment and shipment.get("estimated_delivery"):
            lines.append(f"Estimated delivery: {shipment['estimated_delivery']}")
        if shipment and shipment.get("events"):
            last = shipment["events"][-1]
            lines.append(
                f"Latest update: {last['status']} — {last['location']} "
                f"({last['timestamp'][:10]})"
            )

    elif status == "shipped":
        lines.append(f"**Order {oid} — Shipped**")
        lines.append(f"Items: {items_str}")
        if order.get("tracking_number"):
            lines.append(
                f"Tracking: {order['tracking_number']} "
                f"({order.get('carrier', 'carrier')})"
            )
        lines.append("It should arrive in the next few business days.")

    elif status == "processing":
        lines.append(f"**Order {oid} — Processing**")
        lines.append(f"Items: {items_str}")
        lines.append(f"Total: {total}")
        lines.append(
            "We're preparing your order at our Memphis warehouse. "
            "You'll get a shipping confirmation with tracking within 1–2 business days."
        )

    elif status == "cancelled":
        lines.append(f"**Order {oid} — Cancelled**")
        lines.append("This order has been cancelled and a refund was issued.")
        if order.get("refunded_at"):
            lines.append(f"Refund processed on {order['refunded_at'][:10]}.")
        if order.get("notes"):
            lines.append(f"Note: {order['notes']}")

    elif status == "refunded":
        lines.append(f"**Order {oid} — Refunded**")
        lines.append(f"Items: {items_str}")
        if order.get("refunded_at"):
            lines.append(f"Refund issued on {order['refunded_at'][:10]}.")
        if order.get("notes"):
            lines.append(f"Note: {order['notes']}")

    else:
        lines.append(f"**Order {oid}** — Status: {status}")
        lines.append(f"Items: {items_str}")
        lines.append(f"Total: {total}")

    return "\n".join(lines)


def _format_not_found(order_id: str) -> str:
    return (
        f"I couldn't find order **{order_id}** in our system. "
        f"Could you double-check the order ID? It should look like ORD-100001. "
        f"If you're sure it's correct, I can connect you with a human agent."
    )


def _format_ask_for_order_id() -> str:
    return (
        "I can look that up for you! Could you share your order ID? "
        "It starts with **ORD-** followed by 6 digits (e.g., ORD-100001). "
        "You can find it in your order confirmation email."
    )


# =============================================================================
# LLM (for policy fallback + natural rewriting)
# =============================================================================

_order_llm: ChatGroq | None = None


def _get_order_llm() -> ChatGroq:
    global _order_llm
    if _order_llm is None:
        _order_llm = ChatGroq(
            model=settings.llm_model,
            api_key=settings.groq_api_key,
            temperature=0.2,
            max_tokens=500,
            timeout=30.0,
            max_retries=2,
        )
    return _order_llm


def _polish_response(question: str, raw_response: str) -> str:
    """Ask the LLM to polish the structured response into natural language."""
    llm = _get_order_llm()
    messages = [
        SystemMessage(
            content=(
                "You are VoltNest's support AI. Rewrite the following order "
                "information as a warm, concise reply to the customer. "
                "Do not invent facts. Do not add policies that aren't in the "
                "data. Keep all facts (IDs, dates, amounts) exactly as given. "
                "Two to four sentences max."
            )
        ),
        HumanMessage(
            content=f"Customer asked: {question}\n\nOrder data:\n{raw_response}"
        ),
    ]
    try:
        response = llm.invoke(messages)
        raw = getattr(response, "content", str(response))
        if "<final>" in raw:
            raw = raw.split("<final>")[-1].split("</final>")[0]
        elif "</reasoning>" in raw:
            raw = raw.split("</reasoning>")[-1]
        return raw.strip()
    except Exception:
        # Fallback: return the structured text as-is
        return raw_response


# =============================================================================
# RAG FALLBACK (for policy nuance)
# =============================================================================

def _rag_fallback(question: str) -> tuple[str, list[dict]]:
    """
    If we can't answer from structured data, use the RAG node.

    Returns (response_text, retrieved_docs).
    """
    from src.graph.nodes.rag import rag_node
    from src.graph.state import initial_state

    sub_state = initial_state(user_message=question)
    result = rag_node(sub_state)
    return (
        result.get("final_response", ""),
        result.get("retrieved_docs", []),
    )


# =============================================================================
# NODE
# =============================================================================

def order_node(state: AgentState) -> dict:
    """
    LangGraph node: handle order-related queries.

    Returns partial state with:
        final_response, tool_results, and optionally retrieved_docs.
    """
    question = latest_user_message(state)
    if not question:
        return {
            "final_response": "I didn't receive a message. How can I help?",
            "tool_results": [],
        }

    order_id = _extract_order_id(question)

    # ---- If no order ID was provided, ask for one ----
    if not order_id:
        # But maybe the user is asking a general policy question
        # (e.g., "how do I cancel an order?") — RAG can handle that.
        lower = question.lower()
        general_markers = [
            "how do i cancel",
            "how can i cancel",
            "cancel policy",
            "how do returns work",
            "how do i return",
        ]
        if any(m in lower for m in general_markers):
            text, docs = _rag_fallback(question)
            return {
                "final_response": text,
                "retrieved_docs": docs,
                "tool_results": [
                    {"tool_name": "rag_fallback", "success": True, "data": None, "error": None}
                ],
            }

        return {
            "final_response": _format_ask_for_order_id(),
            "tool_results": [
                {"tool_name": "ask_for_order_id", "success": True, "data": None, "error": None}
            ],
        }

    # ---- Load order ----
    orders = _load_orders()
    order = orders.get(order_id)

    if not order:
        return {
            "final_response": _format_not_found(order_id),
            "tool_results": [
                {
                    "tool_name": "lookup_order",
                    "success": False,
                    "data": None,
                    "error": f"Order {order_id} not found",
                }
            ],
        }

    # ---- Attach shipment info if available ----
    shipment: dict | None = None
    if order.get("tracking_number"):
        shipment = _load_shipments().get(order["tracking_number"])

    # ---- Build structured response ----
    raw = _format_order_response(order, shipment)

    # ---- Polish with LLM ----
    polished = _polish_response(question, raw)

    return {
        "final_response": polished,
        "tool_results": [
            {
                "tool_name": "lookup_order",
                "success": True,
                "data": {
                    "order_id": order_id,
                    "status": order["status"],
                    "has_shipment": shipment is not None,
                },
                "error": None,
            }
        ],
    }


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    from src.graph.state import initial_state

    print("=" * 70)
    print("Order Node Test")
    print("=" * 70)
    print()

    test_queries = [
        "Where is my order ORD-100001?",
        "What's the status of ORD-100002?",
        "Can you check ORD-100008 for me?",
        "Where is ORD-999999?",
        "Where is my order?",  # no ID
        "How do I cancel an order?",
    ]

    for q in test_queries:
        print(f"Q: {q}")
        state = initial_state(user_message=q)
        update = order_node(state)
        print(f"   answer: {update.get('final_response', '')[:250]}")
        tools = update.get("tool_results", [])
        print(f"   tools:  {[t.get('tool_name') for t in tools]}")
        print()

    print("=" * 70)
    print("[OK] Order node works")
    print("=" * 70)