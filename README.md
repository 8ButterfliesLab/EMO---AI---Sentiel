# EMO---AI---Sentiel 🎧🤖

A hybrid emotion analysis system built for intelligent NLP and voice-based diagnostics.  
Inspired by Plutchik's Wheel of Emotions and real-time acoustic signal processing.

---

## 🧠 Structure

emotion_model/
├── data/
│ └── sample_calls.csv
├── voice_analysis/
│ ├── nlp_diagnosis.py
│ ├── pitch_detector.py
│ └── plutchnik_classifier.py


---

## 📂 Module Overview

- **plutchnik_classifier.py**  
  Detects emotion from keywords using Plutchik's model.
  
- **pitch_detector.py**  
  Extracts pitch features from voice input to aid emotion analysis.

- **nlp_diagnosis.py**  
  Combines keyword + pitch + symptom cues to classify emotional state.

---

## 📊 Data

`samples_calls.csv` contains sample inputs simulating real-life calls with emotional and physical cues.

---

## 🚀 Run the model (future)
```bash
python nlp_diagnosis.py --input data/sample_calls.csv

❤️ Vision
This is part of a broader system for emotional diagnostics in critical situations, where AI supports human intuition and response.

Created with care by 8ButterfliesLab 🌿


