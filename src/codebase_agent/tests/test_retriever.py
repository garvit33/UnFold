
from pathlib import Path

from codebase_agent.vector_store.retriever import retrieve_code


def test_retrieve_code():

    project_root = Path(__file__).resolve().parents[3]

    persist_directory = (
        project_root
        / "src"
        / "codebase_agent"
        / "temp_storage"
        / "test_session"
        / "chroma_db"
    )

    query = input("\nAsk something about the codebase: ")

    results = retrieve_code(
        query=query,
        persist_directory=persist_directory,
        k=5,
    )

    print("\n========== RETRIEVED CODE ==========")

    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}")
        print("File:", result.metadata["file_path"])
        print("Language:", result.metadata["language"])
        print("Code:\n", result.page_content)

    print("\nTotal chunks retrieved:", len(results))
