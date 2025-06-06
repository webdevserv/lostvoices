import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
import os
import time
import random

st.set_page_config(layout="wide")

# Inject meta tags
meta_tags = """
<head>
    <meta name="description" content="Streamlit app Dark Waters: A tribute to silenced voices, reflecting on loss, erasure, and justice.">
    <meta name="keywords" content="Natalie Wood, assault, violence againts women, injustice, conceptual art, violence">
      <meta name="author" content="webdevserv">Add commentMore actions
</head>
"""
components.html(meta_tags, height=0)

portrait_folder = "MyImages"
water_texture_path = "DarkWater/dark_water.png"

# 🎯 **Cache dark water texture for performance boost**
@st.cache_data
def load_water_texture():
    return cv2.imread(water_texture_path)

water_texture = load_water_texture()
if water_texture is None:
    st.error("Error loading water texture!")
    st.stop()

# Resize function
def resize_image(img, target_width, target_height):
    h, w, _ = img.shape
    scale = min(target_width / w, target_height / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized_img = cv2.resize(img, (new_w, new_h))

    # Padding for canvas fit
    top_pad = (target_height - new_h) // 2
    bottom_pad = target_height - new_h - top_pad
    left_pad = (target_width - new_w) // 2
    right_pad = target_width - new_w - left_pad
    return cv2.copyMakeBorder(resized_img, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

# UI setup
st.title("AI Digital Memorial to Lost Voices in Dark Water")
image_placeholder = st.empty()
portraits = sorted([os.path.join(portrait_folder, f) for f in os.listdir(portrait_folder) if f.endswith(('.jpg', '.png'))])

# Smooth transition loop (keeps running indefinitely)
while True:
    selected_portrait = random.choice(portraits)
    portrait = cv2.imread(selected_portrait)

    if portrait is not None:
        portrait_resized = resize_image(portrait, 400, 400)
        water_resized = resize_image(water_texture, 400, 400)

        for alpha in np.linspace(0, 1, num=50):  # More transition steps
            blended = cv2.addWeighted(portrait_resized.astype(np.float32), 1 - alpha, 
                                      water_resized.astype(np.float32), alpha, 0)
            blended = np.clip(blended, 0, 255).astype(np.uint8)  # Fixes display issues

            image_placeholder.image(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB), use_container_width=True)
            time.sleep(0.1)  # Reduce sleep for smoother transition

        time.sleep(2)  # Pause before selecting next image



   
