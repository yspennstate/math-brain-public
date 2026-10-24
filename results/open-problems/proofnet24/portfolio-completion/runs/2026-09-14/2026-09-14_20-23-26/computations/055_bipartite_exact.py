#!/usr/bin/env python3
"""Exact certificates for agents/055.md; no floating-point optimization.

Run from research-session:
    python computations/055_bipartite_exact.py

The output is written only to computations/055_bipartite_exact_results.json.
Brute cut enumeration uses all possible part-counts; exchangeability makes
these exactly all cut types, including boundary cuts.
"""

from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import json


def flow_value(a, b):
    return Q(3) - Q(1, a) - Q(1, b)


def cut_value(a, b, k, ell):
    """Direct stationary-mass / boundary-capacity expression."""
    mass = Q(k, 2 * a) + Q(ell, 2 * b)
    capacity = Q(b * k + a * ell - 2 * k * ell, 2 * a * b)
    return 2 * mass * (1 - mass) / capacity


def exhaustive_cuts(a, b):
    """Exact rational comparisons; no prediction of the maximizing cuts."""
    best_num, best_den, witnesses = -1, 1, []
    count = 0
    for k in range(a + 1):
        for ell in range(b + 1):
            boundary = b * k + a * ell - 2 * k * ell
            if not boundary:
                assert (k, ell) in [(0, 0), (a, b)]
                continue
            count += 1
            # Expand 2*pi(S)*pi(S^c)/Q(S,S^c) directly.
            mass_num = b * k + a * ell
            num = mass_num * (2 * a * b - mass_num)
            den = a * b * boundary
            comparison = num * best_den - best_num * den
            if comparison > 0:
                best_num, best_den = num, den
                witnesses = [(k, ell)]
            elif comparison == 0:
                witnesses.append((k, ell))
    return Q(best_num, best_den), witnesses, count


