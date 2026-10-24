from pathlib import Path

def build_inventory(repository_path: str|Path) -> list[dict]:
    repository_path = Path(repository_path)
    
    if not repository_path.exists():
        raise FileNotFoundError(f"repository path doesnt exists : {repository_path}")
    
    if not repository_path.is_dir():
        raise NotADirectoryError(f"given path is not a directory: {repository_path}")
    
    inventory = []
    
    for file_path in repository_path.rglob("*"):
        if not file_path.is_file():
            continue
        
        file_info = {
            "path": str(file_path.relative_to(repository_path).as_posix()),
            "extension": file_path.suffix.lower(),
            "size_bytes": file_path.stat().st_size,
        }
        
        inventory.append(file_info)
        
    return inventory