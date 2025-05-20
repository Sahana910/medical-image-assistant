# 🩺 Medical Image Diagnostic Assistant

A demo AI-powered assistant that analyzes chest X-rays, CT scans, and MRIs to detect abnormalities, suggest differential diagnoses, and prioritize urgent cases using explainable AI techniques.

> ⚠️ **This is a prototype built for educational and demonstration purposes only.**
> It is not intended for clinical use and should not be used for actual diagnosis.

---

## 🔍 Overview

This tool is designed to assist radiologists by:
- Pre-screening medical images
- Flagging potential abnormalities (e.g., pneumonia, pneumothorax)
- Prioritizing urgent cases
- Providing explainable AI insights with heatmaps
- Suggesting differential diagnoses

It uses simulated AI inference and is built with **Streamlit**, making it fast and easy to deploy for demos and hackathons.

---

## 🚀 Live Demo

Try the hosted version here:  
🔗 [https://your-app-name.streamlit.app ](https://your-app-name.streamlit.app )

> Replace this link with your actual deployed URL after deployment.

---

## 🧠 Features

- Upload chest X-ray, CT scan, or MRI image
- View AI-generated heatmap highlighting areas of interest
- See list of predicted conditions with confidence scores
- Urgency level indicator (🔴 High / 🟡 Medium / 🟢 Routine)
- Image metadata display (file name, size, dimensions)
- Optional image description input
- Clean, professional UI with medical theme

---

## 🛠 Tech Stack

| Component | Tool |
|----------|------|
| Frontend | Streamlit |
| Backend | Python |
| AI Logic | Simulated model (`model.py`) |
| Visualization | Pillow, Numpy |
| Hosting | Streamlit Community Cloud / Hugging Face Spaces |

