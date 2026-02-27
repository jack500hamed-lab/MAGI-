import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI Vision</h1>", unsafe_allow_html=True)

# الربط بالمفتاح
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # السر هنا: هننادي الموديل من غير v1beta عشان نهرب من الـ 404
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("المفتاح ناقص في الـ Secrets")

# رفع الصور
uploaded_file = st.file_uploader("ارفع صورة:", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

query = st.text_input("اسأل MAGI AI:")

if st.button("إرسال الطلب 🚀"):
    if query:
        with st.spinner("بيفكر..."):
            try:
                # محاولة الإرسال بأبسط طريقة ممكنة
                content = [query, image] if uploaded_file else query
                response = model.generate_content(content)
                st.success(response.text)
            except Exception as e:
                st.error(f"جوجل بتقول: {e}")
            
