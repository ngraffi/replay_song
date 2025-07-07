import streamlit as st

upload_file = st.file_uploader("Choose a file")

if upload_file is not None:
    st.audio(upload_file)
