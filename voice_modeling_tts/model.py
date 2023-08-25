import numpy as np
from sklearn.mixture import GaussianMixture
import pickle

class Model:
    def __init__(self, features: np.ndarray = None):
        self.features = features
        self.model = None

    def train_model(self) -> GaussianMixture:
        """
        Train a Gaussian Mixture Model (GMM) using the extracted features
        """
        self.model = GaussianMixture(n_components=16, covariance_type='diag', n_init=3)
        self.model.fit(self.features.T)
        return self.model

    def save_model(self, model_path: str = 'model.gmm') -> None:
        """
        Save the trained model to a file
        """
        with open(model_path, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, model_path: str = 'model.gmm') -> GaussianMixture:
        """
        Load a trained model from a file
        """
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)
        return self.model
