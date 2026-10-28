from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    task_type="RETRIEVAL_DOCUMENT",
)

def generate_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]
    
    return embedding_model.embed_documents(texts)
