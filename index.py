import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعدادات واجهة MAGI AI
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# 2. ربط المفتاح (بناخده من الـ Secrets اللي إنت ظبطتها)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # ده السطر السحري اللي هيحل الـ 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("فيه مشكلة في المفتاح السري، اتأكد منه في الـ Secrets")

# 3. قسم رفع الصور
uploaded_file = st.file_uploader("ارفع صورة لـ MAGI AI", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="الصورة جاهزة!", use_container_width=True)

# 4. خانة الدردشة وزرار الإرسال (اللي ظهر في صورك)
user_query = st.text_input("اسأل MAGI AI أي سؤال:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    with st.spinner("MAGI AI بيفكر..."):
        try:
            # هنا بنطلب الرد بطريقة بسيطة جداً
            if img:
                response = model.generate_content([user_query, img])
            else:
                response = model.generate_content(user_query)
            
            # عرض الرد
            st.success(response.text)
        except Exception as e:
            # لو لسه فيه مشكلة، ده هيجرب نسخة تانية احتياطي
            try:
                backup_model = genai.GenerativeModel('gemini-pro')
                response = backup_model.generate_content(user_query)
                st.success(response.text)
            except:
                st.error(f"جوجل بتقول: {e}")

st.sidebar.write("Created by Ayman 🚀")
                
