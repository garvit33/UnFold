
from codebase_agent.ingestion.language_detector import detect_language


def test_detect_python():
    assert detect_language("src/main.py") == "Python"


def test_detect_typescript():
    assert detect_language("src/App.tsx") == "TypeScript"


def test_detect_cpp():
    assert detect_language("src/main.cpp") == "C++"


def test_detect_unknown():
    assert detect_language("data/file.xyz") == "Unknown"


def test_detect_uppercase_extension():
    assert detect_language("src/MAIN.PY") == "Python"
