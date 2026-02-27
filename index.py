import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI Vision</h1>", unsafe_allow_html=True)

# تفعيل المفتاح
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # التعديل الجوهري هنا: نحدد الإصدار v1 عشان نهرب من الـ 404
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
else:
    st.error("المفتاح ناقص في الـ Secrets")

uploaded_file = st.file_uploader("ارفع صورة:", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

query = st.text_input("اسأل MAGI AI:")

if st.button("إرسال الطلب 🚀"):
    if query:
        with st.spinner("بيفكر..."):
            try:
                # لو فيه صورة بيبعتها، لو مفيش بيبعت نص
                content = [query, image] if uploaded_file else query
                response = model.generate_content(content)
                st.success(response.text)
            except Exception as e:
                st.error(f"جوجل بتقول: {e}")
                st.info("نصيحة: جرب تغير سطر المكتبة في requirements.txt لـ google-generativeai>=0.8.0")
    
