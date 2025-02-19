from langgraph.graph import StateGraph, END
from essay_editor import EssayEditorAgent

class Graph:
    def __init__(self, model):
        self.model = model
        self.builder = StateGraph(dict)
        self.agent = EssayEditorAgent(self.model)
        
        self.app = None 
        
    def build_graph(self):
        if self.app:  
            return
        
        self.builder.add_node("plan_edits", self.agent.plan_edits_node)
        self.builder.add_node("edit_essay", self.agent.edit_essay_node)
        self.builder.add_node("critique_essay", self.agent.critique_essay_node)
        self.builder.add_node("reflect_essay_node", self.agent.reflect_essay_node)
        self.builder.add_node("finish", self.agent.finish_node)
        

        self.builder.add_edge("plan_edits", "edit_essay")
        self.builder.add_edge("edit_essay", "critique_essay")
        self.builder.add_edge("critique_essay", "reflect_essay_node")

   
        self.builder.add_conditional_edges(
            "reflect_essay_node", 
            self.agent.should_continue, 
            {"critique_essay": "critique_essay", END: "finish"}
        )
        
        #print("Graph nodes:", self.builder.nodes)
        #print("Graph edges:", self.builder.edges)

        self.builder.set_entry_point("plan_edits")
        self.builder.set_finish_point("finish")

        self.app = self.builder.compile()
        
        print("\n\nApp compiled and ready.")

