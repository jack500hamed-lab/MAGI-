import streamlit as st
import google.generativeai as genai

# إعداد واجهة MAGI AI
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# تفعيل المفتاح السري
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # استخدمنا gemini-pro (النسخة المستقرة جداً اللي مفيهاش مشاكل 404)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("تأكد من الـ API Key")

# خانة الدردشة
user_query = st.text_input("اسأل MAGI AI أي سؤال:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    with st.spinner("MAGI AI بيفكر..."):
        try:
            # طلب الرد
            response = model.generate_content(user_query)
            st.info(response.text)
        except Exception as e:
            st.error("جوجل لسه معاندة، جرب تسأله سؤال بالانجليزي (Hi) وشوف")

st.sidebar.write("Created by Ayman
