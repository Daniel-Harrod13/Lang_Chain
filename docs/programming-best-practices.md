# Programming Best Practices

This page defines the coding standards for projects in this repository.

## Core Principles

- Write code that is easy to read before optimizing for cleverness.
- Prefer small, composable modules over large multi-purpose files.
- Fail fast with clear errors when configuration or inputs are invalid.
- Keep behavior deterministic and reproducible where possible.

## Project Structure

- Use feature-focused folders with `src/`, `tests/`, and `README.md`.
- Keep business logic out of CLI scripts and notebook cells.
- Separate configuration, data loading, indexing, and inference paths.
- Avoid circular imports and hidden global state.

## Python Standards

- Use Python 3.10+ features responsibly with explicit type hints.
- Add docstrings for public functions, classes, and modules.
- Prefer `pathlib.Path` over string path manipulation.
- Use dataclasses for config objects with validation helpers.
- Raise specific exceptions with actionable messages.

## Security and Secrets

- Never commit API keys, tokens, private keys, or credential files.
- Load secrets from environment variables (for example via `.env` in local dev).
- Keep `.env.example` in version control and `.env` ignored.
- Validate required environment variables at startup.
- Minimize logging of raw prompts, user content, and sensitive metadata.

## LangChain / LLM Practices

- Keep prompts versioned and explicit; avoid hidden prompt strings.
- Isolate model provider code behind small adapter functions/classes.
- Keep retrieval settings configurable (chunk size, overlap, `k`, similarity type).
- Store source metadata with chunks for traceability.
- Return source citations with answers whenever possible.

## Testing

- Add unit tests for core logic and edge cases.
- Mock external systems (LLM providers, vector stores, network) in unit tests.
- Keep tests fast and deterministic; use integration tests separately.
- Treat tests as documentation for expected behavior.

## Quality and Tooling

- Run formatting and lint checks before pushing changes.
- Use meaningful commit messages that explain intent, not only file changes.
- Prefer incremental PRs that are easy to review.
- Document trade-offs and TODOs directly in project docs.

## Documentation Expectations

- Every project should include:
  - problem statement
  - architecture overview
  - setup instructions
  - how to run
  - limitations and next steps
- Update docs in the same change where behavior changes.

## Practical Definition of "Good Code" for This Repo

Good code here means code that is:
- understandable by another student in one quick read
- safe with secrets and external APIs
- testable without production credentials
- documented enough to reproduce and extend
