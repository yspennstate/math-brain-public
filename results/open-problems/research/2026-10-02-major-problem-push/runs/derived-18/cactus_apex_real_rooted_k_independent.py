"""Independent exact audit checks for the cactus-apex DR theorem.

This program does not import the author checker.  It combines literal forest
enumeration, exact rational polynomial algebra, Sturm/gcd root counts, an
abstract Schur-complement test, and direct two-marked-edge enumeration.
"""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations, product
from math import gcd
from pathlib import Path
from random import Random
import json


SEED = 10032026
OUT = Path(__file__).with_name("cactus_apex_real_rooted_k_independent_results.json")


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b, scale=Q(1)):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += scale * x
    return trim(out)


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def canonical(labels):
    names = {}
    return tuple(names.setdefault(x, len(names)) for x in labels)


def merge(partition, u, v):
    if partition[u] == partition[v]:
        return None
    a, b = partition[u], partition[v]
    return canonical(a if x == b else x for x in partition)


def forest_states(n, edges):
    states = {tuple(range(n)): Q(1)}
    for u, v, w in edges:
        following = defaultdict(Q)
        for partition, weight in states.items():
            following[partition] += weight
            joined = merge(partition, u, v)
            if joined is not None:
                following[joined] += w * weight
        states = dict(following)
    return states


def apex(n, edges, beta):
    answer = [Q(0)]
    for partition, weight in forest_states(n, edges).items():
        masses = defaultdict(Q)
        for x, value in enumerate(beta):
            masses[partition[x]] += value
        term = [Q(1)]
        for mass in masses.values():
            if mass:
                term = mul(term, [Q(1), mass])
        answer = add(answer, [weight * x for x in term])
    return answer


def apex_pointed(n, edges, beta, u):
    """Return D and partial D/partial z_u after z_x=s beta_x substitution."""
    d, e = [Q(0)], [Q(0)]
    for partition, weight in forest_states(n, edges).items():
        masses = defaultdict(Q)
        for x, value in enumerate(beta):
            masses[partition[x]] += value
        ulabel = partition[u]
        rest = [Q(1)]
        for label, mass in masses.items():
            if label != ulabel and mass:
                rest = mul(rest, [Q(1), mass])
        d = add(d, [weight * x for x in mul(rest, [Q(1), masses[ulabel]])])
        e = add(e, [weight * x for x in rest])
    return d, e


def derivative(p):
    return [Q(i) * p[i] for i in range(1, len(p))] or [Q(0)]


def remainder(a, b):
    a, b = trim(a), trim(b)
    while any(a) and len(a) >= len(b):
        shift, factor = len(a) - len(b), a[-1] / b[-1]
        for i, value in enumerate(b):
            a[shift + i] -= factor * value
        a = trim(a)
    return a


def pgcd(a, b):
    while any(b):
        a, b = b, remainder(a, b)
    return [x / a[-1] for x in a] if any(a) else [Q(0)]


def variations(signs):
    signs = [x for x in signs if x]
    return sum(x != y for x, y in zip(signs, signs[1:]))


def distinct_negative_roots(p):
    sequence = [trim(p), trim(derivative(p))]
    while len(sequence[-1]) > 1:
        r = [-x for x in remainder(sequence[-2], sequence[-1])]
        if not any(r):
            break
        sequence.append(trim(r))
    minus_infinity, zero = [], []
    for row in sequence:
        lead = 1 if row[-1] > 0 else -1
        minus_infinity.append(lead * (-1 if (len(row) - 1) % 2 else 1))
        zero.append(1 if row[0] > 0 else -1 if row[0] < 0 else 0)
    return variations(minus_infinity) - variations(zero)


def negative_roots_with_multiplicity(p):
    total, layer = 0, trim(p)
    while len(layer) > 1:
        total += distinct_negative_roots(layer)
        layer = pgcd(layer, derivative(layer))
        if len(layer) == 1:
            break
    return total


def determinant_polynomial(matrix):
    n, answer = len(matrix), [Q(0)]
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = [Q(-1 if inversions % 2 else 1)]
        for i, j in enumerate(perm):
            term = mul(term, matrix[i][j])
        answer = add(answer, term)
    return answer


def pencil(vectors, profiles):
    d = len(vectors[0])
    matrix = []
    for i in range(d):
        row = []
        for j in range(d):
            coefficient = sum(b * q[i] * q[j] for q, b in zip(vectors, profiles))
            row.append([Q(i == j), coefficient])
        matrix.append(row)
    return matrix


def minor(matrix, index):
    return [[entry for j, entry in enumerate(row) if j != index]
            for i, row in enumerate(matrix) if i != index]


