import streamlit as st
import time
from chains import generate_email


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="centered"
)



# ---------------- PREMIUM CSS ---------------- #

st.markdown("""
<style>

/* BACKGROUND */

.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}



/* MAIN CONTAINER */

.main-box {

    background: rgba(255,255,255,0.08);

    padding: 30px;

    border-radius: 20px;

    backdrop-filter: blur(15px);

    animation: fadeIn 1.5s ease;

}



/* TITLE */

.title {

    text-align:center;

    font-size:45px;

    font-weight:bold;

    color:white;

    margin-bottom:5px;

    animation: slideDown 1s ease;

}


.subtitle {

    text-align:center;

    color:#cccccc;

    margin-bottom:30px;

}



/* TEXTAREA FIX FULL */

.stTextArea textarea {

    background: rgba(0,0,0,0.6) !important;

    color: white !important;

    caret-color: white !important;

    border-radius:12px !important;

    font-size:16px !important;

    border: 2px solid rgba(0,198,255,0.3) !important;

    transition: 0.3s;

}


/* TEXTAREA GLOW ON FOCUS */

.stTextArea textarea:focus {

    border: 2px solid #00c6ff !important;

    box-shadow: 0 0 15px #00c6ff !important;

}



/* LABEL COLOR */

.stTextArea label {

    color: white !important;

    font-weight: bold;

}



/* PLACEHOLDER COLOR */

.stTextArea textarea::placeholder {

    color: #cccccc !important;

    opacity: 1 !important;

}




/* BUTTON */

.stButton button {

    width:100%;

    border-radius:12px;

    background: linear-gradient(90deg,#00c6ff,#0072ff);

    color:white;

    font-size:18px;

    font-weight:bold;

    padding:12px;

    border:none;

    transition:0.3s;

}


.stButton button:hover {

    transform:scale(1.05);

    box-shadow: 0 0 15px #00c6ff;

}




/* OUTPUT BOX */

.output-box {

    background: rgba(0,0,0,0.85);

    color: #00ffcc;

    padding: 20px;

    border-radius: 12px;

    margin-top:20px;

    font-family: monospace;

    font-size:16px;

    min-height:150px;

    border:1px solid #00c6ff;

}



/* ANIMATIONS */

@keyframes fadeIn {

from {opacity:0;}

to {opacity:1;}

}


@keyframes slideDown {

from {

transform:translateY(-50px);

opacity:0;

}

to {

transform:translateY(0);

opacity:1;

}

}

</style>
""", unsafe_allow_html=True)




# ---------------- HEADER ---------------- #

st.markdown('<div class="title">📧 AI Cold Email Generator</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Generate High-Converting Cold Emails using AI</div>', unsafe_allow_html=True)




# ---------------- MAIN BOX ---------------- #

st.markdown('<div class="main-box">', unsafe_allow_html=True)



job = st.text_area(
    "Paste Job Description",
    placeholder="Example: We are looking for a React Native developer..."
)




# ---------------- GENERATE BUTTON ---------------- #

if st.button("🚀 Generate Email"):



    if job:



        with st.spinner("AI is writing your email..."):



            email = generate_email(job)



        st.success("Email Generated Successfully!")



        # Typing animation

        output_area = st.empty()

        typed_text = ""



        for char in email:

            typed_text += char

            output_area.markdown(

                f'<div class="output-box">{typed_text}</div>',

                unsafe_allow_html=True

            )

            time.sleep(0.01)



        # Copy box

        st.code(email, language="markdown")



    else:

        st.warning("Please enter job description")



st.markdown('</div>', unsafe_allow_html=True)
