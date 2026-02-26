import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعدادات الواجهة
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)

# تفعيل المخ بطريقة مستقرة
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # نستخدم الموديل المستقر بدون إضافات
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("فيه مشكلة في المفتاح السري بالـ Secrets")

# رفع الصور
uploaded_file = st.file_uploader("ارفع صورة", type=["jpg", "jpeg", "png"])
img = None
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)

# الدردشة وزرار الإرسال
user_query = st.text_input("اسأل MAGI AI:")
submit = st.button("إرسال الطلب 🚀")

if submit and user_query:
    with st.spinner("MAGI AI بيفكر..."):
        try:
            # هنا التعديل: نحدد الموديل جوه الطلب لضمان الدقة
            if img:
                response = model.generate_content([user_query, img])
            else:
                response = model.generate_content(user_query)
            
            st.success(response.text)
        except Exception as e:
            # محاولة أخيرة بموديل بديل لو جوجل لسه معصلجة
            try:
                backup = genai.GenerativeModel('gemini-pro')
                res = backup.generate_content(user_query)
                st.success(res.text)
            except:
                st.error("جوجل لسه معاندة، جرب تغير الـ API Key بواحد جديد")

st.sidebar.write("Created by Ayman 🚀")
    
