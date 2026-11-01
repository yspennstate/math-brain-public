#!/usr/bin/env python3
"""Exact checker for P03/P0456 full clean marked-integral coefficient reduction.

For B_k ~ Beta(k,N-k+1), Q_k(x)=E[(x-B_k)_+], the checker verifies in
exact rational arithmetic on several finite (N,m,k) instances that

  int_0^1 Q_k(x)^k (1-x)^(m-k-1) dx

agrees with the coefficient-extraction representation

  (N+1)^(-k) sum_J [y^J] P_{N,k}(y)^k * B(J+1,kN+m-J),

where

  P_{N,k}(y)=sum_{j=k+1}^{N+1} (j-k) binom(N+1,j) y^j.

The two sides are constructed independently: the first expands Q_k directly
as a polynomial in x in its Bernstein form and integrates term by term; the
second works in y=x/(1-x) and evaluates beta integrals by factorials.
No floating-point arithmetic is used.
"""

from fractions import Fraction
from math import comb, factorial


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += b[i]
    return trim(out)


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return trim(out)


def poly_pow(a, n):
    out = [Fraction(1)]
    base = list(a)
    while n:
        if n & 1:
            out = poly_mul(out, base)
        n >>= 1
        if n:
            base = poly_mul(base, base)
    return out


def one_minus_x_power(r):
    return [Fraction(((-1) ** j) * comb(r, j)) for j in range(r + 1)]


def q_direct_polynomial(N, k):
    # Q_k(x)=(N+1)^(-1) sum_{j=k+1}^{N+1}
    #        (j-k) C(N+1,j) x^j(1-x)^(N+1-j).
    q = [Fraction(0)]
    for j in range(k + 1, N + 2):
        mon = [Fraction(0)] * j + [
            Fraction((j - k) * comb(N + 1, j), N + 1)
        ]
        mon = poly_mul(mon, one_minus_x_power(N + 1 - j))
        q = poly_add(q, mon)
    return q


def integrate_poly_times_one_minus(poly, r):
    # int_0^1 x^i(1-x)^r dx = i! r!/(i+r+1)!.
    ans = Fraction(0)
    for i, coeff in enumerate(poly):
        if coeff:
            ans += coeff * Fraction(
                factorial(i) * factorial(r), factorial(i + r + 1)
            )
    return ans


def direct_integral(N, m, k):
    q = q_direct_polynomial(N, k)
    return integrate_poly_times_one_minus(poly_pow(q, k), m - k - 1)


def transformed_integral(N, m, k):
    P = [Fraction(0)] * (N + 2)
    for j in range(k + 1, N + 2):
        P[j] = Fraction((j - k) * comb(N + 1, j))
    coeffs = poly_pow(P, k)

    ans = Fraction(0)
    for J, aJ in enumerate(coeffs):
        if not aJ:
            continue
        b = k * N + m - J
        assert b >= 1
        # B(J+1,b)=J! (b-1)!/(J+b)! and J+b=kN+m.
        beta = Fraction(
            factorial(J) * factorial(b - 1), factorial(k * N + m)
        )
        ans += Fraction(aJ, (N + 1) ** k) * beta
    return ans


def marked_probability(m, k, integral):
    # C_{m,k}=(m)_{k+1}/k!=m!/((m-k-1)!k!).
    prefactor = Fraction(
        factorial(m), factorial(m - k - 1) * factorial(k)
    )
    return prefactor * integral


def main():
    cases = [
        (3, 5, 1),
        (5, 7, 2),
        (6, 8, 2),
        (7, 10, 3),
        (8, 11, 3),
    ]

    for N, m, k in cases:
        lhs = direct_integral(N, m, k)
        rhs = transformed_integral(N, m, k)
        assert lhs == rhs
        M = marked_probability(m, k, lhs)
        print(
            f"N={N} m={m} k={k} I={lhs.numerator}/{lhs.denominator} "
            f"M={M.numerator}/{M.denominator} PASS"
        )

    print("FULL_CLEAN_COEFFICIENT_IDENTITY_PASS")


if __name__ == "__main__":
    main()
