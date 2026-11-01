#!/usr/bin/env python3
"""Exact algebra checks for agent 037's P12/P13 staging repair.

This is a recurrence certificate, not a simulation or a proof of the random
matrix theorem. The analytic proofs are in agents/037.md.
"""

from fractions import Fraction as F
from math import isclose, log


def h(beta):
    return beta * log(beta) - (beta - 1) * log(beta - 1)


def binary_entropy(x):
    return -x * log(x) - (1 - x) * log(1 - x)


def g(beta, delta):
    return binary_entropy(delta) + (beta - 1) * binary_entropy(delta / (beta - 1))


def main():
    theta, cap, slab = F(1, 3), F(5, 4), F(1, 11)
    mass0, edges0 = F(1000000), F(17)
    mass, edges = mass0, edges0
    for j in range(9):
        actual = edges / (slab * mass**2)
        corrected = edges0 / mass0**2 * (cap / theta**2)**j * slab**(-j - 1)
        assert actual == corrected
        mass *= theta * slab
        edges *= cap * slab
    print("PASS: exact two-tier invariant for j = 0,...,8")

    ell, medium_factor = F(2, 7), F(3)
    medium0, bad0 = F(23), F(7)
    mass, medium, bad = mass0, medium0, bad0
    for j in range(9):
        assert mass == (theta * ell * slab)**j * mass0
        medium_invariant = medium_factor * medium / mass**2
        expected_medium = (medium0 / mass0**2 * medium_factor
                           * (cap / theta**2)**j * ell**(-4*j)
                           * medium_factor**j)
        assert medium_invariant == expected_medium
        bad_invariant = bad / (slab * mass**2)
        expected_bad = (bad0 / mass0**2 * (cap / theta**2)**j
                        * ell**(-4*j) * slab**(-j-1))
        assert bad_invariant == expected_bad
        mass *= theta * ell * slab
        medium *= cap * ell**(-2) * medium_factor * slab**2
        bad *= cap * ell**(-2) * slab
    print("PASS: exact three-tier mass and both invariants for j = 0,...,8")

    lam, dim = 1.2, 1000
    for stages in (1, 2, 7, 31):
        log_inverse_slab = lam * dim / stages + log(stages) / 2
        assert isclose(stages * log_inverse_slab,
                       lam * dim + stages * log(stages) / 2,
                       rel_tol=1e-14, abs_tol=1e-10)
    print("PASS: k log(1/s) = lambda*m + (k/2)*log(k)")

    gamma, beta, eps = 2.0, 1.95, 0.1
    lam, entropy = h(gamma) - eps, h(beta)
    gap = entropy - lam
    assert gap > 0
    delta = min(1.0, beta - 1, (beta - 1) / beta) / 8
    while g(beta, delta) >= gap / 4:
        delta /= 2
    bad_rate = (lam + entropy) / 2
    high_overlap_rate = entropy - g(beta, delta)
    assert high_overlap_rate > bad_rate > lam
    print("Entropy example (illustrative floating-point values):")
    for name, value in (("lambda", lam), ("h(beta)", entropy),
                        ("delta", delta), ("kappa_B", bad_rate),
                        ("high-overlap rate", high_overlap_rate)):
        print(f"  {name}: {value:.12g}")
    print("All checks passed. These checks do not certify external analytic inputs.")


if __name__ == "__main__":
    main()
