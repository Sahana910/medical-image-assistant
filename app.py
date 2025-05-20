# app.py

import streamlit as st
from PIL import Image
import numpy as np
import model
import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm

st.set_page_config(page_title="Medical Image Diagnostic Assistant", layout="wide")

# Custom CSS for medical theme
st.markdown("""
<style>
    body {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .condition-high { color: red; font-weight: bold; }
    .condition-medium { color: orange; font-weight: bold; }
    .condition-low { color: green; font-weight: bold; }
    h1 {
        text-align: center;
        color: #007BFF;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🩺 Medical Image Diagnostic Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload a chest X-ray, CT scan, or MRI for AI-assisted diagnosis.</p>", unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.image("assets/logo.png", width=80)
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Upload an image.
2. View AI findings.
3. See highlighted regions of interest.
""")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        # Load and display original image
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))

        # Run simulated AI model
        result = model.predict(image)

        # Display image and heatmap side-by-side
        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🖼️ Uploaded Image")
            st.image(image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🧠 AI Analysis")

            # Urgency Level
            urgency_badge = {
                "High": "🔴",
                "Medium": "🟡",
                "Routine": "🟢"
            }
            st.markdown(f"**Urgency Level:** {urgency_badge[result['urgency']]} **{result['urgency']}**")

            # Predicted Conditions
            st.markdown("### 🧾 Predicted Conditions:")
            for pred in result['predictions']:
                conf = int(pred['condition'] in ["Pneumothorax", "Cardiomegaly"]) and "condition-high" or \
                       int(pred['condition'] in ["Pleural Effusion", "Mass"]) and "condition-medium" or "condition-low"
                st.markdown(f"- <span class='{conf}'>{pred['condition']}</span>: {int(pred['confidence'] * 100)}% confidence", unsafe_allow_html=True)

            # Heatmap Overlay
            st.markdown("### 🔥 AI Focus Areas")
            fig, ax = plt.subplots()
            ax.imshow(image, cmap='gray')
            ax.imshow(result['heatmap'], alpha=0.5, cmap=cm.jet)
            ax.axis('off')
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
            buf.seek(0)
            heatmap_img = Image.open(buf)
            st.image(heatmap_img, caption="AI Attention Map", use_container_width=True)

            # Explanation
            st.markdown("### ℹ️ Explanation")
            st.write("The AI analyzed patterns in the lungs and surrounding areas. Abnormalities like air outside the lungs (Pneumothorax) were detected with high confidence.")

            st.markdown('</div>', unsafe_allow_html=True)

        # Image Metadata Section
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📄 Image Metadata")
        st.write(f"**File Name:** {uploaded_file.name}")
        st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")
        st.write(f"**Dimensions:** {image.width} x {image.height}")

        description = st.text_area("📝 Describe this image (optional)", height=100)
        if description:
            st.markdown(f"**Description:** {description}")
        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error("❌ An error occurred while processing the image.")
        st.exception(e)
else:
    st.info("Please upload an image to begin analysis.")
