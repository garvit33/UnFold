
from pathlib import Path

from codebase_agent.ingestion.inventory import build_inventory


def test_build_inventory(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text(
        "print('hello')",
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "# My project",
        encoding="utf-8",
    )

    result = build_inventory(tmp_path)

    assert len(result) == 2

    paths = {item["path"] for item in result}
    assert paths == {"src/main.py", "README.md"}

    python_file = next(
        item for item in result if item["path"] == "src/main.py"
    )
    assert python_file["extension"] == ".py"
    assert python_file["size_bytes"] == len(
        "print('hello')".encode("utf-8")
    )
