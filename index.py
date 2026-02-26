import streamlit as st

# إعدادات الصفحة والألوان
st.set_page_config(page_title="MAGI AI", page_icon="🤖")

# القائمة الجانبية للتحكم (اللغة والألوان)
with st.sidebar:
    st.title("Settings ⚙️")
    lang = st.selectbox("Select Language / اختر اللغة", ["Arabic", "English"])
    theme_color = st.color_picker("Pick a Theme Color / اختر لون الواجهة", "#FF4B4B")
    st.write("---")
    st.write("Created by Ayman 🚀")

# تطبيق النصوص بناءً على اللغة
if lang == "Arabic":
    title = "MAGI AI"
    subtitle = "ارفع صورة للتحليل والتعلم"
    button_text = "تصفح الصور"
else:
    title = "MAGI AI"
    subtitle = "Upload an image for analysis and learning"
    button_text = "Browse images"

# عرض الواجهة الرئيسية
st.markdown(f"<h1 style='text-align: center; color: {theme_color};'>{title}</h1>", unsafe_allow_complete=True)
st.write(f"<p style='text-align: center;'>{subtitle}</p>", unsafe_allow_complete=True)

# خانة رفع الصور
uploaded_file = st.file_uploader(button_text, type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully! / تم رفع الصورة بنجاح")

# خانة الدردشة (عشان تبدأ تتكلم معاه)
st.write("---")
user_input = st.text_input("Ask MAGI AI / اسأل الذكاء الاصطناعي")
if user_input:
    st.write(f"MAGI AI says: I'm processing your request about '{user_input}'...")
