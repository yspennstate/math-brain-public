# Exact E_pi C for a Markov chain on n states via DP over visited subsets.
# C = min{t>=0 : {X_0..X_t} = S}.  h_V(x) = E[C - t | X_t = x, visited set = V].
import numpy as np, itertools, math
from functools import lru_cache

def stationary(P):
    n = P.shape[0]
    w, v = np.linalg.eig(P.T)
    k = np.argmin(abs(w - 1))
    pi = np.real(v[:, k]); pi = pi / pi.sum()
    return pi

def harmonic(m): return sum(1.0/k for k in range(1, m+1))

def cover_expectations(P):
    """returns dict V(bitmask) -> array of h_V(x) for x in V (index by x); only x in V meaningful"""
    n = P.shape[0]
    full = (1 << n) - 1
    H = {}
    # process subsets by decreasing size
    subsets = sorted(range(1, full + 1), key=lambda m: -bin(m).count("1"))
    for V in subsets:
        idx = [x for x in range(n) if V >> x & 1]
        if V == full:
            H[V] = np.zeros(n); continue
        k = len(idx)
        A = np.eye(k); b = np.ones(k)
        for a, x in enumerate(idx):
            for y in range(n):
                p = P[x, y]
                if p == 0: continue
                if V >> y & 1:
                    A[a, idx.index(y)] -= p
                else:
                    b[a] += p * H[V | (1 << y)][y]
        sol = np.linalg.solve(A, b)
        h = np.zeros(n)
        for a, x in enumerate(idx): h[x] = sol[a]
        H[V] = h
    return H

def E_pi_cover(P, pi=None):
    n = P.shape[0]
    if pi is None: pi = stationary(P)
    H = cover_expectations(P)
    return sum(pi[x] * H[1 << x][x] for x in range(n))

def E_x_cover(P):
    n = P.shape[0]
    H = cover_expectations(P)
    return np.array([H[1 << x][x] for x in range(n)])

def target(n): return (n - 1) * harmonic(n - 1)

def rw_on_graph(W):
    """random walk on weighted graph W (symmetric, nonneg)"""
    d = W.sum(1)
    return W / d[:, None]

if __name__ == "__main__":
    for n in range(2, 9):
        W = np.ones((n, n)) - np.eye(n)
        P = rw_on_graph(W)
        print(n, E_pi_cover(P), target(n))
