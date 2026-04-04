import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🧠 EvolveAI")

user_input = st.text_input("Ask something:")

if st.button("Run"):
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a powerful AI that gives intelligent decisions and future ideas."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response.choices[0].message.content)