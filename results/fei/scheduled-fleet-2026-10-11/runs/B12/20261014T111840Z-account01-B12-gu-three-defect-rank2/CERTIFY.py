#!/usr/bin/env python3
"""Rational interval certificate for the finite unmasked three-defect base."""

from fractions import Fraction
from functools import lru_cache

from CHECK import spectral_law, upper_masses, restrict_one, three_defect

TERMS = 80


def ln_unit_interval(x):
    """Rigorous bounds for ln(x), 1 <= x < 2, by the atanh series."""
    z = (x - 1) / (x + 1)
    total = Fraction(0)
    power = z
    for j in range(TERMS):
        total += power / (2 * j + 1)
        power *= z * z
    lo = 2 * total
    # Tail <= 2 z^(2m+1)/((2m+1)(1-z^2)).
    rem = 2 * power / ((2 * TERMS + 1) * (1 - z * z))
    return lo, lo + rem


LN2 = ln_unit_interval(Fraction(2))


@lru_cache(maxsize=None)
def log2_interval(x):
    assert x >= 1
    y = x
    k = 0
    while y >= 2:
        y /= 2
        k += 1
    yl, yu = ln_unit_interval(y)
    nl = k * LN2[0] + yl
    nu = k * LN2[1] + yu
    return nl / LN2[1], nu / LN2[0]


@lru_cache(maxsize=None)
def u_interval(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    lo = Fraction(0)
    hi = Fraction(0)
    for mass, upper in zip(p, pi):
        if mass:
            a, b = log2_interval(upper / mass)
            lo += mass * a
            hi += mass * b
    return lo, hi


def influence(values):
    return sum(Fraction(s.bit_count()) * x
               for s, x in enumerate(spectral_law(values)))


def g_interval(values):
    n = len(values).bit_length() - 1
    rl, ru = u_interval(values)
    lo, hi = n * rl, n * ru
    for i in range(n):
        for bit in (0, 1):
            cl, cu = u_interval(restrict_one(values, i, bit))
            lo -= cu / 2
            hi -= cl / 2
    return lo, hi


def main():
    count = 0
    maximum = (Fraction(-10**9), None)
    for n in range(2, 8):
        for a in range(n + 1):
            for b in range(n - a + 1):
                c = n - a - b
                if min(a + c, b + c, a + b) == 0:
                    continue
                f = three_defect(n, a, b, c)
                gl, gu = g_interval(f)
                inf = influence(f)
                assert gu <= 10 * inf
                maximum = max(maximum, (gu / inf, (n, a, b, c)))
                count += 1
    ratio, witness = maximum
    bad = three_defect(5, 4, 1, 0)
    rl, ru = u_interval(bad)
    c0l, c0u = u_interval(restrict_one(bad, 4, 0))
    c1l, c1u = u_interval(restrict_one(bad, 4, 1))
    delta_lo = rl - (c0u + c1u) / 2
    inf_bad = Fraction(1, 16)
    assert delta_lo > 2 * inf_bad
    print(f"certified_parameter_cases={count}")
    print(f"terms={TERMS}")
    print(f"max_upper_ratio_float={float(ratio):.17g}")
    print(f"max_upper_ratio_witness={witness}")
    print("all_G_le_10I=True")
    print(f"coordinate_2I_falsifier_lower_ratio={float(delta_lo / inf_bad):.17g}")
    print("coordinate_2I_claim=False")


if __name__ == "__main__":
    main()
