import streamlit as st
import requests

st.set_page_config(page_title="AI Chat Clone", page_icon="🤖")

st.title("🤖 My Free AI ChatGPT Clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

def get_ai(prompt):
    url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    res = requests.post(url, json={"inputs": prompt})
    try:
        return res.json().get("generated_text", "Loading AI...")
    except:
        return "Error"

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = get_ai(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})