import streamlit as st
import pdfplumber
from trash.exam_generator import pdf_to_text
from trash.gptprocess import gpt_response

def extract_text(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

uploaded_file = st.file_uploader("Upload a PDF file less than 200 MB", type="pdf")

# extracted_text = pdf_to_text(uploaded_file)

# export PATH=$PATH:/Users/harshpundhir/Library/Python/3.9/bin
# 


if uploaded_file is not None:
    text = extract_text(uploaded_file)
    with st.spinner('Wait for it...'):
        st.header("Here are your questions:")
        st.write(gpt_response(text[:1000]))
    st.success('Done!')

