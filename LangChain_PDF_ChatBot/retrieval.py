class Retrieval:
    def __init__(self, vectordb, embeddings):
        self.vectordb = vectordb
        self.embeddings = embeddings

    def embed_query(self, query_text):
        query_embedding = self.embeddings.embed_documents([query_text])  
        return query_embedding

    def similarity_search(self, query_text, k=5):
        query_embedding = self.embed_query(query_text)
        results = self.vectordb.similarity_search_by_vector(query_embedding[0], k=k) 
        return results

