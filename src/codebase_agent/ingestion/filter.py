from pathlib import PurePosixPath

IGNORED_DIRS = {
     ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
}

IGNORED_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".class",
}

IGNORED_FILES = {
    ".ds_store",
    "thumbs.db",
}
def filter_inventory(inventory: list[dict]) -> list[dict]:
    
    filtered_files = []
    
    for file_info in inventory:
        path = PurePosixPath(file_info["path"])
        filename = path.name.lower()
        
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        
        if path.suffix.lower() in IGNORED_EXTENSIONS:
            continue
        
        if filename in IGNORED_FILES:
            continue
        
        filtered_files.append(file_info)
        
    return filtered_files
