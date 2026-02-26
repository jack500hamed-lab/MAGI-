import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="MAGI AI", page_icon="🤖")

# القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("Settings ⚙️")
    lang = st.selectbox("Select Language / اختر اللغة", ["Arabic", "English"])
    theme_color = st.color_picker("Pick a Theme Color", "#00F2FF")
    st.write("---")
    st.write("Created by Ayman 🚀")

# النصوص بناءً على اللغة
if lang == "Arabic":
    title_text = "MAGI AI"
    subtitle = "ارفع صورة للتحليل والتعلم"
    button_label = "تصفح الصور من جهازك"
    chat_label = "اسأل MAGI AI عن أي شيء..."
else:
    title_text = "MAGI AI"
    subtitle = "Upload an image for analysis"
    button_label = "Browse images from your device"
    chat_label = "Ask MAGI AI anything..."

# عرض العنوان الملون
st.markdown(f"<h1 style='text-align: center; color: {theme_color};'>{title_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{subtitle}</p>", unsafe_allow_html=True)

# خانة رفع الصور
uploaded_file = st.file_uploader(button_label, type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Image Ready!", use_container_width=True)
    st.success("Success! / تم التحميل بنجاح")

# خانة الدردشة
st.write("---")
user_query = st.text_input(chat_label)

if user_query:
    st.info(f"MAGI AI: I received your message: '{user_query}'. I'm learning to respond better!")
    
