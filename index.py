import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعدادات واجهة MAGI AI
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# 2. ربط المفتاح (تأكد إنك كاتبه صح في Secrets)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # ده السطر اللي فيه اللغز كله - استخدمنا الاسم البسيط للموديل
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("فيه مشكلة في المفتاح السري، اتأكد منه في الـ Secrets")

# 3. رفع الصور
uploaded_file = st.file_uploader("ارفع صورة لـ MAGI AI", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="الصورة جاهزة للتحليل", use_container_width=True)

# 4. خانة الدردشة وزرار الإرسال
user_query = st.text_input("اسأل MAGI AI أي سؤال:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    with st.spinner("MAGI AI بيفكر دلوقتي..."):
        try:
            if img:
                # لو فيه صورة بيبعتها للمخ مع السؤال
                response = model.generate_content([user_query, img])
            else:
                # لو كلام بس
                response = model.generate_content(user_query)
            
            st.success(response.text)
        except Exception as e:
            # لو الموديل لسه معصلج، هننادي على النسخة القديمة المضمونة
            try:
                legacy_model = genai.GenerativeModel('gemini-pro')
                response = legacy_model.generate_content(user_query)
                st.success(response.text)
            except:
                st.error(f"جوجل بتقول: {e}")

st.sidebar.markdown("---")
st.sidebar.write("Created by Ayman 🚀")
