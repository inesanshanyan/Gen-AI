import os
import shutil

from langchain_community.vectorstores import Chroma

class VectorStore:
    def __init__(self, embeddings, persist_directory='docs/chroma'):
        self.embeddings = embeddings
        self.persist_directory = persist_directory
              
    def reset_directory(self):
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            #print(f"Deleted existing vector store: {self.persist_directory}")

    def embed_and_store(self, documents):
     
        vectordb = Chroma.from_documents(documents, self.embeddings, persist_directory=self.persist_directory)
        vectordb.persist() 
            
        return vectordb
