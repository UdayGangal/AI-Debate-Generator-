import streamlit as st
import base64
import os # Import os module to handle file paths

# --- Custom CSS for UI/UX Matching ---
def load_css(background_image_path=None):
    # Main app background color - as seen in the new image
    main_background_color = "#1A1A32" # A deep dark blue/purple
    background_css = ""

    if background_image_path:
        # Check if the path exists and is a file
        if os.path.exists(background_image_path) and os.path.isfile(background_image_path):
            try:
                with open(background_image_path, "rb") as f:
                    img_data = f.read()
                # Determine mime type based on extension (assuming .png)
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
                background_css = f"background-color: {main_background_color};" # Fallback solid dark color
        else:
            st.error(f"Background image file not found at path: '{background_image_path}'. Please ensure the path is correct and the file exists. Using solid dark background.")
            background_css = f"background-color: {main_background_color};" # Fallback solid dark color
    else:
        background_css = f"background-color: {main_background_color};" # Default solid dark background if no path provided

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap');

        /* General App Background (solid dark color now, or image if loaded) */
        .stApp {{
            {background_css}
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font globally with !important */
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
            font-family: 'Pixelify Sans', cursive !important; /* Ensure pixel font consistency */
            font-size: 3em; /* Use em for scaling with font size */
            margin-bottom: 0.5em;
        }}
        /* The main subtitle "Enter your topic and customize the participants" is now styled below */

        /* Styles for the NEW outer transparent box covering main content and subtitle */
        .outer-transparent-box {{
            background-color: rgba(0, 0, 0, 0); /* Fully transparent background */
            border-radius: 10px;
            padding: 0rem; /* Adjusted padding as content now has its own boxes */
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
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
        }}


        /* Style for the *inner* content area containing both columns (now inside .outer-transparent-box) */
        .main .block-container {{ /* This class is applied to st.columns container */
            background-color: rgba(0, 0, 0, 0); /* Main container is transparent */
            border-radius: 10px;
            padding: 0; /* No padding here, padding will be inside the new transparent boxes */
            box-shadow: none;
            color: #EEEEEE !important;
            display: flex;
            flex-direction: row;
            width: 100%;
            gap: 2rem; /* Space between the two main content areas */
            min-height: auto;
        }}
        
        /* Adjust column specific padding within the dark box */
        .st-emotion-cache-10y5g9x, .st-emotion-cache-1f89mtp, .st-emotion-cache-1d3jo4v {{ /* Targets for columns */
            padding-right: 0rem; 
            padding-left: 0rem; 
            flex: 1; /* Distribute space equally */
        }}

        /* Input field styling (shorter height, dark background, lighter border) */
        .st-emotion-cache-1wb0q5t, .st-emotion-cache-1ujn73d, .st-emotion-cache-1c7y2gy {{ /* Input containers */
            background-color: #3A3945 !important; /* Darker input background */
            border: 1px solid #4A4955 !important; /* Subtle darker border */
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
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
            padding: 0.25rem 0.5rem !important; /* Reduced padding for inner input */
            min-height: auto !important; /* Ensure auto height */
            line-height: 1.2 !important; /* Compact line height */
        }}

        /* Labels for input fields */
        .st-emotion-cache-h6q4mk {{ /* Labels for text_input, etc. */
            color: #EEEEEE !important;
            font-weight: normal;
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
        }}
        .st-emotion-cache-1ujn73d > div > label > div {{ /* Label for number_input/slider */
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
        }}

        /* Slider styling (shorter, red filled track) */
        .stSlider .st-emotion-cache-p2q3l1 {{ /* Track container */
            background-color: #555566 !important;
            height: 0.5rem; /* Reduced track height */
        }}
        .stSlider .st-emotion-cache-b3z4j {{ /* Filled track */
            background-color: #FF6B6B !important; /* Red filled track */
            height: 0.5rem; /* Reduced track height */
        }}
        .stSlider .st-emotion-cache-13sng9l {{ /* Thumb */
            background-color: #EEEEEE !important;
            border: 2px solid #FF6B6B !important; /* Red border for thumb */
            height: 1rem; /* Smaller thumb */
            width: 1rem; /* Smaller thumb */
            top: -0.25rem; /* Adjust position */
        }}
        .stSlider .st-emotion-cache-1c7y2gy p {{ /* Value label (number above slider) */
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
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


        /* Button styling (dark background, lighter text) */
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
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
        }}
        .st-emotion-cache-lck164:hover {{
            background-color: #4A4955 !important; /* Slightly lighter dark on hover */
        }}
        
        /* Generated Debates title (within its gray box) */
        .st-emotion-cache-fg4pbf {{
            color: #EEEEEE !important; /* White for title text */
            font-weight: bold;
            font-size: 1.1em;
            margin: 0; /* Remove default margin */
            font-family: 'Pixelify Sans', cursive !important; /* Ensure pixel font here too */
        }}

        /* General text (e.g., placeholder text in Generated Debates) */
        .st-emotion-cache-10qik0g {{
            color: #CCCCCC !important;
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
        }}

        /* --- BOXES FOR LAYOUT --- */

        /* Styles for the left column content (no background) */
        .left-column-container {{
            background-color: transparent !important; /* Make transparent */
            border-radius: 10px;
            padding: 0rem; /* No padding from this container itself */
            min-height: auto; /* Auto height */
            flex-grow: 1; /* Allow it to grow in flex container */
            box-shadow: none !important; /* Remove shadow */
        }}

        /* Styles for the top right "Generated Debates" title box */
        .generated-header-box {{
            background-color: #2B2B2B; /* Solid dark gray as in the image */
            border-radius: 10px;
            padding: 1.5rem; /* Padding inside this box */
            width: 100%; /* Spans full width of its column */
            min-height: auto; /* Auto height */
            display: flex; /* For centering content */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            margin-bottom: 1.5rem; /* Space below it */
            flex-shrink: 0; /* Prevent it from shrinking */
            box-shadow: none !important; /* No shadow */
        }}
        .generated-header-box h3 {{
            text-align: center;
        }}

        /* Individual boxes around debate topic/participant names on the right */
        .generated-content-item-box {{
            background-color: #555555; /* Light gray box as in image */
            border-radius: 5px;
            padding: 0.75rem 1rem; /* Padding inside these smaller boxes */
            margin-bottom: 1rem; /* Space between items */
            width: 100%; /* Spans full width of its column */
            min-height: auto; /* Auto height */
        }}
        .generated-content-item-box p {{ /* Ensure p tags inside are styled correctly */
            margin: 0; /* Remove default margin for paragraphs */
            color: #EEEEEE !important; /* Text color inside these boxes */
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
            line-height: 1.2; /* Compact line height */
        }}
        /* Specific override for Streamlit's default 'st.write' paragraph element within these boxes */
        .generated-content-item-box .st-emotion-cache-10qik0g p {{
            margin: 0 !important; /* Important to override Streamlit's default margins */
            color: #EEEEEE !important;
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
            line-height: 1.2;
        }}

        /* Specific alignment for content after the top-right header box */
        .right-column-content-area {{
            padding-left: 0; /* Reset default padding */
            padding-right: 0; /* Reset default padding */
            /* We will ensure alignment using the padding within .generated-content-item-box */
        }}

        /* Style for the placeholder text "Generate convo will come here" */
        .placeholder-text {{
            color: #AAAAAA; /* Slightly muted color */
            font-family: 'Pixelify Sans', cursive !important; /* Apply pixel font with !important */
            text-align: center; /* Centered as requested */
            padding-left: 0.75rem; /* Match padding of generated-content-item-box */
            margin-top: 1rem; /* Space below the header box */
            font-size: 0.9em; /* Smaller font size */
        }}
        /* Transparent box around the placeholder text */
        .placeholder-box {{
            background-color: rgba(0, 0, 0, 0); /* Transparent */
            border-radius: 10px;
            padding: 1rem; /* Padding inside the placeholder box */
            min-height: auto; /* Auto height */
            display: flex; /* For centering */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            width: 100%; /* Take full width of its container */
            box-shadow: none; /* No shadow */
        }}


        /* Hide Streamlit's default header/footer if desired for cleaner look */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)


