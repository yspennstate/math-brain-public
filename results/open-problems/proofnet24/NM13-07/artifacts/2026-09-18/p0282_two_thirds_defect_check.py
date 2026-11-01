#!/usr/bin/env python3
"""Exact finite self-check for the P0282 two-thirds defect theorem.

Validation only: the all-j theorem is proved analytically in the immutable run
report.  This script uses only Python's standard library and exact integer /
Fraction arithmetic.  It reconstructs the relevant LIS counts from residual
Young diagrams at the minimal integer thresholds for j=1,...,20.
"""

from fractions import Fraction
from math import comb, factorial, isqrt


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
    """Return E_j(n)=ell_{n,n-j} and exact Plancherel correction A_j(n)."""
    if j == 0:
        return 1, Fraction(1)
    total = Fraction(0)
    weighted_corr = Fraction(0)
    for mu in partitions(j):
        fmu = tableaux_dim(mu)
        muprime = [
            sum(1 for row in mu if row >= c)
            for c in range(1, mu[0] + 1)
        ]
        corr = Fraction(1)
        for c, h in enumerate(muprime, 1):
            corr *= Fraction(
                n - j - c + 1,
                n - j - c + 1 + h,
            )
        f = comb(n, j) * fmu * corr
        assert f.denominator == 1
        total += f * f
        weighted_corr += Fraction(fmu * fmu, factorial(j)) * corr * corr

    falling_factorial_factor = Fraction(1, factorial(j))
    for t in range(j):
        falling_factorial_factor *= (n - t) * (n - t)
    assert total == falling_factorial_factor * weighted_corr
    assert total.denominator == 1
    return int(total), weighted_corr


def error_bound(n, j):
    """e_j(n) from the analytic proof; exact rational value."""
    if j == 0:
        return Fraction(0)
    assert n >= 2 * j
    first = Fraction(
        j * (j - 1),
        (n - j) * (n - 2 * j + 1),
    )
    second = Fraction(
        j * j,
        2 * (n - 2 * j + 1) ** 2,
    )
    return max(first, second)


def threshold(j):
    """Least n with 3 n^2 >= 64 (j+1)^3."""
    target = 64 * (j + 1) ** 3
    # Need n^2 >= ceil(target/3).
    q = (target + 2) // 3
    n = isqrt(q)
    if n * n < q:
        n += 1
    assert 3 * n * n >= target
    if n > 0:
        assert 3 * (n - 1) * (n - 1) < target
    return n


def main():
    print("P0282 two-thirds defect theorem exact finite self-check")
    for j in range(1, 21):
        n = threshold(j)
        assert n >= 4 * (j + 1)

        # Exact rational inequalities used in the clean corollary.
        for r in (j - 1, j, j + 1):
            if r == 0:
                continue
            assert error_bound(n, r) <= Fraction(8 * r * r, 3 * n * n)

        aggregate_error = (
            4 * error_bound(n, j)
            + 2 * error_bound(n, j - 1)
            + 2 * error_bound(n, j + 1)
        )
        coarse_error = Fraction(64 * j * j + 32, 3 * n * n)
        assert aggregate_error <= coarse_error
        assert coarse_error < Fraction(1, j + 1)

        # Independently reconstruct the three exact LIS counts.
        em, am = residual_data(n, j - 1)
        e0, a0 = residual_data(n, j)
        ep, ap = residual_data(n, j + 1)

        margin = e0 * e0 - em * ep
        assert margin > 0

        # Check the exact adjacent-ratio factorization from the previous run.
        pref = (
            Fraction(j + 1, j)
            * Fraction((n - j + 1) ** 2, (n - j) ** 2)
        )
        assert Fraction(e0 * e0, em * ep) == pref * Fraction(a0 * a0, am * ap)

        print(
            f"j={j} n0={n} "
            f"3n2_minus_64jp1cubed={3*n*n-64*(j+1)**3} "
            f"margin_digits={len(str(margin))} "
            f"aggregate_lt_1_over_jp1={aggregate_error < Fraction(1,j+1)}"
        )

    # The final polynomial comparison used after substituting
    # 3 n^2 >= 64 (j+1)^3 is:
    #   64 j^2 + 32 < 64 (j+1)^2.
    # Check a broad finite range as a guard against a transcription error.
    for j in range(1, 100001):
        assert 64 * j * j + 32 < 64 * (j + 1) * (j + 1)

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
