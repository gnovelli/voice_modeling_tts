import os
from gtts import gTTS

class TextHandler:
    def __init__(self, text_file: str):
        self.text_file = text_file
        self.text = None

    def read_text_file(self) -> str:
        """
        Read the text file and return its content
        """
        with open(self.text_file, 'r') as file:
            self.text = file.read()
        return self.text

    def convert_to_speech(self, lang: str = 'en') -> gTTS:
        """
        Convert the text to speech using Google Text-to-Speech
        """
        self.read_text_file()
        tts = gTTS(text=self.text, lang=lang)
        return tts
