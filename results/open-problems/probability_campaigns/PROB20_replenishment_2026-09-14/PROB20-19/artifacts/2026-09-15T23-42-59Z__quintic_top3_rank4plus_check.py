"""Reproducible checks for PROB20-19 quintic top-three facet, ranks >= 4.

This script checks algebraic identities used in the report and randomized
projection instances. It is supporting self-review, not independent proof.
"""

import math
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# 1. Symbolic two-eigenvalue fifth moment
# ---------------------------------------------------------------------------
l1, l2 = sp.symbols("l1 l2")

def gaussian_even_moment_power(m: int):
    if m == 0:
        return sp.Integer(1)
    return sp.factorial2(2 * m - 1)

H = sum(
    sp.binomial(5, a)
    * l1**a
    * l2 ** (5 - a)
    * gaussian_even_moment_power(a)
    * gaussian_even_moment_power(5 - a)
    for a in range(6)
)

t = l1 + l2
delta = l1 * l2
H_target = 945 * t**5 - 4200 * delta * t**3 + 3600 * delta**2 * t
assert sp.expand(H - H_target) == 0


# ---------------------------------------------------------------------------
# 2. Symbolic diagonal-gap reduction
# ---------------------------------------------------------------------------
r, D2, D3, D4, D5 = sp.symbols("r D2 D3 D4 D5")
S2 = r - D2
S3 = r - D3
S4 = r - D4
S5 = r - D5

upper = (
    450 * S2 * S3
    + 3600 * S2
    - 1800 * S3
    + (525 * r + 2400) * S4
    - 4230 * S5
)
coord = 975 * r**2 - 30 * r
G = sp.expand((coord - upper) / 15)
G_target = (
    30 * D2 * (r - D3)
    + 240 * D2
    + (30 * r - 120) * D3
    + (35 * r + 160) * D4
    - 282 * D5
)
assert sp.expand(G - G_target) == 0

# Scalar ratio certificates used in the analytic proof.
x = sp.symbols("x", nonnegative=True)
assert sp.factor(
    4 * (1 + x + x**2) - 3 * (1 + x + x**2 + x**3)
) == (1 - x) * (3 * x**2 + 2 * x + 1)


# ---------------------------------------------------------------------------
# 3. Randomized projection checks
# ---------------------------------------------------------------------------
def random_projection(p: int, rank: int, rng: np.random.Generator):
    X = rng.normal(size=(p, rank))
    Q, _ = np.linalg.qr(X)
    P = Q @ Q.T
    return P


def invariants(P: np.ndarray):
    d = np.diag(P)
    rank = round(float(np.trace(P)))
    p = len(d)
    S = {k: float(np.sum(d**k)) for k in range(2, 6)}

    J = K = L = M = 0.0
    for i in range(p):
        for j in range(i + 1, p):
            q = float(P[i, j] ** 2)
            dij = float(d[i] * d[j] - q)
            s = float(d[i] + d[j])
            J += dij * d[i] * d[j] * s
            K += dij**2 * s
            L += q * d[i] * d[j] * s
            M += q**2 * s

    C_exact = (
        9450 * S[2] * S[3]
        + 525 * (rank + 8) * S[4]
        - 13230 * S[5]
        - 12600 * J
        + 3600 * K
    )

    C_rewritten = (
        450 * S[2] * S[3]
        + 525 * (rank + 8) * S[4]
        - 4230 * S[5]
        + 5400 * L
        + 3600 * M
    )

    C_upper = (
        450 * S[2] * S[3]
        + 3600 * S[2]
        - 1800 * S[3]
        + (525 * rank + 2400) * S[4]
        - 4230 * S[5]
    )

    return rank, d, S, J, K, L, M, C_exact, C_rewritten, C_upper


rng = np.random.default_rng(20260915)
minimum_gaps = {}

for rank in range(4, 11):
    min_gap = float("inf")
    for p in range(rank + 1, rank + 6):
        for _ in range(50):
            P = random_projection(p, rank, rng)
            (
                rank_check,
                d,
                S,
                J,
                K,
                L,
                M,
                C_exact,
                C_rewritten,
                C_upper,
            ) = invariants(P)

            assert rank_check == rank
            assert np.max(np.abs(P @ P - P)) < 1e-10
            assert abs(C_exact - C_rewritten) < 1e-7 * max(1.0, abs(C_exact))

            # Analytic inequalities (5.5) and (5.7).
            assert L <= S[3] - S[4] + 1e-9
            assert M <= S[2] - 2 * S[3] + S[4] + 1e-9

            coord_value = 975 * rank**2 - 30 * rank
            gap = coord_value - C_exact
            min_gap = min(min_gap, gap)

            assert C_exact <= C_upper + 1e-7
            assert gap >= -1e-6

    minimum_gaps[rank] = min_gap

print("symbolic fifth-moment identity: OK")
print("symbolic diagonal-gap identity: OK")
print("randomized ranks 4..10: OK")
print("minimum raw numerator gaps:")
for rank, gap in minimum_gaps.items():
    print(f"  rank {rank}: {gap:.12g}")
