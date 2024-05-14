import numpy as np
from scipy.linalg import solve

P = np.array([
    [0, 2/3, 1/3],
    [3/8, 1/8, 1/2],
    [1/2, 1/2, 0.0]
])

def lim_distr(P):
    n = P.shape[0]
    A = P.T - np.eye(n)
    A[-1, :] = 1
    b = np.zeros(n)
    b[-1] = 1
    p = solve(A, b)
    return p

p_equilibrio = lim_distr(P)

print("Transition matrix P:\n", P)
print("Stationary distribution p:\n", p_equilibrio)