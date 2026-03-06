"""Vector indexing pipeline for the RAG baseline."""

from __future__ import annotations

from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from .config import AppConfig
from .documents import load_documents
from .splitter import split_documents


def build_index(config: AppConfig, source_dir: Path) -> int:
    """
    Build and persist a Chroma vector index.

    Returns the number of chunks indexed.
    """
    docs = load_documents(source_dir)
    chunks = split_documents(docs, config.chunk_size, config.chunk_overlap)

    embeddings = OpenAIEmbeddings(
        model=config.embedding_model,
        api_key=config.openai_api_key,
    )

    config.vectorstore_dir.mkdir(parents=True, exist_ok=True)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(config.vectorstore_dir),
    )
    if hasattr(vectorstore, "persist"):
        vectorstore.persist()
    return len(chunks)
