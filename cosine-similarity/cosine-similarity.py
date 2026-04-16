import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    norms = np.linalg.norm(a) * np.linalg.norm(b)

    if norms < 1e-12:
        return 0
    else:
        return np.dot(a, b) / norms