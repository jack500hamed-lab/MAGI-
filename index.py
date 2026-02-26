import streamlit as st

# إعدادات الصفحة الأساسية
st.title("MAGI AI 🤖")

# القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("Settings")
    lang = st.selectbox("Language / اللغة", ["Arabic", "English"])
    st.write("Created by Ayman 🚀")

# النصوص بناءً على اللغة
if lang == "Arabic":
    subtitle = "ارفع صورة للتحليل"
    button_label = "اختار صورة"
    chat_label = "اسأل MAGI AI..."
else:
    subtitle = "Upload an image to analyze"
    button_label = "Choose an image"
    chat_label = "Ask MAGI AI..."

st.write(subtitle)

# خانة رفع الصور
uploaded_file = st.file_uploader(button_label, type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Image Ready!")
    st.success("Uploaded successfully!")

# خانة الدردشة
st.write("---")
user_query = st.text_input(chat_label)

if user_query:
    st.write(f"MAGI AI received: {user_query}")
