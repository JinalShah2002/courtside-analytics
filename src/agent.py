"""

@author: Jinal Shah

This class represents the agent

"""
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents.react.agent import create_react_agent
from langchain.agents.agent import AgentExecutor
from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup

# Creating the Statmuse tool -> NEEDS TO BE A FUNCTION FOR LANGCHAIN TO WORK
@tool
def statmuse(query):
    """Search up queries related to the NBA to get statistics."""    
    query_list = query.strip().split(' ')
    url = f"https://www.statmuse.com/nba/ask/{'-'.join(query_list)}"
    resp = requests.get(url).content
    soup = BeautifulSoup(resp, 'html.parser')

    # Getting the answer
    for content in soup.find_all('meta'):
        if content.get('name') == 'description':
            return repr(content.get('content'))
    return "No results found"

class Agent:
    # Constructor
    def __init__(self,api_key,model_name='gpt-4o',temperature=0.7,logging=False):
        self.llm = ChatOpenAI(model_name=model_name,temperature=temperature,max_tokens=None,
                              max_retries=3,openai_api_key=api_key)

        # Getting the tools & prompt
        self.prompt = hub.pull("hwchase17/react")
        self.calculator = Tool.from_function(name='Calculator',func=LLMMathChain.from_llm(llm=self.llm).invoke,
                                             description="This is a calculator tool. You can use it when"+
                                             "you need to answer mathematical questions. This tool is only for math questions"+
                                             "and nothing else. Only input math expressions!")

        self.agent = create_react_agent(llm=self.llm,tools=[self.calculator,statmuse],prompt=self.prompt,stop_sequence=True)
        self.agent_executor = AgentExecutor(agent=self.agent,tools=[self.calculator,statmuse],verbose=logging)
    
    # Method to send input to agent
    def get_answer(self,query):
        return self.agent_executor.invoke({'input':query})
    
    # Method to get prompt
    def get_prompt(self):
        return self.prompt