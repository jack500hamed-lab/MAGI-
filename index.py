import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعدادات الواجهة
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# 2. ربط المخ (API) بنسخة مستقرة
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # استخدمنا النسخة المستقرة 'gemini-pro' للدردشة و 'gemini-pro-vision' للصور
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ تأكد من وضع المفتاح السري في Secrets")

# 3. رفع الصور
uploaded_file = st.file_uploader("ارفع صورة لـ MAGI AI", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Image Ready!", use_container_width=True)

# 4. خانة الدردشة وزرار الإرسال
st.write("---")
user_query = st.text_input("اسأل MAGI AI أي شيء:")
send_button = st.button("إرسال الطلب 🚀") # الزرار اللي كنت ناسيه!

if send_button and user_query:
    with st.spinner("MAGI AI يفكر..."):
        try:
            if img:
                # لو فيه صورة
                response = model.generate_content([user_query, img])
            else:
                # لو كلام بس
                response = model.generate_content(user_query)
            
            st.markdown(f"### 🤖 الرد:\n{response.text}")
        except Exception as e:
            st.error(f"حدث خطأ: {e}")

st.sidebar.write("Created by Ayman 🚀")
