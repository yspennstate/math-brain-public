"""PROB20-17 corroborative checker for the 2026-09-15 2x2 cubic lemma.

Mathematical claims checked numerically here:
  * for random 2x2 PSD A,B,
      ||ABAB|| >= ||AB||^3/(||A|| ||B||);
  * occupancy-layer lower bounds used in the report;
  * final n=4,d=2 factor.

The random checks are diagnostic only.  The proof is in the Markdown report.
"""

import itertools
import math
from collections import Counter

import numpy as np


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd2(rng):
    Q, _ = np.linalg.qr(rng.normal(size=(2, 2)))
    vals = np.exp(rng.normal(0.0, 1.5, size=2))
    return Q @ np.diag(vals) @ Q.T


# Exact scalar constant from the report.
e_star = (27 / 2) ** (2 / 3)
r_over_s = 4 + e_star / 2
normalized = 3 * r_over_s / 32

print("e_* =", e_star)
print("R/S lower constant =", r_over_s)
print("normalized lower factor =", normalized)

assert abs(e_star - 5.669644724526929) < 1e-13
assert abs(r_over_s - 6.8348223622634645) < 1e-13
assert abs(normalized - 0.6407645964621997) < 1e-13

rng = np.random.default_rng(20260915)
min_cubic_ratio = float("inf")
min_full_formula_ratio = float("inf")
min_final_ratio = float("inf")

for trial in range(500):
    A = [rand_psd2(rng) for _ in range(4)]

    # Pairwise cubic alternating lemma.
    for i, j in itertools.combinations(range(4), 2):
        ai = opnorm(A[i])
        aj = opnorm(A[j])
        p = opnorm(A[i] @ A[j])
        if p > 1e-13:
            lhs1 = opnorm(A[i] @ A[j] @ A[i] @ A[j])
            lhs2 = opnorm(A[j] @ A[i] @ A[j] @ A[i])
            rhs = p**3 / (ai * aj)
            min_cubic_ratio = min(min_cubic_ratio, lhs1 / rhs, lhs2 / rhs)
            assert lhs1 + 1e-8 * max(1.0, lhs1) >= rhs
            assert lhs2 + 1e-8 * max(1.0, lhs2) >= rhs

    S = R = Q211 = Q22 = Q31 = Q4 = 0.0
    for w in itertools.product(range(4), repeat=4):
        val = opnorm(A[w[0]] @ A[w[1]] @ A[w[2]] @ A[w[3]])
        R += val
        shape = sorted(Counter(w).values(), reverse=True)
        if shape == [1, 1, 1, 1]:
            S += val
        elif shape == [2, 1, 1]:
            Q211 += val
        elif shape == [2, 2]:
            Q22 += val
        elif shape == [3, 1]:
            Q31 += val
        elif shape == [4]:
            Q4 += val
        else:
            raise RuntimeError(shape)

    a = np.array([opnorm(X) for X in A])
    P = sum(opnorm(A[i] @ A[j]) ** 2 for i, j in itertools.combinations(range(4), 2))
    E = sum((a[i] * a[j]) ** 2 for i, j in itertools.combinations(range(4), 2))
    Q = float(np.sum(a**4))

    # Basic scalar constraints.
    assert S <= 4 * P + 1e-7 * max(1.0, S)
    assert P <= E + 1e-7 * max(1.0, E)
    assert E <= 1.5 * Q + 1e-7 * max(1.0, E)

    if S <= 1e-12:
        continue

    # Cumulative lower formula in the report:
    # R >= 3S + S^2/(2 sqrt(PE)) + 4P + 10 P^(3/2)/sqrt(E) + Q.
    lower = (
        3 * S
        + S * S / (2 * math.sqrt(P * E))
        + 4 * P
        + 10 * P**1.5 / math.sqrt(E)
        + Q
    )
    min_full_formula_ratio = min(min_full_formula_ratio, R / lower)
    assert R + 1e-7 * max(1.0, R) >= lower

    min_final_ratio = min(min_final_ratio, R / (r_over_s * S))
    assert R + 1e-7 * max(1.0, R) >= r_over_s * S

print("minimum observed cubic-lemma ratio =", min_cubic_ratio)
print("minimum observed R / cumulative-lower-formula =", min_full_formula_ratio)
print("minimum observed R / (claimed constant * S) =", min_final_ratio)
print("All 500 random 2x2 PSD diagnostic trials passed.")
