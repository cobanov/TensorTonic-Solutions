import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    norms =(np.linalg.norm(a) * np.linalg.norm(b))
    if norms != 0:
        cos_angle = np.dot(a, b) / norms
        return cos_angle
    else:
        return 0