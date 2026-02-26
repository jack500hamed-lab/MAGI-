import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعدادات الواجهة
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# تفعيل المخ بأكتر من محاولة (عشان نهرب من خطأ 404)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # بنجرب النسخة الأكثر استقراراً حالياً
    model = genai.GenerativeModel('gemini-1.5-pro') 
except:
    st.error("تأكد من الـ API Key في الـ Secrets")

# رفع الصور
uploaded_file = st.file_uploader("ارفع صورة", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)

# الدردشة وزرار الإرسال
user_query = st.text_input("اسأل MAGI AI:")
send = st.button("إرسال الطلب 🚀") # الزرار اللي طلبته ظهر هنا!

if send and user_query:
    with st.spinner("MAGI AI بيفكر..."):
        try:
            # محاولة تانية لو النسخة الأولى فشلت
            if img:
                response = model.generate_content([user_query, img])
            else:
                response = model.generate_content(user_query)
            
            st.success(response.text)
        except Exception as e:
            # لو فشل في pro يجرب flash
            try:
                alt_model = genai.GenerativeModel('gemini-pro')
                response = alt_model.generate_content(user_query)
                st.success(response.text)
            except:
                st.error("جوجل لسه مش شايفة المفتاح، استنى دقيقة وجرب تاني.")

st.sidebar.write("Created by Ayman 🚀")
    
