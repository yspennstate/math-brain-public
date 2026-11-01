"""
PROB20-17 diagnostic checker for the 2026-09-15T144811Z report.

Exact mathematics is in the Markdown report.  This script is corroborative only.
It checks:
  1. s_j(AB)^2 <= ||A||||B|| lambda_j(AB) on random PSD pairs;
  2. the cubic power inequality on random 2x2 Li-Tsai quadratic blocks;
  3. the n=4 inequality numerically on arbitrary-dimensional tensor families
     whose pair products are quadratic.

Random tests are not a proof and must not be cited as independent verification.
"""

import itertools
import math
import numpy as np


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd(d, rng, positive_definite=True):
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
    if positive_definite:
        vals = np.exp(rng.uniform(-4.0, 0.0, size=d))
    else:
        vals = rng.random(d)
    vals /= max(vals.max(), 1e-15)
    return Q @ np.diag(vals) @ Q.T


def singular_eigen_slack(A, B):
    """Minimum slack in ||A||||B|| lambda_j(AB) - s_j(AB)^2."""
    a = opnorm(A)
    b = opnorm(B)
    T = A @ B
    s = np.linalg.svd(T, compute_uv=False)
    lam = np.sort(np.real_if_close(np.linalg.eigvals(T)).real)[::-1]
    return np.min(a * b * lam - s * s)


def occupancy_sum(A):
    perms = set(itertools.permutations(range(4)))
    S = 0.0
    R = 0.0
    for w in itertools.product(range(4), repeat=4):
        value = opnorm(A[w[0]] @ A[w[1]] @ A[w[2]] @ A[w[3]])
        R += value
        if w in perms:
            S += value
    return S, R


rng = np.random.default_rng(20260915)

# 1. Spectral/singular inequality.
minimum_slack = float("inf")
for d in [2, 3, 4, 5, 8]:
    for _ in range(300):
        A = rand_psd(d, rng, True)
        B = rand_psd(d, rng, True)
        minimum_slack = min(minimum_slack, singular_eigen_slack(A, B))

assert minimum_slack >= -1e-9
print("minimum random singular/eigen slack:", minimum_slack)

# 2. Quadratic 2x2 blocks from the Li-Tsai admissible region.
minimum_cubic_ratio = float("inf")
for _ in range(10000):
    alpha, beta = np.sort(rng.random(2))
    pmax = abs(math.sqrt(alpha) - math.sqrt(beta)) * math.sqrt(
        (1.0 - alpha) * (1.0 - beta)
    )
    p = rng.random() * pmax
    T = np.array([[alpha, p], [0.0, beta]])
    normT = opnorm(T)
    if normT > 1e-14:
        ratio = opnorm(T @ T) / (normT**3)
        minimum_cubic_ratio = min(minimum_cubic_ratio, ratio)

assert minimum_cubic_ratio >= 1.0 - 1e-10
print("minimum random quadratic-block cubic ratio:", minimum_cubic_ratio)

# 3. Arbitrary-dimensional pairwise-quadratic n=4 families.
# A_i = M_i tensor I_2 with M_i 2x2 PSD.  Then each pair product has at most
# two distinct eigenvalues (each repeated twice), so the report's theorem applies.
minimum_normalized_factor = float("inf")
for _ in range(100):
    base = [rand_psd(2, rng, True) * rng.uniform(0.1, 2.0) for _ in range(4)]
    mats = [np.kron(M, np.eye(2)) for M in base]
    S, R = occupancy_sum(mats)
    if S > 1e-14:
        factor = (R / 256.0) / (S / 24.0)
        minimum_normalized_factor = min(minimum_normalized_factor, factor)

proved_factor = (3.0 / 32.0) * (4.0 + 0.5 * (27.0 / 2.0) ** (2.0 / 3.0))
assert minimum_normalized_factor >= proved_factor - 1e-10
print("minimum observed pairwise-quadratic n=4 factor:", minimum_normalized_factor)
print("proved pairwise-quadratic factor:", proved_factor)
print("All diagnostics passed; none of these random tests is a proof.")
