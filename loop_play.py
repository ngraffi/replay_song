import streamlit as st

st.set_page_config(
    page_title = "WooChan~",
    page_icon = "😀"
)

upload_file = st.file_uploader("MP3 파일을 선택해주세요", type = ["mp3"])

if upload_file is not None:
    st.audio(upload_file, loop=True, autoplay=True)