def formula_cut(a, b):
    if min(a, b) == 1:
        return Q(2) - Q(1, max(a, b)), None
    g = gcd(a, b)
    if g > 1:
        return Q(2), [(j * a // g, j * b // g) for j in range(1, g)]
    r = pow(b, -1, a)
    s = (b * r - 1) // a
    assert 1 <= r < a and 1 <= s < b and b * r - a * s == 1
    boundary = b * r + a * s - 2 * r * s
    return Q(2) - Q(1, a * b * boundary), sorted([(r, s), (a - r, b - s)])


def verify_primal_dual(a, b):
    """Check the actual signed source flows at every vertex and edge."""
    n = a + b
    pi = [Q(1, 2 * a)] * a + [Q(1, 2 * b)] * b
    edges = [(i, a + j) for i in range(a) for j in range(b)]
    loads = [Q(0) for _ in edges]
    for source in range(n):
        div = [Q(0) for _ in range(n)]
        for index, (i, bj) in enumerate(edges):
            j = bj - a
            if source < a:
                flow = Q(2 * a - 1 if i == source else -1, 2 * a * b)
            else:
                flow = Q(-(2 * b - 1) if j == source - a else 1, 2 * a * b)
            div[i] += flow
            div[bj] -= flow
            loads[index] += pi[source] * abs(flow)
        assert div == [Q(int(v == source)) - pi[v] for v in range(n)]
    capacity = Q(1, 2 * a * b)
    expected = flow_value(a, b)
    assert all(load / capacity == expected for load in loads)
    # Uniform edge length 2; calculate the dual by all ordered pairs.
    dual = Q(0)
    for x in range(n):
        for y in range(n):
            distance = 0 if x == y else (4 if (x < a) == (y < a) else 2)
            dual += pi[x] * pi[y] * distance
    assert sum(capacity * 2 for _ in edges) == 1
    assert dual == expected
    # Half laziness leaves the flow and stationary law unchanged.
    assert all(load / (capacity / 2) == 2 * expected for load in loads)
    return len(edges) * n, n * n


def verify_spectrum(a, b):
    n = a + b
    def apply(vector):
        return [sum(vector[a:]) / b] * a + [sum(vector[:a]) / a] * b
    vectors = [([Q(1)] * n, Q(1)), ([Q(1)] * a + [Q(-1)] * b, Q(-1))]
    for base, size in [(0, a), (a, b)]:
        for j in range(1, size):
            vector = [Q(0)] * n
            vector[base] = Q(1)
            vector[base + j] = Q(-1)
            vectors.append((vector, Q(0)))
    assert len(vectors) == n
    for vector, eigenvalue in vectors:
        assert apply(vector) == [eigenvalue * x for x in vector]
    tau = Q(1, 2) if n == 2 else Q(1)
    diameter = 1 if n == 2 else 2
    return tau, diameter


def h(value):
    fraction = value - value.numerator // value.denominator
    return fraction * (1 - fraction)


def main():
    cut_instances = 0
    cut_types = 0
    for a in range(1, 65):
        for b in range(a, 65):
            actual, witnesses, count = exhaustive_cuts(a, b)
            predicted, predicted_witnesses = formula_cut(a, b)
            assert actual == predicted, (a, b, actual, predicted)
            if predicted_witnesses is not None:
                assert sorted(witnesses) == sorted(predicted_witnesses), (a, b, witnesses)
            cut_instances += 1
            cut_types += count
            assert flow_value(a, b) <= Q(3, 2) * actual
    signed_entries, dual_pairs, flow_instances = 0, 0, 0
    for a in range(1, 11):
        for b in range(1, 11):
            entries, pairs = verify_primal_dual(a, b)
            signed_entries += entries
            dual_pairs += pairs
            verify_spectrum(a, b)
            flow_instances += 1
    h_checks = 0
    for denominator in range(1, 41):
        for numerator in range(denominator + 1):
            value = Q(numerator, denominator)
            for multiplier in range(-40, 41):
                assert h(multiplier * value) <= abs(multiplier) * h(value)
                h_checks += 1
    seed_checks = 0
    for m in range(1, 301):
        value, _ = formula_cut(2, m)
        expected = Q(2) if m % 2 == 0 else Q(2) - Q(1, 2 * m * m)
        assert value == expected
        gap = flow_value(2, m) / value
        assert gap < Q(5, 4)
        seed_checks += 1
    examples = []
    for a, b in [(1, 1), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5),
                 (2, 100), (2, 101), (3, 4), (3, 5), (4, 7), (5, 5), (100, 100)]:
        B, witnesses = formula_cut(a, b)
        if witnesses is None:
            _, witnesses, _ = exhaustive_cuts(a, b)
        F = flow_value(a, b)
        tau, diameter = verify_spectrum(a, b)
        examples.append({"a": a, "b": b, "F": str(F), "B": str(B),
                         "gap": str(F / B), "tau2": str(tau), "diameter": diameter,
                         "diameter_ratio": str(F / (tau * diameter)),
                         "maximizing_count_pairs": witnesses})
    result = {"status": "all exact checks passed", "arithmetic": "Python integers and fractions.Fraction",
              "exhaustive_cut_instances": cut_instances, "exhaustive_cut_types": cut_types,
              "cut_range": "1 <= a <= b <= 64; all 0<=k<=a, 0<=ell<=b except trivial cuts",
              "explicit_signed_flow_instances": flow_instances, "signed_flow_entries_checked": signed_entries,
              "dual_ordered_pairs_checked": dual_pairs, "flow_range": "1 <= a,b <= 10",
              "periodic_h_multiplier_checks": h_checks, "K2m_formula_checks": seed_checks,
              "examples": examples,
              "limitation": "Finite checks corroborate the written proofs; no finite enumeration proves a universal theorem."}
    out = Path(__file__).with_name("055_bipartite_exact_results.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "examples"}, indent=2))
    for row in examples:
        print(f"K_{{{row['a']},{row['b']}}}: F={row['F']}; B={row['B']}; gap={row['gap']}; R={row['diameter_ratio']}")
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
