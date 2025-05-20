import streamlit as st
from PIL import Image
import numpy as np
import model  # Your simulated or real model logic

# ----------------------
# Page Configuration
# ----------------------
st.set_page_config(page_title="Medical Image Diagnostic Assistant", layout="wide")
st.markdown("""
<style>
    body {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .reportview-container {
        padding: 20px;
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
</style>
""", unsafe_allow_html=True)

# ----------------------
# Header Section
# ----------------------
st.markdown("<h1 style='text-align: center;'>🩺 Medical Image Diagnostic Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Upload a chest X-ray, CT scan, or MRI for AI-assisted diagnosis.</p>", unsafe_allow_html=True)

# ----------------------
# Sidebar Instructions
# ----------------------
st.sidebar.image("assets/logo.png", width=80)
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Upload an image.
2. View the AI's findings.
3. See highlighted regions of interest.
""")

# ----------------------
# File Uploader
# ----------------------
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB").resize((224, 224))

    # Run model
    result = model.predict(image)

    # ----------------------
    # Image Viewer
    # ----------------------
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🖼️ Uploaded Image")
        st.image(image, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 AI Analysis")

        # Urgency Level
        urgency = result['urgency']
        urgency_badge = {
            "High": "🔴",
            "Medium": "🟡",
            "Routine": "🟢"
        }

        st.markdown(f"**Urgency Level:** {urgency_badge[urgency]} **{urgency}**")

        # Predictions
        st.markdown("### 🧾 Predicted Conditions:")
        for pred in result['predictions']:
            condition = pred['condition']
            conf = int(pred['confidence'] * 100)
            color_class = "condition-high" if condition in ["Pneumothorax", "Cardiomegaly"] else \
                         "condition-medium" if condition in ["Pleural Effusion", "Mass"] else "condition-low"

            st.markdown(f"- <span class='{color_class}'>{condition}</span>: {conf}% confidence", unsafe_allow_html=True)

        # Heatmap
        st.markdown("### 🔥 AI Focus Areas")
        heatmap = result['heatmap']
        heatmap -= heatmap.min()
        heatmap /= heatmap.max()
        heatmap = np.uint8(255 * heatmap)
        heatmap_img = Image.fromarray(heatmap).resize((224, 224)).convert("RGB")
        st.image(heatmap_img, caption="AI Attention Map", use_column_width=True)

        # Explanation
        st.markdown("### ℹ️ Explanation")
        st.markdown("The AI analyzed patterns in the lungs and surrounding areas. Abnormalities like air outside the lungs (Pneumothorax) were detected with high confidence.", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Please upload an image to begin analysis.")
