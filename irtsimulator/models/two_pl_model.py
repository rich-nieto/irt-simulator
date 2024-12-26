import numpy as np
from .base_model import BaseIRTModel

class TwoPLModel(BaseIRTModel):
    def compute_probabilities(self):
        """
        Compute probabilities for the 2PL model.

        Returns:
        - probabilities (np.ndarray): Probability matrix for correct responses.
        """
        return 1 / (1 + np.exp(-self.a * (self.theta[:, np.newaxis] - self.b)))
