import streamlit as st
import base64
import os # Import os module to handle file paths

# --- Custom CSS for UI/UX Matching ---
def load_css(background_image_path=None):
    background_css = ""
    if background_image_path:
        # Check if the path exists and is a file
        if os.path.exists(background_image_path) and os.path.isfile(background_image_path):
            try:
                with open(background_image_path, "rb") as f:
                    img_data = f.read()
                background_image_base64 = base64.b64encode(img_data).decode()
                background_css = f"""
                    background-image: url("data:image/png;base64,{background_image_base64}"); /* Assuming .png now based on your path */
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                """
            except Exception as e:
                st.error(f"Error loading background image: {e}. Using solid dark background.")
                background_css = "background-color: #1A1A32;" # Fallback solid dark color
        else:
            st.error(f"Background image file not found at path: {background_image_path}. Using solid dark background.")
            background_css = "background-color: #1A1A32;" # Fallback solid dark color
    else:
        background_css = "background-color: #1A1A32;" # Dark purplish-blue background

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap');

        /* General App Background (from user's image) */
        .stApp {{
            {background_css}
            font-family: 'Pixelify Sans', cursive; /* Apply pixel font globally */
            color: #EEEEEE; /* Light text color for main app titles outside the box */
            display: flex;
            flex-direction: column; /* Allow header and main content to stack */
            justify-content: flex-start;
            align-items: center;
            min-height: 100vh;
            padding-top: 2rem;
            line-height: 1.5; /* Improve readability for pixel font */
        }}

        /* Main Header and Subtitle Styling (outside the main content box) */
        h1 {{
            text-align: center;
            color: #EEEEEE; /* White for header texts */
            font-family: 'Pixelify Sans', cursive; /* Ensure pixel font consistency */
            font-size: 3em; /* Use em for scaling with font size */
            margin-bottom: 0.5em;
        }}
        /* The main subtitle "Enter your topic and customize the participants" will be inside the new outer box */

        /* Styles for the NEW outer transparent box covering main content and subtitle */
        .outer-transparent-box {{
            background-color: rgba(35, 33, 48, 0); /* Fully transparent background */
            border-radius: 10px;
            padding: 2.5rem; /* Padding for the entire content area inside this box */
            box-shadow: none; /* No shadow */
            color: #EEEEEE !important;
            display: flex;
            flex-direction: column;
            width: 90%; /* Responsive width: 90% of viewport */
            max-width: 1200px; /* Max limit */
            margin-top: 0rem;
            min-height: auto;
        }}
        .outer-transparent-box > p {{ /* Subtitle inside the new outer box */
            font-size: 1.2em; /* Use em for scaling */
            margin-top: 0;
            margin-bottom: 2em; /* Spacing below subtitle */
            text-align: center;
            color: #EEEEEE;
            font-family: 'Pixelify Sans', cursive;
        }}


        /* Style for the *inner* content area containing both columns (now inside .outer-transparent-box) */
        .main .block-container {{ /* This class is applied to st.columns container */
            background-color: rgba(35, 33, 48, 0); /* Main container is transparent */
            border-radius: 10px;
            padding: 0; /* No padding here, padding will be inside the new transparent boxes */
            box-shadow: none;
            color: #EEEEEE !important;
            display: flex;
            flex-direction: row;
            width: 100%;
            gap: 2rem; /* Space between the two main transparent boxes */
            min-height: auto;
        }}
        
        /* Adjust column specific padding within the dark box */
        .st-emotion-cache-10y5g9x, .st-emotion-cache-1f89mtp, .st-emotion-cache-1d3jo4v {{ /* Targets for columns */
            padding-right: 0rem; 
            padding-left: 0rem; 
            flex: 1; /* Distribute space equally */
        }}

        /* Input field styling (shorter height) */
        .st-emotion-cache-1wb0q5t, .st-emotion-cache-1ujn73d, .st-emotion-cache-1c7y2gy {{ /* Input containers */
            background-color: #3A3945 !important;
            border: 1px solid #555566 !important;
            border-radius: 5px !important;
            color: #EEEEEE !important;
            padding: 0.25rem 0.5rem; /* Reduced vertical padding */
            margin-bottom: 1rem;
            min-height: auto !important; /* Ensure auto height */
        }}
        .st-emotion-cache-1wb0q5t:focus-within, .st-emotion-cache-1ujn73d:focus-within, .st-emotion-cache-1c7y2gy:focus-within {{
            border-color: #88AACC !important;
            box-shadow: 0 0 0 0.2rem rgba(136, 170, 204, 0.25) !important;
        }}
        .st-emotion-cache-1wb0q5t > div > label + div > div > input {{ /* Actual input text field */
            background-color: #3A3945 !important;
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive;
            padding: 0.25rem 0.5rem !important; /* Reduced padding for inner input */
            min-height: auto !important; /* Ensure auto height */
            line-height: 1.2 !important; /* Compact line height */
        }}

        /* Labels for input fields */
        .st-emotion-cache-h6q4mk {{ /* Labels for text_input, etc. */
            color: #EEEEEE !important;
            font-weight: normal;
            font-family: 'Pixelify Sans', cursive;
        }}
        .st-emotion-cache-1ujn73d > div > label > div {{ /* Label for number_input/slider */
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive;
        }}

        /* Slider styling (shorter) */
        .stSlider .st-emotion-cache-p2q3l1 {{ /* Track container */
            background-color: #555566 !important;
            height: 0.5rem; /* Reduced track height */
        }}
        .stSlider .st-emotion-cache-b3z4j {{ /* Filled track */
            background-color: #88AACC !important;
            height: 0.5rem; /* Reduced track height */
        }}
        .stSlider .st-emotion-cache-13sng9l {{ /* Thumb */
            background-color: #EEEEEE !important;
            border: 2px solid #88AACC !important;
            height: 1rem; /* Smaller thumb */
            width: 1rem; /* Smaller thumb */
            top: -0.25rem; /* Adjust position */
        }}
        .stSlider .st-emotion-cache-1c7y2gy p {{ /* Value label (number above slider) */
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive;
            font-size: 0.9em; /* Smaller font size */
            margin-top: -0.5rem !important; /* Pull it up */
            margin-bottom: 0 !important; /* Remove bottom margin */
            line-height: 1 !important; /* Compact line height */
        }}
        /* Make sure the overall slider component doesn't take too much vertical space */
        .stSlider {{
            margin-bottom: 1rem; /* Space below the slider */
            padding-top: 0.5rem; /* Adjust padding for slider area */
            padding-bottom: 0.5rem; /* Adjust padding for slider area */
        }}


        /* Button styling */
        .st-emotion-cache-lck164 {{
            background-color: #3A3945 !important;
            color: #EEEEEE !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: bold !important;
            border: none !important;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            transition: background-color 0.2s;
            width: 100%;
            margin-top: 1rem;
            font-family: 'Pixelify Sans', cursive;
        }}
        .st-emotion-cache-lck164:hover {{
            background-color: #4A4955 !important;
        }}
        
        /* Generated Debates title (within red box) */
        .st-emotion-cache-fg4pbf {{
            color: #CCCCCC !important;
            font-weight: bold;
            font-size: 1.1em;
            margin: 0; /* Remove default margin */
            font-family: 'Pixelify Sans', cursive;
        }}

        /* General text (e.g., placeholder text in Generated Debates) */
        .st-emotion-cache-10qik0g {{
            color: #CCCCCC !important;
            font-family: 'Pixelify Sans', cursive;
            /* Adjustments for alignment - moved to a new class below */
        }}

        /* Styles for the brown transparent box covering all left inputs */
        .left-main-brown-box {{
            background-color: rgba(139, 69, 19, 0.4); /* Brown with 40% transparency */
            border-radius: 10px;
            padding: 2.5rem; /* Padding inside this big brown box */
            min-height: auto; /* Auto height */
            flex-grow: 1; /* Allow it to grow in flex container */
        }}

        /* Styles for the red transparent box at the top right */
        .top-right-red-box {{
            background-color: rgba(255, 0, 0, 0.4); /* Red with 40% transparency */
            border-radius: 10px;
            padding: 1.5rem; /* Padding inside the red box */
            width: 100%; /* Spans the width of its column */
            min-height: auto; /* Auto height, as requested */
            display: flex; /* For centering content */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            margin-bottom: 1.5rem; /* Space below it */
            flex-shrink: 0; /* Prevent it from shrinking */
        }}
        /* Ensure the H3 inside the red box aligns correctly */
        .top-right-red-box h3 {{
            text-align: center; /* Center the text inside */
        }}

        /* New class for aligning debate content texts */
        .debate-content-text {{
            color: #CCCCCC !important;
            font-family: 'Pixelify Sans', cursive;
            padding-left: 0rem !important; /* Reset default Streamlit padding */
            margin-left: 0rem !important; /* Reset default Streamlit margin */
            line-height: 1.5em; /* Standard line height for readability */
            margin-bottom: 0.5em; /* Space between paragraphs */
        }}
        .debate-content-text.bold {{
            color: #EEEEEE !important;
            font-weight: bold;
        }}

        /* Hide Streamlit's default header/footer if desired for cleaner look */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)


