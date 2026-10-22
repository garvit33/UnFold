import shutil
import uuid
import json 
import tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path

DEFAULT_TIMEOUT_MINUTES = 30

def utc_now() -> datetime:
    return datetime.now(timezone.utc())


class SessionManager:
    def __init__(self,
            storage_root: str | Path | None = None,
            timeout_miniutes:int = DEFAULT_TIMEOUT_MINUTES,
            ):
        if(timeout_miniutes<=0):
            raise ValueError("timeout minutes must be positive")
        
        if storage_root is None:
            storage_root = (
                Path(tempfile.gettempdir())/"codebase_agent"
            )
        
        self.storage_root = Path(storage_root)
        self.storage_root.mkdir(parents=True,exist_ok=True)
        
        self.timeout = timedelta(minutes=timeout_miniutes)
        

    def session_path(self) :
        session_id = str(uuid.uuid4())
        session_path = self.storage_root/session_id 
        
        session_path.mkdir()
        
        (session_path /"repository").mkdir()
        (session_path /"vector_index").mkdir()
        
        metadata = {
            "session_id": session_id,
            "created_at": self._current_time(),
            "last_activity_at": self._current_time(),
        }
        
        self._save_metadata(session_path,metadata)
        
        return session_id

    def _current_time(self):
        return datetime.now(timezone.utc).isoformat()

    def _save_metadata(self,session_path,metadata):
        metadata_path = session_path/"metadata.json"
        
        metadata_path.write_text(
            json.dumps(metadata,indent=2),
            encoding = "utf-8",
        )
        
    def touch_session(self,session_id):
        session_path = self.storage_root/"session_id"
        metadata_path = session_path/"metadata.json"
        
        if not metadata_path.exists():
            raise FileNotFoundError("session not found")
        
        metadata = json.loads(
            metadata_path.read_text(encoding = "utf-8")
            
        )
        
        metadata["last activity at "] = self._current_time()
        
        self._save_metadata(session_path,metadata)
        
    def cleanup_session(self,session_id):
        session_path = self.storage_root/"session_id"
        
        if session_path.exists():
            shutil.rmtree(session_path)

    def cleanup_expired(self):
        now = datetime.now(timezone.utc)
        
        for session_path in self.storage_root.iterdir():
            metadata_path = session_path/"metadata.json"
            
            if not metadata_path.is_file():
                continue
            
            metadata = json.loads(
                metadata_path.read_text(encoding="utf-8")
            )       
            
            last_activity = datetime.fromisoformat(
                metadata["last_activity_at"]
            )
        
            inactive_time = now - last_activity
            
            if inactive_time > self.timeout:
                self.cleanup_Session(session_path.name)
            

    
    
    
        