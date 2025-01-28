import streamlit as st
from langchain.document_loaders import PyPDFLoader
import os
from embedding import add_documents
from llm import generate_response

st.header("Ask your knowledge base")

document = st.sidebar.file_uploader(label = "Upload your knowledge base in pdf", 
                         type = ['pdf'])

process_document_button = st.sidebar.button("Process document")

if process_document_button:
    if document:
        with open(f"{document.name}","wb") as f:
            f.write(document.getbuffer())
        document_loader = PyPDFLoader(f"{document.name}")
        documents = document_loader.load()
        vector_store = add_documents(documents)
        
question = st.text_input("Ask a question")

generate_response_button = st.button("Generate response")

if generate_response_button:
    if question:
        response = generate_response(question)
        st.write(response)
    else:
        st.write("Write a question first")
    