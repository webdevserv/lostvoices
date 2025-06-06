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

st.write("""
**AI Digital Memorial to Lost Voices in Dark Waters**  
Honoring women murdered, raped, abused, or assaulted by men in war and peace.  
We visualize their disappearance into dark waters, symbolizing loss, erasure, and the urgency for justice.  
Inspired by the German Lost Girl and Natalie Wood’s husband's unsettling 6-minute interview—haunting proof that in patriarchal systems, some crimes fade into silence, and justice is never guaranteed. When violence is ignored, erased, or excused, getting away with murder isn’t an anomaly—it’s a built-in failure of the system.""")

# Closing statement (displayed once)
st.write("""
Dark Waters: This artistic work is a tribute to those whose voices have been silenced. Through visual transitions, we reflect on loss, erasure, and the urgency for justice. May this serve as a reminder to stop violence against women.

Lan artistiko hau isilduak izan direnen omenaldia da. Irudien bidezko trantsizioekin, galera, ezabaketa eta justiziaren premia hausnartzen ditugu. Gogoan hartzea erresistentzia da, eta ekimen honek hori gogorarazi nahi du.

Cette œuvre artistique est un hommage à ceux dont la voix a été réduite au silence. À travers des transitions visuelles, nous réfléchissons à la perte, à l'effacement et à l'urgence de la justice. Que cela rappelle l'importance de mettre fin à la violence envers les femmes.

Esta obra artística es un homenaje a quienes han sido silenciados. A través de transiciones visuales, reflexionamos sobre la pérdida, el borrado y la urgencia de justicia. Que esto sirva como un recordatorio para detener la violencia contra las mujeres.
Github: https://github.com/webdevserv/gll
""")
contact_form = """
    <a href="https://webdevserv.github.io/html_bites/dev/webdev.html">More info</a>.</p>
    <div style="margin: 0.75em 0;"><a href="https://www.buymeacoffee.com/Artgen" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>
"""
st.markdown(contact_form, unsafe_allow_html=True)


# Smooth transition loop (keeps running indefinitely)
while True:
    selected_portrait = random.choice(portraits)
    portrait = cv2.imread(selected_portrait)

    if portrait is not None:
        portrait_resized = resize_image(portrait, 800, 800)
        water_resized = resize_image(water_texture, 800, 800)

    for alpha in np.linspace(0, 1, num=30):  # Very slow transition
        blended = cv2.addWeighted(portrait_resized, 1 - alpha, water_resized, alpha, 0)
        image_placeholder.image(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB), use_container_width=True)
        time.sleep(0.5)  # Increase sleep time for visibility

    time.sleep(1)  # Pause before selecting next image



   
