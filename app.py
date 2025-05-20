# app.py

import streamlit as st
from PIL import Image
import numpy as np
import model

st.set_page_config(page_title="Medical Image Diagnostic Assistant", layout="wide")

st.title("🩺 Medical Image Diagnostic Assistant")
st.markdown("Upload a chest X-ray, CT scan, or MRI for AI-assisted diagnosis.")

# Sidebar
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Upload an image.
2. View the AI's findings.
3. See highlighted regions of interest.
""")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize((224, 224))

    # Run model
    result = model.predict(image)

    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("🖼️ Uploaded Image")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("🧠 AI Analysis")
        st.markdown(f"**Urgency Level:** {'🔴 High' if result['urgency'] == 'High' else '🟢 Routine'}")

        st.markdown("### Predicted Conditions:")
        for pred in result['predictions']:
            st.markdown(f"- **{pred['condition']}**: {int(pred['confidence']*100)}% confidence")

        # Generate heatmap overlay
        heatmap = result['heatmap']
        heatmap -= heatmap.min()
        heatmap /= heatmap.max()
        heatmap = np.uint8(255 * heatmap)
        heatmap = Image.fromarray(heatmap).resize((224, 224)).convert("RGB")

        st.markdown("### 🔥 Heatmap Overlay")
        st.image(heatmap, caption="AI Focus Areas", use_column_width=True)

else:
    st.info("Please upload an image to begin analysis.")