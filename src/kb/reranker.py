"""
Two-stage retrieval with LLM reranking.

Stage 1 (recall):    Chroma semantic search → top N candidates
Stage 2 (precision): LLM scores candidates → top K final results

This is the production pattern used by major RAG systems.

Public API:
    retrieve(vectorstore, query, top_k=None, candidates=None) -> list[RankedChunk]

Loads the reranker LLM from src.config (settings.rerank_model).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_groq import ChatGroq

from src.config import settings


# =============================================================================
# DATA MODEL
# =============================================================================

@dataclass
class RankedChunk:
    """A retrieved chunk with its scores."""
    doc_name: str
    category: str
    heading_path: str
    content: str
    semantic_score: float
    rerank_rank: int  # 0 = most relevant


# =============================================================================
# LLM CLIENT
# =============================================================================

_rerank_llm: ChatGroq | None = None


def _get_rerank_llm() -> ChatGroq:
    """
    Lazily build the reranker LLM (cached for the process).

    Uses Groq with the model from settings.rerank_model.
    Reasoning models (like gpt-oss) need more tokens and time.
    """
    global _rerank_llm
    if _rerank_llm is None:
        _rerank_llm = ChatGroq(
            model=settings.rerank_model,
            api_key=settings.groq_api_key,
            temperature=0,
            max_tokens=800,
            timeout=30.0,
            max_retries=2,
        )
    return _rerank_llm


# =============================================================================
# PROMPT
# =============================================================================

_RERANK_PROMPT = """You rerank documents for a customer support retrieval system.

Given a customer QUESTION and a numbered list of CANDIDATES, return the indices of the 3 most relevant candidates, ordered from most to least relevant.

Scoring rules:
- Prioritize candidates that DIRECTLY answer the question.
- Prefer specific documents (policies, product pages) over general ones (FAQs, glossaries) when the question is about a specific rule or product.
- Ignore candidates that are only tangentially related.
- Return ONLY a JSON array of up to 3 integers. Example: [2, 0, 5]
- If fewer than 3 candidates exist, return only the valid indices.
- Do NOT include any explanation, markdown, or text outside the JSON array.

QUESTION:
{question}

CANDIDATES:
{candidates}

