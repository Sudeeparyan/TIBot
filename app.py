import streamlit as st
from dotenv import load_dotenv, find_dotenv

# Load secrets from .env file
load_dotenv(find_dotenv(), override=True)
from llama_index import VectorStoreIndex, Document

chunks = []
with open(
    r"C:\Users\sudeeparyan.g\Downloads\QAonFilesSample\QAonFilesSample\content\docs\page1.txt"
) as f:
    content = f.read()
    chunks.append(content)
    print(content)
documents = list(map(lambda chunk: Document(text=chunk), chunks))
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()


st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = query_engine.query(prompt).response
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