def exact_schur_cases(rng, count=12):
    records = []
    for trial in range(count):
        d1, d2 = 3, 2
        common1, common2 = [Q(1), Q(0), Q(0)], [Q(1), Q(0)]
        q1 = [common1, [Q(1), Q(1), Q(0)], [Q(2), Q(0), Q(1)], [Q(0), Q(1), Q(1)]]
        q2 = [common2, [Q(1), Q(2)], [Q(0), Q(1)]]
        total = Q(rng.randrange(1, 6), rng.randrange(1, 5))
        split = Q(rng.randrange(0, 6), 5) * total
        b1 = [split] + [Q(rng.randrange(1, 6), rng.randrange(1, 4)) for _ in q1[1:]]
        b2 = [total - split] + [Q(rng.randrange(1, 6), rng.randrange(1, 4)) for _ in q2[1:]]
        a1, a2 = pencil(q1, b1), pencil(q2, b2)
        dpoly1, dpoly2 = determinant_polynomial(a1), determinant_polynomial(a2)
        epoly1, epoly2 = determinant_polynomial(minor(a1, 0)), determinant_polynomial(minor(a2, 0))

        embedded = [[Q(1), Q(0), Q(0), Q(0)]]
        profiles = [total]
        for q, b in zip(q1[1:], b1[1:]):
            embedded.append([q[0], q[1], q[2], Q(0)]); profiles.append(b)
        for q, b in zip(q2[1:], b2[1:]):
            embedded.append([q[0], Q(0), Q(0), q[1]]); profiles.append(b)
        observed = determinant_polynomial(pencil(embedded, profiles))
        predicted = add(add(mul(dpoly1, epoly2), mul(epoly1, dpoly2)), mul(epoly1, epoly2), Q(-1))
        assert observed == predicted
        records.append({"trial": trial, "shared_profile": str(total), "side_1_share": str(split),
                        "coefficients_ascending": list(map(str, observed))})
    return records


