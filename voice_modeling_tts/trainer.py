import argparse
from audio_handler import AudioHandler
from model import Model

class Trainer:
    def __init__(self, audio_files: list[str]):
        self.audio_files = audio_files
        self.audio_handler = None
        self.model = None

    def create_model(self) -> None:
        """
        Create a vocal model from the audio files
        """
        features = []
        for audio_file in self.audio_files:
            self.audio_handler = AudioHandler(audio_file)
            features.append(self.audio_handler.extract_features())
        self.model = Model(features)
        self.model.train_model()

    def save_model(self, model_path: str = 'model.gmm') -> None:
        """
        Save the created vocal model to a file
        """
        self.model.save_model(model_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a vocal model from audio files.')
    parser.add_argument('audio_files', nargs='+', help='One or more audio files to train from.')
    parser.add_argument('--model_path', default='model.gmm', help='Path to save the trained model.')
    args = parser.parse_args()

    trainer = Trainer(args.audio_files)
    trainer.create_model()
    trainer.save_model(args.model_path)
