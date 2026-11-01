#!/usr/bin/env python3
"""Exact finite checks for B13 critical-core/tensor-tax report.

Standard-library only.  Fourier coefficients and all activation quantities are
Fractions.  The theorem itself is analytic; this file checks the algebra on all
Boolean functions modulo global output sign through two variables, all ordered
pairs of dimensions 1 or 2, and the explicit strict non-tensorization witness.
"""
from fractions import Fraction
import json


def walsh(vals):
    N = len(vals)
    return [
        Fraction(
            sum(v * (-1 if ((S & x).bit_count() & 1) else 1)
                for x, v in enumerate(vals)),
            N,
        )
        for S in range(N)
    ]


def spectral(vals):
    return [a * a for a in walsh(vals)]


def phi(z, k):
    return sum((z ** r for r in range(k)), Fraction(0))


def activation(vals, z):
    p = spectral(vals)
    N = len(vals)
    best = None
    for T in range(N):
        q = sum(p[S] * phi(z, (S ^ T).bit_count()) for S in range(N))
        if best is None or q < best:
            best = q
    return best


def folded_J(vals):
    p = spectral(vals)
    N = len(vals)
    n = N.bit_length() - 1
    ans = Fraction(0)
    for i in range(n):
        pi = sum(p[S] for S in range(N) if (S >> i) & 1)
        ans += min(pi, 1 - pi)
    return ans


def tensor(f, g):
    # First factor occupies the low-order coordinates.
    return [a * b for b in g for a in f]


def character_multiply(vals, T):
    return [
        v * (-1 if ((x & T).bit_count() & 1) else 1)
        for x, v in enumerate(vals)
    ]


def functions_mod_global_sign(n):
    N = 1 << n
    # Fix f(0)=+1.
    for mask in range(1 << (N - 1)):
        vals = [1]
        for x in range(1, N):
            vals.append(-1 if ((mask >> (x - 1)) & 1) else 1)
        yield vals


def main():
    product_identity_checks = 0
    rational_tax_checks = 0
    character_gauge_checks = 0
    max_tax_ratio = Fraction(-10, 1)

    # Character invariance and A_z <= J at the dimension-cooling scale.
    for n in (1, 2):
        z = Fraction(n - 1, n)
        for f in functions_mod_global_sign(n):
            A = activation(f, z)
            J = folded_J(f)
            assert A <= J
            for T in range(1 << n):
                assert activation(character_multiply(f, T), z) == A
                character_gauge_checks += 1

    # Exact common-scale product identity and the clean rational J/4 tax.
    for n1 in (1, 2):
        for n2 in (1, 2):
            d = n1 + n2
            z = Fraction(d - 1, d)
            z1 = Fraction(n1 - 1, n1)
            z2 = Fraction(n2 - 1, n2)
            for f in functions_mod_global_sign(n1):
                for g in functions_mod_global_sign(n2):
                    fg = tensor(f, g)
                    Afg = activation(fg, z)
                    Af = activation(f, z)
                    Ag = activation(g, z)
                    assert Afg == Af + Ag - Fraction(1, d) * Af * Ag
                    product_identity_checks += 1

                    own_sum = activation(f, z1) + activation(g, z2)
                    Jfg = folded_J(fg)
                    excess = own_sum - Afg
                    assert excess <= Jfg / 4
                    rational_tax_checks += 1
                    if Jfg and excess / Jfg > max_tax_ratio:
                        max_tax_ratio = excess / Jfg

    # Strict Boolean witness: two copies of the two-bit one-point defect.
    w = [1, -1, 1, 1]
    ww = tensor(w, w)
    A_own = activation(w, Fraction(1, 2))
    A_common = activation(w, Fraction(3, 4))
    A_product = activation(ww, Fraction(3, 4))
    J_product = folded_J(ww)
    strict_excess = 2 * A_own - A_product
    assert A_own == Fraction(7, 8)
    assert A_common == Fraction(15, 16)
    assert A_product == Fraction(1695, 1024)
    assert J_product == 2
    assert strict_excess == Fraction(97, 1024)

    result = {
        "status": "PASS",
        "product_identity_checks": product_identity_checks,
        "rational_tax_checks": rational_tax_checks,
        "character_gauge_checks": character_gauge_checks,
        "total_checks": product_identity_checks + rational_tax_checks + character_gauge_checks,
        "max_small_case_tax_ratio": str(max_tax_ratio),
        "strict_boolean_witness": {
            "factor_truth_table": w,
            "A_factor_own_z_1_over_2": str(A_own),
            "A_factor_common_z_3_over_4": str(A_common),
            "A_product_z_3_over_4": str(A_product),
            "J_product": str(J_product),
            "sum_own_A_minus_product_A": str(strict_excess),
            "ratio_to_J_product": str(strict_excess / J_product),
        },
        "note": "The sharper analytic tax kappa=2*exp(-1/2)-1 is proved on the page; the exact checker uses the weaker rational 1/4 corollary.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
