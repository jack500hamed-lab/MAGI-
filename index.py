import streamlit as st
import requests

st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.title("🤖 MAGI AI")

# هنا بنكلم جوجل "مباشرة" من غير وسيط
def ask_gemini(text):
    api_key = st.secrets["GOOGLE_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts":[{"text": text}]}]}
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

user_query = st.text_input("اسأل أي حاجة:")
if st.button("إرسال الطلب 🚀"):
    if user_query:
        with st.spinner("MAGI AI بيفكر..."):
            try:
                res = ask_gemini(user_query)
                answer = res['candidates'][0]['content']['parts'][0]['text']
                st.success(answer)
            except:
                st.error("جوجل لسه قافلة الباب، جرب API Key جديد.")

st.sidebar.write("Created by Ayman 🚀")
                
