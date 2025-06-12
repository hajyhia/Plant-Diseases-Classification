import streamlit as st
from PIL import Image

st.title("🖼️ Image Uploader")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)

    # Display image details
    st.write("**Filename:**", uploaded_file.name)
    st.write("**Format:**", image.format)
    st.write("**Size:**", image.size)

    # Show the image
    st.image(image, caption="Uploaded Image")
