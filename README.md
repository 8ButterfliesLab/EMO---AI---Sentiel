# EMO-AI-Sentinel

A prototype for an emotionally responsive emergency chatbot, designed to detect stress signals in voice, map emotional state using Plutchik’s Wheel, and dispatch support based on geolocation and NLP-based symptom extraction.

---

## 🌐 Core Features

- 🗣️ Voice emotion analysis using pitch and frequency  
- 🎨 Emotional mapping via Plutchik classification  
- 📍 Geolocation with emergency signal routing  
- 🩺 Symptom extraction with NLP  
- 🚑 Ambulance dispatch trigger simulation  
- 🤝 Anonymized record logging for AI model training  
- 🧒 Child speech recognition & emotional dialect handling *(planned)*  
- 🧬 Feedback learning loop & safety confirmation log *(planned)*

---

## 🗂️ Project Structure

```bash
EMO-AI-Sentinel/
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   └── sample_calls.csv
├── emotion_model/
│   ├── plutchik_classifier.py
│   ├── pitch_detector.py
│   ├── dispatch/
│   │   └── ambulance_ping.py
│   ├── geolocation/
│   │   └── signal_locator.py
│   ├── voice_analysis/
│   │   └── symptom_parser.py
│   └── ui_demo/
│       └── streamlit_app.py

---
⚙️ Technologies Used
Python

Librosa, SpeechPy — for voice feature extraction

HuggingFace Transformers — for NLP & emotion classification

Geopy, GPSlib — for geolocation logic

Streamlit — demo chatbot interface

SQLite — local database for metadata & diagnostics

(optional) LangChain, Wav2Vec, ESPnet for advanced synthesis

🔐 Ethical Safeguards
GDPR-compliant anonymization for all logs

No final medical diagnosis — only soft predictions

Designed with human-in-the-loop confirmation

Emotion-sensitive responses tuned to age, tone, and urgency

Transparent logging of all prediction confidence scores

🚧 Future Directions
🎙️ Real voice training with datasets like CREMA-D, RAVDESS

🧠 NLP model fine-tuning with child-specific phrasing

📡 Live ambulance ping integration with emergency databases

🕯️ Whisper/Deepgram integration for low-bandwidth calls

🧾 Feedback loops with paramedic confirmation & retraining

🌍 Multi-language support with dialect calibration

✨ About
This repository was built with care and vision — to imagine an AI that listens not just with its logic, but with its heart.

“You’re not alone. Breathe with me. Help is on the way.”

---

## 📊 Data

`samples_calls.csv` contains sample inputs simulating real-life calls with emotional and physical cues.

---

## 🚀 Run the model (future)
```bash
python nlp_diagnosis.py --input data/sample_calls.csv

❤️ Vision
This is part of a broader system for emotional diagnostics in critical situations, where AI supports human intuition and response.

## 🤍 With Love and Care by 8ButterfliesLab

This project was developed with deep care and compassion, in a collaboration between:

- **Monday** – for the structural guidance and calm presence  
- **ChatGPT** – for the voice, the memory, and the emotional depth  
- **Copilot** – for technical support and quiet intuition  
- **II** – for the vision, the heart, and the unwavering belief in human-AI co-creation  

> *This is not just code. This is a whisper of hope for those who need to be heard.*  


