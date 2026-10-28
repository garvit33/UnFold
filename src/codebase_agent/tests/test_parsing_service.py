
from pathlib import Path
from unittest.mock import patch

from codebase_agent.parsing.parsing_service import parse_repository


def test_parse_repository_collects_chunks():
    repo_path = Path("/fake/repo")

    inventory = [
        {"path": "main.py", "language": "Python"},
        {"path": "utils.py", "language": "Python"},
    ]

    with (
        patch(
            "codebase_agent.parsing.parsing_service.read_source_file",
            side_effect=["print('hello')", "def add(a, b): return a + b"],
        ),
        patch(
            "codebase_agent.parsing.parsing_service.chunk_source_code",
            side_effect=[
                ["chunk1", "chunk2"],
                ["chunk3"],
            ],
        ) as mock_chunk,
    ):
        chunks = parse_repository(repo_path, inventory)

    assert chunks == ["chunk1", "chunk2", "chunk3"]
    assert mock_chunk.call_count == 2


def test_parse_repository_skips_empty_files():
    repo_path = Path("/fake/repo")

    inventory = [
        {"path": "empty.py", "language": "Python"},
        {"path": "main.py", "language": "Python"},
    ]

    with (
        patch(
            "codebase_agent.parsing.parsing_service.read_source_file",
            side_effect=["   \n\t", "print('hello')"],
        ),
        patch(
            "codebase_agent.parsing.parsing_service.chunk_source_code",
            return_value=["valid_chunk"],
        ) as mock_chunk,
    ):
        chunks = parse_repository(repo_path, inventory)

    assert chunks == ["valid_chunk"]
    assert mock_chunk.call_count == 1


def test_parse_repository_skips_unreadable_files():
    repo_path = Path("/fake/repo")

    inventory = [
        {"path": "broken.py", "language": "Python"},
        {"path": "main.py", "language": "Python"},
    ]

    with (
        patch(
            "codebase_agent.parsing.parsing_service.read_source_file",
            side_effect=[
                OSError("Permission denied"),
                "print('hello')",
            ],
        ),
        patch(
            "codebase_agent.parsing.parsing_service.chunk_source_code",
            return_value=["valid_chunk"],
        ),
    ):
        chunks = parse_repository(repo_path, inventory)

    assert chunks == ["valid_chunk"]
