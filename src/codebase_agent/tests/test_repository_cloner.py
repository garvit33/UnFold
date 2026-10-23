import tempfile
from pathlib import Path

from codebase_agent.ingestion.repo_cloner import RepositoryCloner


def test_clone_repository():
    repo_url = "https://github.com/octocat/Hello-World.git"

    with tempfile.TemporaryDirectory() as temp_dir:
        destination = Path(temp_dir) / "Hello-World"
        cloner = RepositoryCloner()

        cloned_path = cloner.clone(repo_url, destination)

        assert cloned_path.exists()
        assert cloned_path.is_dir()
        assert any(cloned_path.iterdir())