# --- Global variable for background image path (User will set this) ---
# IMPORTANT: Place your 'bg.png' file in the same directory as this Python script.
# Then you can use a relative path like "bg.png".
# If you insist on an absolute path, replace "bg.png" with something like:
# BACKGROUND_IMAGE_PATH = r"C:\Users\udayg\AppData\Roaming\Python\AI-Debate-Generator-\bg.png"
BACKGROUND_IMAGE_PATH = "final bg.png" # Changed to relative path for better reliability

# Load the CSS with the specified background image
load_css(BACKGROUND_IMAGE_PATH)

st.set_page_config(layout="wide", page_title="AI Debate Generator")

# --- Header ---
# Removed default 'st.title' as we're using markdown for styling
st.markdown("<h1 style='text-align: center;'>AI Debate Generator</h1>", unsafe_allow_html=True)

# --- Outer Container for Subtitle and Main Columns ---
# This acts as the main content wrapper. Its padding and responsiveness are defined in .outer-transparent-box CSS.
st.markdown("<div class='outer-transparent-box'>", unsafe_allow_html=True)
# The subtitle is now inside this outer-transparent-box as per the provided code structure
st.markdown("<p style='text-align: center;'>Enter your topic and customize the participants.</p>", unsafe_allow_html=True)

# --- Main Content Area: Columns for Inputs and Generated Debates ---
# Streamlit applies .main .block-container to the div wrapping these columns.
# We've made .main .block-container transparent and set gap between columns.
col1, col2 = st.columns(2)

