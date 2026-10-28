from langchain_core.documents import Document
from codebase_agent.embeddings.embedder import generate_embeddings


def test_generate_embeddings():
    chunks = [
        Document(
            page_content="def add(a, b):\n    return a + b",
            metadata={"file_path": "src/math_utils.py"},
        )
    ]

    embeddings = generate_embeddings(chunks)

    print("\nNumber of vectors:", len(embeddings))
    print("Vector dimensions:", len(embeddings[0]))
    print("First 10 values:", embeddings[0][:10])

    assert len(embeddings) == 1
    assert len(embeddings[0]) == 3072