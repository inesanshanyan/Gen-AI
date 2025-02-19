## Essay Editing Bot with LangGraph

This bot is built using **LangGraph** and **Gradio** to provide an interactive interface for editing essays. Users can edit both the latest version of the essay and the original one, with the ability to track changes and apply edits dynamically.

## How to Use

1. **Clone the Repository**  
   Clone this repository to your local machine.

2. **Install Necessary Libraries**  
   Make sure you have Python 3 installed. Then, install the required libraries by running:

   ```bash
   pip install langgraph langchain-openai gradio langchain-core
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


4. **Run the EssayBot**  
   Execute the chatbot by running:

   ```bash
   python3 main.py
   ```

5. **Interface Preview**  
   You will first see a textbox for inserting your essay and another for entering your task. Once you have done that, press the Edit Original Essay button. The interface will display the edited version of your essay, along with the Edit History section.

   Afterward, a new button will appear labeled Edit Latest Edited Essay. You can now input a new task and choose either the Edit Original Essay or the Edit Latest Edited Essay button, depending on which version of your essay you would like to modify.

   Every change made will be automatically recorded in the Edit History textbox.

## File Structure

The project has the following structure:

```
├── controller.py          # Manages the overall flow and interactions
├── essay_editor.py        # Handles essay editing logic
├── gradio_view.py         # Manages the Gradio interface
├── graph.py               # Builds the graph
├── main.py                # Main script to run the bot
└── prompts.py             # Contains system prompts and instructions
```

