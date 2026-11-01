#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 2026-09-16T073428Z.

Checks only.  The proofs are in the accompanying Markdown report.
"""

import itertools
import math
import numpy as np

SEED = 20260916073428
rng = np.random.default_rng(SEED)


def abs_gram(n, d):
    z = rng.normal(size=(n, d)) + 1j * rng.normal(size=(n, d))
    z /= np.linalg.norm(z, axis=1, keepdims=True)
    return np.abs(z @ z.conj().T)


def hamilton_mean(g):
    n = g.shape[0]
    total = 0.0
    for sigma in itertools.permutations(range(n)):
        term = 1.0
        for r in range(n - 1):
            term *= g[sigma[r], sigma[r + 1]]
        total += term
    return total / math.factorial(n)


def transfer_numerator(g, a):
    q = np.sqrt(a)
    m = (q[:, None] * g) * q[None, :]
    return float(q @ np.linalg.matrix_power(m, len(a) - 1) @ q)


def blakley_roy_lower(g, a):
    n = len(a)
    s = float(np.sum(a))
    return s ** (2 - n) * float(a @ g @ a) ** (n - 1)


def hamilton_upper(g):
    n = g.shape[0]
    w = float(np.triu(g, 1).sum())
    return (w / (n - 1)) ** (n - 1) / math.factorial(n - 1)


def c_n(n):
    return (n / 2.0) ** (n - 1) / math.factorial(n - 1)


def tau_n(n):
    return 1.0 / (n * c_n(n) ** (1.0 / (n - 1)) - (n - 1))


min_br_ratio = float("inf")
min_ham_ratio = float("inf")
min_direct_ratio = float("inf")
num_cases = 0

for n in (4, 5, 6):
    trials = 80 if n < 6 else 30
    for _ in range(trials):
        g = abs_gram(n, max(2, n - 1))
        a = np.exp(rng.normal(0.0, 1.0, size=n))

        transfer = transfer_numerator(g, a)
        br = blakley_roy_lower(g, a)
        assert transfer + 1e-10 >= br
        min_br_ratio = min(min_br_ratio, transfer / br)

        h = hamilton_mean(g)
        hu = hamilton_upper(g)
        assert hu + 1e-12 >= h
        if h > 0:
            min_ham_ratio = min(min_ham_ratio, hu / h)

        left = float(np.prod(a)) * h
        right = transfer / (n ** n)
        if left > 1e-15:
            min_direct_ratio = min(min_direct_ratio, right / left)
        num_cases += 1

# Equal-scale n=5 two-cluster rank-one example.
n = 5
c = 1.0 / 3.0
g5 = np.ones((n, n))
for i in range(2):
    for j in range(2, 5):
        g5[i, j] = g5[j, i] = c

w5 = float(np.triu(g5, 1).sum())
bar5 = 2.0 * w5 / (n * (n - 1))
tau5 = tau_n(5)
h5 = hamilton_mean(g5)
hu5 = hamilton_upper(g5)
mu5 = float(np.mean(g5))
walk5 = float(np.ones(5) @ np.linalg.matrix_power(g5, 4) @ np.ones(5)) / 5**5
old_band_rhs = (1.0 + 4.0 * c) / 5.0
assert abs(bar5 - 0.6) < 1e-14
assert bar5 < tau5
assert hu5 <= mu5**4 + 1e-14
assert h5 <= hu5 + 1e-14
assert walk5 >= mu5**4 - 1e-14
assert 1.0 > old_band_rhs  # g_+=1, so the old overlap-band test fails.

# Previous four-angle absolute Gram example: G is not PSD, hence the new direct
# Blakley-Roy lower bound strictly dominates every PSD-minorant objective.
angles = np.deg2rad([0.0, 60.0, 75.0, 105.0])
u = np.array([[np.cos(t), np.sin(t)] for t in angles])
g4 = np.abs(u @ u.T)
eigs4 = np.linalg.eigvalsh(g4)
assert eigs4[0] < -1e-3
mu4 = float(np.mean(g4))
h4 = hamilton_mean(g4)
assert h4 <= mu4**3 + 1e-12

print(f"seed={SEED}")
print(f"random_cases={num_cases}")
print(f"min_transfer_over_BlakleyRoy={min_br_ratio:.16g}")
print(f"min_HamiltonUpper_over_H={min_ham_ratio:.16g}")
print(f"min_actual_R_over_L_random={min_direct_ratio:.16g}")
print("tau_4_to_10=" + repr({k: tau_n(k) for k in range(4, 11)}))
print(
    "n5_cluster="
    + repr(
        {
            "cross_c": c,
            "bar_g": bar5,
            "tau_5": tau5,
            "H_5": h5,
            "Hamilton_upper": hu5,
            "mu": mu5,
            "mu^4": mu5**4,
            "actual_R_equal_scale": walk5,
            "old_band_rhs_for_gplus": old_band_rhs,
        }
    )
)
print(
    "four_angle="
    + repr(
        {
            "lambda_min_abs_Gram": float(eigs4[0]),
            "mu": mu4,
            "H_4": h4,
            "mu^3": mu4**3,
        }
    )
)
