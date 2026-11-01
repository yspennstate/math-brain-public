#!/usr/bin/env python3
"""Finite bookkeeping checks for the PROB20-20 feasible-tail/band report.

This is NOT evidence for Janson Problem 18.39.  It checks, on finite rational toy
laws, the exact feasible-tail Palm identity and the binary coarse-graining
inequalities used in the 2026-09-16T05-32-13Z report.
"""

from collections import defaultdict
from fractions import Fraction
from math import log

WEIGHTS = [30, 20, 14, 10, 8, 6, 5, 4, 3, 2, 1]
Z = sum(WEIGHTS)
PI = [Fraction(w, Z) for w in WEIGHTS]
NU = sum(Fraction(k) * PI[k] for k in range(len(PI)))
QBAR = [Fraction(0)] * len(PI)
for k in range(1, len(PI)):
    QBAR[k] = Fraction(k) * PI[k] / NU


def convolution_pmf(n):
    d = {0: Fraction(1)}
    for _ in range(n):
        nd = defaultdict(Fraction)
        for s, p in d.items():
            for k, pk in enumerate(PI):
                nd[s + k] += p * pk
        d = dict(nd)
    return d


PMF = {n: convolution_pmf(n) for n in range(1, 8)}
CASES = [(4, 13, 2, 7), (5, 18, 3, 8), (6, 21, 4, 9), (7, 27, 5, 9)]

max_identity_error = 0.0
min_binary_slack = float("inf")
min_step_slack = float("inf")

print(f"mean_nu={float(NU):.15g} exact={NU}")

for N, M, K, U in CASES:
    p_nm = PMF[N].get(M, Fraction(0))
    assert p_nm > 0

    kernel = {}
    for k in range(1, min(len(PI) - 1, M) + 1):
        p_res = PMF[N - 1].get(M - k, Fraction(0))
        if p_res:
            kernel[k] = Fraction(N) * k * PI[k] * p_res / (Fraction(M) * p_nm)

    kernel_norm = sum(kernel.values())
    alpha = sum(v for k, v in kernel.items() if k > K)
    cloud = {k: v / alpha for k, v in kernel.items() if k > K}

    q_km = sum(QBAR[k] for k in range(K + 1, min(M, len(PI) - 1) + 1))
    reference = {k: QBAR[k] / q_km for k in cloud}

    kl = sum(float(p) * log(float(p / reference[k])) for k, p in cloud.items())
    b_n = -log(float(p_nm))
    e_b_res = 0.0
    for k, p in cloud.items():
        p_res = PMF[N - 1][M - k]
        e_b_res += float(p) * (-log(float(p_res)))

    lhs = b_n - e_b_res
    rhs = kl + log(float(Fraction(M, N) / NU)) + log(float(alpha / q_km))
    identity_error = abs(lhs - rhs)
    max_identity_error = max(max_identity_error, identity_error)

    p_a = sum(p for k, p in cloud.items() if k <= U)
    q_band = sum(QBAR[k] for k in range(K + 1, min(U, len(PI) - 1) + 1))
    pp = float(p_a)
    entropy = 0.0
    if 0.0 < pp < 1.0:
        entropy = -pp * log(pp) - (1.0 - pp) * log(1.0 - pp)

    coarse_lower = pp * log(float(q_km / q_band)) - entropy
    binary_slack = kl - coarse_lower
    min_binary_slack = min(min_binary_slack, binary_slack)

    density = log(float(Fraction(M, N) / NU))
    decrement = kl + density + log(float(alpha / q_km))
    band_log_cost = log(1.0 / float(q_band))
    one_step_lower = pp * band_log_cost + log(float(alpha)) + density - entropy
    step_slack = decrement - one_step_lower
    min_step_slack = min(min_step_slack, step_slack)

    print(
        f"case N={N} M={M} K={K} U={U} "
        f"kernel_norm_err={abs(float(kernel_norm)-1):.3e} "
        f"identity_err={identity_error:.3e} "
        f"binary_slack={binary_slack:.6g} "
        f"step_slack={step_slack:.6g} "
        f"alpha={float(alpha):.6g} QKM={float(q_km):.6g} "
        f"Qband={float(q_band):.6g} pA={pp:.6g}"
    )

print(f"checks={len(CASES)}")
print(f"max_identity_error={max_identity_error:.3e}")
print(f"min_binary_slack={min_binary_slack:.12g}")
print(f"min_step_slack={min_step_slack:.12g}")

ok = (
    max_identity_error < 1e-12
    and min_binary_slack > -1e-12
    and min_step_slack > -1e-12
)
print("PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
