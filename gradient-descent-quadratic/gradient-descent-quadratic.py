def derivativeQuadratic(a, b, c, x):
    y1 = 2*a*x + b
    return y1

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = x0
    for i in range(steps):
        x = x - lr*derivativeQuadratic(a, b, c, x)
    return x