# --- Global variable for background image path (User will set this) ---
# IMPORTANT: Replace "your_pixel_background.jpg" with the actual path to your image
# For example: BACKGROUND_IMAGE_PATH = "C:/Users/udayg/Downloads/final bg.png"
# Or if it's in the same directory as your script: BACKGROUND_IMAGE_PATH = "final bg.png" if it's in the same folder.
BACKGROUND_IMAGE_PATH = r"C:\Users\udayg\AppData\Roaming\Python\AI-Debate-Generator-\bg.png" # Updated path!

# Load the CSS with the specified background image
load_css(BACKGROUND_IMAGE_PATH)

st.set_page_config(layout="wide", page_title="AI Debate Generator")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>AI Debate Generator</h1>", unsafe_allow_html=True)

# --- New Outer Transparent Box to contain the subtitle and the main columns ---
st.markdown("<div class='outer-transparent-box'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your topic and customize the participants.</p>", unsafe_allow_html=True)

# --- Main Content Area: The overall layout container ---
# This st.container typically gets the .main .block-container styling automatically.
# We'll rely on the CSS applied to .main .block-container to make it transparent and control its internal layout.
with st.container(): 
    col1, col2 = st.columns(2)

    # --- Left Column: Debate Topic and Participants Input (All in one brown transparent box) ---
    with col1:
        # Wrap ALL left-side content in the new brown transparent box
        st.markdown("<div class='left-inputs-container'>", unsafe_allow_html=True)
        
        st.text_input("Debate Topic", value="random", key="debate_topic") 

        # Slider for Number of Participants
        num_participants = st.slider("Number of Participants", min_value=2, max_value=10, value=2, step=1, key="num_participants")

        participant_names = []
        # Display participant input fields based on the number chosen
        for i in range(int(num_participants)):
            initial_value = ""
            if i == 0:
                initial_value = "ram" 
            elif i == 1:
                initial_value = "sur" 
            
            st.text_input(f"Participant {i+1} Name", value=initial_value, key=f"participant_{i+1}_name")
            participant_names.append(st.session_state[f"participant_{i+1}_name"])


        # Generate Debate Button
        generate_button = st.button("Generate Debate")
        st.markdown("</div>", unsafe_allow_html=True) # Close the left-inputs-container

    # --- Right Column: Generated Debates Display ---
    with col2:
        # The red box at the top right
        st.markdown("""
        <div class='top-right-red-box'>
            <h3 class='st-emotion-cache-fg4pbf'>Generated Debates</h3>
        </div>
        """, unsafe_allow_html=True)

        # Content to display when button is clicked or initially (these are outside the red header box)
        # Use a consistent element for all these text lines to control alignment easily
        # Applying padding to a div containing the content for alignment
        st.markdown("<div class='debate-content-alignment'>", unsafe_allow_html=True) 

        if generate_button:
            topic = st.session_state.debate_topic
            st.markdown(f"<p class='debate-content-text bold'>{topic}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='debate-content-text'>This is a sample argument in favor of \"{topic}\".</p>", unsafe_allow_html=True)

            for i, participant in enumerate(participant_names):
                if participant.strip() == "":
                    continue
                st.markdown(f"<p class='debate-content-text bold'>{participant}</p>", unsafe_allow_html=True)
                if i % 2 == 0:
                    st.markdown(f"<p class='debate-content-text'>This is a sample argument against \"{topic}\" by {participant}.</p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<p class='debate-content-text'>This is a sample argument in favor of \"{topic}\" by {participant}.</p>", unsafe_allow_html=True)
        else:
            # Static preview matching the latest image
            st.markdown("<p class='debate-content-text bold'>random</p>", unsafe_allow_html=True)
            st.markdown("<p class='debate-content-text'>This is a sample argument in favor of \"random\".</p>", unsafe_allow_html=True)
            st.markdown("<p class='debate-content-text bold'>ram</p>", unsafe_allow_html=True)
            st.markdown("<p class='debate-content-text'>This is a sample argument against \"random\" by ram.</p>", unsafe_allow_html=True)
            st.markdown("<p class='debate-content-text bold'>sur</p>", unsafe_allow_html=True)
            st.markdown("<p class='debate-content-text'>This is a sample argument in favor of \"random\" by sur.</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True) # Close content alignment div
