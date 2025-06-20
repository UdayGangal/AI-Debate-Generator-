import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

custom_css = """
<style>
    body {
        background: linear-gradient(to bottom, #22313F, #1B262C);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 40px;
        margin-top: 30px;
        flex-wrap: wrap;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        color: #f0f0f0;
        flex: 1;
        min-width: 350px;
        transition: all 0.4s ease-in-out;
    }
    .debate-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        color: #f0f0f0;
        flex: 1;
        min-width: 350px;
    }
    .stSlider > div > div {
        color: #fff !important;
    }
    .stButton > button {
        background-color: #ec008c;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff5ec4;
        box-shadow: 0 0 15px #ff5ec4;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center;'>🤖 AI Debate Generator</h1>
    <p style='text-align: center;'>Enter your topic and customize the participants</p>
""", unsafe_allow_html=True)

if "generate_clicked" not in st.session_state:
    st.session_state.generate_clicked = False

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        topic = st.text_input("🎯 Debate Topic", placeholder="e.g., Is AI replacing creativity?")
        num_participants = st.slider("👥 Number of Participants", min_value=2, max_value=6, value=2)
        participant_names = []
        for i in range(num_participants):
            name = st.text_input(f"Name of Participant {i + 1}")
            participant_names.append(name)

        if st.button("💬 Generate Debate"):
            st.session_state.generate_clicked = True
        st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.generate_clicked:
    with col2:
        st.markdown("<div class='debate-box'>", unsafe_allow_html=True)
        st.subheader("💬 AI Debate Simulation")
        for i, name in enumerate(participant_names):
            st.markdown(f"**{name}:** This is a placeholder argument.")
        st.markdown("</div>", unsafe_allow_html=True)
