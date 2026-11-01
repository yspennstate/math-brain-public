#!/usr/bin/env python3
"""R01 independent finite algebra cross-check for P0458.

This is only a finite/exact self-check supporting an independent written audit.
It is not the theorem proof and does not count as a separate auditor.
"""
from fractions import Fraction
from math import factorial, comb


def beta_influence(n, k):
    # C(n-3,k-1) * B(k,n-k-1)
    return Fraction(
        comb(n - 3, k - 1) * factorial(k - 1) * factorial(n - k - 2),
        factorial(n - 2),
    )


for n in range(4, 31):
    for k in range(1, n - 1):
        assert beta_influence(n, k) == Fraction(1, n - 2)


def mu_from_lambda(r):
    # A~Gamma(r,1), Lambda_r(a)=e^-a sum_{l=0}^{r-1}(r-l)a^l/l!.
    s = Fraction(0, 1)
    for l in range(r):
        s += Fraction(
            (r - l) * factorial(r + l - 1),
            factorial(l) * 2 ** (r + l) * factorial(r - 1),
        )
    return s


def mu_closed(r):
    return Fraction(r * comb(2 * r, r), 4**r)


def m2(r):
    s = Fraction(0, 1)
    for l in range(r):
        for m in range(r):
            s += Fraction(
                (r - l) * (r - m) * factorial(r + l + m - 1),
                factorial(r - 1)
                * factorial(l)
                * factorial(m)
                * 3 ** (r + l + m),
            )
    return s


for r in range(1, 13):
    assert mu_from_lambda(r) == mu_closed(r)

assert m2(1) == Fraction(1, 3)
assert m2(2) == Fraction(22, 27)
nu1 = mu_closed(1) + m2(1) - mu_closed(1) ** 2
nu2 = mu_closed(2) + m2(2) - mu_closed(2) ** 2
assert nu1 == Fraction(7, 12)
assert nu2 == Fraction(433, 432)
assert mu_closed(1) ** 2 / nu1 == Fraction(3, 7)
assert mu_closed(2) ** 2 / nu2 == Fraction(243, 433)

print("R01_P0458_INDEPENDENT_EXACT_CROSSCHECK_PASS")
print("beta_integral_grid=ALL_PASS n=4..30")
print("mu_two_routes_r=1..12=ALL_PASS")
print("r1: mu=1/2 M2=1/3 nu=7/12 endpoint_sq=3/7")
print("r2: mu=3/4 M2=22/27 nu=433/432 endpoint_sq=243/433")
