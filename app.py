import streamlit as st
from elevenlabs_api import get_voices, text_to_speech

st.set_page_config(page_title="🎤 TTS with ElevenLabs API", layout="centered")
st.title("🎤 Text-to-Speech (API-based)")

# Input
text_input = st.text_area("Enter the text to convert to speech:", height=200)

# Get voice options
try:
    voices = get_voices()
    voice_dict = {f"{v['name']} ({v['labels'].get('accent', 'Default')})": v["voice_id"] for v in voices}
    voice_name = st.selectbox("Select Voice:", list(voice_dict.keys()))
    voice_id = voice_dict[voice_name]
except Exception as e:
    st.error(f"Failed to fetch voices: {e}")
    st.stop()

# Generate audio
if st.button("🔊 Generate Voice"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating voice..."):
            try:
                audio_file = text_to_speech(text_input, voice_id)
                st.success("✅ Audio generated!")
                st.audio(audio_file)
                with open(audio_file, "rb") as f:
                    st.download_button("⬇️ Download MP3", f, "output.mp3", "audio/mpeg")
            except Exception as e:
                st.error(f"Error: {e}")
