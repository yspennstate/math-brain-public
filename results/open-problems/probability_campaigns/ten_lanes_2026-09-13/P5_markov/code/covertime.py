import os
"""E_pi[C], the stationary-start expected cover time of a finite chain.

h(S,i) = expected further time to cover, currently at i, having visited S.
h(V,i)=0;  for S != V and i in S:
    h(S,i) = 1 + sum_{j in S} P_ij h(S,j) + sum_{j notin S} P_ij h(S+j, j).
Solved by decreasing |S|, one linear system of size |S| per subset.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np

def cover_exact(P):
    """P: n x n list of lists of Fraction. Returns (pi, E_pi C, {i: E_i C})."""
    n = len(P)
    full = (1 << n) - 1
    # stationary distribution, exact
    A = [[P[k][c] - (Fr(1) if k == c else Fr(0)) for c in range(n)] for k in range(n)]
    A[-1] = [Fr(1)] * n
    b = [Fr(0)] * n; b[-1] = Fr(1)
    from antivoter import solve_exact
    pi = solve_exact(A, b)
    h = {}
    for i in range(n):
        h[(full, i)] = Fr(0)
    for size in range(n - 1, 0, -1):
        for comb in itertools.combinations(range(n), size):
            S = 0
            for c in comb: S |= (1 << c)
            idx = {v: t for t, v in enumerate(comb)}
            m = len(comb)
            M = [[Fr(0)] * m for _ in range(m)]
            rhs = [Fr(0)] * m
            for t, i in enumerate(comb):
                M[t][t] += 1
                rhs[t] += 1
                for j in range(n):
                    if P[i][j] == 0: continue
                    if (S >> j) & 1:
                        M[t][idx[j]] -= P[i][j]
                    else:
                        rhs[t] += P[i][j] * h[(S | (1 << j), j)]
            sol = solve_exact(M, rhs)
            for t, i in enumerate(comb):
                h[(S, i)] = sol[t]
    Ei = {i: h[(1 << i, i)] for i in range(n)}
    EpiC = sum(pi[i] * Ei[i] for i in range(n))
    return pi, EpiC, Ei

def cover_float(W):
    """W symmetric nonnegative weight matrix (numpy). Fast float version."""
    n = W.shape[0]
    w = W.sum(1)
    P = W / w[:, None]
    full = (1 << n) - 1
    ev, evec = np.linalg.eig(P.T)
    k = int(np.argmin(np.abs(ev - 1.0)))
    pi = np.real(evec[:, k]); pi = pi / pi.sum()
    h = np.zeros((1 << n, n))
    for size in range(n - 1, 0, -1):
        for comb in itertools.combinations(range(n), size):
            S = 0
            for c in comb: S |= (1 << c)
            idx = list(comb); m = len(idx)
            M = np.eye(m) - P[np.ix_(idx, idx)]
            rhs = np.ones(m)
            for t, i in enumerate(idx):
                for j in range(n):
                    if not ((S >> j) & 1):
                        rhs[t] += P[i, j] * h[S | (1 << j), j]
            sol = np.linalg.solve(M, rhs)
            for t, i in enumerate(idx):
                h[S, i] = sol[t]
    return float(sum(pi[i] * h[1 << i, i] for i in range(n)))

def target(n):
    return Fr(n - 1) * sum(Fr(1, k) for k in range(1, n))

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for n in range(2, 7):
        W = np.ones((n, n)) - np.eye(n)
        P = [[Fr(0) if i == j else Fr(1, n - 1) for j in range(n)] for i in range(n)]
        pi, E, Ei = cover_exact(P)
        print(f"n={n} nonlazy K_n: E_pi C = {E} = {float(E):.8f}   target (n-1)H_(n-1) = "
              f"{target(n)} = {float(target(n)):.8f}   float={cover_float(W):.8f}")
