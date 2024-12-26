import numpy as np

class BaseIRTModel:
    def __init__(self, a, b, theta):
        """
        Base class for IRT models.

        Parameters:
        - a (np.ndarray): Discrimination parameters for items.
        - b (np.ndarray): Difficulty parameters for items.
        - theta (np.ndarray): Ability parameters for respondents.
        """
        self.a = a
        self.b = b
        self.theta = theta

    def compute_probabilities(self):
        """
        Compute probabilities for each respondent-item pair.
        To be implemented by subclasses.
        """
        raise NotImplementedError("This method should be implemented in a subclass.")

    def simulate_responses(self, probabilities):
        """
        Simulate responses based on probabilities.

        Parameters:
        - probabilities (np.ndarray): Probabilities of correct responses.

        Returns:
        - responses (np.ndarray): Simulated binary responses.
        """
        return (np.random.rand(*probabilities.shape) < probabilities).astype(int)
