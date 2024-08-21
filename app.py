import streamlit as st
import google.generativeai as genai


st.title("WELCOME TO MADHESH CHAT GPT")

genai.configure(api_key="AIzaSyCL684KyWgjnXKiRS188YcqGgjMcYqgVzQ")

text = st.text_input("enter the question")


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("click me"):
       response = chat.send_message(text)
       st.write(response.text)
