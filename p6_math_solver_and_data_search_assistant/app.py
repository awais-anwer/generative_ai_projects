import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler


## Set up the streamlit app
st.set_page_config(page_title="Text to Math problem solver and Data search Assistant", page_icon="🧮")
st.title("🧮 Text to Math Problem Solver")

groq_api_key = st.sidebar.text_input(label="Groq API key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

## Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name = "Wikipedia",
    func = wikipedia_wrapper.run,
    description="A tool for searching the internet to find various information on the topic mentioned"
)

## Initialize Match tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions. Only input mathematic expression needs to be provided"
)

## Preparing reasoning tool
prompt="""
You are an agent tasked for solving user's mathematical questions. Logically arrive at the solution and provide detailed explaination 
and display it pointwise for the question below
Question: {question}
Answer:
"""
prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## initialize the agents
assistant_agent = initialize_agent(
    tools = [reasoning_tool, calculator, wikipedia_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_error=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role": "assistant", "content": "Hi, I'm a math Chatbot who can answer all your math question"}
    ]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


## interaction
user_question=st.text_area("Enter you question", placeholder="I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")
if st.button("find my answer"):
    if user_question:
        with st.spinner("Generating response.."):
            st.session_state.messages.append({"role":"user", "content":user_question})
            st.chat_message("user").write(user_question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({'role':'assistant', 'content': response})
            st.write("### Response: ")
            st.success(response)

    else:
        st.warning("Please enter the Question")
