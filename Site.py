import streamlit as st

# Page config
st.set_page_config(page_title="AI Debate Generator", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #2c3e50, #1a252f);
        color: #f5f5f5;
    }
    .main-container {
        display: flex;
        justify-content: space-between;
        gap: 2rem;
        margin-top: 2rem;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 2rem;
        flex: 1;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        color: #ffffff;
        transition: all 0.5s ease;
    }
    .glass-box h3 {
        color: #ffffff;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🤖 AI Debate Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your topic and customize the participants</p>", unsafe_allow_html=True)

# State for generating
if "show_output" not in st.session_state:
    st.session_state.show_output = False

# Layout containers
left_col, right_col = st.columns(2)

with left_col:
    with st.form(key="debate_form"):
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

        st.text_input("🎯 Debate Topic", placeholder="e.g., Is AI replacing creativity?")
        num_participants = st.slider("👥 Number of Participants", 2, 6, 2)

        for i in range(num_participants):
            st.text_input(f"Name of Participant {i+1}", key=f"name_{i}")

        submitted = st.form_submit_button("🧠 Generate Debate")
        st.markdown("</div>", unsafe_allow_html=True)

        if submitted:
            st.session_state.show_output = True

# Right box (appears on generate)
if st.session_state.show_output:
    with right_col:
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        st.markdown("### 💬 AI Debate Simulation")
        st.write("**Bot 1:** This is a placeholder for generated argument.")
        st.write("**Bot 2:** And this is another perspective.")
        st.markdown("</div>", unsafe_allow_html=True)
