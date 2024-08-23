import streamlit as st
from gtts import gTTS
import os

def language_selector():
    """Allows users to select their preferred language."""
    return st.sidebar.selectbox("Select Language", ["English", "Setswana"])

def play_audio(text, lang):
    """Converts text to speech and plays the audio."""
    tts = gTTS(text=text, lang=lang)
    tts.save("temp_audio.mp3")
    audio_file = open("temp_audio.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
    os.remove("temp_audio.mp3")

def translate_text(text, lang):
    """Translates text based on the selected language."""
    if lang == "Setswana":
        # Example translations; you can add more here
        translations = {
            "Welcome to R&R Telehealth": "Amogelesega go R&R Telehealth",
            "**Your health, our priority!!!** Access quality healthcare from the comfort of your home. R&R Telehealth ensures that everyone has healthy lives and well-being for all ages is promoted.": 
            "**Boitekanelo jwa gago, ke ntlha ya konokono!!!** Fokotsa pharakano ka go dirisa ditiro tsa kalafi go tswa ka fa ntlong ya gago. R&R Telehealth e tshegetsa gore botlhe ba nne le matshelo a a siameng le go tokafatsa botsogo jwa batho ba dingwaga tsotlhe.",
            # Add more translations as needed
        }
        return translations.get(text, text)
    return text
