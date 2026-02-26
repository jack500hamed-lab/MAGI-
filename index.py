import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعدادات واجهة MAGI AI
st.set_page_config(page_title="MAGI AI", page_icon="🤖")
st.markdown("<h1 style='text-align: center; color: #00F2FF;'>🤖 MAGI AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>مساعدك الذكي لتحليل الصور والدردشة</p>", unsafe_allow_html=True)

# 2. تفعيل الذكاء الاصطناعي (Gemini)
try:
    # بيسحب المفتاح اللي إنت لسه حطيته في الـ Secrets
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ تأكد من إضافة المفتاح السري في إعدادات Secrets")

# 3. قسم رفع الصور
uploaded_file = st.file_uploader("ارفع صورة لـ MAGI AI", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="MAGI AI is looking at this image...", use_container_width=True)

# 4. قسم الدردشة والرد العبقري
st.write("---")
user_query = st.text_input("اسأل MAGI AI أي شيء (عن الصورة أو عام):")

if user_query:
    with st.spinner("MAGI AI يفكر الآن..."):
        try:
            if uploaded_file:
                # لو فيه صورة، بيحللها مع السؤال
                response = model.generate_content([user_query, img])
            else:
                # لو مفيش صورة، بيرد كدردشة عادية
                response = model.generate_content(user_query)
            
            # عرض الرد بشكل احترافي
            st.markdown("### 🤖 الرد:")
            st.info(response.text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء المعالجة: {e}")

# توقيعك في الموقع
st.sidebar.write("---")
st.sidebar.write("Created with ❤️ by **Ayman**")
                
