#!/usr/bin/env python3
"""Exact certificates for C034's common-permutation projection-DPP coupling.

Only the Python standard library is used. Complex arithmetic is in Q(sqrt(-3)).
The all-parameter theorem is proved in agents/C034.md; this script independently
checks every projection law in two concrete full Boolean lattices, their labeled
diamonds, and the five-site obstruction to a common permutation at gamma=4.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] - 3 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def norm2(x):
    return x[0] * x[0] + 3 * x[1] * x[1]


def inv(x):
    d = norm2(x)
    assert d
    return (x[0] / d, -x[1] / d)


def determinant(a):
    a = [list(row) for row in a]
    result = ONE
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            result = neg(result)
        value = a[col][col]
        result = mul(result, value)
        reciprocal = inv(value)
        for row in range(col + 1, len(a)):
            factor = mul(a[row][col], reciprocal)
            for j in range(col + 1, len(a)):
                a[row][j] = add(a[row][j], neg(mul(factor, a[col][j])))
            a[row][col] = ZERO
    return result


def subsets(n, size=None):
    return [frozenset(s) for k in (range(n + 1) if size is None else [size])
            for s in combinations(range(n), k)]


def permuted(p, a):
    return frozenset(p[i] for i in a)


def transposition(n, i, j):
    p = list(range(n))
    p[i], p[j] = j, i
    return tuple(p)


def cycle(n, i, j, k):
    p = list(range(n))
    p[i], p[j], p[k] = j, k, i
    return tuple(p)


def iid_triple_weights(s, gamma):
    n = len(s)
    weights = {tuple(range(n)): 1 - gamma * (1 - sum(x**3 for x in s)) / 3}
    for i, j in combinations(range(n), 2):
        weights[transposition(n, i, j)] = gamma * s[i] * s[j] * (s[i] + s[j])
    for i, j, k in combinations(range(n), 3):
        value = gamma * s[i] * s[j] * s[k]
        weights[cycle(n, i, j, k)] = value
        weights[cycle(n, i, k, j)] = value
    assert min(weights.values()) >= 0
    assert sum(weights.values()) == 1
    return {p: value for p, value in weights.items() if value}


def flat_weights(n, gamma):
    assert n >= 3
    weights = {tuple(range(n)): 1 - gamma * F(n - 1, 3 * n)}
    value = gamma / (n * n * (n - 2))
    for i, j, k in combinations(range(n), 3):
        weights[cycle(n, i, j, k)] = value
        weights[cycle(n, i, k, j)] = value
    assert min(weights.values()) >= 0
    assert sum(weights.values()) == 1
    return {p: value for p, value in weights.items() if value}


def unitary(g, c):
    denominator = sum(x*x for x in g)
    q = [[add(ONE if i == j else ZERO,
              mul(c, (F(g[i] * g[j], denominator), F(0))))
          for j in range(len(g))] for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g)):
            actual = ZERO
            for k in range(len(g)):
                actual = add(actual, mul(conj(q[k][i]), q[k][j]))
            assert actual == (ONE if i == j else ZERO)
    return q


def minor_probability(q, a, b):
    return norm2(determinant([[q[i][j] for j in sorted(a)] for i in sorted(b)]))


def verify_all_projection_laws(q, s, gamma, weights):
    n = len(q)
    count = 0
    for a in subsets(n):
        distribution = defaultdict(F)
        for p, value in weights.items():
            distribution[permuted(p, a)] += value
        alpha = sum(s[i] for i in a)
        for b in subsets(n, len(a)):
            exact = minor_probability(q, a, b)
            assert distribution[b] == exact, (a, b, distribution[b], exact)
            removed, added = a - b, b - a
            if not removed:
                formula = 1 - gamma * alpha * (1 - alpha)
            elif len(removed) == 1:
                formula = gamma * s[next(iter(removed))] * s[next(iter(added))]
            else:
                formula = F(0)
            assert exact == formula
            count += 1
    return count


def serial_distribution(distribution):
    return [{"set": sorted(a), "probability": str(value)}
            for a, value in sorted(distribution.items(), key=lambda item: tuple(sorted(item[0])))
            if value]


def verify_labeled_diamond(q, weights, base, u, v):
    base = frozenset(base)
    source = [base, base | {u}, base | {v}, base | {u, v}]
    marginals = [defaultdict(F) for _ in range(4)]
    outcomes = defaultdict(F)
    for p, value in weights.items():
        sets = [permuted(p, a) for a in source]
        assert sets[0] == sets[1] & sets[2]
        assert sets[3] == sets[1] | sets[2]
        outcomes[(tuple(sorted(sets[0])), p[u], p[v])] += value
        for table, target in zip(marginals, sets):
            table[target] += value
    for a, table in zip(source, marginals):
        for b in subsets(len(q), len(a)):
            assert table[b] == minor_probability(q, a, b)
    assert sum(outcomes.values()) == 1
    return {
        "base": sorted(base), "first_update": u, "second_update": v,
        "atoms": [{"bottom": list(a), "first_addition": i, "second_addition": j,
                   "probability": str(value)}
                  for (a, i, j), value in sorted(outcomes.items())],
        "marginals": [serial_distribution(table) for table in marginals],
    }


def permutation_record(weights):
    return [{"image": list(p), "probability": str(value)} for p, value in sorted(weights.items())]


def verify_obstruction():
    n = 5
    all_sets = subsets(n)
    eligible = []
    excluded = 0
    for p in permutations(range(n)):
        if all(len(permuted(p, a) - a) <= 1 for a in all_sets):
            eligible.append(p)
        else:
            excluded += 1
    assert len(eligible) == 1 + 10 + 20 == 31
    assert max(sum(p[i] != i for i in range(n)) for p in eligible) == 3
    required_expected_moved = F(4) * (1 - F(1, n))
    assert required_expected_moved == F(16, 5) > 3
    return {"dimension": n, "gamma": "4", "eligible_permutations": len(eligible),
            "excluded_permutations": excluded, "maximum_moved": 3,
            "required_expected_moved": str(required_expected_moved),
            "conclusion": "No common coordinate permutation realizes every projection law."}


def main():
    output_dir = Path(__file__).resolve().parent
    g = [1, 2, 3, 4, 5, 6]
    s = [F(x*x, 91) for x in g]
    gamma = F(3)
    q = unitary(g, (F(-3, 2), F(1, 2)))
    weights = iid_triple_weights(s, gamma)
    checks_six = verify_all_projection_laws(q, s, gamma, weights)
    assert checks_six == 924
    diamond = verify_labeled_diamond(q, weights, {0, 1, 2}, 3, 4)
    # Four sites reach the sharp flat-vector bound at the real reflection gamma=4.
    flat_q = unitary([1, 1, 1, 1], (F(-2), F(0)))
    flat_s = [F(1, 4)] * 4
    flat = flat_weights(4, F(4))
    checks_four = verify_all_projection_laws(flat_q, flat_s, F(4), flat)
    assert checks_four == 70
    flat_diamond = verify_labeled_diamond(flat_q, flat, {0}, 1, 2)
    obstruction = verify_obstruction()
    certificate = {
        "field": "Q(t), t^2=-3, conjugation t -> -t",
        "six_site": {
            "h": "(1,2,3,4,5,6)/sqrt(91)", "omega": "(-1+t)/2", "gamma": "3",
            "coordinate_masses": [str(x) for x in s],
            "permutation_weights": permutation_record(weights),
            "top_corank_one_labeled_diamond": diamond,
        },
        "four_site_flat_boundary": {
            "h": "(1,1,1,1)/2", "omega": "-1", "gamma": "4",
            "permutation_weights": permutation_record(flat),
            "top_corank_one_labeled_diamond": flat_diamond,
        },
        "five_site_obstruction": obstruction,
    }
    summary = {
        "status": "ALL EXACT CHECKS PASSED",
        "six_site_projection_probability_identities": checks_six,
        "six_site_permutation_atoms": len(weights),
        "six_site_top_corank_one_diamond_atoms": len(diamond["atoms"]),
        "four_site_projection_probability_identities": checks_four,
        "four_site_permutation_atoms": len(flat),
        "four_site_top_corank_one_diamond_atoms": len(flat_diamond["atoms"]),
        "unitarity": "exact for both displayed frames",
        "labeled_diamond_marginals": "all four checked separately in both examples",
        "obstruction": obstruction,
    }
    (output_dir / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    (output_dir / "verified_output.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
