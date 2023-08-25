import argparse
from text_handler import TextHandler
from model import Model

class TTS:
    def __init__(self, text_file: str, model_path: str = 'model.gmm'):
        self.text_file = text_file
        self.text_handler = TextHandler(self.text_file)
        self.model = Model()
        self.model.load_model(model_path)

    def perform_tts(self) -> None:
        """
        Perform text-to-speech using the loaded vocal model
        """
        tts = self.text_handler.convert_to_speech()
        tts.save('output.mp3')
        print(f'Text-to-speech output saved as output.mp3')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform text-to-speech using a trained vocal model.')
    parser.add_argument('text_file', help='Text file to convert to speech.')
    parser.add_argument('--model_path', default='model.gmm', help='Path to the trained model.')
    args = parser.parse_args()

    tts = TTS(args.text_file, args.model_path)
    tts.perform_tts()