# --- Left Column: Debate Topic and Participants Input ---
with col1:
    # This st.container helps logically group content for Streamlit,
    # and we apply the 'left-column-container' CSS class to make it transparent.
    with st.container(border=False): 
        # Inputs are directly here, styled by the global CSS for input fields
        # Removed default 'value' for empty start
        st.text_input("Debate Topic", value="", key="debate_topic") 

        # Slider for Number of Participants - value defaults to min_value if not specified
        num_participants = st.slider("Number of Participants", min_value=2, max_value=10, value=2, step=1, key="num_participants")

        participant_names = []
        # Display participant input fields based on the number chosen
        for i in range(int(num_participants)):
            # Removed all 'initial_value' assignments to make them start empty
            st.text_input(f"Participant {i+1} Name", value="", key=f"participant_{i+1}_name")
            participant_names.append(st.session_state[f"participant_{i+1}_name"])


        # Generate Debate Button
        generate_button = st.button("Generate Debate")

# --- Right Column: Generated Debates Display ---
with col2:
    # The solid dark gray box at the top right for the title "Generated Debates"
    st.markdown("""
    <div class='generated-header-box'>
        <h3 class='st-emotion-cache-fg4pbf'>Generated Debates</h3>
    </div>
    """, unsafe_allow_html=True)

    # Content to display when button is clicked or initially (each within its own gray box)
    # The new .right-column-content-area div helps align everything below the header box.
    st.markdown("<div class='right-column-content-area'>", unsafe_allow_html=True) 

    if generate_button:
        # Check if topic and at least two participant names are provided before generating
        valid_participants = [name for name in participant_names if name.strip() != ""]
        if not st.session_state.debate_topic.strip() or len(valid_participants) < 2:
            st.warning("Please enter a debate topic and at least two participant names to generate a debate.")
            # If input is invalid, show the placeholder or a specific error message within the placeholder box
            st.markdown("""
            <div class='placeholder-box'>
                <p class='placeholder-text'>Please fill in all required fields to generate a debate.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            topic = st.session_state.debate_topic
            
            # Display generated content only after button click and valid input
            st.markdown(f"<div class='generated-content-item-box'><p>{topic}</p></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='generated-content-item-box'><p>This is a sample argument in favor of '{topic}'....</p></div>", unsafe_allow_html=True)

            for i, participant in enumerate(participant_names):
                if participant.strip() == "": # Only display if name is provided
                    continue
                st.markdown(f"<div class='generated-content-item-box'><p>{participant}</p></div>", unsafe_allow_html=True)
                if i % 2 == 0:
                    st.markdown(f"<div class='generated-content-item-box'><p>This is a sample argument against '{topic}' by {participant}...</p></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='generated-content-item-box'><p>This is a sample argument in favor of '{topic}' by {participant}....</p></div>", unsafe_allow_html=True)
    else:
        # Placeholder text "Generate convo will come here" is the ONLY thing displayed initially
        # Wrapped in the new transparent placeholder-box
        st.markdown("""
        <div class='placeholder-box'>
            <p class='placeholder-text'>Generate convo will come here</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # Close right-column-content-area

st.markdown("</div>", unsafe_allow_html=True) # Close the outer-transparent-box
