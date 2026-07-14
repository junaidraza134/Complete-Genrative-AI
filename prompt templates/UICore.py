import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-small-latest")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert information extraction assistant.

Your job is to extract useful information from the given paragraph.

Extract the following details if available:

- Title
- Type
- Genre
- Creator / Author
- Director
- Main Cast
- Main Characters
- Release Year
- End Year
- Total Seasons
- Total Episodes
- Network / Platform
- Language
- Country
- Runtime
- Awards
- Summary
- Important Facts

Rules:
- Extract only information present in the paragraph.
- Do not guess missing information.
- If a field is missing, write "Not Mentioned".
- Keep the summary short (2-4 sentences).
- Present the output in a clean and readable format.
"""
        ),
        (
            "human",
            """
Extract information from this paragraph:

{paragraph}
"""
        ),
    ]
)

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Information Extractor", layout="centered")

st.title("Information Extractor")

paragraph = st.text_area(
    "Enter Paragraph",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Extract Information"):
    if paragraph.strip():
        with st.spinner("Extracting..."):
            final_prompt = prompt.invoke({"paragraph": paragraph})
            response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.markdown(response.content)
    else:
        st.warning("Please enter a paragraph.")