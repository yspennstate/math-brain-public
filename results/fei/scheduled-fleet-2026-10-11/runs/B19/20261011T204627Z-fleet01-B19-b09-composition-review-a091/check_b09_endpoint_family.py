#!/usr/bin/env python3
"""Independent numerical check of the analytic two-bit endpoint family.

The proof in REPORT.md is analytic.  This script only corroborates the exact
closed formulas and the limiting coefficient.  No randomness or search.
"""

import math


def h2(t):
    if t == 0.0 or t == 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)


def quantities(p, q):
    r = 4.0 * q * (1.0 - q)
    masses = (
        (1.0 - 2.0 * p * q) ** 2,
        4.0 * p * (1.0 - p) * q * q,
        4.0 * p * p * q * (1.0 - q),
        4.0 * p * (1.0 - p) * q * (1.0 - q),
    )
    assert abs(sum(masses) - 1.0) < 2e-15
    t = p * r
    M = sum(-x * math.log2(x) for x in masses if x) - h2(t)
    J = h2(t) - p * h2(r)
    # Equivalent conditional formula for M.
    a_x = masses[1]
    M_cond = (1.0 - t) * h2(a_x / (1.0 - t)) + t * h2(p)
    assert abs(M - M_cond) < 2e-14
    return masses, M, J


def main():
    q = 0.25
    print("q=1/4; predicted leading coefficient 4q(1-2q)=1/2")
    for k in (3, 4, 6, 8, 10, 12, 16, 20, 24, 30, 40):
        p = 2.0 ** (-k)
        masses, M, J = quantities(p, q)
        scale = p * math.log2(1.0 / p)
        print({
            "k": k,
            "p": p,
            "M": M,
            "J": J,
            "J_minus_M": J - M,
            "ratio_to_p_log2_1_over_p": (J - M) / scale,
        })
    masses, M, J = quantities(1.0 / 8.0, q)
    print("fixed_certificate_crosscheck", {
        "masses": masses,
        "M": M,
        "J": J,
        "gap": J - M,
    })


if __name__ == "__main__":
    main()
