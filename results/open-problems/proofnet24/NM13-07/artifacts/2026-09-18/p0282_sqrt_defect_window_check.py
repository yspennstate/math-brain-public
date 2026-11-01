#!/usr/bin/env python3
"""Exact finite self-check for the P0282 growing-defect theorem.

This is validation only, not a proof of the all-n theorem.  The proof in the run
report is analytic.  The checker uses exact integers/Fractions and the residual
partition hook formula to verify representative boundary points j=1..12.
"""

from fractions import Fraction
from math import comb, factorial


def partitions(n, maxpart=None):
    if n == 0:
        yield ()
        return
    if maxpart is None or maxpart > n:
        maxpart = n
    for a in range(maxpart, 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def tableaux_dim(lam):
    n = sum(lam)
    if n == 0:
        return 1
    hooks = 1
    for r, row in enumerate(lam):
        for c in range(row):
            below = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            hooks *= (row - c) + below
    return factorial(n) // hooks


def residual_data(n, j):
    if j == 0:
        return 1, Fraction(1)
    total = Fraction(0)
    weighted_corr = Fraction(0)
    for mu in partitions(j):
        fmu = tableaux_dim(mu)
        muprime = [sum(1 for r in mu if r >= c) for c in range(1, mu[0] + 1)]
        corr = Fraction(1)
        for c, h in enumerate(muprime, 1):
            corr *= Fraction(n - j - c + 1, n - j - c + 1 + h)
        f = comb(n, j) * fmu * corr
        assert f.denominator == 1
        total += f * f
        weighted_corr += Fraction(fmu * fmu, factorial(j)) * corr * corr
    assert total.denominator == 1
    B = Fraction(1, factorial(j))
    for t in range(j):
        B *= (n - t) * (n - t)
    assert total == B * weighted_corr
    return int(total), weighted_corr


def main():
    print("P0282 sqrt-defect theorem exact finite self-check")
    for j in range(1, 13):
        n = 4 * j * j + 6 * j - 1
        assert n >= 2 * (j + 1)
        em, am = residual_data(n, j - 1)
        e0, a0 = residual_data(n, j)
        ep, ap = residual_data(n, j + 1)
        assert e0 * e0 > em * ep
        assert Fraction(1, j + 1) >= Fraction(4 * j, n - 2 * j + 1)
        # Exact falling-factorial prefactor identity.
        pref = Fraction(j + 1, j) * Fraction((n - j + 1) ** 2, (n - j) ** 2)
        assert Fraction(e0 * e0, em * ep) == pref * Fraction(a0 * a0, am * ap)
        margin = e0 * e0 - em * ep
        print(
            f"j={j} n0={n} exact_margin_positive={margin > 0} "
            f"margin_digits={len(str(margin))}"
        )
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
