def f(x):
    return a * x**2 + b * x + c

def grad(x, a, b):
    return 2*a*x + b

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    
    # Write code here
    x = x0
    for _ in range(steps):
        x = x - lr * grad(x, a, b)
        print(x)
    return x