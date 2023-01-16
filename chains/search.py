from langchain import OpenAI
from langchain.agents import Tool
from langchain import OpenAI, SerpAPIWrapper
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

#Search chain 
def chain(input):

    search = SerpAPIWrapper()
    tools = [
        Tool(
            name = "Current Search",
            func=search.run,
            description="useful for when you need to answer questions about current events or the current state of the world"
        ),
    ]

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm=OpenAI(temperature=0)
    agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)
    
    return agent_chain.run(input=input)
