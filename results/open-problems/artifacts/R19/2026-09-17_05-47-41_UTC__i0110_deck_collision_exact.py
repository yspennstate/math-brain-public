#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def check_two_sheet_nonuniform():
    # Quotient X x Z2 -> X with a nonuniform stationary reference.
    X = [0, 1, 2]
    Gamma = [0, 1]
    tilde = [(x, g) for x in X for g in Gamma]
    pi = {0: Fraction(1, 2), 1: Fraction(1, 3), 2: Fraction(1, 6)}
    vals = [
        Fraction(1, 10), Fraction(1, 20),
        Fraction(1, 8), Fraction(1, 12),
        Fraction(1, 6), Fraction(9, 40),
    ]
    rt = dict(zip(tilde, vals))
    m = sum(rt.values(), Fraction(0))
    r = {x: sum((rt[(x, g)] for g in Gamma), Fraction(0)) for x in X}
    lhs = sum((r[x] - m * pi[x]) ** 2 / pi[x] for x in X)
    coll = Fraction(0)
    for h in Gamma:
        for x, g in tilde:
            coll += rt[(x, g)] * rt[(x, (g + h) % 2)] / pi[x]
    rhs = coll - m * m
    assert lhs == rhs
    return m, lhs


def check_lattice_quotient_uniform():
    # Finite lattice proxy: Z4^2 -> Z2^2 with deck group (2 Z4)^2.
    tilde = list(product(range(4), repeat=2))
    base = list(product(range(2), repeat=2))
    Gamma = [(0, 0), (2, 0), (0, 2), (2, 2)]
    pi = {x: Fraction(1, 4) for x in base}
    rt = {
        z: Fraction((3 * z[0] + 5 * z[1] + 1) % 11 + 1, 200)
        for z in tilde
    }
    m = sum(rt.values(), Fraction(0))
    phi = lambda z: (z[0] % 2, z[1] % 2)
    r = {
        x: sum((rt[z] for z in tilde if phi(z) == x), Fraction(0))
        for x in base
    }
    lhs = sum((r[x] - m * pi[x]) ** 2 / pi[x] for x in base)
    coll = Fraction(0)
    for h in Gamma:
        for z in tilde:
            hz = ((z[0] + h[0]) % 4, (z[1] + h[1]) % 4)
            coll += rt[z] * rt[hz] / pi[phi(z)]
    rhs = coll - m * m
    assert lhs == rhs
    return m, lhs


def check_pair_bijection():
    # Every ordered pair in one fiber must correspond to exactly one deck element.
    Gamma = list(range(7))
    for a in Gamma:
        for b in Gamma:
            hits = [h for h in Gamma if (a + h) % 7 == b]
            assert len(hits) == 1


if __name__ == "__main__":
    check_pair_bijection()
    m1, d1 = check_two_sheet_nonuniform()
    m2, d2 = check_lattice_quotient_uniform()
    print("C015_PAIR_BIJECTION_PASS Z7")
    print(f"C015_NONUNIFORM_PASS mass={m1} defect={d1}")
    print(f"C015_LATTICE_PASS mass={m2} defect={d2}")
    print("ALL_EXACT_CHECKS_PASS")
