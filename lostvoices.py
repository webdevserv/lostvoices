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
    <meta name="keywords" content="Natalie Wood, Richard Wagner assault, violence againts women, injustice, conceptual art, violence">
      <meta name="author" content="webdevserv">Add commentMore actions
</head>
"""
@@ -56,7 +56,7 @@
if portrait is not None:
    portrait_resized = resize_image(portrait, 400, 400)
    water_resized = resize_image(water_texture, 400, 400)
    image_placeholder.image(cv2.cvtColor(portrait_resized, cv2.COLOR_BGR2RGB), use_container_width=True)
    time.sleep(3)

# 💡 **Smooth transition loop**
@@ -70,7 +70,7 @@

        for alpha in np.linspace(0, 1, num=20):
            blended = cv2.addWeighted(portrait_resized, 1 - alpha, water_resized, alpha, 0)
            image_placeholder.image(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB), use_container_width=True)
            time.sleep(0.2)

        time.sleep(2)
