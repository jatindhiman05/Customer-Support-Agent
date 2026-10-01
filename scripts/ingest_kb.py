"""
Knowledge Base Ingestion Pipeline.

Reads all markdown files from data/kb/, splits them into chunks,
enriches each chunk with metadata, validates against the schema,
embeds them with a local model, and stores them in Chroma.

Run:
    python scripts/ingest_kb.py

Output:
    chroma_db/  — persistent vector store, ready for retrieval
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import jsonschema
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Make src importable when run as a script
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings
from src.kb.loader import KBDocument, load_all_documents


# =============================================================================
# SCHEMA PATH
# =============================================================================

SCHEMA_PATH = settings.schemas_dir / "kb_document.schema.json"


# =============================================================================
# SPLITTER
# =============================================================================
# Prefer markdown structure (## headers), then paragraphs, then sentences.

SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=settings.chunk_size,
    chunk_overlap=settings.chunk_overlap,
    length_function=len,
    separators=[
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)


# =============================================================================
# CHUNK IDS
# =============================================================================

def make_chunk_id(doc_name: str, index: int) -> str:
    """Build a deterministic chunk id: {slug}__chunk_{index:03d}."""
    slug = doc_name.replace(".md", "").replace("-", "_").lower()
    return f"{slug}__chunk_{index:03d}"


def content_hash(text: str) -> str:
    """SHA-256 hash of the chunk text (for change detection)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def count_tokens(text: str) -> int:
    """Rough token estimate (chars / 4). Good enough for validation."""
    return max(1, len(text) // 4)


# =============================================================================
# TAGS
# =============================================================================

# Base tags for every chunk in a category.
_CATEGORY_TAGS: dict[str, list[str]] = {
    "company":          ["company_info"],
    "policies":         ["policy", "rules"],
    "products":         ["product"],
    "faqs":             ["faq"],
    "troubleshooting":  ["troubleshooting", "how_to_fix"],
    "order_management": ["order_management", "process"],
    "account":          ["account", "user_settings"],
    "escalation":       ["escalation", "internal"],
    "glossary":         ["glossary", "definition"],
}

# Keyword → additional tag.
_KEYWORD_TAGS: dict[str, str] = {
    "shipping": "shipping", "delivery": "delivery", "tracking": "shipment_tracking",
    "cancel": "order_cancellation", "refund": "refund", "return": "return_policy",
    "warranty": "warranty_policy", "customs": "customs", "duty": "customs",
    "international": "international_shipping",
    "payment": "payment_method", "card": "payment_method", "paypal": "payment_method",
    "klarna": "bnpl", "afterpay": "bnpl",
    "promo": "promo_code", "coupon": "promo_code",
    "gift card": "gift_card", "giftcard": "gift_card",
    "earbuds": "wireless_earbuds", "voltbuds": "wireless_earbuds",
    "speaker": "bluetooth_speaker", "voltboom": "bluetooth_speaker",
    "charger": "wall_charger", "voltcharge": "wall_charger",
    "power bank": "power_bank", "voltbank": "power_bank",
    "phone case": "phone_case", "voltshield": "phone_case",
    "watch band": "smartwatch_band", "voltfit": "smartwatch_band",
    "bluetooth": "bluetooth", "waterproof": "waterproof",
    "battery": "battery_life", "charging": "charging",
    "password": "password_reset", "2fa": "two_factor_auth",
    "two-factor": "two_factor_auth", "authenticator": "two_factor_auth",
    "login": "login_issue", "delete account": "account_deletion",
    "privacy": "privacy_policy", "price match": "price_match_policy",
    "human": "escalation", "loyalty": "loyalty_program",
    "rewards": "loyalty_program", "referral": "referral_program",
}


def generate_tags(doc: KBDocument, chunk_text: str) -> list[str]:
    """
    Generate 2–8 tags per chunk from category + content keywords.

    Ensures at least 2 tags (falls back to "reference").
    """
    tags: set[str] = set(_CATEGORY_TAGS.get(doc.category, []))
    lower = chunk_text.lower()
    for keyword, tag in _KEYWORD_TAGS.items():
        if keyword in lower:
            tags.add(tag)

    # Cap at 8, alphabetical for determinism
    tags_list = sorted(tags)[:8]
    if len(tags_list) < 2:
        tags_list.append("reference")
    return tags_list


# =============================================================================
# HEADING EXTRACTION
# =============================================================================

import re

_HEADING_RE = re.compile(r"^#{1,3}\s+(.+?)\s*$", re.MULTILINE)
_LINK_RE = re.compile(r"\]\(\.\.?/?[^)]*?([a-z0-9_]+\.md)\)")


def extract_heading_path(chunk_text: str) -> list[str]:
    """Extract up to 3 headings from a chunk."""
    return [m.strip() for m in _HEADING_RE.findall(chunk_text)][:3]


def extract_related_docs(chunk_text: str) -> list[str]:
    """Extract markdown links to KB files."""
    return sorted(set(_LINK_RE.findall(chunk_text)))


def to_relative(path: Path) -> str:
    """Relative path from project root, forward slashes."""
    try:
        rel = path.relative_to(settings.project_root)
    except ValueError:
        rel = path
    return str(rel).replace("\\", "/")


# =============================================================================
# CHUNKING
# =============================================================================

def split_document(doc: KBDocument) -> list[dict]:
    """Split a KBDocument into enriched chunk dicts matching the schema."""
    text = doc.body
    raw_chunks = SPLITTER.split_text(text)
    total = len(raw_chunks)
    chunks: list[dict] = []

    for i, chunk_text in enumerate(raw_chunks):
        chunk_text = chunk_text.strip()
        if len(chunk_text) < 80:
            continue

        chunk = {
            # Identity
            "id": make_chunk_id(doc.doc_name, i),
            "source": to_relative(doc.source_path),
            "doc_name": doc.doc_name,
            "category": doc.category,
            "chunk_index": i,
            "total_chunks": total,

            # Content
            "content": chunk_text,

            # Metadata
            "audience": doc.audience,
            "last_updated": doc.last_updated,
            "tags": generate_tags(doc, chunk_text),

            # Sizing
            "token_count": count_tokens(chunk_text),
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "content_hash": content_hash(chunk_text),

            # Context
            "heading_path": extract_heading_path(chunk_text),
            "related_docs": extract_related_docs(chunk_text),

            # Provenance
            "embedding_model": settings.embedding_model,
            "embedding_dimensions": settings.embedding_dimensions,
            "version": "1.0.0",
        }
        chunks.append(chunk)

    return chunks


# =============================================================================
# VALIDATION
# =============================================================================

def load_schema() -> dict:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_chunks(chunks: list[dict], schema: dict) -> list[dict]:
    """Validate chunks; drop invalid ones with a warning."""
    validator = jsonschema.Draft7Validator(schema)
    valid: list[dict] = []
    dropped = 0
    for chunk in chunks:
        errors = list(validator.iter_errors(chunk))
        if errors:
            dropped += 1
            if dropped <= 5:
                print(f"  [INVALID] {chunk.get('id', '?')}: {errors[0].message}")
        else:
            valid.append(chunk)
    if dropped:
        print(f"  [WARN] Dropped {dropped} invalid chunks")
    return valid


# =============================================================================
# EMBEDDINGS
# =============================================================================

def build_embeddings() -> HuggingFaceEmbeddings:
    """Build the local embedding model (cached after first download)."""
    print(f"Loading embedding model: {settings.embedding_model}")
    print("  (first run downloads ~90 MB — cached after)")
    print()
    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


# =============================================================================
# INGESTION
# =============================================================================

def ingest(force_rebuild: bool = True) -> int:
    """Run the full pipeline. Returns number of chunks stored."""
    start = time.time()

    # ---- Step 1: load ----
    print("=" * 60)
    print("Step 1: Loading KB documents")
    print("=" * 60)
    documents = load_all_documents()
    print()

    # ---- Step 2: chunk ----
    print("=" * 60)
    print("Step 2: Chunking")
    print("=" * 60)
    all_chunks: list[dict] = []
    for doc in documents:
        all_chunks.extend(split_document(doc))
    print(f"[OK] Created {len(all_chunks)} chunks")
    print()

    # ---- Step 3: validate ----
    print("=" * 60)
    print("Step 3: Validating against schema")
    print("=" * 60)
    schema = load_schema()
    valid_chunks = validate_chunks(all_chunks, schema)
    print(f"[OK] {len(valid_chunks)} valid chunks")
    print()
    if not valid_chunks:
        print("[ERROR] No valid chunks to ingest.")
        return 0

    # ---- Step 4: wipe old DB ----
    if force_rebuild and settings.chroma_dir.exists():
        print(f"Wiping existing Chroma DB at {settings.chroma_dir}")
        shutil.rmtree(settings.chroma_dir)
        print()

    # ---- Step 5: embeddings ----
    print("=" * 60)
    print("Step 4: Building embeddings")
    print("=" * 60)
    embeddings = build_embeddings()
    print("[OK] Embedding model ready")
    print()

    # ---- Step 6: flatten for Chroma ----
    texts: list[str] = []
    metadatas: list[dict] = []
    ids: list[str] = []

    for chunk in valid_chunks:
        texts.append(chunk["content"])
        ids.append(chunk["id"])
        metadatas.append({
            "source": chunk["source"],
            "doc_name": chunk["doc_name"],
            "category": chunk["category"],
            "chunk_index": chunk["chunk_index"],
            "total_chunks": chunk["total_chunks"],
            "audience": chunk["audience"],
            "last_updated": chunk["last_updated"],
            "token_count": chunk["token_count"],
            "ingested_at": chunk["ingested_at"],
            "content_hash": chunk["content_hash"],
            "heading_path": " > ".join(chunk["heading_path"]),
            "related_docs": ",".join(chunk["related_docs"]),
            "tags": ",".join(chunk["tags"]),
            "embedding_model": chunk["embedding_model"],
            "version": chunk["version"],
        })

    # ---- Step 7: store ----
    print("=" * 60)
    print("Step 5: Embedding + storing in Chroma")
    print("=" * 60)
    print(f"Embedding {len(texts)} chunks — this takes 1–3 minutes...")
    print()

    Chroma.from_texts(
        texts=texts,
        metadatas=metadatas,
        ids=ids,
        embedding=embeddings,
        collection_name=settings.chroma_collection,
        persist_directory=str(settings.chroma_dir),
    )

    # ---- Step 8: report ----
    elapsed = time.time() - start

    print()
    print("=" * 60)
    print("Ingestion complete")
    print("=" * 60)
    print(f"  Documents:  {len(documents)}")
    print(f"  Chunks:     {len(texts)}")
    print(f"  Collection: {settings.chroma_collection}")
    print(f"  Location:   {settings.chroma_dir}")
    print(f"  Time:       {elapsed:.1f}s")
    print()

    from collections import Counter
    cats = Counter(c["category"] for c in valid_chunks)
    print("Chunks by category:")
    for cat in sorted(cats):
        print(f"  {cat:<20} {cats[cat]}")
    print()

    return len(texts)


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    try:
        total = ingest(force_rebuild=True)
        print(f"[OK] Ingestion finished: {total} chunks stored")
    except KeyboardInterrupt:
        print("\n[CANCELLED] Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)