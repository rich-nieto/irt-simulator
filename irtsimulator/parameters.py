import numpy as np

def generate_item_parameters(n_items, a_dist=(0.5, 2.0), b_dist=(0, 1), seed=None):
    """
    Generate item parameters for IRT models.

    Parameters:
    - n_items (int): Number of items to generate.
    - a_dist (tuple): Range for item discrimination (a). Default: Uniform(0.5, 2.0).
    - b_dist (tuple): Mean and std for item difficulty (b). Default: Normal(0, 1).
    - seed (int): Random seed for reproducibility. Default: None.

    Returns:
    - a (np.ndarray): Discrimination parameters.
    - b (np.ndarray): Difficulty parameters.
    """
    if seed is not None:
        np.random.seed(seed)

    a = np.random.uniform(a_dist[0], a_dist[1], n_items)
    b = np.random.normal(b_dist[0], b_dist[1], n_items)

    return a, b


def generate_person_parameters(n_respondents, theta_dist=(0, 1), seed=None):
    """
    Generate person ability parameters for IRT models.

    Parameters:
    - n_respondents (int): Number of respondents to generate.
    - theta_dist (tuple): Mean and std for person abilities (theta). Default: Normal(0, 1).
    - seed (int): Random seed for reproducibility. Default: None.

    Returns:
    - theta (np.ndarray): Latent ability parameters.
    """
    if seed is not None:
        np.random.seed(seed)

    theta = np.random.normal(theta_dist[0], theta_dist[1], n_respondents)

    return theta
