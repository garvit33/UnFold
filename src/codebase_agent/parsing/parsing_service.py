from pathlib import Path

from src.codebase_agent.parsing.source_reader import read_source_file
from src.codebase_agent.parsing.chunker import chunk_source_code

def parse_repository(
    repository_path:Path,
    filtered_inventory: list[dict],
) -> list:
    all_chunks = []
    
    for file_info in filtered_inventory:
        relative_path = file_info["path"]
        language = file_info.get("language","Unknown")
    
        
        try:
            source_code = read_source_file(
                repository_path,
                relative_path,
            )        
        except OSError as exc:
            print(f"skipping {relative_path}: {exc}")
            continue
            
        if not source_code.strip():
            continue
        
        chunks = chunk_source_code(
            source_code=source_code,
            file_path=relative_path,
            language=language,
        )
        
        all_chunks.extend(chunks)
        
    return all_chunks