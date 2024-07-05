import os
import pathlib
from PIL import Image
import google.generativeai as genai
import streamlit as st

# Replace with your API key
api_key1 = "***********************"
genai.configure(api_key=api_key1)

def get_image_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([image])
    return response.text

def read_image(image):
    return Image.open(image)

# Define the recent_images list
recent_images = []

st.set_page_config(page_title="Image Recognition with Genie", page_icon=":camera:", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title("Image Recognition with Genie")
    st.write("Upload an image and get a description from Genie")
    uploaded_image = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"], help="Upload an image to get a description")

    if uploaded_image:
        image = read_image(uploaded_image)
        response = get_image_response(image)
        st.write("Description:")
        st.write(response)
        recent_images.append(image)

with col2:
    st.write("Or, take a photo using your webcam:")
    camera_image = st.camera_input("Take a photo")

    if camera_image:
        image = read_image(camera_image)
        response = get_image_response(image)
        st.write("Description:")
        st.write(response)
        recent_images.append(image)

# Add history tab in the left sidebar
st.sidebar.title("History")

# Set the background color to white
st.sidebar.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the 5 most recent images captured
for i, image in enumerate(recent_images[-5:]):
    st.sidebar.write(f"Image {i+1}", unsafe_allow_html=True)
    st.sidebar.image(image, width=150)

st.markdown("### About this app")
st.write("This app uses the Gemini Pro Vision model to generate descriptions for uploaded images.")
st.write("Try uploading an image or taking a photo to see it in action!")
