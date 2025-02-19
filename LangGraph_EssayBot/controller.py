from langchain_openai import ChatOpenAI
from graph import Graph  

class Controller:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o")  
        self.graph = Graph(self.model)
        self.graph.build_graph() 
        
        self.latest_edited_essay = None

    def run_workflow(self, essay: str, tasks: str, use_latest: bool = False):
        state = {
            "task": tasks,
            "essay": essay,
            "draft": self.latest_edited_essay if use_latest and self.latest_edited_essay else essay,
            "critique": None,
            "revision_number": 0, 
            "max_revisions": 2,
            "finish": None
        }
        result = self.graph.app.invoke(state)
        return result["draft"]

    
    def accept_edit(self, new_edited_essay: str):
        self.latest_edited_essay = new_edited_essay
