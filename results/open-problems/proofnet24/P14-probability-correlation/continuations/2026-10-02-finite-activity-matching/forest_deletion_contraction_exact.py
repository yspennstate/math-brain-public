"""Exact deletion/contraction obstruction and independent verification.

No floating point and no external packages are used.  The primary routine
enumerates acyclic edge subsets.  The independent routine enumerates vertex
partitions and uses the matrix-tree theorem on each component.
"""

from collections import Counter
from itertools import combinations, permutations, product
import json
from pathlib import Path


def forest_masks(n, edges):
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                u, v = root(u), root(v)
                if u == v:
                    break
                parent[u] = v
        else:
            yield mask


def triple_coefficients(n, edges, marked, weights=None):
    weights = weights or [1] * len(edges)
    coeffs = [0] * 8
    for mask in forest_masks(n, edges):
        key = sum(((mask >> i) & 1) << j for j, i in enumerate(marked))
        weight = 1
        for i, w in enumerate(weights):
            if i not in marked and mask & (1 << i):
                weight *= w
        coeffs[key] += weight
    return coeffs


def rayleigh_coefficients(coeffs):
    a00, a10, a01, a11, b00, b10, b01, b11 = coeffs
    return [
        a10 * a01 - a00 * a11,
        a10 * b01 + b10 * a01 - a00 * b11 - b00 * a11,
        b10 * b01 - b00 * b11,
    ]


def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for blocks in partitions(rest):
        yield [[first]] + blocks
        for j in range(len(blocks)):
            yield blocks[:j] + [[first] + blocks[j]] + blocks[j + 1:]


def determinant(matrix):
    n = len(matrix)
    value = 0
    for perm in permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = sign
        for i in range(n):
            term *= matrix[i][perm[i]]
        value += term
    return value


def partition_forest_polynomial(n, edges, weights):
    """Each forest is uniquely a vertex partition plus one tree per block."""
    total = 0
    for blocks in partitions(list(range(n))):
        term = 1
        for block in blocks:
            positions = {v: i for i, v in enumerate(block)}
            lap = [[0] * len(block) for _ in block]
            for (u, v), w in zip(edges, weights):
                if u in positions and v in positions:
                    i, j = positions[u], positions[v]
                    lap[i][i] += w
                    lap[j][j] += w
                    lap[i][j] -= w
                    lap[j][i] -= w
            term *= determinant([row[:-1] for row in lap[:-1]])
        total += term
    return total


def independent_triple_coefficients(n, edges, marked, weights=None):
    weights = list(weights or [1] * len(edges))
    evaluations = []
    for mask in range(8):
        local = weights[:]
        for j, i in enumerate(marked):
            local[i] = (mask >> j) & 1
        evaluations.append(partition_forest_polynomial(n, edges, local))
    return [
        sum((-1) ** ((mask.bit_count() - sub.bit_count())) * evaluations[sub]
            for sub in range(8) if sub & mask == sub)
        for mask in range(8)
    ]


def polynomial_add(left, right, sign=1):
    result = Counter(left)
    for monomial, coefficient in right.items():
        result[monomial] += sign * coefficient
    return {m: c for m, c in result.items() if c}


def polynomial_multiply(left, right):
    result = Counter()
    for a, x in left.items():
        for b, y in right.items():
            result[tuple(u + v for u, v in zip(a, b))] += x * y
    return dict(result)


def k4_symbolic_check():
    n = 4
    edges = list(combinations(range(n), 2))
    masks = list(forest_masks(n, edges))
    negative = []
    for e, f in combinations(range(len(edges)), 2):
        for g in range(len(edges)):
            if g in (e, f):
                continue
            others = [i for i in range(len(edges)) if i not in (e, f, g)]
            coeffs = [Counter() for _ in range(8)]
            for mask in masks:
                key = ((mask >> e) & 1) + 2 * ((mask >> f) & 1) + 4 * ((mask >> g) & 1)
                monomial = tuple((mask >> i) & 1 for i in others)
                coeffs[key][monomial] += 1
            a00, a10, a01, a11, b00, b10, b01, b11 = coeffs
            middle = polynomial_add(polynomial_multiply(a10, b01), polynomial_multiply(b10, a01))
            middle = polynomial_add(middle, polynomial_multiply(a00, b11), -1)
            middle = polynomial_add(middle, polynomial_multiply(b00, a11), -1)
            bad = {str(m): c for m, c in middle.items() if c < 0}
            if bad:
                negative.append({"marked": [e, f, g], "negative_monomials": bad})
    return {"cases": 60, "negative_cases": negative}


def main():
    k4_edges = list(combinations(range(4), 2))
    k4_marked = [k4_edges.index((0, 1)), k4_edges.index((2, 3)), k4_edges.index((0, 2))]
    k4_weights = [1, 1, 2, 2, 1, 1]
    k4_coeffs = triple_coefficients(4, k4_edges, k4_marked, k4_weights)
    k4_independent = independent_triple_coefficients(4, k4_edges, k4_marked, k4_weights)
    assert k4_coeffs == k4_independent == [18, 12, 12, 6, 14, 4, 4, 1]
    assert rayleigh_coefficients(k4_coeffs) == [36, -6, 2]

    n = 5
    edges = list(combinations(range(n), 2))
    marked = [edges.index((0, 2)), edges.index((1, 3)), edges.index((0, 1))]
    coeffs = triple_coefficients(n, edges, marked)
    independent = independent_triple_coefficients(n, edges, marked)
    assert coeffs == independent == [82, 46, 46, 24, 52, 18, 18, 5]
    rayleigh = rayleigh_coefficients(coeffs)
    assert rayleigh == [148, -2, 64]

    # Nontrivial positive integer activities on all seven other edges.
    weighted = [1, 1, 2, 3, 4, 1, 2, 3, 4, 2]
    weighted_coeffs = triple_coefficients(n, edges, marked, weighted)
    assert weighted_coeffs == independent_triple_coefficients(n, edges, marked, weighted)
    k4 = k4_symbolic_check()
    result = {
        "weighted_k4_witness": {
            "edges": k4_edges,
            "marked_edges_e_f_g": [k4_edges[i] for i in k4_marked],
            "weights": k4_weights,
            "coefficients": k4_coeffs,
            "independent_coefficients": k4_independent,
            "rayleigh_in_g": rayleigh_coefficients(k4_coeffs),
            "rayleigh_discriminant": -252,
        },
        "graph": "K5", "vertices": list(range(n)), "edges": edges,
        "marked_edges_e_f_g": [edges[i] for i in marked],
        "unweighted_coefficients": coeffs,
        "independent_coefficients": independent,
        "rayleigh_in_g": rayleigh,
        "rayleigh_discriminant": rayleigh[1] ** 2 - 4 * rayleigh[0] * rayleigh[2],
        "nontrivial_weights": weighted,
        "nontrivial_weight_coefficients": weighted_coeffs,
        "nontrivial_weight_rayleigh": rayleigh_coefficients(weighted_coeffs),
        "k4_symbolic_middle_check": k4,
    }
    destination = Path(__file__).with_name("forest_deletion_contraction_exact_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
