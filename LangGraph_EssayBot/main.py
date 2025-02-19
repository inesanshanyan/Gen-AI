from gradio_view import build_gradio_ui
from controller import Controller

from dotenv import load_dotenv

_ = load_dotenv("path") # your absolute path to .env file

controller = Controller()  
gradio_ui = build_gradio_ui(controller)
gradio_ui.launch()
