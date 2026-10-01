"""
Centralized configuration for the Customer Support Agent.

Every module in the project imports settings from here.
Settings are loaded once at import time from `.env`.

Usage:
    from src.config import settings
    print(settings.llm_model)

Design goals:
    - Single source of truth for all tunables
    - Fail fast at startup if required env vars are missing
    - No hardcoded API keys, paths, or model names anywhere else in the codebase
    - Type-safe (uses Python type hints)
    - Reusable across scripts, agent nodes, tools, and the API

Supports:
    - LLM provider: Groq (OpenAI GPT-OSS-120B and others)
    - Embeddings: local SentenceTransformers (BAAI/bge-small-en-v1.5)
    - Vector store: Chroma (local)
    - Reranking: LLM-based two-stage retrieval
    - Optional LangSmith tracing
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


# =============================================================================
# ENVIRONMENT LOADING
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

if not ENV_PATH.exists():
    raise FileNotFoundError(
        f"Missing .env file at {ENV_PATH}. "
        f"Copy .env.example to .env and fill in your API keys."
    )

load_dotenv(ENV_PATH, override=False)


# =============================================================================
# ENV HELPERS
# =============================================================================

def _get(name: str, default: str | None = None) -> str:
    """
    Fetch a string environment variable.

    Raises ValueError if required (no default) and missing.
    """
    value = os.getenv(name)
    if value is None or value.strip() == "":
        if default is None:
            raise ValueError(
                f"Missing required environment variable: {name}. "
                f"Add it to your .env file."
            )
        return default
    return value.strip()


def _get_int(name: str, default: int) -> int:
    """Fetch an integer environment variable with fallback."""
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw.strip())
    except ValueError as e:
        raise ValueError(
            f"Environment variable {name} must be an integer, got {raw!r}"
        ) from e


def _get_float(name: str, default: float) -> float:
    """Fetch a float environment variable with fallback."""
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return float(raw.strip())
    except ValueError as e:
        raise ValueError(
            f"Environment variable {name} must be a float, got {raw!r}"
        ) from e


def _get_bool(name: str, default: bool = False) -> bool:
    """Fetch a boolean environment variable with fallback."""
    raw = os.getenv(name)
    if raw is None:
        return default
    normalized = raw.strip().lower()
    if normalized in {"true", "1", "yes", "on"}:
        return True
    if normalized in {"false", "0", "no", "off", ""}:
        return False
    raise ValueError(
        f"Environment variable {name} must be a boolean, got {raw!r}"
    )


# =============================================================================
# SETTINGS
# =============================================================================

@dataclass(frozen=True)
class Settings:
    """
    Immutable project settings.

    Every field has a clear type. Loaded once at import time.
    Access via the module-level `settings` singleton below.
    """

    # -------------------------------------------------------------------------
    # LLM (Groq)
    # -------------------------------------------------------------------------
    groq_api_key: str
    llm_model: str
    triage_model: str
    llm_temperature: float

    # -------------------------------------------------------------------------
    # Embeddings (Local)
    # -------------------------------------------------------------------------
    embedding_model: str
    embedding_dimensions: int

    # -------------------------------------------------------------------------
    # Vector Store
    # -------------------------------------------------------------------------
    chroma_persist_dir: str
    chroma_collection: str

    # -------------------------------------------------------------------------
    # Chunking
    # -------------------------------------------------------------------------
    chunk_size: int
    chunk_overlap: int

    # -------------------------------------------------------------------------
    # Retrieval
    # -------------------------------------------------------------------------
    retrieval_top_k: int
    retrieval_min_score: float

    # -------------------------------------------------------------------------
    # Reranking
    # -------------------------------------------------------------------------
    rerank_enabled: bool
    rerank_candidates: int
    rerank_top_k: int
    rerank_model: str

    # -------------------------------------------------------------------------
    # LangSmith (Optional)
    # -------------------------------------------------------------------------
    langchain_api_key: str
    langchain_tracing_v2: bool
    langchain_project: str

    # -------------------------------------------------------------------------
    # Paths
    # -------------------------------------------------------------------------
    project_root: Path = field(default_factory=lambda: PROJECT_ROOT)
    data_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data")
    kb_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "kb")
    mock_data_dir: Path = field(
        default_factory=lambda: PROJECT_ROOT / "data" / "mock_data"
    )
    eval_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "eval")
    taxonomy_dir: Path = field(
        default_factory=lambda: PROJECT_ROOT / "data" / "taxonomy"
    )
    schemas_dir: Path = field(
        default_factory=lambda: PROJECT_ROOT / "data" / "schemas"
    )
    scripts_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "scripts")
    evals_output_dir: Path = field(
        default_factory=lambda: PROJECT_ROOT / "evals" / "output"
    )
    chroma_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "chroma_db")

    # -------------------------------------------------------------------------
    # Validation
    # -------------------------------------------------------------------------
    def validate(self) -> None:
        """
        Verify all critical paths exist. Call this at application startup.

        Raises FileNotFoundError if any required directory is missing.
        """
        required_dirs = [
            self.data_dir,
            self.kb_dir,
            self.mock_data_dir,
            self.eval_dir,
            self.taxonomy_dir,
            self.schemas_dir,
        ]
        missing = [p for p in required_dirs if not p.exists()]
        if missing:
            raise FileNotFoundError(
                "Missing required data directories:\n"
                + "\n".join(f"  - {p}" for p in missing)
            )

    def as_dict(self) -> dict:
        """Return a sanitized dict (no secrets) for logging."""
        return {
            "llm_model": self.llm_model,
            "triage_model": self.triage_model,
            "embedding_model": self.embedding_model,
            "embedding_dimensions": self.embedding_dimensions,
            "chroma_collection": self.chroma_collection,
            "chroma_persist_dir": self.chroma_persist_dir,
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap,
            "retrieval_top_k": self.retrieval_top_k,
            "rerank_enabled": self.rerank_enabled,
            "rerank_candidates": self.rerank_candidates,
            "rerank_top_k": self.rerank_top_k,
            "rerank_model": self.rerank_model,
            "langchain_tracing_v2": self.langchain_tracing_v2,
            "langchain_project": self.langchain_project,
        }


# =============================================================================
# SINGLETON
# =============================================================================

def _build_settings() -> Settings:
    """Construct the Settings instance from environment variables."""
    return Settings(
        # LLM
        groq_api_key=_get("GROQ_API_KEY"),
        llm_model=_get("LLM_MODEL", "openai/gpt-oss-120b"),
        triage_model=_get("TRIAGE_MODEL", "llama-3.1-8b-instant"),
        llm_temperature=_get_float("LLM_TEMPERATURE", 0.0),

        # Embeddings
        embedding_model=_get("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5"),
        embedding_dimensions=_get_int("EMBEDDING_DIMENSIONS", 384),

        # Vector store
        chroma_persist_dir=_get("CHROMA_PERSIST_DIR", "./chroma_db"),
        chroma_collection=_get("CHROMA_COLLECTION", "voltnest_kb"),

        # Chunking
        chunk_size=_get_int("CHUNK_SIZE", 500),
        chunk_overlap=_get_int("CHUNK_OVERLAP", 75),

        # Retrieval
        retrieval_top_k=_get_int("RETRIEVAL_TOP_K", 3),
        retrieval_min_score=_get_float("RETRIEVAL_MIN_SCORE", 0.25),

        # Reranking
        rerank_enabled=_get_bool("RERANK_ENABLED", True),
        rerank_candidates=_get_int("RERANK_CANDIDATES", 20),
        rerank_top_k=_get_int("RERANK_TOP_K", 3),
        rerank_model=_get("RERANK_MODEL", "llama-3.1-8b-instant"),

        # LangSmith
        langchain_api_key=_get("LANGCHAIN_API_KEY", ""),
        langchain_tracing_v2=_get_bool("LANGCHAIN_TRACING_V2", False),
        langchain_project=_get("LANGCHAIN_PROJECT", "customer-support-agent"),
    )


settings = _build_settings()


# =============================================================================
# LANGSMITH ENVIRONMENT SYNC
# =============================================================================
# LangChain reads these directly from os.environ. We set them here so that
# importing `src.config` is sufficient to enable tracing.

if settings.langchain_tracing_v2 and settings.langchain_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = settings.langchain_api_key
    os.environ["LANGCHAIN_PROJECT"] = settings.langchain_project


# =============================================================================
# SELF-CHECK
# =============================================================================
# Run this file directly to verify the config:
#     python -m src.config

if __name__ == "__main__":
    print("=" * 70)
    print("VoltNest Customer Support Agent — Configuration Check")
    print("=" * 70)
    print()

    print("LLM:")
    print(f"  Model:                {settings.llm_model}")
    print(f"  Triage model:         {settings.triage_model}")
    print(f"  Temperature:          {settings.llm_temperature}")
    print(f"  Groq key loaded:      {'yes' if settings.groq_api_key else 'NO'}")
    print()

    print("Embeddings:")
    print(f"  Model:                {settings.embedding_model}")
    print(f"  Dimensions:           {settings.embedding_dimensions}")
    print()

    print("Vector Store:")
    print(f"  Collection:           {settings.chroma_collection}")
    print(f"  Persist dir:          {settings.chroma_persist_dir}")
    print()

    print("Chunking:")
    print(f"  Chunk size:           {settings.chunk_size}")
    print(f"  Chunk overlap:        {settings.chunk_overlap}")
    print()

    print("Retrieval:")
    print(f"  Top k:                {settings.retrieval_top_k}")
    print(f"  Min score:            {settings.retrieval_min_score}")
    print()

    print("Reranking:")
    print(f"  Enabled:              {settings.rerank_enabled}")
    print(f"  Candidates:           {settings.rerank_candidates}")
    print(f"  Top k (final):        {settings.rerank_top_k}")
    print(f"  Model:                {settings.rerank_model}")
    print()

    print("LangSmith:")
    print(f"  Tracing enabled:      {settings.langchain_tracing_v2}")
    print(f"  Project:              {settings.langchain_project}")
    print(f"  Key loaded:           {'yes' if settings.langchain_api_key else 'no'}")
    print()

    print("Paths:")
    print(f"  Project root:         {settings.project_root}")
    print(f"  KB dir:               {settings.kb_dir}")
    print(f"  Mock data dir:        {settings.mock_data_dir}")
    print(f"  Eval dir:             {settings.eval_dir}")
    print(f"  Taxonomy dir:         {settings.taxonomy_dir}")
    print(f"  Schemas dir:          {settings.schemas_dir}")
    print(f"  Chroma dir:           {settings.chroma_dir}")
    print()

    # Path validation
    try:
        settings.validate()
        print("Data paths:             [OK] all present")
    except FileNotFoundError as e:
        print(f"Data paths:             [MISSING]")
        print(f"  {e}")
    print()

    print("=" * 70)
    print("[OK] Config loaded successfully")
    print("=" * 70)