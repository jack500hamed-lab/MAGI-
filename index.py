import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# 2. تشغيل الـ API بأمان
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("المفتاح مش موجود في Secrets!")
else:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # ده الموديل اللي السيرفر طالبه بالظبط
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    except Exception as e:
        st.error(f"خطأ في الإعداد: {e}")

# 3. رفع الصور
uploaded_file = st.file_uploader("ارفع صورة للتحليل", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)

# 4. الدردشة وزرار الإرسال اللي ضفناه
user_query = st.text_input("اسأل MAGI AI:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    if "GOOGLE_API_KEY" in st.secrets:
        with st.spinner("MAGI AI يقتحم سيرفرات جوجل..."):
            try:
                # محاولة الإرسال بأبسط طريقة ممكنة
                if img:
                    response = model.generate_content([user_query, img])
                else:
                    response = model.generate_content(user_query)
                
                st.success(response.text)
            except Exception as e:
                # لو لسه فيه 404، هننادي على النسخة المضمونة gemini-pro
                try:
                    alt_model = genai.GenerativeModel("gemini-pro")
                    response = alt_model.generate_content(user_query)
                    st.success(response.text)
                except Exception as e2:
                    st.error("جوجل لسه قافلة الباب، جرب تعمل Refresh للمتصفح.")

st.sidebar.write("Created by Ayman 🚀")
