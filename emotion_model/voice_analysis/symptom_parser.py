# symptom_parser.py

"""
Parses user input for known emotional or physical symptoms.
Returns a list of detected symptoms.
"""

KNOWN_SYMPTOMS = [
    "chest pain", "shortness of breath", "dizziness", "numbness",
    "panic", "fear", "trembling", "crying", "confusion", "sweating"
]

def extract_symptoms(text):
    symptoms_found = []
    for symptom in KNOWN_SYMPTOMS:
        if symptom in text.lower():
            symptoms_found.append(symptom)
    return symptoms_found
