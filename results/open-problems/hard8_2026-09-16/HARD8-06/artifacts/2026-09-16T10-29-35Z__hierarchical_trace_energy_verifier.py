#!/usr/bin/env python3
"""
Exact verifier for HARD8-06 checkpoint 2026-09-16T10-29-35Z.

Checks the combinatorial hierarchical q-adic collision energy used in the
report. Standard library only; all arithmetic is exact integers/Fraction.
"""
from itertools import combinations
from fractions import Fraction


def balanced_ordered_collision_count(m, s):
    a, r = divmod(s, m)
    return m * a * (a - 1) + 2 * r * a


def hierarchical_energy(q, s):
    total = 0
    ell = 1
    while q ** ell < s:
        total += balanced_ordered_collision_count(q ** ell, s)
        ell += 1
    return total


def residue_tree_energy(q, H, subset):
    total = 0
    for ell in range(1, H + 1):
        m = q ** ell
        counts = [0] * m
        for x in subset:
            counts[x % m] += 1
        total += sum(c * (c - 1) for c in counts)
    return total


def L_q(q, s):
    L = 0
    ell = 1
    while q ** ell < s:
        L = ell
        ell += 1
    return L


def exact_decomposition(q, s):
    L = L_q(q, s)
    geom = sum(
        (Fraction(1, q ** ell) for ell in range(1, L + 1)),
        Fraction(0, 1),
    )
    correction = Fraction(0, 1)
    for ell in range(1, L + 1):
        m = q ** ell
        _, r = divmod(s, m)
        correction += Fraction(r * (m - r), m)
    rhs = Fraction(s * s) * geom - L * s + correction
    return L, rhs, correction


def brute_box_min(m, s):
    # Exhaust all weak compositions for small m,s only.
    best = None

    def rec(left, boxes, prefix):
        nonlocal best
        if boxes == 1:
            occ = prefix + [left]
            val = sum(x * (x - 1) for x in occ)
            if best is None or val < best:
                best = val
            return
        for x in range(left + 1):
            rec(left - x, boxes - 1, prefix + [x])

    rec(s, m, [])
    return best


box_checks = 0
for m in range(1, 8):
    for s in range(0, 10):
        formula = balanced_ordered_collision_count(m, s)
        brute = brute_box_min(m, s)
        assert formula == brute, (m, s, formula, brute)
        box_checks += 1


decomp_checks = 0
for q in range(2, 8):
    for s in range(1, 100):
        E = hierarchical_energy(q, s)
        L, rhs, correction = exact_decomposition(q, s)
        assert Fraction(E, 1) == rhs, (q, s, E, rhs)
        assert correction >= 0

        # Exact lower bound (7.3) in the report.
        if L:
            lower = (
                Fraction(s * s)
                * (Fraction(1, 1) - Fraction(1, q ** L))
                / Fraction(q - 1, 1)
                - L * s
            )
        else:
            lower = Fraction(0, 1)
        assert Fraction(E, 1) >= lower

        # Each correction term r(1-r/m) <= m/4, summed exactly.
        corr_upper = sum(
            (Fraction(q ** ell, 4) for ell in range(1, L + 1)),
            Fraction(0, 1),
        )
        assert correction <= corr_upper
        decomp_checks += 1


# Exhaustive finite q-adic residue-tree minima.
tree_checks = 0
for q, H, max_s in [(2, 4, 8), (3, 2, 6), (4, 2, 5)]:
    N = q ** H
    for s in range(1, min(max_s, N) + 1):
        target = hierarchical_energy(q, s)
        best = None
        for S in combinations(range(N), s):
            val = residue_tree_energy(q, H, S)
            if best is None or val < best:
                best = val
        assert best == target, (q, H, s, best, target)

        # The first s base-q labels are balanced modulo q^ell at every level.
        explicit = residue_tree_energy(q, H, tuple(range(s)))
        assert explicit == target, (q, H, s, explicit, target)
        tree_checks += 1


# Compare against the previous single-level Cauchy energy exactly.
comparison_checks = 0
strict_improvements = 0
for q in range(2, 10):
    for s in range(1, 200):
        old = max(Fraction(0, 1), Fraction(s * s, q) - s)
        new = Fraction(hierarchical_energy(q, s), 1)
        assert new >= old
        if s > q * q:
            assert new > old
            strict_improvements += 1
        comparison_checks += 1


print("ALL_CHECKS_PASSED")
print("box_minimum_checks =", box_checks)
print("exact_decomposition_checks =", decomp_checks)
print("exhaustive_tree_minimum_checks =", tree_checks)
print("single_level_comparison_checks =", comparison_checks)
print("strict_higher_level_improvements =", strict_improvements)
