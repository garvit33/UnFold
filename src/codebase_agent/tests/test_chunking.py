
from codebase_agent.parsing.chunker import chunk_source_code


def test_chunk_multiple_files():
    files = [
        {
            "path": "src/main.py",
            "language": "Python",
            "source_code": "def greet():\n    print('Hello')\n",
        },
        {
            "path": "src/utils.js",
            "language": "JavaScript",
            "source_code": "function add(a, b) {\n    return a + b;\n}\n",
        },
    ]

    all_chunks = []

    for file_info in files:
        chunks = chunk_source_code(
            source_code=file_info["source_code"],
            file_path=file_info["path"],
            language=file_info["language"],
        )

        all_chunks.extend(chunks)

    # Check that chunks were generated
    assert len(all_chunks) > 0

    # Check that both files are represented
    file_paths = {
        chunk.metadata["file_path"]
        for chunk in all_chunks
    }

    assert "src/main.py" in file_paths
    assert "src/utils.js" in file_paths

    # Print output so we can inspect it
    for i, chunk in enumerate(all_chunks, start=1):
        print(f"\n--- Chunk {i} ---")
        print("File:", chunk.metadata["file_path"])
        print("Language:", chunk.metadata["language"])
        print("Content:")
        print(chunk.page_content)
