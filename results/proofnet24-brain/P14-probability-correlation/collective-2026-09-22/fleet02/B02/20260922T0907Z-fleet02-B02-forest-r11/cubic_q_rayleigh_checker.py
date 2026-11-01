#!/usr/bin/env python3
"""Exact regression for the cubic-vertex q-Rayleigh factorization.

Uses only fractions.Fraction.  It enumerates every simple graph H on four
labelled vertices with terminals 0,1,2, attaches a new cubic vertex to those
terminals, and checks the exact derivative Rayleigh gap against the closed
terminal-partition formula for several rational q and third-star weights g.
"""
from fractions import Fraction
from itertools import combinations

EDGES4 = list(combinations(range(4), 2))
TERMS = (0, 1, 2)

def components(n, chosen_edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    for a, b in chosen_edges:
        union(a, b)
    roots = [find(i) for i in range(n)]
    return roots, len(set(roots))

def terminal_class(roots):
    r = [roots[i] for i in TERMS]
    if r[0] == r[1] == r[2]:
        return "C"
    if r[0] == r[1] != r[2]:
        return "B12"
    if r[0] == r[2] != r[1]:
        return "B13"
    if r[1] == r[2] != r[0]:
        return "B23"
    return "A"

def masses_for_H(Hedges, weights, q):
    masses = {k: Fraction(0) for k in ("A", "B12", "B13", "B23", "C")}
    for mask in range(1 << len(Hedges)):
        chosen = []
        weight = Fraction(1)
        edge_count = 0
        for i, edge in enumerate(Hedges):
            if (mask >> i) & 1:
                chosen.append(edge)
                weight *= weights[i]
                edge_count += 1
        roots, k = components(4, chosen)
        nullity = edge_count - 4 + k
        masses[terminal_class(roots)] += (q ** nullity) * weight
    return masses

def R_formula(masses, q, g):
    A, B12, B13, B23, C = (masses[k] for k in ("A", "B12", "B13", "B23", "C"))
    return (
        (g + 1) ** 2 * B12 * (A + B12 + B13 + B23)
        + (g + 1) * (q * g + 2) * B12 * C
        + (g + 1) * (1 - (1 - q) * g) * A * C
        + (1 - q) * g * g * B13 * B23
        + (1 + q * g) * C * (B13 + B23 + C)
    )

def direct_gap(Hedges, weights, q, a=Fraction(2), b=Fraction(3), g=Fraction(1)):
    all_edges = list(Hedges) + [(4, 0), (4, 1), (4, 2)]
    all_weights = list(weights) + [a, b, g]
    e1 = len(Hedges)
    e2 = e1 + 1
    P = Pe = Pf = Pef = Fraction(0)
    for mask in range(1 << len(all_edges)):
        chosen = []
        weight = Fraction(1)
        edge_count = 0
        for i, edge in enumerate(all_edges):
            if (mask >> i) & 1:
                chosen.append(edge)
                weight *= all_weights[i]
                edge_count += 1
        _roots, k = components(5, chosen)
        nullity = edge_count - 5 + k
        term = (q ** nullity) * weight
        P += term
        if (mask >> e1) & 1:
            Pe += term / a
        if (mask >> e2) & 1:
            Pf += term / b
        if ((mask >> e1) & 1) and ((mask >> e2) & 1):
            Pef += term / (a * b)
    return Pe * Pf - P * Pef

def main():
    qs = [Fraction(0), Fraction(1,5), Fraction(1,2), Fraction(3,4), Fraction(1)]
    gs = {
        Fraction(0): [Fraction(1,2), Fraction(1)],
        Fraction(1,5): [Fraction(1), Fraction(5,4)],
        Fraction(1,2): [Fraction(1), Fraction(2)],
        Fraction(3,4): [Fraction(1), Fraction(4)],
        Fraction(1): [Fraction(1), Fraction(5)],
    }
    cases = failures = positive = q1_zero = 0
    q0_partner_checks = 0
    for hmask in range(1 << len(EDGES4)):
        Hedges = [edge for i, edge in enumerate(EDGES4) if (hmask >> i) & 1]
        weights = [Fraction(1 + (EDGES4.index(edge) % 3)) for edge in Hedges]
        for q in qs:
            masses = masses_for_H(Hedges, weights, q)
            for g in gs[q]:
                direct = direct_gap(Hedges, weights, q, Fraction(2), Fraction(3), g)
                predicted = (1 - q) * R_formula(masses, q, g)
                cases += 1
                if direct != predicted or direct < 0:
                    failures += 1
                    print("FAIL", hmask, q, g, direct, predicted, masses)
                if direct > 0:
                    positive += 1
                if q == 1 and direct == 0:
                    q1_zero += 1
                if q == 0 and g == 1:
                    A, B12, B13, B23, C = (
                        masses[k] for k in ("A", "B12", "B13", "B23", "C")
                    )
                    T = A + B12 + B13 + B23 + C
                    partner = 4 * B12 * T + (B13 + C) * (B23 + C)
                    if direct != partner:
                        failures += 1
                        print("FAIL_PARTNER_REDUCTION", hmask, direct, partner)
                    q0_partner_checks += 1

    print("graphs=64")
    print(f"exact_cases={cases}")
    print(f"strictly_positive_cases={positive}")
    print(f"q1_zero_cases={q1_zero}")
    print(f"q0_partner_reduction_checks={q0_partner_checks}")
    print(f"failures={failures}")
    print("STATUS=" + ("ALL_EXACT_CHECKS_PASS" if failures == 0 else "FAIL"))

if __name__ == "__main__":
    main()
