import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("🧠 EvolveAI")

user_input = st.text_input("Ask something:")

if st.button("Run"):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a smart AI for decisions."},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
