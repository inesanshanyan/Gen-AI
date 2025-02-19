from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFProcessor:
    def load_pdf(self, path):
        self.pdf_path = path
        loader = PyPDFLoader(self.pdf_path)
        pdf_content = loader.load()
        return pdf_content
        
        
    def split_text(self, document, chunk_size=1500, chunk_overlap=200):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return splitter.split_documents(document)

        
        
        
        
