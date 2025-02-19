# PDF Question-Answering Chatbot

This chatbot is built using **LangChain** and is designed to answer questions about a specific PDF document. You can insert a PDF file, and the chatbot will provide answers based on the content of the document.

## How to Use

1. **Clone the Repository**  
   Clone this repository to your local machine.

2. **Install Necessary Libraries**  
   Make sure you have Python 3 installed. Then, install the required libraries by running:

   ```bash
   pip install langchain langchain-community langchain-openai openai chromadb
   ```

3. **Set Up Environment Variables**  
   Create a `.env` file and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Then, update the API key path in `main.py`:

   ```python
   _ = load_dotenv("path")  # your absolute path to .env file
   ```

4. **Insert Your PDF File**  
   Place your PDF file in the project directory. Update the `main.py` file to point to your PDF file:

   ```python
   controller = Controller("./your_pdf_file.pdf")
   ```

5. **Run the Chatbot**  
   Execute the chatbot by running:

   ```bash
   python3 main.py
   ```

6. **Ask Questions**  
   Once the chatbot is running, you can ask questions about the PDF document. Type `exit` to end the conversation.

## File Structure

The project has the following structure:

```
|──Metamorphosis.pdf        # Example PDF file
├── main.py                 # Main script to run the chatbot
├── p_vs_np.pdf             # Example PDF file
├── pdf_processor.py        # Handles PDF loading and processing
├── question_and_answer.py  # Manages the Q&A logic 
├── retrieval.py            # Handles document retrieval for answering queries
└── vector_store.py         # Manages vector storage for efficient searching
```

