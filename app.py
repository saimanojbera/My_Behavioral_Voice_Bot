import streamlit as st
from utils import (
    get_answer,
    text_to_speech,
    autoplay_audio,
    speech_to_text,
    load_my_story
)
from audio_recorder_streamlit import audio_recorder
from streamlit_float import float_init
import os

# Enable floating UI elements
float_init()

# Load your personal context once
my_story_context = load_my_story()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm here to answer any behavioral questions you have."}]

# Page title
st.title("🎤 Behavioral Voice Bot (Saimanoj Bera)")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Record user audio
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

# If audio is recorded, process it
if audio_bytes:
    with st.spinner("Transcribing your question..."):
        webm_file_path = "temp_input_audio.mp3"
        with open(webm_file_path, "wb") as f:
            f.write(audio_bytes)

        transcript = speech_to_text(webm_file_path)
        os.remove(webm_file_path)

        if transcript:
            st.session_state.messages.append({"role": "user", "content": transcript})
            with st.chat_message("user"):
                st.write(transcript)

# Generate response if last message is user
if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_text = get_answer(st.session_state.messages, my_story_context)
        with st.spinner("Generating voice response..."):
            audio_file = text_to_speech(response_text)
            autoplay_audio(audio_file)
        st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        os.remove(audio_file)
