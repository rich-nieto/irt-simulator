import numpy as np
from .base_model import BaseIRTModel

class GradedResponseModel(BaseIRTModel):
    def compute_probabilities(self):
        """
        Compute probabilities for the Graded Response Model (GRM).

        Returns:
        - probabilities (list of np.ndarray): List of probability matrices, one for each category.
        """
        n_categories = self.b.shape[1]  # Number of response categories per item
        n_respondents, n_items = len(self.theta), len(self.a)

        # Compute cumulative probabilities (P^* above)
        cumulative_probs = np.zeros((n_respondents, n_items, n_categories + 1))
        for k in range(n_categories):
            cumulative_probs[:, :, k] = 1 / (1 + np.exp(-self.a * (self.theta[:, np.newaxis] - self.b[:, k])))

        # Compute category probabilities as differences of cumulative probabilities
        probabilities = np.zeros((n_respondents, n_items, n_categories))
        for k in range(n_categories):
            probabilities[:, :, k] = cumulative_probs[:, :, k] - cumulative_probs[:, :, k + 1]

        return probabilities

    def simulate_responses(self, probabilities):
        """
        Simulate responses for polytomous items using the GRM.

        Parameters:
        - probabilities (np.ndarray): Probability matrices for each category.

        Returns:
        - responses (np.ndarray): Simulated ordinal responses.
        """
        n_respondents, n_items, n_categories = probabilities.shape
        responses = np.zeros((n_respondents, n_items), dtype=int)

        for i in range(n_items):
            for j in range(n_respondents):
                responses[j, i] = np.random.choice(range(n_categories), p=probabilities[j, i])

        return responses
