import streamlit as st
import google.generativeai as genai

# شكل الموقع اللي إنت تعبت فيه
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# الربط بالمفتاح المظبوط
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # السر هنا: هنستخدم الموديل باسمه المباشر عشان نهرب من الـ 404
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("المفتاح مش موجود في الـ Secrets")

# الدردشة والزرار
query = st.text_input("اسأل MAGI AI:")
if st.button("إرسال الطلب 🚀"):
    if query:
        with st.spinner("بيفكر..."):
            try:
                # محاولة ببروتوكول مختلف
                response = model.generate_content(query)
                st.success(response.text)
            except Exception as e:
                # لو فشل، بيجرب النسخة المضمونة
                alt = genai.GenerativeModel('gemini-pro')
                st.info(alt.generate_content(query).text)

st.sidebar.write("Created by Ayman 🚀")
                
