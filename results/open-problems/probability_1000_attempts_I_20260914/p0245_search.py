"""Aldous-Fill Open Problem 6.30: E_pi C >= (n-1) h_{n-1} for every irreducible reversible discrete-time chain on n states?
Exact subset DP for the stationary-start cover time; random search + Nelder-Mead over reversible chains on n = 4, 5 (self-loops allowed).
"""
import numpy as np, sys, itertools
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)

def cover_pi(P, pi):
    n = P.shape[0]; full = (1 << n) - 1
    # h[S][i] = expected remaining time to cover from i having visited S (i in S). Solve in decreasing |S|.
    h = {}
    subsets = sorted(range(1, full + 1), key=lambda S: -bin(S).count('1'))
    for S in subsets:
        idx = [i for i in range(n) if (S >> i) & 1]
        if S == full:
            for i in idx: h[(S, i)] = 0.0
            continue
        # unknowns h(S,i) for i in idx: h(S,i) = 1 + sum_{j in S} P_ij h(S,j) + sum_{j notin S} P_ij h(S|j, j)
        m = len(idx); A = np.eye(m); b = np.ones(m)
        for a, i in enumerate(idx):
            for j in range(n):
                if (S >> j) & 1: A[a, idx.index(j)] -= P[i, j]
                else: b[a] += P[i, j] * h[(S | (1 << j), j)]
        sol = np.linalg.solve(A, b)
        for a, i in enumerate(idx): h[(S, i)] = sol[a]
    return sum(pi[i] * h[(1 << i, i)] for i in range(n))

def chain_from_x(x, n):
    W = np.zeros((n, n)); iu = np.triu_indices(n); W[iu] = np.exp(np.clip(x, -10, 10)); W = W + W.T - np.diag(np.diag(W))
    w = W.sum(1); P = W / w[:, None]; pi = w / w.sum()
    return P, pi

def hn(m): return sum(1.0 / k for k in range(1, m + 1))

for n in [3, 4, 5]:
    target = (n - 1) * hn(n - 1)
    # control: complete graph non-lazy
    P = (np.ones((n, n)) - np.eye(n)) / (n - 1); pi = np.ones(n) / n
    print(f"n={n}: K_n cover from pi = {cover_pi(P, pi):.6f}, target (n-1)h_(n-1) = {target:.6f}")
    best = (np.inf, None)
    for rep in range(int(sys.argv[2]) if len(sys.argv) > 2 else 200):
        x0 = rng.normal(0, 1.5, n * (n + 1) // 2)
        f = lambda x: cover_pi(*chain_from_x(x, n))
        r = minimize(f, x0, method='Nelder-Mead', options={'maxiter': 1500, 'xatol': 1e-7, 'fatol': 1e-10})
        if r.fun < best[0]: best = (r.fun, r.x)
    P, pi = chain_from_x(best[1], n)
    print(f"   best found E_pi C = {best[0]:.6f}  (ratio to target {best[0]/target:.6f})")
    print("   P =", np.array2string(P, precision=4, suppress_small=True).replace('\n', '\n       '))
