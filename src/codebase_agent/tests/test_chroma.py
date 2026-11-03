
from pathlib import Path

from langchain_core.documents import Document

from codebase_agent.vector_store.chroma_store import (
    create_vector_store,
)


def test_create_real_chroma_database():

    project_root = Path(__file__).resolve().parents[3]

    persist_directory = (
        project_root
        / "src"
        / "codebase_agent"
        / "temp_storage"
        / "test_session"
        / "chroma_db"
    )

    chunks = [
        Document(
            page_content="def add(a, b): return a + b",
            metadata={
                "file_path": "math_utils.py",
                "language": "Python",
            },
        ),
        Document(
            page_content="def greet(name): return f'Hello {name}'",
            metadata={
                "file_path": "greetings.py",
                "language": "Python",
            },
        ),
        Document(
            page_content="def multiply(a, b): return a * b",
            metadata={
                "file_path": "calculator.py",
                "language": "Python",
            },
        ),
    ]

    vector_store = create_vector_store(
        chunks=chunks,
        persist_directory=persist_directory,
    )

    count = vector_store._collection.count()

    print(f"\nDatabase location: {persist_directory}")
    print(f"Stored chunks: {count}")

    assert count == len(chunks)
    assert persist_directory.exists()

    results = vector_store.similarity_search(
        "How do we multiply two numbers?",
        k=2,
    )

    print("\nRetrieved chunks:")

    for result in results:
        print("\nFile:", result.metadata["file_path"])
        print("Code:", result.page_content)

    assert len(results) == 2
