import streamlit as st
import requests
import json
import os

VISION_API_KEY ="74zfy9oNEFghoq9YhWvdkz4P73G2fC9t3tfMqgqndVvwUhu7TX1MJQQJ99BJAC5T7U2XJ3w3AAAFACOGLsqX"
VISION_ENDPOINT = "https://asdaasdasdads.cognitiveservices.azure.com/"
ANALYZE_URL = VISION_ENDPOINT + "/vision/v3.2/analyze"

st.title("🔎 Azure Vision Image Analyzer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_data = uploaded_file.read()
    st.image(image_data, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        headers = {
            "Ocp-Apim-Subscription-Key": VISION_API_KEY,
            "Content-Type": "application/octet-stream"
        }
        params = {"visualFeatures": "Objects,Faces,Tags,Description"}
        response = requests.post(ANALYZE_URL, headers=headers, params=params, data=image_data)
        result = response.json()

        st.subheader("📊 Analysis Result (JSON)")
        st.json(result)
