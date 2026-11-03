from pathlib import Path
from langchain_chroma import Chroma
from uuid import uuid4
from codebase_agent.embeddings.embedder import embedding_model,generate_embeddings


def create_vector_store(
    chunks,
    persist_directory:Path, 
) -> Chroma:
    
    if not chunks: 
        raise ValueError("cannot create vector store without chunks.")
    
    persist_directory.mkdir(parents=True,exist_ok=True)
    
    texts = [chunk.page_content for chunk in chunks]
    metadatas =[chunk.metadata for chunk in chunks]

    vectors = generate_embeddings(texts)
    
    vector_store = Chroma(
        collection_name ="code_chunks",
        embedding_function=embedding_model,
        persist_directory=str(persist_directory)
    )
    
    ids = [str(uuid4()) for _ in chunks]
    
    vector_store._collection.add(
        documents=texts,
        embeddings = vectors,
        metadatas = metadatas,
        ids=ids,
        )
    
    return vector_store 