Answer (JSON array only):"""


# =============================================================================
# HELPERS
# =============================================================================

def _format_candidates(candidates: list[dict]) -> str:
    """Format candidates for the prompt — compact and readable."""
    lines: list[str] = []
    for i, c in enumerate(candidates):
        heading = c.get("heading_path", "") or c.get("doc_name", "")
        preview = c["content"][:280].replace("\n", " ").strip()
        lines.append(f"[{i}] {c['doc_name']} — {heading}\n    {preview}")
    return "\n\n".join(lines)


def _parse_indices(raw: str, max_index: int) -> list[int]:
    """
    Extract integer indices from an LLM response.

    Handles:
      - "[2, 0, 5]"
      - "```json\\n[2, 0, 5]\\n```"
      - "2, 0, 5"
      - any text containing bracketed ints
      - reasoning model output with <final>...</final> or <reasoning>...</reasoning>
    """
    raw = raw.strip()

    # Strip reasoning model tags if present
    if "<final>" in raw:
        raw = raw.split("<final>")[-1].split("</final>")[0]
    elif "</reasoning>" in raw:
        raw = raw.split("</reasoning>")[-1]

    # Try to find a JSON array of integers first
    array_match = re.search(r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", raw)
    if array_match:
        try:
            values = json.loads(array_match.group(0))
            return [
                v for v in values
                if isinstance(v, int) and 0 <= v <= max_index
            ][:3]
        except json.JSONDecodeError:
            pass

    # Fallback: pull all integers, keep the first 3 that are valid
    ints = [int(x) for x in re.findall(r"\d+", raw)]
    return [i for i in ints if 0 <= i <= max_index][:3]


def _dedupe_by_doc(
    results: list[tuple[Document, float]],
) -> list[dict]:
    """
    Collapse multiple chunks from the same document into one entry.

    Keeps the highest-scoring chunk per source file.
    """
    best: dict[str, dict] = {}
    for doc, score in results:
        doc_name = doc.metadata.get("doc_name", "?")
        if doc_name not in best or score > best[doc_name]["semantic_score"]:
            best[doc_name] = {
                "doc_name": doc_name,
                "category": doc.metadata.get("category", "?"),
                "heading_path": doc.metadata.get("heading_path", ""),
                "content": doc.page_content,
                "semantic_score": round(score, 4),
            }
    return sorted(best.values(), key=lambda x: -x["semantic_score"])


# =============================================================================
# PUBLIC API
# =============================================================================

def retrieve(
    vectorstore: Chroma,
    query: str,
    top_k: int | None = None,
    candidates: int | None = None,
    use_rerank: bool | None = None,
) -> list[RankedChunk]:
    """
    Two-stage retrieval with optional LLM reranking.

    Args:
        vectorstore: Chroma instance
        query: user question
        top_k: number of results to return (default from settings)
        candidates: number of candidates to retrieve before rerank (default from settings)
        use_rerank: override the settings.rerank_enabled flag (for testing)

    Returns:
        List of RankedChunk, sorted by rerank_rank ascending (0 = best).
    """
    top_k = top_k or settings.rerank_top_k
    candidates = candidates or settings.rerank_candidates
    if use_rerank is None:
        use_rerank = settings.rerank_enabled

    # ---------- Stage 1: semantic search ----------
    raw = vectorstore.similarity_search_with_relevance_scores(query, k=candidates)
    if not raw:
        return []

    deduped = _dedupe_by_doc(raw)

    # If reranking is off, return the semantic top-k
    if not use_rerank or len(deduped) <= top_k:
        return [
            RankedChunk(
                doc_name=c["doc_name"],
                category=c["category"],
                heading_path=c["heading_path"],
                content=c["content"],
                semantic_score=c["semantic_score"],
                rerank_rank=i,
            )
            for i, c in enumerate(deduped[:top_k])
        ]

    # ---------- Stage 2: LLM reranking ----------
    llm = _get_rerank_llm()
    prompt = _RERANK_PROMPT.format(
        question=query,
        candidates=_format_candidates(deduped),
    )

    try:
        response = llm.invoke(prompt)
        raw_text = getattr(response, "content", str(response))
        indices = _parse_indices(raw_text, max_index=len(deduped) - 1)
    except Exception as e:
        print(f"  [RERANK FALLBACK] {type(e).__name__}: {e}")
        indices = []

    # If we got fewer than top_k indices, pad with the semantic order
    if len(indices) < top_k:
        for i in range(len(deduped)):
            if i not in indices:
                indices.append(i)
            if len(indices) >= top_k:
                break

    # Build the final ranked result
    ranked: list[RankedChunk] = []
    for rank, idx in enumerate(indices[:top_k]):
        c = deduped[idx]
        ranked.append(
            RankedChunk(
                doc_name=c["doc_name"],
                category=c["category"],
                heading_path=c["heading_path"],
                content=c["content"],
                semantic_score=c["semantic_score"],
                rerank_rank=rank,
            )
        )
    return ranked


# =============================================================================
# SELF-CHECK
# =============================================================================

if __name__ == "__main__":
    from langchain_huggingface import HuggingFaceEmbeddings

    print("=" * 70)
    print("Reranker Test")
    print("=" * 70)
    print()

    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    print("Opening Chroma...")
    vs = Chroma(
        collection_name=settings.chroma_collection,
        persist_directory=str(settings.chroma_dir),
        embedding_function=embeddings,
    )
    print(f"[OK] {vs._collection.count()} chunks in collection")
    print()

    test_queries = [
        "How do I send something back to you?",
        "How much does shipping cost to Canada?",
        "My earbuds keep disconnecting",
        "What does IP67 mean?",
        "Can I use two promo codes together?",
    ]

    for q in test_queries:
        print(f"Q: {q}")
        results = retrieve(vs, q, top_k=3, use_rerank=True)
        for i, r in enumerate(results):
            print(
                f"  {i + 1}. {r.doc_name:<30} "
                f"[{r.category:<18}] semantic={r.semantic_score:.3f}"
            )
        print()

    print("=" * 70)
    print("[OK] Reranker works")
    print("=" * 70)