import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    g = np.array(g)
    st = beta*np.array(s) + (1-beta)*g*g
    wt = np.array(w) - lr*g/(np.sqrt(st+eps))
    return (wt,st)