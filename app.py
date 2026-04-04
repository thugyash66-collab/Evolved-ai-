import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🧠 EvolveAI")

user_input = st.text_input("Ask something:")

if st.button("Run"):
    if user_input:
        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=user_input
            )
            st.write(response.output[0].content[0].text)
        except Exception as e:
            st.error(f"Error: {e}")