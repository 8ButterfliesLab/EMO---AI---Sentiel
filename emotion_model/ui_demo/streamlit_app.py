# streamlit_app.py

import streamlit as st
from emotion_model.plutchik_classifier import classify_emotion
from emotion_model.voice_analysis.pitch_detector import extract_pitch

st.title("EMO-AI-Sentinel 🌐")
st.write("Emotion-aware emergency assistant")

voice_input = st.text_input("Simulate voice input (describe tone, emotion or keywords):")

if st.button("Analyze"):
    pitch = extract_pitch(voice_input)
    emotion = classify_emotion(pitch, voice_input)
    st.success(f"Detected emotion: **{emotion}**")
