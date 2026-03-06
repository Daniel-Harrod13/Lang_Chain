# Project 01: RAG Baseline

A clean baseline Retrieval-Augmented Generation (RAG) project using LangChain.

## Goal

Create a reproducible starting point for:
- indexing local text/markdown documents
- retrieving relevant chunks for a question
- generating grounded answers with source references

## Structure

- `src/rag_baseline/` - core package code
- `tests/` - unit tests for key logic
- `data/source_docs/` - input corpus for indexing
- `requirements.txt` - project dependencies

## Setup

```bash
cd projects/01_rag_baseline
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` in this folder (or repo root):

```bash
OPENAI_API_KEY=your_key_here
RAG_CHAT_MODEL=gpt-4o-mini
RAG_EMBEDDING_MODEL=text-embedding-3-small
RAG_CHUNK_SIZE=800
RAG_CHUNK_OVERLAP=120
RAG_RETRIEVAL_K=4
RAG_VECTORSTORE_DIR=data/vectorstore
```

## Run

From `projects/01_rag_baseline`:

1) Add source files in `data/source_docs/` (`.txt` or `.md`)

2) Build index:

```bash
PYTHONPATH=src python -m rag_baseline.main index
```

3) Ask a question:

```bash
PYTHONPATH=src python -m rag_baseline.main ask "What is this project about?"
```

## Testing

```bash
PYTHONPATH=src pytest -q
```

## Next Improvements

- add reranking and retrieval metrics
- add prompt evaluation scripts
- add ingestion for PDFs and web content
