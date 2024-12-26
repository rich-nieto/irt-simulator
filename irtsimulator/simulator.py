import numpy as np
from .models.two_pl_model import TwoPLModel

class IRTSimulator:
    def __init__(self, model="2PL", n_respondents=1000, n_items=50, seed=None):
        """
        Initialize the IRTSimulator.

        Parameters:
        - model (str): The IRT model to use (e.g., "2PL").
        - n_respondents (int): Number of test-takers to simulate.
        - n_items (int): Number of items to simulate.
        - seed (int): Random seed for reproducibility.
        """
        self.model = model
        self.n_respondents = n_respondents
        self.n_items = n_items
        self.seed = seed
        self.irt_model = None
        np.random.seed(seed)

    def generate_parameters(self, a_dist=(0.5, 2.0), b_dist=(0, 1), theta_dist=(0, 1)):
        """
        Generate item and person parameters.

        Parameters:
        - a_dist (tuple): Range for item discrimination (a), default uniform(0.5, 2.0).
        - b_dist (tuple): Mean and std for item difficulty (b), default normal(0, 1).
        - theta_dist (tuple): Mean and std for ability (theta), default normal(0, 1).

        Returns:
        - a, b, theta (np.ndarray): Generated parameters for items and respondents.
        """
        self.a = np.random.uniform(a_dist[0], a_dist[1], self.n_items)
        self.b = np.random.normal(b_dist[0], b_dist[1], self.n_items)
        self.theta = np.random.normal(theta_dist[0], theta_dist[1], self.n_respondents)
        return self.a, self.b, self.theta

    def simulate_responses(self):
        """
        Simulate response data based on the specified IRT model.

        Returns:
        - responses (pd.DataFrame): Simulated response matrix.
        """
        if not hasattr(self, 'a') or not hasattr(self, 'b') or not hasattr(self, 'theta'):
            raise ValueError("Parameters not generated. Call generate_parameters() first.")

        # Load the appropriate IRT model
        if self.model == "2PL":
            self.irt_model = TwoPLModel(self.a, self.b, self.theta)
        else:
            raise NotImplementedError(f"Model {self.model} is not implemented.")

        # Simulate responses
        probabilities = self.irt_model.compute_probabilities()
        responses = self.irt_model.simulate_responses(probabilities)

        return responses
