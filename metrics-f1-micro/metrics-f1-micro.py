import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    tp = (y_true == y_pred).sum()
    n = len(y_true)
    
    return 2 * tp / (2 * tp + (n - tp) + (n - tp))