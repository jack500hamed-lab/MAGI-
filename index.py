import streamlit as st
import google.generativeai as genai

# إعداد واجهة MAGI AI
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# تفعيل المفتاح السري
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # استخدمنا الاسم المختصر لضمان عمل السيرفر
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"خطأ في الإعداد: {e}")
else:
    st.error("المفتاح مش موجود في الـ Secrets!")

# خانة الدردشة وزرار الإرسال
user_query = st.text_input("اسأل MAGI AI أي حاجة:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    with st.spinner("MAGI AI بيفكر..."):
        try:
            # طلب الرد
            response = model.generate_content(user_query)
            st.success(response.text)
        except Exception as e:
            st.error(f"جوجل بتقول: {e}")

st.sidebar.write("Created by Ayman 🚀")
