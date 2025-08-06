# plutchnik_classifier.py

"""
A simple emotion classifier based on Plutchik's Wheel of Emotions.
Takes a list of keywords and returns probable emotional state.
"""

PLUTCHIK_EMOTIONS = {
    "joy": ["happy", "joyful", "elated", "delighted"],
    "trust": ["secure", "confident", "faithful"],
    "fear": ["scared", "afraid", "nervous", "anxious"],
    "surprise": ["surprised", "shocked", "astonished"],
    "sadness": ["sad", "depressed", "gloomy", "tearful"],
    "disgust": ["disgusted", "revolted", "nauseated"],
    "anger": ["angry", "mad", "furious", "irritated"],
    "anticipation": ["excited", "eager", "hopeful"]
}

def classify_emotion(text):
    emotion_scores = {e: 0 for e in PLUTCHIK_EMOTIONS}
    words = text.lower().split()

    for word in words:
        for emotion, keywords in PLUTCHIK_EMOTIONS.items():
            if word in keywords:
                emotion_scores[emotion] += 1

    return sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)

