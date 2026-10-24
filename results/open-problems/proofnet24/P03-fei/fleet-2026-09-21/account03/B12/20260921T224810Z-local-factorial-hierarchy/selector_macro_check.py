#!/usr/bin/env python3
"""Numerical diagnostic for the selector-of-parities macro remainder.

The theorem in REPORT.md is analytic. This script only evaluates the exact
finite-m formulas in Section 6 using the Python standard library.
"""
import math


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def entropy(ps) -> float:
    return -sum(p * math.log2(p) for p in ps if p > 0.0)


def selector_macro(m: int):
    if m < 2:
        raise ValueError("m must be at least 2")
    a = (2 * m + 1) / (4 * (m + 1))
    z = 1 / (2 * (m + 1))
    ih = entropy((a, a, z)) + 1 / (2 * (m + 1))
    for t in range(1, m):
        r = 2 * m + 2 - t
        ih += r / (2 * (m + 1)) * h2(1 / r)
    q_mac = 0.5 * math.log2(m + 1)
    return ih, q_mac, ih - q_mac


def main():
    print("m\tI_H_M_given_P\tQ_mac\tR_mac\tR_mac_minus_2")
    for m in (10, 20, 50, 100, 200, 500, 1000, 5000, 20000):
        ih, q, r = selector_macro(m)
        print(f"{m}\t{ih:.12f}\t{q:.12f}\t{r:.12f}\t{r-2:.12f}")


if __name__ == "__main__":
    main()
