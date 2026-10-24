#!/usr/bin/env python3
"""Targeted calculation for Route 19.

This is NOT an exhaustive FEI sweep.  It evaluates the exact one-point Boolean
family and the strongest spanning-tree lower bound on spectral total
correlation.  Decimal logarithms are displays of exact dyadic probabilities.
"""

from math import log2, sqrt

C_SCALE = 6.521845710923046575


def h2(q: float) -> float:
    if q == 0.0 or q == 1.0:
        return 0.0
    return -q * log2(q) - (1.0 - q) * log2(1.0 - q)


def pair_mi(q: float) -> float:
    # Exact joint law for two spectral-membership bits of the one-point family:
    # P11=P10=P01=q/2, P00=1-3q/2, both marginals Bernoulli(q).
    p00 = 1.0 - 1.5 * q
    ans = 0.0
    for p, denom in (
        (p00, (1.0 - q) ** 2),
        (q / 2.0, q * (1.0 - q)),
        (q / 2.0, q * (1.0 - q)),
        (q / 2.0, q * q),
    ):
        ans += p * log2(p / denom)
    return ans


def threshold(C: float) -> float:
    lo, hi = 0.0, 0.5
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if h2(mid) / mid > C:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def row(n: int):
    # f_n=+1 except at one cube point, where it is -1.
    # q=Inf_i=2^(1-n), p_empty=(1-q)^2, every nonempty spectral atom=q^2.
    q = 2.0 ** (1 - n)
    p0 = (1.0 - q) ** 2
    eps = q * q
    count_tail = 2**n - 1
    H = -p0 * log2(p0) - count_tail * eps * log2(eps)
    I = n * q
    TC = n * h2(q) - H
    required = n * (h2(q) - C_SCALE * q)
    mi = pair_mi(q)
    tree = (n - 1) * mi
    atom_cancel = sqrt(p0) + sqrt(eps)
    return n, q, H, I, H / I, TC, required, tree, tree / required, atom_cancel


print(f"C_scale={C_SCALE:.18f}")
print(f"q_star solving h2(q)=C_scale*q: {threshold(C_SCALE):.18g}")
print("n q H I H/I TC required_TC tree_pair_MI tree/required sqrt(p0)+sqrt(ptail)")
for n in (7, 8, 10, 12, 16, 24, 32):
    vals = row(n)
    print(
        f"{vals[0]:2d} {vals[1]:.16g} {vals[2]:.16g} {vals[3]:.16g} "
        f"{vals[4]:.16g} {vals[5]:.16g} {vals[6]:.16g} {vals[7]:.16g} "
        f"{vals[8]:.16g} {vals[9]:.16g}"
    )

# A decisive exact-admissible boundary check at n=10.
n10 = row(10)
assert n10[7] < n10[6]      # tree pairwise information does not pay the target deficit
assert n10[4] < C_SCALE     # nevertheless the actual Boolean function satisfies this C-scale FEI inequality
assert abs(n10[9] - 1.0) < 1e-14  # atom-cancellation inequality is saturated

print("checks: PASS (n=10 pairwise-tree subroute refuted; Boolean FEI not refuted; atom bound saturated)")
print("asymptotic theorem: for every fixed C, tree_pair_MI/required_TC -> 1/2 as n -> infinity")
