import streamlit as st

## Import required libraries
from dotenv import load_dotenv
import os
from time import sleep
from langchain_openai import AzureChatOpenAI                                    ## This object is a connector/wrapper for ChatOpenAI engine
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage      ## These are the commonly used chat messages
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(override=True)

st.set_page_config(page_title="ChatBot",page_icon=":books:")
st.title(":book: Chatchat")
st.header("I am a robot!")
st.markdown("Welcome :sunglasses:")

with st.sidebar:
    st.header("Profile")
    gender = st.radio(
        label="Gender",
        options = ("Male","Female")
    )
    if gender == "Male":
        st.header("Welcome Guys :boy:")
    else: 
        st.header("Welcome Girls :girl:")

#Initialise session state
if "messages" not in st.session_state:
    st.session_state.messages =[]

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Hardcoded responses
hardcode_responses = {
    "hello":"Hello! How can I help you today?",
    "how are you?":"I'm a chatbot, what can I help you?",
    "what is your name?":"I am a simple chatbot",
    "bye":"Goodbye! Have a great day!",
}

# Get user input 
prompt = st.chat_input("Tell me something...")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #add user message to chat history
    st.session_state.messages.append({"role":"user","content":prompt})

    #generate a hardcoded response based on user input
    response = hardcode_responses.get(prompt.lower(),"Sorry, I don't understand that.")

    #Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    #add assistant message to chat history
    st.session_state.messages.append({"role":"assistant","content":response})

