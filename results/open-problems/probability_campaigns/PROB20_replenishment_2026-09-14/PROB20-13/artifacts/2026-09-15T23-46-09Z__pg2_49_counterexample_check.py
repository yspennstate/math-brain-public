#!/usr/bin/env python3
"""Exact checker for the PROB20-13 projective-plane cone counterexample.

No floating-point step is used in the proof-critical assertions.

The script:
1. constructs GF(49)=GF(7)[a]/(a^2+1);
2. enumerates the 2451 projective points and 2451 projective line-coefficient
   classes in PG(2,49);
3. verifies every point and line has degree 50;
4. verifies every pair of distinct points has exactly one common line;
5. checks the exact cone parameters, spectrum formula, dual normalization,
   metric objective, and strict violation of F <= 2 tau_rel D;
6. checks the polynomial criterion for the infinite square-order family at t=7.

This is a reproducibility check for the exact proof in the corresponding report.
"""

from fractions import Fraction

P = 7
QFIELD = 49


def make_field_tables():
    # Encode a+b*alpha as a+7*b, with alpha^2=-1 over GF(7).
    add = [[0] * QFIELD for _ in range(QFIELD)]
    mul = [[0] * QFIELD for _ in range(QFIELD)]
    for x in range(QFIELD):
        a, b = x % P, x // P
        for y in range(QFIELD):
            c, d = y % P, y // P
            add[x][y] = ((a + c) % P) + P * ((b + d) % P)
            mul[x][y] = ((a * c - b * d) % P) + P * ((a * d + b * c) % P)

    inv = [None] * QFIELD
    for x in range(1, QFIELD):
        for y in range(1, QFIELD):
            if mul[x][y] == 1:
                inv[x] = y
                break
        assert inv[x] is not None
    return add, mul, inv


def projective_representatives(mul, inv):
    reps = set()
    for x in range(QFIELD):
        for y in range(QFIELD):
            for z in range(QFIELD):
                if x == y == z == 0:
                    continue
                pivot = x or y or z
                ip = inv[pivot]
                reps.add((mul[x][ip], mul[y][ip], mul[z][ip]))
    reps = sorted(reps)
    assert len(reps) == 2451
    return reps


def dot_zero(u, v, add, mul):
    x, y, z = u
    a, b, c = v
    return add[add[mul[x][a]][mul[y][b]]][mul[z][c]] == 0


def construct_incidence(reps, add, mul):
    point_neigh = [[] for _ in reps]
    line_degrees = [0] * len(reps)
    for i, p in enumerate(reps):
        for j, ell in enumerate(reps):
            if dot_zero(p, ell, add, mul):
                point_neigh[i].append(j)
                line_degrees[j] += 1

    assert all(len(ns) == 50 for ns in point_neigh)
    assert all(d == 50 for d in line_degrees)
    assert sum(map(len, point_neigh)) == 122550
    return point_neigh


def verify_unique_line(point_neigh):
    masks = []
    for ns in point_neigh:
        mask = 0
        for j in ns:
            mask |= 1 << j
        masks.append(mask)

    for i in range(len(masks)):
        mi = masks[i]
        for j in range(i + 1, len(masks)):
            assert (mi & masks[j]).bit_count() == 1


def exact_counterexample_checks():
    s = 49
    N = s * s + s + 1
    nH = 2 * N
    r = s + 1

    assert N == 2451
    assert nH == 4902
    assert r == 50

    # Cone G=K1 join H.
    mH = N * r
    m = mH + nH
    assert mH == 122550
    assert m == 127452

    D = 2
    pi_h = Fraction(1, 52)
    pi_base_each = Fraction(51, 2 * m)
    assert pi_base_each * nH == Fraction(51, 52)
    capacity = Fraction(1, 2 * m)
    assert capacity == Fraction(1, 254904)

    # Incidence spectrum: B B^T = 49 I + J gives singular values 50 and 7.
    # In the cone, nonconstant base eigenvalues are divided by base degree 51.
    lambda2 = Fraction(7, 51)
    tau = Fraction(1, 1) / (1 - lambda2)
    target = 2 * tau * D
    assert tau == Fraction(51, 44)
    assert target == Fraction(51, 11)

    # Exact dual edge lengths.
    x = Fraction(156, 53)  # spoke
    y = Fraction(104, 53)  # incidence edge
    assert 2 * x == 3 * y

    total_edge_length = nH * x + mH * y
    assert total_edge_length == 2 * m
    assert capacity * total_edge_length == 1

    # Distance distribution in the projective-plane incidence graph.
    layers = [1, 50, 2450, 2401]
    assert sum(layers) == nH
    mean_H = Fraction(50 + 2 * 2450 + 3 * 2401, nH)
    assert mean_H == Fraction(4051, 1634)

    # Since 2x=3y and diam(H)=3, base weighted distances equal y*d_H.
    objective = (
        2 * pi_h * Fraction(51, 52) * x
        + Fraction(51, 52) ** 2 * y * mean_H
    )
    assert objective == Fraction(10786653, 2251652)

    gap = objective - target
    assert gap == Fraction(3818931, 24768172)
    assert gap > 0

    return objective, target, gap


def family_polynomial(t):
    return (
        t**8
        - 5 * t**7
        - 3 * t**6
        - 19 * t**5
        - 29 * t**4
        - 13 * t**3
        - 42 * t**2
        - 8 * t
        - 32
    )


def main():
    add, mul, inv = make_field_tables()

    # x^2+1 is irreducible over GF(7): -1=6 is not among quadratic residues.
    quadratic_residues = {(a * a) % 7 for a in range(7)}
    assert 6 not in quadratic_residues

    reps = projective_representatives(mul, inv)
    point_neigh = construct_incidence(reps, add, mul)
    verify_unique_line(point_neigh)

    objective, target, gap = exact_counterexample_checks()

    assert family_polynomial(7) == 898572
    assert family_polynomial(7) > 0

    print("PG(2,49) representatives:", len(reps))
    print("incidence edges:", sum(map(len, point_neigh)))
    print("dual objective:", objective)
    print("2*tau_rel*D:", target)
    print("exact positive gap:", gap)
    print("square-order family polynomial P(7):", family_polynomial(7))
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
