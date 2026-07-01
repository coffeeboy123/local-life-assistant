# build_vector_db.py
# data 폴더의 생활 문서를 읽고 Chroma 벡터DB로 저장하는 파일

import os
import shutil
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_DIR = Path("data")
DB_PATH = "./chroma_db"
EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")


def load_supported_documents():
    """data 폴더 아래의 Markdown, PDF 문서를 모두 불러온다."""
    paths = sorted(
        list(DATA_DIR.rglob("*.md"))
        + list(DATA_DIR.rglob("*.txt"))
        + list(DATA_DIR.rglob("*.pdf"))
    )

    if not paths:
        raise FileNotFoundError("data 폴더에서 문서를 찾지 못했습니다.")

    documents = []

    for path in paths:
        suffix = path.suffix.lower()

        if suffix in {".md", ".txt"}:
            loader = TextLoader(str(path), encoding="utf-8")
        elif suffix == ".pdf":
            loader = PyPDFLoader(str(path))
        else:
            continue

        loaded = loader.load()

        for document in loaded:
            document.metadata["source"] = str(path)
            document.metadata["title"] = path.stem
            document.metadata["file_type"] = suffix

        documents.extend(loaded)

    return documents


def main():
    if Path(DB_PATH).exists():
        shutil.rmtree(DB_PATH)
        print("기존 chroma_db 삭제 완료")

    documents = load_supported_documents()

    print(f"로드된 문서 개수: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    splits = splitter.split_documents(documents)

    print(f"분할된 chunk 개수: {len(splits)}")

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

    Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("벡터DB 생성 완료")
    print(f"저장 위치: {DB_PATH}")
    print(f"임베딩 모델: {EMBEDDING_MODEL}")


if __name__ == "__main__":
    main()