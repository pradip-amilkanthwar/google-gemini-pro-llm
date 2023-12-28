import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_pro_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]

        return image_parts
    else:
        return FileNotFoundError("No file uploaded")


st.set_page_config(page_title="Image Extractor")
st.header("Image Extractor")

uploaded_file = st.file_uploader(
    "Chose an image of the invoice...", type=["jpg", "jpeg", "png"]
)
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

input = st.text_input("Input your query: ", key="input")

submit = st.button("Tell me about the invoice")

if submit:
    image_data = input_image_setup(uploaded_file)

    st.subheader(
        "Response is ... ",
    )

    input_prompt = """
    We will upload image as invoice and you will answer any questions based on uploaded image
    """
    get_gemini_pro_response(input_prompt, image_data, input)
