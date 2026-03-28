import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    _, freq = np.unique(y, return_counts=True)
    p = freq/len(y)
    logp = np.empty_like(p, dtype=float)
    mask = (p > 0)
    logp[mask] = np.log2(p[mask])
    return -1*(np.sum(p*logp))
