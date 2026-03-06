"""CLI entrypoint for the RAG baseline project."""

from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path

from dotenv import load_dotenv

from .config import AppConfig
from .indexer import build_index
from .qa import answer_question


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="rag-baseline",
        description="Index local files and ask grounded questions with LangChain.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Build vector index from source docs.")
    index_parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("data/source_docs"),
        help="Directory containing .txt or .md files.",
    )
    index_parser.add_argument(
        "--vectorstore-dir",
        type=Path,
        default=None,
        help="Override vectorstore output directory.",
    )

    ask_parser = subparsers.add_parser("ask", help="Ask a question against the index.")
    ask_parser.add_argument("question", type=str, help="Question to answer.")
    ask_parser.add_argument(
        "--vectorstore-dir",
        type=Path,
        default=None,
        help="Override vectorstore directory.",
    )

    return parser


def main() -> None:
    """Run CLI command."""
    load_dotenv()
    args = build_parser().parse_args()
    config = AppConfig.from_env(require_api_key=True)

    if args.vectorstore_dir is not None:
        config = replace(config, vectorstore_dir=args.vectorstore_dir)

    if args.command == "index":
        chunk_count = build_index(config, source_dir=args.source_dir)
        print(f"Indexed {chunk_count} chunks into {config.vectorstore_dir}.")
        return

    if args.command == "ask":
        answer, sources = answer_question(config, question=args.question)
        print("Answer:\n")
        print(answer)
        print("\nSources:")
        for source in sources:
            print(f"- {source}")
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
