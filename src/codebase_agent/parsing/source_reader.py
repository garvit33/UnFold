from pathlib import Path

def read_source_file(
    repository_path: str|Path,
    relative_path: str|Path,
) -> str:
    repository_path = Path(repository_path)
    file_path = repository_path/relative_path
    
    return file_path.read_text(
        encoding="utf-8",
        errors="replace",
    )
    
    