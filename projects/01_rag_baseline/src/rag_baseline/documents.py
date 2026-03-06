"""Document loading utilities."""

from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document

SUPPORTED_SUFFIXES = {".txt", ".md"}


def discover_source_files(source_dir: Path) -> list[Path]:
    """Return supported source files under the input directory."""
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Expected a directory, got: {source_dir}")

    files = [
        path
        for path in source_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    ]
    if not files:
        raise FileNotFoundError(
            f"No supported files found in {source_dir}. Expected: {sorted(SUPPORTED_SUFFIXES)}"
        )
    return sorted(files)


def load_documents(source_dir: Path) -> list[Document]:
    """Load source files into LangChain Documents."""
    docs: list[Document] = []
    for file_path in discover_source_files(source_dir):
        text = file_path.read_text(encoding="utf-8")
        docs.append(
            Document(
                page_content=text,
                metadata={"source": str(file_path)},
            )
        )
    return docs
