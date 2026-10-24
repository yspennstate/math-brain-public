#!/usr/bin/env python3
"""Exact lower bound refuting a naive globalization of the local 3-block coupling.

For the one-point defect f_n, the sensitivity-set law is supported on
  empty, [n], and the n singletons.
The spectral law assigns the same mass c=2^(2-2n) to every nonempty subset.
Any Hamming transport from the spectral law to the sensitivity law therefore
costs at least E_mu dist(S, support(nu)).  This script evaluates that lower
bound exactly and compares it to (2/3) I(f_n).
"""
from fractions import Fraction
from math import comb


def lower_bound(n: int):
    c = Fraction(1, 2 ** (2 * n - 2))
    distance_sum = sum(
        comb(n, k) * min(k - 1, n - k)
        for k in range(1, n + 1)
    )
    lb = c * distance_sum
    influence = Fraction(n, 2 ** (n - 1))
    return lb, influence


def main():
    for n in [8, 10, 11, 12, 16, 24, 32]:
        lb, influence = lower_bound(n)
        ratio = lb / influence
        print(
            f"n={n} lower_bound={lb} influence={influence} "
            f"ratio={ratio} ratio_float={float(ratio):.12f} "
            f"exceeds_two_thirds={ratio > Fraction(2,3)}"
        )


if __name__ == "__main__":
    main()
