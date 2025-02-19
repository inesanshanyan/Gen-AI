from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
from prompts import PLAN_EDITS_PROMPT, EDITOR_PROMPT, CRITIQUE_PROMPT, REFLECT_PROMPT
from langgraph.graph import END

class EssayEditorAgent:
    def __init__(self, model):
        self.model = model
        
    def plan_edits_node(self, state: dict):
        messages = [
            SystemMessage(content=PLAN_EDITS_PROMPT),
            HumanMessage(content=f"Task: {state['task']}\nEssay:\n{state['essay']}")
        ]
        response = self.model.invoke(messages)
        print(type(response))
        #print("Response from model:", response)
        #print("Content:", response.content)
        state['plan_edits'] = response.content
        print("\n\n[DEBUG] Updated state in plan_edits_node:", state)

        return state
    
    def edit_essay_node(self, state: dict):
        print("\n\n[DEBUG IN THE EDIT]", state)
        if not state.get("plan_edits"):
            raise ValueError("EDIT ESSAY: No 'plan_edits' found in state!")
        messages = [
            SystemMessage(content=EDITOR_PROMPT),
            HumanMessage(content=f"Edit Plan:\n{state['plan_edits']}\n\nDraft:\n{state['draft']}")
        ]
        response = self.model.invoke(messages)
        state['draft'] = response.content
        return state

    
    def critique_essay_node(self, state: dict):
        print("\n\n[DEBUG IN CRITIQUE] :", state)
        if state.get("critique"):
            del state['critique']
        messages = [
            SystemMessage(content=CRITIQUE_PROMPT),
            HumanMessage(content=f"Task: {state['task']}\n\nDraft:\n{state['draft']}\n\nEssay:\n{state['essay']}")
        ]
        response = self.model.invoke(messages)
        state['critique'] = response.content
        return state
    
    def reflect_essay_node(self, state: dict):
        print("\n\n[DEBUG IN REFLECT]:", state)
        messages = [
            SystemMessage(content=REFLECT_PROMPT),
            HumanMessage(content=f"Edit Plan:\n{state['plan_edits']}\n\nDraft:\n{state['draft']}\n\nCritique:\n{state['critique']}")
        ]
        response = self.model.invoke(messages)
        state['draft'] = response.content
        state['revision_number'] = state['revision_number'] + 1
        return state
    
    def finish_node(self, state: dict):
        return state

    def should_continue(self, state: dict):
        if state["revision_number"] < state["max_revisions"]:
            return "critique_essay"
        return END  

