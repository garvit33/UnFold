
import json
from pathlib import Path

from codebase_agent.ingestion import service


def test_service_with_real_repository(tmp_path, monkeypatch):
    # Keep test data separate from normal project storage
    monkeypatch.setattr(
        service,
        "__file__",
        str(
            tmp_path
            / "src"
            / "codebase_agent"
            / "ingestion"
            / "service.py"
        ),
    )

    service.main()

    # Locate the generated session
    storage_root = (
        tmp_path
        / "src"
        / "codebase_agent"
        / "temp_storage"
    )

    sessions = list(storage_root.iterdir())
    assert len(sessions) == 1

    session_path = sessions[0]
    inventory_path = session_path / "inventory.json"
    repository_path = session_path / "repository"

    # Check that cloning and inventory generation worked
    assert repository_path.is_dir()
    assert inventory_path.is_file()

    inventory = json.loads(
        inventory_path.read_text(encoding="utf-8")
    )

    assert isinstance(inventory, list)
    assert len(inventory) > 0

    # Check the structure of each inventory record
    for file_info in inventory:
        assert "path" in file_info
        assert "extension" in file_info
        assert "size_bytes" in file_info
        assert "language" in file_info

    # Check that the repository actually contains files
    assert any(path.is_file() for path in repository_path.rglob("*"))
