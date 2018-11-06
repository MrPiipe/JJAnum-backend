import numpy as np
from math import sqrt

def initializeParams(A, b, x0=None):
    n = int(sqrt(len(A)))
    new_A = np.zeros((n, n))
    new_b = np.zeros((1, n))

    for i in range(n):
        for j in range(n):
            pos = str(i) + str(j)
            new_A[i, j] = A[pos]
        new_b[0, i] = b[str(i)]

    if x0 is not None:
        new_x0 = np.zeros(n)
        for i in range(n):
            new_x0[i] = x0[str(i)]
        return new_A, new_b, new_x0
    else:
        return new_A, new_b
