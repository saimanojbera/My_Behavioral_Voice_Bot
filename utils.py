import os
import base64
import streamlit as st
import json
from openai import OpenAI

# Initialize OpenAI client with secret key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_my_story():
    with open("my_story.json", "r", encoding="utf-8") as file:
        return json.load(file)

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcript

def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    response.stream_to_file(webm_file_path)
    return webm_file_path

def get_answer(messages, context_data):
    # Build context string
    context = f"Name: {context_data['basics']['name']}\nSummary: {context_data['summary']}\n\nExperience:\n"
    for exp in context_data["experience"]:
        context += f"\nRole: {exp['role']} at {exp['company']} ({exp['period']})"
        for resp in exp['responsibilities']:
            context += f"\n- {resp}"

    context += "\n\nSkills: " + ", ".join(context_data["skills"]["programming"] + context_data["skills"]["ai_ml"])
    context += "\n\nPersonal Traits: " + context_data["personal_traits"]["identity"]
    context += "\nMotivation: " + context_data["personal_traits"]["motivation"]
    context += "\nSuperpower: " + context_data["personal_traits"]["superpower"]

    for testimonial in context_data["testimonials"]:
        context += f"\n\nTestimonial from {testimonial['from']}: {testimonial['content']}"

    # System prompt
    system_message = {
        "role": "system",
        "content": f"""You are Saimanoj Bera answering behavioral and professional questions.
Speak directly in first person (I, me, my). Never mention you are an AI or assistant.
Base all answers strictly on the following context:

{context}
"""
    }

    messages_with_context = [system_message] + messages

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages_with_context
    )
    return response.choices[0].message.content

def autoplay_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
