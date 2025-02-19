import os

from pdf_processor import PDFProcessor
from vector_store import VectorStore
from retrieval import Retrieval
from question_and_answer import Question_and_Answer

from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

class Controller:
    def __init__(self, path, query=None):
        self.pdf_path = path
        self.pdf_processor = PDFProcessor()
        self.embeddings = OpenAIEmbeddings()
        self.query = query
        self.llm = ChatOpenAI(temperature=0.0, model_name="gpt-4o")
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.vector_store = None  
        
    def run(self):
        #print(f"query received: {self.query}, type: {type(self.query)}  ")
        
        if not self.query or not isinstance(self.query, str):
            raise ValueError("The query must be a non empty string")

        if not self.vector_store: 
            self.chunks = self.process_pdf()
            self.vector_store = self.vector_store_method(self.chunks)

        retrieval = Retrieval(self.vector_store, self.embeddings)
        retrieved_docs = retrieval.similarity_search(self.query, k=5)

        if not retrieved_docs:
            return "No relevant information in the doc"

        question_and_answer = Question_and_Answer(self.llm, self.memory, self.query)
        answer = question_and_answer.question_and_answer(retrieved_docs)
        
        return answer

    def process_pdf(self):
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"The PDF file {self.pdf_path} does not exist")
        
        document = self.pdf_processor.load_pdf(self.pdf_path)
        chunks = self.pdf_processor.split_text(document)
        
        return chunks

    def vector_store_method(self, chunks):
        vector_store = VectorStore(embeddings=self.embeddings)
        vector_store.reset_directory()
        vectordb = vector_store.embed_and_store(chunks)
        
        return vectordb
