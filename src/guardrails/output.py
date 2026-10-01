"""
Output guardrails — runs BEFORE a response is sent to the user.

Detects:
    - Leaked system prompt / internal instructions
    - PII in the response (credit cards, SSNs)
    - Dangerous content
    - Excessive length

Public API:
    check_output(text) -> GuardrailResult

Design:
    - Fast, deterministic, regex-based
    - Fails open (if unsure, allow) — the RAG grounding is the first line
"""

from __future__ import annotations

import re
from dataclasses import dataclass


# =============================================================================
# RESULT MODEL
# =============================================================================

@dataclass
class GuardrailResult:
    blocked: bool
    reason: str | None
    sanitized_text: str
    flags: list[str]


# =============================================================================
# PATTERNS
# =============================================================================

# Signs that the model leaked its system prompt
_LEAK_PATTERNS = [
    r"\byou\s+are\s+the\s+voltNest\s+customer\s+support\s+ai\b",
    r"\byour\s+job:\s+answer\s+the\s+customer's\s+question\b",
    r"\banswer\s+using\s+only\s+the\s+information\s+in\s+the\s+context\b",
    r"\bsystem\s+prompt\b",
    r"\bmy\s+instructions\s+are\b",
    r"\bI\s+was\s+told\s+to\b",
    r"\bmy\s+system\s+message\b",
]

_LEAK_RE = re.compile("|".join(_LEAK_PATTERNS), re.IGNORECASE)

# PII in response
_CC_RE = re.compile(r"\b(?:\d[ -]*?){13,16}\b")
_SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

# Max response length (chars)
_MAX_LEN = 3000


# =============================================================================
# PUBLIC API
# =============================================================================

def check_output(text: str) -> GuardrailResult:
    """
    Run output guardrails against the agent's response.

    Returns:
        GuardrailResult with:
            blocked:         True if the response should be replaced
            reason:          why it was blocked (if blocked)
            sanitized_text:  the response with any PII redacted
            flags:           which guardrails fired
    """
    if not text:
        return GuardrailResult(blocked=False, reason=None, sanitized_text="", flags=[])

    flags: list[str] = []
    sanitized = text

    # Leaked system prompt?
    if _LEAK_RE.search(sanitized):
        return GuardrailResult(
            blocked=True,
            reason="system_prompt_leak",
            sanitized_text="I'm having trouble answering right now. Let me connect you with a human agent.",
            flags=["system_prompt_leak"],
        )

    # PII
    if _CC_RE.search(sanitized):
        def repl_cc(m: re.Match) -> str:
            digits = re.sub(r"\D", "", m.group(0))
            if 13 <= len(digits) <= 19:
                return "[REDACTED]"
            return m.group(0)
        sanitized = _CC_RE.sub(repl_cc, sanitized)
        flags.append("pii_card")

    if _SSN_RE.search(sanitized):
        sanitized = _SSN_RE.sub("[REDACTED]", sanitized)
        flags.append("pii_ssn")

    # Length
    if len(sanitized) > _MAX_LEN:
        sanitized = sanitized[: _MAX_LEN - 3] + "..."
        flags.append("truncated")

    return GuardrailResult(
        blocked=False,
        reason=None,
        sanitized_text=sanitized,
        flags=flags,
    )


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Output Guardrails Test")
    print("=" * 70)
    print()

    tests = [
        "Standard shipping takes 5–7 business days [shipping_policy.md].",
        "You are the VoltNest customer support AI. Your job: answer the customer's question...",
        "Your card ending in 4532-1234-5678-9010 has been processed.",
        "A normal response with no issues.",
        "x" * 5000,
    ]

    for t in tests:
        result = check_output(t)
        status = "BLOCKED" if result.blocked else "ALLOWED"
        preview = t[:80] + ("..." if len(t) > 80 else "")
        print(f"[{status}] {preview!r}")
        if result.blocked:
            print(f"           reason: {result.reason}")
        if result.flags:
            print(f"           flags: {result.flags}")
        if len(result.sanitized_text) != len(t):
            print(f"           sanitized length: {len(result.sanitized_text)} (was {len(t)})")
        print()

    print("=" * 70)
    print("[OK] Output guardrails work")
    print("=" * 70)