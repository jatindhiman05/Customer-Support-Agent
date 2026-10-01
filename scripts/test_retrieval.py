"""
Retrieval accuracy test (with two-stage retrieval + LLM reranking).

Loads questions from data/eval/{EVAL_FILE} (default: test_questions.json),
runs the full retrieval pipeline for each, and reports accuracy.

Run:
    python scripts/test_retrieval.py

Or with a specific eval file:
    $env:EVAL_FILE="holdout_questions.json"
    python scripts/test_retrieval.py

Target:
    Top-1 accuracy >= 80%
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings
from src.kb.reranker import retrieve


# =============================================================================
# LOADING
# =============================================================================

def load_questions() -> list[dict]:
    filename = os.getenv("EVAL_FILE", "test_questions.json")
    path = settings.eval_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Eval file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_vectorstore() -> Chroma:
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    return Chroma(
        collection_name=settings.chroma_collection,
        persist_directory=str(settings.chroma_dir),
        embedding_function=embeddings,
    )


# =============================================================================
# EVALUATION
# =============================================================================

def evaluate(vs: Chroma, questions: list[dict], k: int = 3) -> dict:
    results = []
    total = len(questions)

    for i, q in enumerate(questions, 1):
        ranked = retrieve(vs, q["question"], top_k=k, use_rerank=True)
        docs = [r.doc_name for r in ranked]
        expected = q["expected_source"]

        top1_hit = (docs[0] == expected) if docs else False
        top3_hit = expected in docs

        results.append({
            "id": q["id"],
            "question": q["question"],
            "expected": expected,
            "top1_got": docs[0] if docs else None,
            "top3_got": docs,
            "top1_hit": top1_hit,
            "top3_hit": top3_hit,
            "semantic_score": ranked[0].semantic_score if ranked else 0,
            "difficulty": q.get("difficulty", "unknown"),
            "category": q.get("expected_category", "unknown"),
        })

        status = "OK  " if top1_hit else "MISS"
        preview = docs[0] if docs else "(no results)"
        print(f"  [{i:>2}/{total}] {status}  {q['id']:<6} {preview}")

    # Metrics
    top1 = sum(1 for r in results if r["top1_hit"]) / total
    top3 = sum(1 for r in results if r["top3_hit"]) / total

    # By category
    by_category: dict[str, dict] = {}
    for r in results:
        cat = r["category"]
        by_category.setdefault(cat, {"total": 0, "top1": 0, "top3": 0})
        by_category[cat]["total"] += 1
        if r["top1_hit"]:
            by_category[cat]["top1"] += 1
        if r["top3_hit"]:
            by_category[cat]["top3"] += 1

    # By difficulty
    by_difficulty: dict[str, dict] = {}
    for r in results:
        diff = r["difficulty"]
        by_difficulty.setdefault(diff, {"total": 0, "top1": 0, "top3": 0})
        by_difficulty[diff]["total"] += 1
        if r["top1_hit"]:
            by_difficulty[diff]["top1"] += 1
        if r["top3_hit"]:
            by_difficulty[diff]["top3"] += 1

    return {
        "overall": {
            "total": total,
            "top1_accuracy": top1,
            "top3_accuracy": top3,
        },
        "by_category": by_category,
        "by_difficulty": by_difficulty,
        "results": results,
    }


# =============================================================================
# REPORTING
# =============================================================================

def print_report(metrics: dict) -> None:
    print()
    print("=" * 70)
    print("RETRIEVAL REPORT (with LLM reranking)")
    print("=" * 70)
    print()

    o = metrics["overall"]
    print(f"Total questions:  {o['total']}")
    print(f"Top-1 accuracy:   {o['top1_accuracy'] * 100:.1f}%")
    print(f"Top-3 accuracy:   {o['top3_accuracy'] * 100:.1f}%")
    print()

    print("By category:")
    print(f"  {'Category':<20} {'Total':>6} {'Top-1':>8} {'Top-3':>8}")
    print(f"  {'-' * 20} {'-' * 6} {'-' * 8} {'-' * 8}")
    for cat in sorted(metrics["by_category"]):
        s = metrics["by_category"][cat]
        t1 = s["top1"] / s["total"] * 100 if s["total"] else 0
        t3 = s["top3"] / s["total"] * 100 if s["total"] else 0
        print(f"  {cat:<20} {s['total']:>6} {t1:>7.1f}% {t3:>7.1f}%")
    print()

    print("By difficulty:")
    print(f"  {'Difficulty':<20} {'Total':>6} {'Top-1':>8} {'Top-3':>8}")
    print(f"  {'-' * 20} {'-' * 6} {'-' * 8} {'-' * 8}")
    for diff in sorted(metrics["by_difficulty"]):
        s = metrics["by_difficulty"][diff]
        t1 = s["top1"] / s["total"] * 100 if s["total"] else 0
        t3 = s["top3"] / s["total"] * 100 if s["total"] else 0
        print(f"  {diff:<20} {s['total']:>6} {t1:>7.1f}% {t3:>7.1f}%")
    print()

    failures = [r for r in metrics["results"] if not r["top1_hit"]]
    if failures:
        print(f"Failures ({len(failures)}):")
        print()
        for r in failures[:20]:
            print(f"  [{r['id']}] {r['question']}")
            print(f"      expected: {r['expected']}")
            print(f"      got:      {r['top1_got']}")
            print(f"      top-3:    {r['top3_got']}")
            print()
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more")
            print()

    print("=" * 70)
    top1 = o["top1_accuracy"] * 100
    if top1 >= 85:
        print(f"[PASS] Top-1 {top1:.1f}% (target: 85%)")
    elif top1 >= 70:
        print(f"[GOOD] Top-1 {top1:.1f}% — usable")
    else:
        print(f"[LOW]  Top-1 {top1:.1f}%")
    print("=" * 70)
    print()


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    filename = os.getenv("EVAL_FILE", "test_questions.json")
    print(f"Loading questions from: {filename}")
    questions = load_questions()
    print(f"[OK] {len(questions)} questions")
    print()

    print("Opening Chroma + loading reranker...")
    vs = build_vectorstore()
    print(f"[OK] Collection: {settings.chroma_collection}")
    print(f"[OK] Rerank model: {settings.rerank_model}")
    print()

    print("Running two-stage retrieval (semantic + LLM rerank)...")
    print(f"(Each query takes ~2-5s with {settings.rerank_model})")
    print()

    metrics = evaluate(vs, questions, k=3)
    print_report(metrics)

    # Save
    output_dir = settings.evals_output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    report_name = f"retrieval_{filename.replace('.json', '')}.json"
    output_path = output_dir / report_name
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(f"[OK] Saved to: {output_path}")
    print()