#!/usr/bin/env python3
"""Exact/numerical audit for the A077 compensated sparse-defect tower.

The proof in SPARSE_DEFECT_TOWERS.tex is analytic.  This script checks the
closed formulas with high-precision Decimal arithmetic and prints finite
ledgers.  No floating-point value is used as proof of an all-k claim.
"""

from decimal import Decimal, getcontext

getcontext().prec = 80
LN2 = Decimal(2).ln()
LOG2E = Decimal(1) / LN2


def log2(x: Decimal) -> Decimal:
    return x.ln() / LN2


def h2(x: Decimal) -> Decimal:
    if x == 0 or x == 1:
        return Decimal(0)
    return -x * log2(x) - (1 - x) * log2(1 - x)


def one_scale(k: int):
    two = Decimal(2)
    e = two ** (-k)
    r = 4 * e * e * (1 - e)
    s = 4 * e * (1 - e)
    mx = r * e
    alpha = mx / (1 - r)
    J = h2(r) - e * h2(s)
    M = (1 - r) * h2(alpha) + r * h2(e)
    I_core = 2 * r
    L = log2(two**k - 1)
    D = Decimal(k) * two ** (k - 1) / (two**k - 1)
    M_code = M + r * L
    I_code = 2 * r * D

    delta = two ** (-2 * k)
    W = 4 * delta * (1 - delta)
    H_point = h2(W) + W * log2(two ** (2 * k) - 1)
    I_point = Decimal(k) * two ** (2 - 2 * k)
    assert abs(I_code - I_point) < Decimal("1e-70")

    # Analytic lower/upper bounds used in the proof.
    J_lower = r * (Decimal(k) - LOG2E)
    M_upper = r * e * (4 * Decimal(k) + 2 * LOG2E)
    assert J >= J_lower
    assert M <= M_upper
    return {
        "k": k,
        "eps": e,
        "r": r,
        "J": J,
        "M": M,
        "I_core": I_core,
        "core_ratio": J / (I_core + M),
        "L": L,
        "D": D,
        "M_code": M_code,
        "I_code": I_code,
        "coded_ratio": J / (I_code + M_code),
        "H_point": H_point,
        "I_point": I_point,
        "FEI_ratio": H_point / I_point,
    }


def fmt(x: Decimal) -> str:
    return f"{x:.12E}"


print("k eps core_J/(I+M) coded_J/(I+Mcode) point_H/I")
for k in [3, 4, 5, 8, 12, 20, 32]:
    z = one_scale(k)
    print(k, fmt(z["eps"]), fmt(z["core_ratio"]),
          fmt(z["coded_ratio"]), fmt(z["FEI_ratio"]))

print("tower_K dimension core_ratio actual_H/I actual_I")
for K in [3, 4, 5, 8, 12]:
    J = M = Icore = H = I = Decimal(0)
    dimension = 0
    for k in range(3, K + 1):
        z = one_scale(k)
        N = 2 ** (2 * k)
        dimension += N * 2 * k
        J += Decimal(N) * z["J"]
        M += Decimal(N) * z["M"]
        Icore += Decimal(N) * z["I_core"]
        H += Decimal(N) * z["H_point"]
        I += Decimal(N) * z["I_point"]
    expected_I = Decimal(4) * sum(Decimal(k) for k in range(3, K + 1))
    assert abs(I - expected_I) < Decimal("1e-60")
    print(K, dimension, fmt(J / (Icore + M)), fmt(H / I), fmt(I))

print("PASS: exact identities and analytic one-scale bounds verified")
