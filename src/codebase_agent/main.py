from langgraph.graph import StateGraph,START,END
from codebase_agent.ingestion.service import ingest_repository
from typing import TypedDict

#state

class WorkflowState(TypedDict):
    
    repo_url:str
    question:str
    
    #ingestion
    session_id:str  
    repository_path:str
    filtered_inventory:list
    
    #parsing
    chunks: list
    
    
    #vector storgr
    persist_directory:str
    
    #retrieval
    retrieved_chunks:list
    
    #generation
    answer:str
    

def ingest_node(state: WorkflowState):
    result = ingest_repository(state["repo_url"])
    
    return{
        "session_id": result["session_id"],
        "repository_path": result["repository_path"],
        "filtered_inventory": result["filtered_inventory"],
        "persist_directory": result["storage_root"]
    }
    
    


