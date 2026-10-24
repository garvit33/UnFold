from pathlib import PurePosixPath

EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".h": "C/C++ Header",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".hpp": "C++ Header",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".dart": "Dart",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".sql": "SQL",
    ".sh": "Shell",
    ".ps1": "PowerShell",
    ".r": "R",
    ".ipynb": "Jupyter Notebook",
    ".md": "Markdown",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".xml": "XML",
    ".vue": "Vue",
    ".svelte": "Svelte",
}

def detect_language(file_path: str) -> str:
    extension = PurePosixPath(file_path).suffix.lower()
    
    return EXTENSION_LANGUAGE_MAP.get(extension,"Unknown")