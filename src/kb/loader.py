"""
Knowledge Base loader.

Reads every markdown file under data/kb/, parses its metadata block,
and returns structured KBDocument objects.

Every KB file follows this shape:

    # Title

    > **Category**: policies
    > **Audience**: customer, agent
    > **Last updated**: 2026-01-15

    Content follows...

This module is used by the ingestion script and by the retriever when
it needs the full body of a document for citations.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from src.config import settings


# =============================================================================
# DATA MODEL
# =============================================================================

@dataclass
class KBDocument:
    """A parsed markdown file from the KB."""

    # Identity
    source_path: Path
    doc_name: str           # e.g., "return_refund_policy.md"
    category: str           # e.g., "policies" (folder name)
    title: str              # First H1

    # Metadata block
    audience: str           # "customer" | "agent" | "both"
    last_updated: str       # ISO date string (YYYY-MM-DD)

    # Content
    raw_content: str        # Full markdown (with metadata block)
    body: str               # Content with metadata block removed
    headings: list[str] = field(default_factory=list)

    # Relationships
    related_docs: list[str] = field(default_factory=list)

    # Derived
    char_count: int = 0
    word_count: int = 0


# =============================================================================
# REGEX PATTERNS
# =============================================================================

# "> **Category**: policies"  →  key=Category, value=policies
_META_LINE_RE = re.compile(
    r"^>\s*\*\*(?P<key>[A-Za-z][A-Za-z ]+?)\*\*\s*:\s*(?P<value>.+?)\s*$"
)

# "# Title"  (first H1 only)
_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# "## Section" or "### Sub"
_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.MULTILINE)

# markdown link: [text](./file.md) or [text](../folder/file.md)
_LINK_RE = re.compile(r"\[[^\]]+\]\(\.\.?/?[^)]*?([a-z0-9_]+\.md)\)")


# =============================================================================
# PARSING HELPERS
# =============================================================================

def _extract_title(content: str) -> str:
    match = _H1_RE.search(content)
    return match.group(1).strip() if match else "Untitled"


def _extract_headings(content: str) -> list[str]:
    return [m.group(2).strip() for m in _HEADING_RE.finditer(content)]


def _extract_metadata(content: str) -> dict[str, str]:
    """
    Parse the blockquote metadata lines near the top of a document.

    Returns lowercase keys, e.g.:
        {"category": "policies", "audience": "customer, agent",
         "last updated": "2026-01-15"}
    """
    metadata: dict[str, str] = {}
    # Metadata lives in the first 30 lines
    head = "\n".join(content.splitlines()[:30])
    for line in head.splitlines():
        match = _META_LINE_RE.match(line.strip())
        if match:
            key = match.group("key").strip().lower()
            value = match.group("value").strip()
            metadata[key] = value
    return metadata


def _strip_metadata_block(content: str) -> str:
    """Remove the metadata blockquotes from the document body."""
    lines_out: list[str] = []
    for line in content.splitlines():
        if _META_LINE_RE.match(line.strip()):
            continue
        lines_out.append(line)
    return "\n".join(lines_out).strip()


def _normalize_audience(raw: str) -> str:
    """Map 'customer, agent' to 'both', etc."""
    lower = raw.lower().replace(" ", "")
    has_customer = "customer" in lower
    has_agent = "agent" in lower
    if has_customer and has_agent:
        return "both"
    if has_customer:
        return "customer"
    if has_agent:
        return "agent"
    return "both"


def _extract_related_docs(content: str) -> list[str]:
    """Return filenames referenced in markdown links."""
    return sorted({m.group(1) for m in _LINK_RE.finditer(content)})


# =============================================================================
# LOADING
# =============================================================================

def load_document(path: Path) -> Optional[KBDocument]:
    """
    Load and parse a single KB markdown file.

    Returns None if required metadata is missing (with a warning printed).
    """
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [WARN] Could not read {path}: {e}")
        return None

    meta = _extract_metadata(content)

    category = meta.get("category")
    audience_raw = meta.get("audience")
    last_updated = meta.get("last updated")

    if not category:
        print(f"  [WARN] Missing 'Category' metadata in {path.name}")
        return None
    if not audience_raw:
        print(f"  [WARN] Missing 'Audience' metadata in {path.name}")
        return None
    if not last_updated:
        print(f"  [WARN] Missing 'Last updated' metadata in {path.name}")
        return None

    body = _strip_metadata_block(content)

    return KBDocument(
        source_path=path,
        doc_name=path.name,
        category=category,
        title=_extract_title(content),
        audience=_normalize_audience(audience_raw),
        last_updated=last_updated,
        raw_content=content,
        body=body,
        headings=_extract_headings(content),
        related_docs=_extract_related_docs(content),
        char_count=len(body),
        word_count=len(body.split()),
    )


def load_all_documents() -> list[KBDocument]:
    """Load every .md file under data/kb/, recursively."""
    kb_dir = settings.kb_dir
    if not kb_dir.exists():
        raise FileNotFoundError(f"KB directory not found: {kb_dir}")

    paths = sorted(kb_dir.glob("**/*.md"))
    documents: list[KBDocument] = []

    print(f"Loading markdown files from {kb_dir}...")
    for path in paths:
        doc = load_document(path)
        if doc is not None:
            documents.append(doc)

    print(f"[OK] Loaded {len(documents)} documents")
    return documents


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("KB Loader Test")
    print("=" * 70)
    print()

    docs = load_all_documents()
    print()

    print(f"Total documents: {len(docs)}")
    print()

    # By category
    from collections import Counter
    cats = Counter(d.category for d in docs)
    print("By category:")
    for cat in sorted(cats):
        print(f"  {cat:<20} {cats[cat]}")
    print()

    # By audience
    auds = Counter(d.audience for d in docs)
    print("By audience:")
    for aud in sorted(auds):
        print(f"  {aud:<20} {auds[aud]}")
    print()

    # Sample
    if docs:
        s = docs[0]
        print("Sample document:")
        print(f"  doc_name:     {s.doc_name}")
        print(f"  category:     {s.category}")
        print(f"  title:        {s.title}")
        print(f"  audience:     {s.audience}")
        print(f"  last_updated: {s.last_updated}")
        print(f"  words:        {s.word_count}")
        print(f"  headings:     {len(s.headings)}")
        print(f"  related_docs: {s.related_docs[:3]}")
        print()

    print("=" * 70)
    print("[OK] Loader works")
    print("=" * 70)