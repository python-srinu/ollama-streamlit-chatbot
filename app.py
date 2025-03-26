from langchain_ollama import OllamaLLM
import streamlit as st

llm = OllamaLLM(model="tinyllama") 

st.title("Chatbot using Ollamallm") 

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(llm.invoke(prompt))
