from codebase_agent.parsing.source_reader import read_source_file


def test_read_source_file(tmp_path):
    repository = tmp_path / "repo"
    repository.mkdir()

    source_file = repository / "calculator.py"
    source_file.write_text(
        "def add(a, b):\n    return a + b\n",
        encoding="utf-8",
    )

    result = read_source_file(repository, "calculator.py")

    assert result == "def add(a, b):\n    return a + b\n"