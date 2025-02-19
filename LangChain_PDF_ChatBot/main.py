import os
import openai

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from controller import Controller

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv("path") # your absolute path to .env file
openai.api_key = os.environ['OPENAI_API_KEY']

controller = Controller("./Metamorphosis.pdf")
#controller = Controller("./p_vs_np.pdf")

print("Ask questions about the document, type 'exit' to end")

while True:
    query = input("Your question: ")
    
    if query.lower() == 'exit':
        print("Ending the conversation")
        break
    
    if not query.strip():
        print("Enter a valid question")
        continue
    
    controller.query = query
    answer = controller.run()
    print("Answer: ", answer)
    