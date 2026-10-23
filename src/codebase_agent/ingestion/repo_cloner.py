import subprocess
from pathlib import Path

class RepositoryCloner:
    def __init__(self):
        pass
    
    def clone(self,repo_url:str,destination: Path)->Path:
        try:
            subprocess.run(
                [
                    "git",
                    "clone",
                    "--depth","1",
                    "--",
                    repo_url,
                    str(destination),
                ],
                check = True,
                capture_output=True,
                text=True,
                timeout=120,
            )
            
            return destination
        
        except subprocess.CalledProcessError as error:
            raise RuntimeError(
                f"Git clone failed: {error.stderr.strip()}"
            ) from error
            
        except subprocess.TimeoutExpired as error:
            raise RuntimeError(
                "Git clone timed out"
            )from error
        