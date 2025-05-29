import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")
st.title("📝 Text Summarizer using BERT")
st.write("Enter long text, and this app will summarize it using a pre-trained BERT model.")

text_input = st.text_area("Enter Text Here:", height=300)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_input)
            st.subheader("Summary:")
            st.success(summary)
    else:
        st.warning("Please enter some text first.")
