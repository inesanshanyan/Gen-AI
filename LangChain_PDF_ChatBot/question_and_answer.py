from langchain.schema import AIMessage

class Question_and_Answer:
    def __init__(self, llm, memory, query):
        self.llm = llm
        self.memory = memory
        self.query = query

    def question_and_answer(self, retrieved_docs):
        context = " ".join([doc.page_content for doc in retrieved_docs])
        conversation_history = self.memory.chat_memory.messages
        if conversation_history:
            context = "\n".join([message.content for message in conversation_history[-5:]]) + "\n" + context

        prompt = f"Answer the following question based on the provided context:\n\nContext: {context}\n\nQuestion: {self.query}\nAnswer:"

        response = self.llm.predict(prompt)

        ai_message = AIMessage(content=response)
        self.memory.chat_memory.add_message(ai_message)

        user_message = AIMessage(content=self.query) 
        self.memory.chat_memory.add_message(user_message)

        return response
