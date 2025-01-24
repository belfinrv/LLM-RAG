import re
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

class ChatUtility:
    def __init__(self, repo_id="meta-llama/Llama-3.2-3B-Instruct"):
        self.llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"max_new_tokens": 100})
        self.memory = ConversationBufferMemory(input_key="question", memory_key="history")
        self.prompt_template = PromptTemplate(
            input_variables=["history", "context", "question"],
            template="""
            Use the following pieces of information enclosed in <context> tags to provide an answer to the question enclosed in <question> tags.
            Also consider the previous conversation history:
            <history>
            {history}
            </history>
            <context>
            {context}
            </context>
            <question>
            {question}
            </question>
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template, memory=self.memory)

    def get_answer(self, context, question):
        raw_answer = self.chain.run({
            "history": self.memory.load_memory_variables({}).get("history", ""),
            "context": context,
            "question": question
        })
        return re.sub(r'<.*?>', '', raw_answer).strip()
