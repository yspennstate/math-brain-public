#!/usr/bin/env python3
"""Exact arithmetic checker for the auxiliary one-defect Gamma model in P03/P0456 Claim 298.

For integer k>=1 let Y~Gamma(k,1), W~Gamma(k+1,1) independently and

    A_k = E[(k/W) (Y-k-W)_+].

Writing A_k=e^{-k} B_k, the proof gives an exact rational finite-sum formula for B_k.
This script evaluates B_k in two algebraically independent exact Fraction forms:
(1) the displayed double sum after integrating each monomial directly;
(2) explicit construction of the polynomial
      P_k(w)=-w sum_{j=0}^{k-1}(k+w)^j/j! +(k+w)^k/(k-1)!
    followed by exact integration of w^{k-1}P_k(w)e^{-2w}.
It asserts equality for k=1,...,30, then prints selected convergence diagnostics.
The floating-point diagnostics are not part of the exact certificate.
"""

from fractions import Fraction
from math import comb, factorial, exp, sqrt, log, pi


def B_double_sum(k: int) -> Fraction:
    pos = Fraction(0, 1)
    for ell in range(k + 1):
        pos += Fraction(
            comb(k, ell) * k ** (k - ell) * factorial(k + ell - 1),
            factorial(k - 1) * 2 ** (k + ell),
        )
    neg = Fraction(0, 1)
    for j in range(k):
        for ell in range(j + 1):
            neg += Fraction(
                comb(j, ell) * k ** (j - ell) * factorial(k + ell),
                factorial(j) * 2 ** (k + ell + 1),
            )
    return Fraction(k, factorial(k)) * (pos - neg)


def poly_add(p, q):
    n = max(len(p), len(q))
    r = [Fraction(0, 1) for _ in range(n)]
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def poly_mul_x(p):
    return [Fraction(0, 1)] + p


def poly_kplusw_pow(k: int, j: int):
    return [Fraction(comb(j, ell) * k ** (j - ell), 1) for ell in range(j + 1)]


def B_polynomial(k: int) -> Fraction:
    P = [Fraction(0, 1)]
    for j in range(k):
        term = [x / factorial(j) for x in poly_kplusw_pow(k, j)]
        term = [-x for x in poly_mul_x(term)]
        P = poly_add(P, term)
    term = [x / factorial(k - 1) for x in poly_kplusw_pow(k, k)]
    P = poly_add(P, term)

    integ = Fraction(0, 1)
    for d, coeff in enumerate(P):
        integ += coeff * Fraction(factorial(k - 1 + d), 2 ** (k + d))
    return Fraction(k, factorial(k)) * integ


def main() -> None:
    for k in range(1, 31):
        b1 = B_double_sum(k)
        b2 = B_polynomial(k)
        assert b1 == b2, (k, b1, b2)

    eta = sqrt(2.0) - 1.0 - log((1.0 + sqrt(2.0)) / 2.0)
    C = (sqrt(2.0) + 1.0) / sqrt(2.0 * pi * (2.0 - sqrt(2.0)))

    print("EXACT_IDENTITY_PASS k=1..30")
    print(f"eta_dir={eta:.15f}")
    print(f"candidate_prefactor_C={C:.15f}")
    print("k  digits(num) digits(den)  sqrt(k)*exp(eta*k)*A_k")
    for k in (5, 10, 20, 40, 80, 120, 160, 200):
        b = B_double_sum(k)
        A = exp(-k) * (b.numerator / b.denominator)
        scaled = A * sqrt(k) * exp(eta * k)
        print(f"{k:3d} {len(str(b.numerator)):11d} {len(str(b.denominator)):11d} {scaled:.15f}")


if __name__ == "__main__":
    main()
