import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="MAGI AI - Vision", page_icon="📸")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI Vision</h1>", unsafe_allow_html=True)

# تفعيل المفتاح
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # بنستخدم gemini-1.5-flash عشان بيدعم الصور والسرعة
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("المفتاح مش موجود في الـ Secrets!")

# خاصية رفع الصور اللي كانت ناقصة
uploaded_file = st.file_uploader("ارفع صورة عشان MAGI AI يشوفها:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة اللي رفعتها', use_container_width=True)

# خانة السؤال
user_query = st.text_input("اسأل عن الصورة أو أي حاجة تانية:")

if st.button("إرسال الطلب 🚀"):
    if user_query:
        with st.spinner("MAGI AI بيفكر..."):
            try:
                if uploaded_file:
                    # لو فيه صورة، بيبعت الصورة مع السؤال
                    response = model.generate_content([user_query, image])
                else:
                    # لو مفيش صورة، بيرد نص بس
                    response = model.generate_content(user_query)
                st.success(response.text)
            except Exception as e:
                st.error(f"فيه مشكلة صغيرة: {e}")
                st.info("نصيحة: جرب تعمل Reboot لـ App من لوحة التحكم.")

st.sidebar.write("Created by Ayman 🚀")
