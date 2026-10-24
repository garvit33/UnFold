
from codebase_agent.ingestion.filter import filter_inventory


def test_filter_inventory():
    inventory = [
        {"path": "src/main.py", "extension": ".py", "size_bytes": 100},
        {"path": "src/__pycache__/main.pyc", "extension": ".pyc", "size_bytes": 50},
        {"path": "node_modules/lib/index.js", "extension": ".js", "size_bytes": 200},
        {"path": "README.md", "extension": ".md", "size_bytes": 80},
        {"path": "build/output.py", "extension": ".py", "size_bytes": 300},
        {"path": "src/.DS_Store", "extension": "", "size_bytes": 20},
    ]

    result = filter_inventory(inventory)

    paths = {file_info["path"] for file_info in result}

    assert paths == {"src/main.py", "README.md"}
