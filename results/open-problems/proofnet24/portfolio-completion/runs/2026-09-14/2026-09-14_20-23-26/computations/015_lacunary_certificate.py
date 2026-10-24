#!/usr/bin/env python3
"""Exact rational checks for the fixed law proved in agents/015.md.

No simulation and no approximation to a conditioned tree is performed.
The displayed intervals include the unconstructed infinite tail using the
analytic bounds in the report. All assertions use fractions, not floats.
"""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as F
from math import isqrt


def decimal_endpoint(value, rounding):
    with localcontext() as ctx:
        ctx.prec = 32
        ctx.rounding = rounding
        return Decimal(value.numerator) / Decimal(value.denominator)


def show_interval(label, lower, upper):
    assert lower <= upper
    lo = decimal_endpoint(lower, ROUND_FLOOR)
    hi = decimal_endpoint(upper, ROUND_CEILING)
    print(f"{label}: [{lo}, {hi}]")


def main(stages=3):
    q = F(1, 4)
    n = 256
    deficit = 1 - q
    mean = q
    second_moment = q
    rare_mass = F(0)
    previous_n = 1

    for r in range(1, stages + 1):
        center = deficit * n
        assert center.denominator == 1
        root = isqrt(n)
        assert root * root == n
        lower_atom = int(center) - root
        upper_atom = int(center) + root
        assert F(5, 8) * n < lower_atom < upper_atom < n
        assert lower_atom > previous_n
        p = F(1, n**4)
        mean += p * (lower_atom + upper_atom)
        second_moment += p * (lower_atom**2 + upper_atom**2)
        rare_mass += 2 * p
        deficit *= 1 - F(2, n**3)
        assert mean == 1 - deficit
        print(f"stage {r}: n={n}; atoms=({lower_atom}, {upper_atom})")
        previous_n, n = n, n**4

    # n is the first omitted scale. For a>0, sum_{s>=r} n_s^-a
    # is at most 2*n_r^-a. Each omitted pair has atoms below n_s.
    mean_tail = F(4, n**3)
    second_tail = F(4, n**2)
    mass_tail = F(4, n**4)
    pi0_lower = 1 - q - rare_mass - mass_tail
    pi0_upper = 1 - q - rare_mass
    mean_lower, mean_upper = mean, mean + mean_tail
    variance_lower = second_moment - mean_upper**2
    variance_upper = second_moment + second_tail - mean_lower**2
    gamma_lower = q * (1 - mean_upper)
    gamma_upper = q * (1 - mean_lower)
    shift_lower = gamma_lower / variance_upper
    shift_upper = gamma_upper / variance_lower
    b = q * (1 - q)
    branch_variance_lower = b - gamma_upper**2 / variance_lower
    branch_variance_upper = b - gamma_lower**2 / variance_upper

    assert pi0_lower > F(1, 2)
    assert q < mean_lower <= mean_upper < F(5, 16)
    assert 0 < variance_lower <= variance_upper < F(1, 2)
    assert 0 < shift_lower <= shift_upper
    assert 0 < branch_variance_lower <= branch_variance_upper < b
    show_interval("pi_0", pi0_lower, pi0_upper)
    show_interval("nu", mean_lower, mean_upper)
    show_interval("sigma^2", variance_lower, variance_upper)
    show_interval("a_*", shift_lower, shift_upper)
    show_interval("v_*", branch_variance_lower, branch_variance_upper)
    print("All exact rational checks passed; bounds include the infinite tail.")


if __name__ == "__main__":
    main()
