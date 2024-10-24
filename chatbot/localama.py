from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_community.llms import Ollama -depricated
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo with GEMMA model')
input_text = st.text_input("Search the topic u want")

# Ollama LLAMA2 LLM
llm = OllamaLLM(model="gemma")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    result = chain.invoke({"question":input_text})
    st.write(result)