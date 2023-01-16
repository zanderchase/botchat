from langchain import OpenAI
from langchain.agents import Tool
from langchain import OpenAI, SerpAPIWrapper
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

#MyFitness chain 
def chain(input):

    #Need to add in tool that can get my fitness pal info
    #Doc: https://langchain.readthedocs.io/en/latest/modules/memory/examples/conversational_agent.html
    tools = [
        
    ]

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm=OpenAI(temperature=0)
    agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)
    
    return agent_chain.run(input=input)
