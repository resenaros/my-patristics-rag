from langchain_ollama import Ollamaembeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv('patristics.csv')
embeddings = Ollamaembeddings(model="embeddings")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        doc = Document(
            page_content=row["Author"] + " " + row["Text"] + " " + row["Source"],
            metadata={"source": row["Source"], "author": row["Author"]}
        )