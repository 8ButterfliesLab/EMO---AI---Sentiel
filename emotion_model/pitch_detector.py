# pitch_detector.py

"""
Basic pitch detector using autocorrelation.
To be replaced by more accurate ML-based model in future.
"""

import numpy as np
import librosa

def detect_pitch(audio_path):
    y, sr = librosa.load(audio_path)
    autocorr = np.correlate(y, y, mode='full')
    autocorr = autocorr[len(autocorr)//2:]

    peak = np.argmax(autocorr)
    pitch = sr / peak if peak != 0 else 0
    return pitch


