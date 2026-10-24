"""Remark 8.2 with affine terms: for the two-star matrix, Q = Z_1 + Z_2 + c with
Z_k = U_k (2 w.V_k + alpha_k) + beta_k.V_k has density at most 4 sqrt(e) for every b.

Coordinates are uniform on [-1/2, 1/2] (density one), centred so that w.V is near zero and the density of Q
is as large as this family allows. The hardest affine terms for the bound are those with beta_k
parallel to w, where v(u) = 2uw + beta_k vanishes inside the support of U_k; the cases below include them.
Each case samples S points and reports the largest histogram density.
"""
import math

import numpy as np

rng = np.random.default_rng(20260925)
N = 400
S = 1_000_000
w = np.ones(N) / math.sqrt(N)
bound = 4 * math.sqrt(math.e)


def sample(alpha, beta):
    """alpha: shape (2,), beta: shape (2, N). Returns S samples of Z_1 + Z_2."""
    U = rng.uniform(-0.5, 0.5, size=(S, 2))
    Lw = np.zeros((S, 2))
    Lb = np.zeros((S, 2))
    for j in range(N):
        v = rng.uniform(-0.5, 0.5, size=(S, 2))
        Lw += w[j] * v
        Lb += beta[:, j] * v
    Z = U * (2 * Lw + alpha) + Lb
    return Z.sum(axis=1)


def max_density(q, bins=4000):
    hist, edges = np.histogram(q, bins=bins)
    return (hist / (q.size * (edges[1] - edges[0]))).max()


cases = []
cases.append(("b = 0", np.zeros(2), np.zeros((2, N))))
cases.append(("beta = 0.4 w, alpha = 0.3 (v(u) vanishes at u = -0.2)", np.array([0.3, 0.3]), np.vstack([0.4 * w, 0.4 * w])))
cases.append(("beta = -0.6 w, alpha = -1 (vanishes at u = 0.3)", np.array([-1.0, -1.0]), np.vstack([-0.6 * w, -0.6 * w])))
g = rng.standard_normal((2, N))
g -= np.outer(g @ w, w)
g /= np.linalg.norm(g, axis=1, keepdims=True)
cases.append(("beta = 0.4 w + 0.05 (unit vector orthogonal to w)", np.array([0.0, 0.5]), np.vstack([0.4 * w, 0.4 * w]) + 0.05 * g))
cases.append(("beta random Gaussian, |beta| = 1", rng.standard_normal(2), rng.standard_normal((2, N)) / math.sqrt(N)))

ok = True
for name, alpha, beta in cases:
    d = max_density(sample(alpha, beta))
    passed = d < bound
    ok &= passed
    print(f"  {name:55s} max empirical density {d:.4f} < 4 sqrt(e) = {bound:.4f}: {passed}", flush=True)
print("ALL PASS" if ok else "FAIL")
