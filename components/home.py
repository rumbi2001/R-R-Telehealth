import streamlit as st
from utils import language_selector, translate_text

def app():
    # Language selection
    lang = language_selector()

    # Translated title
    st.title(translate_text("Welcome to R&R Telehealth", lang))
    
    # Display image
    st.image("images/telehealth3.jpg", width=400)

    # Translated text
    text = translate_text(
        "**Your health, our priority!!!** Access quality healthcare from the comfort of your home. R&R Telehealth ensures that everyone has healthy lives and well-being for all ages is promoted.", lang)
    st.write(text)

    # Custom CSS for moving text animation
    st.markdown("""
        <style>
        .floating-container {
            position: relative;
            height: 400px;
            width: 100%;
        }
        .floating-text {
            position: absolute;
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
            animation: float 5s ease-in-out infinite;
        }

        @keyframes float {
            0% { transform: translate(0, 0); }
            25% { transform: translate(50px, -50px); }
            50% { transform: translate(100px, 0); }
            75% { transform: translate(-50px, 50px); }
            100% { transform: translate(0, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # HTML for floating text elements
    floating_texts = ["Good Health", "Well-Being", "Healthy Lives", "Telemedicine", "Care", "Support"]
    translated_texts = [translate_text(text, lang) for text in floating_texts]

    # Updated floating text elements with translation
    st.markdown("""
        <div class="floating-container">
            <div class="floating-text" style="top: 20px; left: 20px;">{}</div>
            <div class="floating-text" style="top: 100px; left: 100px;">{}</div>
            <div class="floating-text" style="top: 180px; left: 180px;">{}</div>
            <div class="floating-text" style="top: 260px; left: 260px;">{}</div>
            <div class="floating-text" style="top: 340px; left: 340px;">{}</div>
            <div class="floating-text" style="top: 420px; left: 420px;">{}</div>
        </div>
    """.format(*translated_texts), unsafe_allow_html=True)

if __name__ == "__main__":
    app()
