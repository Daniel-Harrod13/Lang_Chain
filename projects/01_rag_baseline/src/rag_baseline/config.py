"""Configuration for the RAG baseline project."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """Runtime settings for indexing and Q&A."""

    openai_api_key: str
    chat_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    chunk_size: int = 800
    chunk_overlap: int = 120
    retrieval_k: int = 4
    vectorstore_dir: Path = Path("data/vectorstore")

    @classmethod
    def from_env(cls, require_api_key: bool = True) -> "AppConfig":
        """Build config from environment variables."""
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if require_api_key and not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not set. Add it to your environment or .env file."
            )

        chunk_size = int(os.getenv("RAG_CHUNK_SIZE", "800"))
        chunk_overlap = int(os.getenv("RAG_CHUNK_OVERLAP", "120"))
        retrieval_k = int(os.getenv("RAG_RETRIEVAL_K", "4"))

        config = cls(
            openai_api_key=api_key,
            chat_model=os.getenv("RAG_CHAT_MODEL", "gpt-4o-mini"),
            embedding_model=os.getenv("RAG_EMBEDDING_MODEL", "text-embedding-3-small"),
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            retrieval_k=retrieval_k,
            vectorstore_dir=Path(os.getenv("RAG_VECTORSTORE_DIR", "data/vectorstore")),
        )
        config.validate()
        return config

    def validate(self) -> None:
        """Validate config values early with clear errors."""
        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be > 0.")
        if self.chunk_overlap < 0:
            raise ValueError("chunk_overlap must be >= 0.")
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size.")
        if self.retrieval_k <= 0:
            raise ValueError("retrieval_k must be > 0.")
