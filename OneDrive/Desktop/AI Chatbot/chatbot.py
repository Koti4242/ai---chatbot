import streamlit as st
from openai import OpenAI

# OpenRouter API Key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
   api_key=st.secrets["OPENROUTER_API_KEY"]

# Title
st.title("🤖 AI Chatbot")

# Input
user_input = st.text_input("Ask me anything")

# AI Response
if user_input:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = completion.choices[0].message.content
    st.write(reply)