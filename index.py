import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة اللي تعبنا فيها
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# تفعيل المفتاح السري اللي إنت لسه جايبه
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # هنستخدم gemini-pro لأنه الأكثر استقراراً مع المفاتيح الجديدة
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        st.error(f"مشكلة في التفعيل: {e}")
else:
    st.error("يا أيمن، حط المفتاح الجديد في الـ Secrets!")

# خانة السؤال والزرار
user_query = st.text_input("اسأل MAGI AI أي حاجة:")
if st.button("إرسال الطلب 🚀"):
    if user_query:
        with st.spinner("MAGI AI بيفكر..."):
            try:
                response = model.generate_content(user_query)
                st.success(response.text)
            except Exception as e:
                st.error("جرب تعمل ريفريش للموقع، المفتاح لسه بيفوق!")

st.sidebar.write("Created by Ayman 🚀")
    
