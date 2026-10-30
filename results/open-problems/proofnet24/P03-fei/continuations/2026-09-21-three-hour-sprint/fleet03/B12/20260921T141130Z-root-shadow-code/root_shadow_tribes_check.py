#!/usr/bin/env python3
"""Reproduce B12 route-1/3 stress tests with standard-library arithmetic.

1. One-point defect: exact entropy/influence ratio of the *sensitivity-set*
   random variable; this diverges, refuting the raw sensitivity-set entropy
   reduction.
2. Balanced tribes: Fourier level law from the exact disjoint-block product
   formula; compute the global-influence ordered-code quantity
      U = H(K) + I H(q) - E log2(K!)
   and show U/I grows with width.
No exhaustive Boolean-function sweep is performed.
"""
from math import comb, log, log2, lgamma


def one_point_sensitivity_ratio(n: int) -> float:
    N = 1 << n
    p0 = 1.0 - (n + 1) / N
    H = 0.0
    if p0 > 0:
        H -= p0 * log2(p0)
    H += (n + 1) * (1 / N) * n
    I = 2 * n / N
    return H / I


def conv(a, b):
    out = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0.0:
            continue
        for j, y in enumerate(b):
            if y:
                out[i + j] += x * y
    return out


def tribes_stats(w: int, rmax: int = 40):
    eps = 2.0 ** (-w)
    a = 1.0 - eps
    m = max(1, round(log(0.5) / log(a)))
    am = a ** m

    # Conditional size law inside an active tribe:
    # uniform over its 2^w-1 nonempty subsets.
    L = [0.0] + [comb(w, j) / (2**w - 1) for j in range(1, w + 1)]

    # Q is the normalized squared-spectrum product law of G=prod_j(1-AND_j).
    # Number of active blocks R~Bin(m,eps).  Truncate only after rmax; for
    # the displayed widths the omitted tail is below roundoff.
    Q = [0.0] * (rmax * w + 1)
    dist = [1.0]
    pr = a**m
    Q[0] += pr
    total_r = pr
    for r in range(1, min(m, rmax) + 1):
        dist = conv(dist, L)
        pr *= (m - r + 1) / r * (eps / a)
        total_r += pr
        for k, x in enumerate(dist):
            Q[k] += pr * x

    # For f=2G-1, nonempty spectral weights are 4*a^m times Q.
    p0 = (2 * am - 1) ** 2
    W = [4 * am * x for x in Q]
    W[0] = p0
    I = sum(k * W[k] for k in range(1, len(W)))
    HK = -sum(x * log2(x) for x in W if x > 0)
    Elogfac = sum(W[k] * lgamma(k + 1) / log(2) for k in range(1, len(W)))
    n = m * w
    Hq = log2(n)  # all variable influences are equal by symmetry
    U = HK + I * Hq - Elogfac
    Esb_logK = sum(k * W[k] * log2(k) for k in range(1, len(W))) / I
    sigma = 4 * am * (1 - am)
    root_ratio = sigma * log2(n) / I
    return {
        "w": w,
        "m": m,
        "balance": am,
        "binomial_tail": 1 - total_r,
        "I": I,
        "Hq_minus_Esb_logK": Hq - Esb_logK,
        "U_over_I": U / I,
        "root_first_member_cost_over_I": root_ratio,
    }


if __name__ == "__main__":
    print("ROOT_BOUND_BITS", (2.0 + 1.0 / 2.718281828459045) / log(2))
    print("ONE_POINT_SENSITIVITY_SET")
    for n in (4, 8, 12, 16, 20):
        print(n, f"{one_point_sensitivity_ratio(n):.12f}")
    print("BALANCED_TRIBES")
    print("w m balance I Hq-E*logK U/I root/I tail")
    for w in range(2, 13):
        d = tribes_stats(w)
        print(
            d["w"],
            d["m"],
            f'{d["balance"]:.12f}',
            f'{d["I"]:.12f}',
            f'{d["Hq_minus_Esb_logK"]:.12f}',
            f'{d["U_over_I"]:.12f}',
            f'{d["root_first_member_cost_over_I"]:.12f}',
            f'{d["binomial_tail"]:.3e}',
        )
