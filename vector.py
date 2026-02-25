# vector.py - Setting up the vector store using ChromaDB and Ollama embeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv('patristics.csv')
embeddings = OllamaEmbeddings(model="nomic-embed-text")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        doc = Document(
            page_content=row["text"],
            metadata={"source": row["source"], "author": row["author"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(doc)
        
vector_store = Chroma(
    collection_name="patristics",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)