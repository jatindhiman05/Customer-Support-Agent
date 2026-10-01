"""
Interactive CLI to chat with the VoltNest support agent.

Runs the LangGraph agent in a loop with a persistent conversation thread.
Displays the intent, route, and final answer for each turn.

Run:
    python scripts/chat.py
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langchain_core.messages import HumanMessage

from src.graph.build import build_graph
from src.graph.state import initial_state


# =============================================================================
# DISPLAY HELPERS
# =============================================================================

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"


def _print_header() -> None:
    print()
    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║  VoltNest Customer Support Agent                        ║{RESET}")
    print(f"{BOLD}{CYAN}║  Powered by LangGraph + GPT-OSS-120B                    ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    print()
    print(f"{DIM}Type your question below. Type 'exit' or 'quit' to end.{RESET}")
    print(f"{DIM}Try: 'Where is my order ORD-100001?'{RESET}")
    print()


def _print_turn(response: dict) -> None:
    """Print metadata + final answer for one turn."""
    intent = response.get("intent", "?")
    route = response.get("route", "?")
    blocked = response.get("blocked", False)
    escalated = response.get("escalated", False)
    ticket = response.get("ticket_id")
    citations = response.get("response_citations", [])

    # Metadata line
    parts: list[str] = []
    parts.append(f"{DIM}intent{RESET} {CYAN}{intent}{RESET}")
    if route:
        parts.append(f"{DIM}route{RESET} {CYAN}{route}{RESET}")
    if blocked:
        parts.append(f"{RED}BLOCKED{RESET}")
    if escalated:
        parts.append(f"{YELLOW}ESCALATED{RESET}")
    if ticket:
        parts.append(f"{DIM}ticket{RESET} {YELLOW}{ticket}{RESET}")

    print(f"   {' | '.join(parts)}")

    # Answer
    answer = response.get("final_response") or "(no response)"
    print()
    for line in answer.splitlines():
        print(f"   {line}")
    print()

    # Citations
    if citations:
        print(f"   {DIM}sources: {', '.join(citations)}{RESET}")
        print()


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    _print_header()

    print("Compiling agent graph...")
    graph = build_graph(use_memory=True)
    print(f"{GREEN}[OK]{RESET} Agent ready")
    print()

    # One thread for the whole session (conversation memory)
    thread_id = f"session-{uuid.uuid4().hex[:8]}"
    config = {"configurable": {"thread_id": thread_id}}

    while True:
        try:
            user_input = input(f"{BOLD}{MAGENTA}You:{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print(f"{DIM}Goodbye.{RESET}")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit", ":q"}:
            print(f"{DIM}Goodbye.{RESET}")
            break

        # Build fresh state with the new user message.
        # LangGraph will merge history via the checkpointer.
        state = initial_state(user_message=user_input, thread_id=thread_id)

        try:
            response = graph.invoke(state, config=config)
        except Exception as e:
            print(f"{RED}Error: {type(e).__name__}: {e}{RESET}")
            continue

        print()
        _print_turn(response)


if __name__ == "__main__":
    main()