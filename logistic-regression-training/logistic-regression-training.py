import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
    
def train_logistic_regression(X, y, lr=0.1, steps=1000):
    n, d = X.shape
    w = np.zeros(d)
    b = 0

    for _ in range(steps):

        p = _sigmoid(X @ w + b)
        error = p - y
        w -= lr * (X.T @ error)
        b -= lr * np.mean(error)

    return (w, b)