"""

@author: Jinal Shah

This class represents the agent

"""
from langchain_openai import OpenAI
from langchain.chains import LLMMathChain
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType

class Agent:
    # Constructor
    def __init__(self,api_key,model_name='gpt-4o'):
        self.llm = OpenAI(model_name=model_name,openai_api_key=api_key,max_tokens=-1)

        self.agent = None
    
    # Method to send input to agent
    def get_answer(self,query):
        return self.agent.invoke({'input':query})