import streamlit as st

st.set_page_config(page_title= "ChatBot", page_icon=":books:")
st.title(":books: AskNarelle")

with st.sidebar:
    st.header("Profile")
    gender = st.radio(
        label = "Gender",
        options = ("Male", "Female")
    )
    if gender == "Male":
        st.header("Welcome Guys :boy:")
    else:
        st.header("Welcome Girls :girl:")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Hardcoded responses
hardcode_responses = {
    "hello": "Hello! How can I help you today?",
    "how are you?": "I'm a chatbot, What can I help you?",
    "what is your name?": "I'm a simple chatbot.",
    "bye": "Goodbye! Have a great day!",
}

# Get user input
prompt = st.chat_input("What's up?")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate a hardcoded response based on user input
    response = hardcode_responses.get(prompt.lower(), "Sorry, I can't give you the answer.")

    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})