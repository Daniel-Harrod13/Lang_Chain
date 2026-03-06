"""Question-answering flow for the RAG baseline."""

from __future__ import annotations

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from .config import AppConfig

RAG_PROMPT = ChatPromptTemplate.from_template(
    """You are a precise research assistant.
Answer the question using only the context below.
If the answer is not in the context, say you do not have enough information.

Context:
{context}

Question:
{question}
"""
)


def extract_sources(docs: list[Document]) -> list[str]:
    """Collect unique source paths from retrieved chunks."""
    seen: set[str] = set()
    ordered: list[str] = []
    for doc in docs:
        source = str(doc.metadata.get("source", "unknown"))
        if source not in seen:
            seen.add(source)
            ordered.append(source)
    return ordered


def answer_question(config: AppConfig, question: str) -> tuple[str, list[str]]:
    """Run retrieval + generation and return answer with source paths."""
    embeddings = OpenAIEmbeddings(
        model=config.embedding_model,
        api_key=config.openai_api_key,
    )
    vectorstore = Chroma(
        persist_directory=str(config.vectorstore_dir),
        embedding_function=embeddings,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": config.retrieval_k})
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)
    llm = ChatOpenAI(model=config.chat_model, temperature=0, api_key=config.openai_api_key)
    messages = RAG_PROMPT.format_messages(context=context, question=question)
    response = llm.invoke(messages)

    return str(response.content), extract_sources(docs)
