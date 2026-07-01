# rag.py
# ChromaDB에 저장된 생활 문서를 검색하는 모듈

import os
from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings


DB_PATH = "./chroma_db"
EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")


def load_vector_db():
    """저장된 Chroma 벡터DB를 불러온다."""
    if not Path(DB_PATH).exists():
        raise FileNotFoundError(
            "chroma_db가 없습니다. 먼저 `python build_vector_db.py`를 실행하세요."
        )

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    return vectordb


def format_docs_with_sources(docs) -> str:
    """검색된 문서를 출처와 함께 프롬프트에 넣기 좋은 문자열로 변환한다."""
    formatted = []

    for index, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        content = doc.page_content.strip()
        formatted.append(f"[문서 {index}: {source}]\n{content}")

    return "\n\n".join(formatted)


def search_life_docs(query: str, k: int = 4) -> str:
    """
    생활 문서에서 질문과 관련된 내용을 검색한다.

    Args:
        query: 사용자 질문
        k: 가져올 문서 chunk 개수

    Returns:
        검색된 문서 내용 문자열
    """
    vectordb = load_vector_db()
    docs = vectordb.similarity_search(query, k=k)

    if not docs:
        return "관련 문서를 찾지 못했습니다."

    return format_docs_with_sources(docs)


def search_personal_docs(query: str, k: int = 4) -> str:
    """기존 코드 호환을 위한 별칭."""
    return search_life_docs(query, k=k)


if __name__ == "__main__":
    # 단독 실행 테스트
    test_query = "교수님께 메일 보낼 때 어떻게 써야 해?"
    result = search_life_docs(test_query)

    print("[검색 질문]")
    print(test_query)

    print("\n[검색 결과]")
    print(result)
