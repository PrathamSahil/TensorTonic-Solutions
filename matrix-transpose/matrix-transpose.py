import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    N, M = len(A), len(A[0])
    T = np.empty((M, N))
    for i in range(N):
        for j in range(M):
            T[j][i] = A[i][j]
    return T
