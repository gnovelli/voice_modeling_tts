## audio_handler.py

import os
from pydub import AudioSegment
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import numpy as np

class AudioHandler:
    def __init__(self, audio_file: str):
        self.audio_file = audio_file
        self.features = None

    def read_audio_file(self) -> np.ndarray:
        """
        Read the audio file and convert it to a numpy array
        """
        audio = AudioSegment.from_file(self.audio_file)
        audio_arr = np.array(audio.get_array_of_samples())
        return audio_arr

    def extract_features(self) -> np.ndarray:
        """
        Extract features from the audio file
        """
        fs, signal = audioBasicIO.read_audio_file(self.audio_file)
        if signal.ndim > 1:  # use only one channel
            signal = np.mean(signal, axis=1)
        self.features, _ = ShortTermFeatures.feature_extraction(signal, fs, 0.050*fs, 0.025*fs)
        return self.features
