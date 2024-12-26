import numpy as np

def validate_parameters(a, b, theta):
    """
    Validate that the parameters have the correct dimensions.
    """
    if len(a.shape) != 1 or len(b.shape) != 1:
        raise ValueError("Item parameters a and b must be 1-dimensional arrays.")
    if len(theta.shape) != 1:
        raise ValueError("Theta must be a 1-dimensional array.")
    if a.shape[0] != b.shape[0]:
        raise ValueError("The number of discrimination and difficulty parameters must match.")
