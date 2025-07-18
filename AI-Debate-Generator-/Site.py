
import streamlit as st
import base64
import os
from backend import generate_debate

# CSS
def load_css(background_image_path=None):
    main_background_color = "#1A1A32"
    background_css = ""
    if background_image_path and os.path.exists(background_image_path):
        try:
            with open(background_image_path, "rb") as f:
                img_data = f.read()
            mime_type = "image/png" if background_image_path.lower().endswith(".png") else "image/jpeg"
            background_image_base64 = base64.b64encode(img_data).decode()
            background_css = f"""
                background-image: url("data:{mime_type};base64,{background_image_base64}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            """
        except Exception as e:
            st.error(f"Error loading background image from file '{background_image_path}': {e}. Using solid dark background.")
            background_css = f"background-color: {main_background_color};"
    else:
        background_css = f"background-color: {main_background_color};"

    st.markdown(f"""
        <style>
            .stApp {{
                {background_css}
                font-family: 'Pixelify Sans', cursive;
                color: #EEEEEE;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding-top: 2rem;
            }}
            .block-container {{
                display: flex;
                flex-direction: row;
                gap: 2rem;
                width: 90%;
                max-width: 1200px;
            }}
        </style>
    """, unsafe_allow_html=True)

#Background
BACKGROUND_IMAGE_PATH = "final bg.png"
load_css(BACKGROUND_IMAGE_PATH)

st.set_page_config(layout="wide", page_title="AI Debate Generator")

st.markdown("<h1 style='text-align: center;'>AI Debate Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your topic and customize the participants.</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.text_input("Debate Topic", value="", key="debate_topic") 
    num_participants = st.slider("Number of Participants", min_value=2, max_value=10, value=2, step=1, key="num_participants")
    participant_names = []
    for i in range(num_participants):
        st.text_input(f"Participant {i+1} Name", value="", key=f"participant_{i+1}_name")
        participant_names.append(st.session_state[f"participant_{i+1}_name"])
    generate_button = st.button("Generate Debate")

with col2:
    st.markdown("""
    <div style='background-color: #2B2B2B; border-radius: 10px; padding: 1rem; margin-bottom: 1rem;'>
        <h3 style='text-align: center; font-family: Pixelify Sans, cursive;'>Generated Debates</h3>
    </div>
    """, unsafe_allow_html=True)

    if generate_button:
        valid_participants = [name for name in participant_names if name.strip() != ""]
        if not st.session_state.debate_topic.strip() or len(valid_participants) < 2:
            st.warning("Please enter a debate topic and at least two participant names to generate a debate.")
            st.markdown("""
            <div style='color: #AAAAAA; text-align: center;'>Please fill in all required fields to generate a debate.</div>
            """, unsafe_allow_html=True)
        else:
            topic = st.session_state.debate_topic
            debate_results = generate_debate(topic, valid_participants)
            for name, stance, argument in debate_results:
                st.markdown(f"<div style='background-color: #555; border-radius: 5px; padding: 1rem; margin-bottom: 1rem;'><p><b>{name} ({stance}):</b> {argument}</p></div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='color: #AAAAAA; text-align: center;'>Generate convo will come here</div>
        """, unsafe_allow_html=True)
