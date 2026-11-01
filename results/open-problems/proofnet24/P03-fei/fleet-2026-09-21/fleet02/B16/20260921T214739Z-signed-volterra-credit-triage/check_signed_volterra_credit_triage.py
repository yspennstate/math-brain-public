#!/usr/bin/env python3
"""Exact/self-checks for B16 signed live-window compensation triage.

This checker verifies only algebra stated in the accompanying report:
(1) the exact squared Fourier mass of an affine two-plane defect,
(2) the explicit R16 high-resolvent upper bound on that family,
(3) vanishing of the central/Ward gap at (q,k)=(3,1), and
(4) a finite-window Volterra integration-by-parts identity on rational
    polynomial test fields.

It is falsification evidence, not an end-to-end FEI proof.
"""
from fractions import Fraction
from math import log


def check_fourier_and_r16():
    max_ratio = 0.0
    last_ratio = None
    count = 0
    for D in range(4, 41):
        N = 1 << D
        n = D - 1
        p0 = Fraction((N - 8) ** 2, N ** 2)
        p = Fraction(64, N ** 2)
        multiplicity = N // 4 - 1
        assert p0 + multiplicity * p == 1

        delta_inf = (
            float(p0) * log(3.0 / (2.0 + float(p0)))
            + multiplicity * float(p) * log(3.0 / (2.0 + float(p)))
        )
        J = 8.0 * n / N
        explicit_bound = (8.0 + 16.0 * log(1.5)) / N
        assert -1e-18 <= delta_inf <= explicit_bound * (1.0 + 5e-14)

        ratio = delta_inf / J
        max_ratio = max(max_ratio, ratio)
        last_ratio = ratio
        count += 1
    return count, max_ratio, last_ratio


def check_ward_gap():
    q = Fraction(3)
    k = Fraction(1)
    ward = 1 - 1 / q
    eps = 2 * (Fraction(1, 2) ** q) / q * (
        (Fraction(1, 2) ** k) / k - (Fraction(1, 2) ** q) / q
    )
    rho = Fraction(11, 192) * ward - eps
    assert eps == Fraction(11, 288)
    assert rho == 0
    return rho


def int_power(a, b, p):
    return (b ** (p + 1) - a ** (p + 1)) / Fraction(p + 1)


def volterra_case(a, b, m):
    # Scalar test field u(s)=s^m. Then
    # v(s)=int_a^s u(t)t^-3 dt and the identity
    # int_a^b u(s)^2 s^-3 ds = u(b)v(b)-int_a^b u'(s)v(s)ds
    # is evaluated in exact rational arithmetic.
    assert m >= 3
    energy = int_power(a, b, 2 * m - 3)
    v_b = int_power(a, b, m - 3)
    boundary = (b ** m) * v_b

    # v(s)=(s^(m-2)-a^(m-2))/(m-2)
    # u'(s)v(s)=m*s^(m-1)*v(s)
    cross = Fraction(m, m - 2) * (
        int_power(a, b, 2 * m - 3)
        - (a ** (m - 2)) * int_power(a, b, m - 1)
    )
    assert boundary - cross == energy
    return energy, boundary, cross


def main():
    count, max_ratio, last_ratio = check_fourier_and_r16()
    rho = check_ward_gap()
    tests = [
        (Fraction(0), Fraction(1, 2), 3),
        (Fraction(1, 10), Fraction(1, 2), 3),
        (Fraction(1, 4), Fraction(3, 5), 4),
    ]
    out = []
    for a, b, m in tests:
        energy, boundary, cross = volterra_case(a, b, m)
        out.append({
            "a": str(a), "b": str(b), "m": m,
            "energy": str(energy), "boundary": str(boundary), "cross": str(cross),
        })
    print("PASS")
    print(f"fourier_cases={count}")
    print(f"max_delta_over_J={max_ratio:.17g}")
    print(f"D40_delta_over_J={last_ratio:.17g}")
    print(f"ward_gap_q3k1={rho}")
    for row in out:
        print("volterra", row)


if __name__ == "__main__":
    main()
