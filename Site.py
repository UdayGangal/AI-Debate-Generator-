import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI Debate Generator",  # Changed from AIDEDGENES GENERAL
    page_icon="💬",
    layout="centered"  # Centered the page
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;  /* Light gray background */
    }
    .stTextInput input {
        border-radius: 8px;
        border: 2px solid #4a6fa5 !important;
        padding: 10px;
    }
    .stSlider {
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .generate-btn {
        background-color: #4a6fa5 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
    }
    .generate-btn:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;  /* Added shadow on hover */
        transform: translateY(-1px) !important;
    }
    .debate-card {
        background-color: rgba(255,255,255,0.7);  /* Semi-transparent */
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        border: 2px solid #e0e0e0;  /* Added border */
    }
    .title {
        text-align: center;  /* Centered title */
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Centered title
st.markdown('<div class="title"><h1>AI Debate Generator</h1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; margin-bottom: 2rem;">Enter your topic and customize the participants.</div>', unsafe_allow_html=True)

# Create two columns
input_col, output_col = st.columns([1, 1], gap="large")

with input_col:
    # Debate topic section
    st.subheader("Debate Topic")
    topic = st.text_input("Enter debate topic", placeholder="e.g. Should AI be regulated?", label_visibility="collapsed")
    
    # Changed to slider
    num_participants = st.slider("Number of Participants", min_value=2, max_value=6, value=2)
    
    participants = []
    for i in range(num_participants):
        participant = st.text_input(
            f"Participant {i+1} Name", 
            placeholder=f"Enter name for participant {i+1}", 
            key=f"participant_{i}",
            label_visibility="collapsed"
        )
        participants.append(participant if participant else f"Participant {i+1}")
    
    # Generate button with custom class
    generate_btn = st.button("Generate Debate", key="generate_debate", use_container_width=True)

with output_col:
    if generate_btn:
        if topic:
            st.subheader("Generated Debates")
            
            # Generate debate cards
            for i, participant in enumerate(participants):
                with st.container():
                    st.markdown(f'<div class="debate-card">', unsafe_allow_html=True)
                    st.markdown(f'**{participant}**', unsafe_allow_html=True)
                    
                    if i % 2 == 0:
                        argument = f"This is a sample argument in favor of '{topic}'..."
                    else:
                        argument = f"This is a sample argument against '{topic}'..."
                    
                    st.markdown(f'<div style="margin-top: 8px;">{argument}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a debate topic first")
    else:
        st.markdown("""
            <div style="text-align: center; color: #666; margin-top: 50%;">
                Generated debates will appear here<br>
                Configure your debate and click generate
            </div>
        """, unsafe_allow_html=True)
