from pathlib import Path

import pytest
from langchain_core.documents import Document

from rag_baseline.config import AppConfig
from rag_baseline.documents import discover_source_files
from rag_baseline.qa import extract_sources


def test_config_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ValueError):
        AppConfig.from_env(require_api_key=True)


def test_extract_sources_deduplicates_and_preserves_order() -> None:
    docs = [
        Document(page_content="A", metadata={"source": "doc1.md"}),
        Document(page_content="B", metadata={"source": "doc2.md"}),
        Document(page_content="C", metadata={"source": "doc1.md"}),
    ]
    assert extract_sources(docs) == ["doc1.md", "doc2.md"]


def test_discover_source_files_rejects_missing_directory(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(FileNotFoundError):
        discover_source_files(missing)
