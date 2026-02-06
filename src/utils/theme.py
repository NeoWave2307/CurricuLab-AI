"""
Centralized UI Theme Utility
Implements the Creme/Beige professional theme with specific typography.
"""
import streamlit as st

def apply_theme():
    """Apply the global application theme."""
    st.markdown("""
    <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Libre+Bodoni:ital,wght@0,400;0,700;1,400&family=Nunito:wght@300;400;600&family=Lato:wght@400;700&display=swap');

        /* Hide Streamlit Elements */
        #MainMenu {display: none !important;}
        footer {display: none !important;}
        header {display: none !important;}
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        [data-testid="stDecoration"] {display: none !important;}
        
        /* Animated Background */
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .stApp {
            font-family: 'Nunito', sans-serif; /* Mild superellipse font for body */
            background: linear-gradient(-45deg, #F5F5DC, #FFFDD0, #F2E8CF, #EAE2B7);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #4A4A4A;
        }

        /* Typography */
        h1, .app-title, .header-title {
            font-family: 'Libre Bodoni', serif !important; /* Serif Didone for titles */
            color: #3E2723 !important; /* Dark Brown */
        }

        h2, h3, .app-subtitle, .header-subtitle {
            font-family: 'Lato', sans-serif !important; /* Appropriate font for subheadings */
            color: #5D4037 !important; /* Medium Brown */
        }
        
        p, .stMarkdown, .role-label, div[data-testid="stCaptionContainer"] {
            font-family: 'Nunito', sans-serif !important;
            color: #4E342E;
        }

        /* Dashboard Header */
        .dashboard-header {
            background: rgba(255, 255, 255, 0.85);
            border-bottom: 1px solid #D7CCC8;
            padding: 1.5rem 0;
            margin-bottom: 2rem;
            padding-left: 20px;
            box-shadow: 0 4px 6px rgba(139, 69, 19, 0.1);
            border-radius: 8px;
            backdrop-filter: blur(5px);
        }

        /* Professional Buttons (Beige/Brown Theme) */
        .stButton>button {
            background: rgba(255, 255, 255, 0.7);
            color: #5D4037;
            border: 1px solid #D7CCC8;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-family: 'Lato', sans-serif;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        .stButton>button:hover {
            background: #FFF8E1;
            border-color: #8D6E63;
            color: #3E2723;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(139, 69, 19, 0.15);
        }
        
        /* Input Fields */
        .stTextInput>div>div, .stTextArea>div>div, .stSelectbox>div>div {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 8px;
            border: 1px solid #D7CCC8;
            color: #4E342E;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            font-family: 'Lato', sans-serif;
            color: #5D4037;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 4px;
        }
        
        /* Cards/Containers */
        div[data-testid="stForm"] {
            background-color: rgba(255, 255, 255, 0.6);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid #EFEBE9;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

    </style>
    """, unsafe_allow_html=True)
