# LangChain Projects

A personal workspace for building and documenting LangChain-based projects.

I am an AI graduate student, and this repository is dedicated to hands-on experiments in:
- LLM application development
- Retrieval-Augmented Generation (RAG)
- Agent workflows and tool use
- Evaluation, reliability, and prompt engineering

## Why This Repo Exists

This repository is my practical learning lab for turning AI concepts into real systems.  
Each project is designed to strengthen both research understanding and engineering skills.

## Repository Layout

- `projects/` - Hands-on LangChain projects (production-style scaffolds)
- `docs/` - Engineering standards and project documentation
- `.env.example` - Environment variable template (safe to commit)
- `.gitignore` - Security-first ignore rules for secrets and local artifacts

## Current Projects

- `projects/01_rag_baseline/` - Local-document RAG baseline with indexing, retrieval, and source-cited answers.

## Planned Project Areas

- `rag/` - Retrieval pipelines, chunking strategies, and vector search experiments
- `agents/` - Tool-using agents and multi-step reasoning workflows
- `chatbots/` - Domain-focused assistants and conversational interfaces
- `evaluation/` - Prompt, response quality, latency, and cost benchmarking
- `notebooks/` - Research notes, prototypes, and experiment tracking

## Engineering Standards

- `docs/programming-best-practices.md` - Repository coding standards for structure, security, testing, and LLM application quality.

## Tech Stack (Expected)

- Python 3.10+
- LangChain
- OpenAI (or other model providers)
- Vector databases (e.g., Chroma, FAISS, Pinecone)
- Jupyter notebooks for rapid experimentation

## Start Here

Use this order:
1. Read `docs/programming-best-practices.md`
2. Run `projects/01_rag_baseline/`
3. Extend with experiments and evaluations

## Getting Started (Repo)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Lang_Chain
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Create your environment file from the template:
   ```bash
   cp .env.example .env
   ```
4. Install dependencies for a project (example first project):
   ```bash
   cd projects/01_rag_baseline
   pip install -r requirements.txt
   ```
5. Add your API key in `.env`:
   ```bash
   OPENAI_API_KEY=your_key_here
   ```

## Quickstart: Project 01 RAG Baseline

From repo root:

```bash
cd projects/01_rag_baseline
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../../.env.example .env
```

Then:

1. Put `.txt` or `.md` files in `projects/01_rag_baseline/data/source_docs/`
2. Build index:
   ```bash
   PYTHONPATH=src python -m rag_baseline.main index
   ```
3. Ask a question:
   ```bash
   PYTHONPATH=src python -m rag_baseline.main ask "What is this project about?"
   ```

## Roadmap

- [x] Create base project structure
- [x] Add first RAG prototype
- [ ] Add first agentic workflow
- [ ] Add evaluation scripts
- [ ] Document results and lessons learned

## Notes

This README will evolve as projects are added.  
The goal is to keep this repo focused, reproducible, and research-informed.