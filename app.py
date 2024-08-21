import streamlit as st
import google.generativeai as genai
st.title("welcome to genai")
genai.configure(api_key="AIzaSyBPCB_QNiCqB_vQ0Cv3GOQE2WF6D270gj8")
text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click me"):
  response =chat.send_message(text)
  st.write(response.text)