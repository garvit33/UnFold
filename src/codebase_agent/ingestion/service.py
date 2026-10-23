from pathlib import Path
from codebase_agent.ingestion.repo_cloner import RepositoryCloner
from codebase_agent.ingestion.session_manager import SessionManager

def main():
    project_root = Path(__file__).resolve().parents[3]
    storage_root = project_root/"src"/"codebase_agent"/"temp_storage"
    
    session_manager = SessionManager(storage_root=storage_root)
    cloner = RepositoryCloner()
    
    session_id = session_manager.session_path()
    session_path = storage_root/session_id
    repository_path = session_path/"repository"
    
    repo_url = "https://github.com/octocat/Hello-World.git"
    
    try:
        cloned_path = cloner.clone(repo_url, repository_path)

        print("Session ID:", session_id)
        print("Repository cloned to:", cloned_path)

    except (RuntimeError, FileNotFoundError) as error:
        session_manager.cleanup_session(session_id)
        print("Repository setup failed:", error)

if __name__ == "__main__":
    main()
                                                