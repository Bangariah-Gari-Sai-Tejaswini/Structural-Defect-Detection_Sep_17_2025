import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
st.sidebar.title('UPLOAD YOUR IMAGE HERE')
uploaded_image = st.sidebar.file_uploader('Here',type=['jpeg','jpg','png'])
image = Image.open(uploaded_image)

st.title('UPLOADED IMAGE')
st.image(image)

