from pathlib import Path
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

query_embedding_model = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001",
    task_type="RETRIEVAL_QUERY",
)

def retrieve_code(query: str,
                  persist_directory:Path,
                  k:int = 5,
):
    if not query.strip():
        raise ValueError("query cannot be empty")
    
    if not persist_directory.exists():
        raise FileNotFoundError("vector db not found")
    
    vector_store = Chroma(
        collection_name="code_chunks",
        embedding_function=query_embedding_model,
        persist_directory=str(persist_directory),
    )
    
    results = vector_store.similarity_search(
        query=query,
        k=k,
    )
    
    return results