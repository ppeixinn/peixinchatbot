import streamlit as st
from langchain_openai import AzureChatOpenAI

## Initialize LLM using AzureChatOpenAI
llm = AzureChatOpenAI(
    openai_api_version=st.secrets["AZURE_OPENAI"]["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=st.secrets["AZURE_OPENAI"]["AZURE_OPENAI_ENDPOINT"],
    api_key=st.secrets["AZURE_OPENAI"]["AZURE_OPENAI_APIKEY"],
    azure_deployment=st.secrets["AZURE_OPENAI"]["DEPLOYMENT_NAME"],
    temperature=1
)

st.set_page_config(page_title= "ChatBot", page_icon=":books:")

with st.sidebar:
    st.header("Profile")
    option = st.selectbox(
    "How would you like to be contacted?",
    ("Messenger", "Whatsapp", "Mobile phone"))

    st.subheader(f"You selected: {option}")
    st.write("You selected:", option)
    st.latex("1 + 2 = 3")

    gender = st.radio(
        label = "Gender",
        options = ("Male", "Female")
    )
    if gender == "Male":
        st.header("Welcome Guys :boy:")
    else:
        st.header("Welcome Girls :girl:")

    rating = st.select_slider(
    "Rate this chatbot",
    options=["1", "2", "3", "4", "5"])
    st.write("Your rating is", rating)


st.title(":books: AskMe")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Tell me something...")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"user", "content": prompt})

    chat_history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    ai_message = llm.invoke(chat_history)
   
    # Extract the response content
    full_response = ai_message.content

    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})


