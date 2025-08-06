# nlp_diagnosis.py

"""
Module for NLP-based emotional diagnosis.
Processes input text and returns a diagnosis based on detected emotional patterns.
"""

def diagnose_emotion(text):
    if "help" in text.lower():
        return "Crisis detected: help requested."
    elif "alone" in text.lower():
        return "Crisis detected: user feels isolated."
    elif "panic" in text.lower():
        return "Crisis detected: panic symptoms identified."
    else:
        return "No immediate crisis detected."