def solve(matrix, rhs):
    augmented = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    n = len(matrix)
    for col in range(n):
        pivot = next(i for i in range(col, n) if augmented[i][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        value = augmented[col][col]
        augmented[col] = [x / value for x in augmented[col]]
        for i in range(n):
            if i != col and augmented[i][col]:
                value = augmented[i][col]
                augmented[i] = [x - value * y for x, y in zip(augmented[i], augmented[col])]
    return [row[-1] for row in augmented]


def normalization_cases(rng, count=20):
    records = []
    ks = [Q(1, 3), Q(2, 5), Q(3, 5)]
    for trial in range(count):
        k = rng.choice(ks)
        K, vectors = [[Q(1)]], [[Q(1)]]
        for _ in range(1 + trial % 5):
            parent = rng.randrange(len(vectors))
            w = k * k / (1 - k * k)
            d = len(K)
            K = [row + [Q(0)] for row in K] + [[Q(0)] * d + [1 + w]]
            old_vectors = vectors
            vectors = [q + [Q(0)] for q in old_vectors]
            vectors.append([k * x for x in old_vectors[parent]] + [Q(1)])
        values = []
        for q in vectors:
            x = solve(K, q)
            values.append(sum(a * b for a, b in zip(q, x)))
        assert all(x == 1 for x in values)
        records.append({"trial": trial, "dimension": len(K), "normalizations": list(map(str, values))})
    return records


def one_sum_literal_cases(count=12):
    records = []
    for trial in range(count):
        e1 = [(0, 1, Q(1 + trial % 3)), (1, 2, Q(2)), (2, 0, Q(3))]
        e2 = [(0, 1, Q(2)), (1, 2, Q(1 + trial % 2)), (2, 0, Q(4))]
        final_shared = Q(3 + trial % 4, 2)
        split = Q(trial % 5, 5) * final_shared
        b1 = [split, Q(2), Q(3)]
        b2 = [final_shared - split, Q(1), Q(2 + trial % 3)]
        d1, f1 = apex_pointed(3, e1, b1, 0)
        d2, f2 = apex_pointed(3, e2, b2, 0)
        joined = e1 + [(0, 3, w) if (u, v) == (0, 1) else
                       (3, 4, w) if (u, v) == (1, 2) else (4, 0, w)
                       for u, v, w in e2]
        observed = apex(5, joined, [final_shared, b1[1], b1[2], b2[1], b2[2]])
        predicted = add(add(mul(d1, f2), mul(f1, d2)), mul(f1, f2), Q(-1))
        assert observed == predicted
        records.append({"trial": trial, "shared_profile": str(final_shared),
                        "side_1_share": str(split), "coefficients_ascending": list(map(str, observed))})
    return records


def direct_marked(n, edges, beta, rows, condition=None):
    condition = condition or [-1] * len(edges)
    state, factor, optional = tuple(range(n + 4)), Q(1), []
    for (u, v, w), status in zip(edges, condition):
        if status == 0:
            continue
        if status == 1:
            joined = merge(state, u, v)
            if joined is None or w == 0:
                return None
            state, factor = joined, factor * w
        else:
            optional.append((u, v, w))
    optional += [(n + r, x, rows[r] * beta[x]) for r in range(4) for x in range(n)
                 if rows[r] * beta[x]]
    states = {state: factor}
    for u, v, w in optional:
        following = defaultdict(Q)
        for partition, weight in states.items():
            following[partition] += weight
            joined = merge(partition, u, v)
            if joined is not None:
                following[joined] += w * weight
        states = dict(following)
    coefficients = [Q(0)] * 4
    for partition, weight in states.items():
        for mask in range(4):
            target = partition
            if mask & 1:
                target = merge(target, n, n + 1)
            if target is not None and mask & 2:
                target = merge(target, n + 2, n + 3)
            if target is not None:
                coefficients[mask] += weight
    return coefficients


def contracted_profile_rank(n, edges, beta, condition):
    partition = tuple(range(n))
    for (u, v, w), status in zip(edges, condition):
        if status == 1:
            if w == 0:
                return None
            partition = merge(partition, u, v)
            if partition is None:
                return None
    masses = defaultdict(Q)
    for x, value in enumerate(beta):
        masses[partition[x]] += value
    return sum(value > 0 for value in masses.values())


def main():
    rng = Random(SEED)
    normalizations = normalization_cases(rng)
    schur = exact_schur_cases(rng)
    gluing = one_sum_literal_cases()

    templates = [
        (5, [(0, 1, Q(1)), (1, 2, Q(2)), (2, 0, Q(3)),
             (0, 3, Q(2)), (3, 4, Q(1)), (4, 0, Q(4))]),
        (7, [(0, 1, Q(2)), (1, 2, Q(1)), (2, 0, Q(3)), (2, 3, Q(5, 2)),
             (3, 4, Q(1)), (4, 5, Q(2)), (5, 3, Q(3)), (5, 6, Q(4, 3))]),
        (8, [(0, 1, Q(1)), (1, 2, Q(2)), (2, 0, Q(1)), (0, 3, Q(3)),
             (3, 4, Q(2)), (4, 5, Q(1)), (5, 3, Q(2)),
             (4, 6, Q(1)), (6, 7, Q(3)), (7, 4, Q(2))]),
    ]
    cactus_records = []
    for case in range(12):
        n, edges = templates[case % len(templates)]
        beta = [Q(rng.randrange(0, 6), rng.randrange(1, 5)) for _ in range(n)]
        if not any(beta):
            beta[0] = Q(1)
        polynomial = apex(n, edges, beta)
        degree = sum(x > 0 for x in beta)
        roots = negative_roots_with_multiplicity(polynomial)
        assert len(polynomial) - 1 == degree == roots
        cactus_records.append({"case": case, "vertices": n, "degree": degree,
                               "negative_roots_counting_multiplicity": roots,
                               "coefficients_ascending": list(map(str, polynomial))})

    n, figure_eight = templates[0]
    rows = [Q(1, 2), Q(2, 3), Q(3, 4), Q(4, 5)]
    beta = [Q(1), Q(0), Q(0), Q(2), Q(0)]
    marked = direct_marked(n, figure_eight, beta, rows)
    rayleigh = marked[1] * marked[2] - marked[0] * marked[3]
    assert rayleigh > 0

    # Exhaust all 3^4 cylinder states on two parallel-edge 2-cycles sharing
    # their articulation.  Forced parallel pairs are zero-probability cycles.
    small_edges = [(0, 1, Q(2)), (0, 1, Q(3)), (0, 2, Q(5)), (0, 2, Q(7))]
    small_beta = [Q(1), Q(0), Q(2)]
    checked = strict = equality = skipped = 0
    for condition in product((-1, 0, 1), repeat=4):
        rank = contracted_profile_rank(3, small_edges, small_beta, condition)
        values = direct_marked(3, small_edges, small_beta, rows, condition)
        if rank is None or values is None:
            skipped += 1
            continue
        value = values[1] * values[2] - values[0] * values[3]
        expected = rank >= 2
        assert value >= 0 and (value > 0) == expected
        checked += 1; strict += expected; equality += not expected

    report = {
        "status": "PASS; finite exact independent audit, analytic proof in separate audit",
        "arithmetic": "fractions, literal forest partitions, exact determinant permutations, exact Sturm/gcd",
        "seed": SEED,
        "normalization_cases": normalizations,
        "abstract_schur_one_sum_cases": schur,
        "literal_one_sum_cases": gluing,
        "genuine_multicycle_cactus_cases": cactus_records,
        "figure_eight_marked_case": {"coefficients_A_E_G_C": list(map(str, marked)),
                                      "Rayleigh": str(rayleigh), "strict": True},
        "conditioning_case": {"graph": "two parallel-edge 2-cycles sharing one vertex",
                              "positive_probability": checked, "strict": strict,
                              "equality": equality, "zero_probability_skipped": skipped},
        "summary": {"normalization_cases": len(normalizations),
                    "abstract_schur_one_sum_cases": len(schur),
                    "literal_one_sum_cases": len(gluing),
                    "genuine_multicycle_cactus_root_cases": len(cactus_records),
                    "marked_cases": 1, "positive_probability_conditionings": checked,
                    "conditioning_strict": strict, "conditioning_equality": equality,
                    "skipped_zero_probability": skipped, "counterexamples": 0},
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
