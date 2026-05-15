import streamlit as st
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask me anything")

if user_input:
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)