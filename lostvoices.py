import streamlit as st
import cv2
import numpy as np
import os
import time

# Paths to images
portrait_folder = "MyImages"
water_texture_path = "DarkWater/dark_water.png"

# Get sorted list of portraits
portraits = sorted([os.path.join(portrait_folder, f) for f in os.listdir(portrait_folder) if f.endswith(('.jpg', '.png'))])

# Load water texture
water_texture = cv2.imread(water_texture_path)
if water_texture is None:
    st.error("Error loading water texture!")
    st.stop()

# Function to resize images properly
def resize_image(img, target_width, target_height):
    h, w, _ = img.shape
    scale = min(target_width / w, target_height / h)  # Maintain aspect ratio
    new_w, new_h = int(w * scale), int(h * scale)
    resized_img = cv2.resize(img, (new_w, new_h))

    # Add padding to fit canvas
    top_pad = (target_height - new_h) // 2
    bottom_pad = target_height - new_h - top_pad
    left_pad = (target_width - new_w) // 2
    right_pad = target_width - new_w - left_pad
    padded_img = cv2.copyMakeBorder(resized_img, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    return padded_img

# Streamlit UI
st.title("Disappearance Transition Effect")
st.write("Observe portraits fading seamlessly into dark water.")

# Select portrait
selected_portrait = st.selectbox("Choose a portrait:", [os.path.basename(p) for p in portraits])

# Load and resize portrait
portrait_path = os.path.join(portrait_folder, selected_portrait)
portrait = cv2.imread(portrait_path)
if portrait is None:
    st.error("Error loading portrait!")
    st.stop()

portrait_resized = resize_image(portrait, 800, 800)
water_resized = resize_image(water_texture, 800, 800)

# Transition effect using a slider
alpha = st.slider("Blend Strength", 0.0, 1.0, 0.0, 0.1)
blended = cv2.addWeighted(portrait_resized, 1 - alpha, water_resized, alpha, 0)
st.image(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB), use_column_width=True)

# Auto-transition effect
if st.button("Start Auto Transition"):
    for alpha in np.linspace(0, 1, num=20):
        blended = cv2.addWeighted(portrait_resized, 1 - alpha, water_resized, alpha, 0)
        st.image(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB), use_column_width=True)
        time.sleep(0.2)

st.write("Adjust the slider or press 'Start Auto Transition' to see the effect.")
