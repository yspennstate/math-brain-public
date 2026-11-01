"""Independent exact all-vertex audit for the disjoint-pair theorem.

This checker does not import the author transfer implementation.  It retains
all backbone and attachment vertices, processes every ordinary edge by a
skip/join connectivity-partition update, and inserts the two marked edges
literally in all four subsets.  Arithmetic is fractions.Fraction throughout.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from random import Random
import json


OUT = Path(__file__).with_name(
    "forest_disjoint_rank_one_attachment_forest_backbone_k_independent_results.json"
)
SEED = 20261003


def canonical(labels):
    names = {}
    return tuple(names.setdefault(label, len(names)) for label in labels)


def join(state, u, v):
    """Join two blocks, or return None when the edge would make a cycle."""
    if state[u] == state[v]:
        return None
    left, right = state[u], state[v]
    return canonical(tuple(left if label == right else label for label in state))


def direct_coefficients(n, backbone, profile, columns, status):
    """Return A,E,F,C after a partial coordinate conditioning of backbone."""
    state = tuple(range(n + 4))
    fixed_mass = F(1)
    optional = []
    for (u, v, weight), value in zip(backbone, status):
        if value == 0:
            continue
        if value == 1:
            state = join(state, u, v)
            assert state is not None  # the supplied backbone is a forest
            fixed_mass *= weight
        else:
            optional.append((u, v, weight))

    unmarked = optional + [
        (n + i, j, columns[i] * profile[j])
        for i in range(4)
        for j in range(n)
        if columns[i] * profile[j]
    ]
    frontier = {state: fixed_mass}
    for u, v, weight in unmarked:
        following = defaultdict(F)
        for partition, mass in frontier.items():
            following[partition] += mass
            target = join(partition, u, v)
            if target is not None:
                following[target] += mass * weight
        frontier = dict(following)

    coefficients = [F(0)] * 4
    for partition, mass in frontier.items():
        for marked in range(4):
            target = partition
            if marked & 1:
                target = join(target, n, n + 1)
            if target is not None and marked & 2:
                target = join(target, n + 2, n + 3)
            if target is not None:
                coefficients[marked] += mass
    return coefficients


def is_forest(n, edges):
    parent = list(range(n))

    def root(vertex):
        while parent[vertex] != vertex:
            vertex = parent[vertex]
        return vertex

    for u, v, _ in edges:
        u, v = root(u), root(v)
        if u == v:
            return False
        parent[u] = v
    return True


def positive_contracted_profiles(n, backbone, profile, status):
    parent = list(range(n))

    def root(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for (u, v, _), value in zip(backbone, status):
        if value == 1:
            u, v = root(u), root(v)
            parent[u] = v
    sums = defaultdict(F)
    for vertex, value in enumerate(profile):
        sums[root(vertex)] += value
    return sum(value > 0 for value in sums.values())


def check_case(n, backbone, profile, columns, status):
    coefficients = direct_coefficients(n, backbone, profile, columns, status)
    A, E, G, C = coefficients
    rayleigh = E * G - A * C
    rank = positive_contracted_profiles(n, backbone, profile, status)
    expected_strict = bool(all(columns) and rank >= 2)
    assert rayleigh >= 0
    assert (rayleigh > 0) == expected_strict
    return rayleigh, expected_strict


def exhaustive():
    checked = strict = equality = 0
    minimum_positive = None
    by_vertices = {}
    for n in range(1, 4):
        vertex_checked = 0
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            backbone = [
                (u, v, F(2 + u + 2 * v))
                for i, (u, v) in enumerate(pairs)
                if mask >> i & 1
            ]
            if not is_forest(n, backbone):
                continue
            for profile in product(range(3), repeat=n):
                for columns in product(range(2), repeat=4):
                    for status in product((-1, 0, 1), repeat=len(backbone)):
                        rayleigh, is_strict = check_case(
                            n, backbone, profile, columns, status
                        )
                        checked += 1
                        vertex_checked += 1
                        strict += is_strict
                        equality += not is_strict
                        if rayleigh > 0:
                            minimum_positive = (
                                rayleigh
                                if minimum_positive is None
                                else min(minimum_positive, rayleigh)
                            )
        by_vertices[str(n)] = vertex_checked
    return {
        "cases": checked,
        "strict_cases": strict,
        "equality_cases": equality,
        "cases_by_backbone_vertices": by_vertices,
        "smallest_positive_Rayleigh": str(minimum_positive),
        "counterexamples": 0,
    }


def random_rational(trials=1200):
    rng = Random(SEED)

    def fraction(maximum=7):
        return F(rng.randrange(maximum), rng.randrange(1, maximum))

    minimum_positive = None
    strict = equality = 0
    by_vertices = defaultdict(int)
    for _ in range(trials):
        n = rng.randrange(1, 6)
        backbone = []
        # Each accepted edge joins a new vertex to an earlier one, hence this
        # constructs a labeled forest without calling is_forest.
        for vertex in range(1, n):
            if rng.random() < 0.75:
                backbone.append(
                    (
                        vertex,
                        rng.randrange(vertex),
                        fraction() + F(1, 7),
                    )
                )
        profile = [fraction() for _ in range(n)]
        columns = [fraction() for _ in range(4)]
        status = [rng.choice((-1, 0, 1)) for _ in backbone]
        rayleigh, is_strict = check_case(
            n, backbone, profile, columns, status
        )
        strict += is_strict
        equality += not is_strict
        by_vertices[str(n)] += 1
        if rayleigh > 0:
            minimum_positive = (
                rayleigh
                if minimum_positive is None
                else min(minimum_positive, rayleigh)
            )
    return {
        "seed": SEED,
        "cases": trials,
        "strict_cases": strict,
        "equality_cases": equality,
        "cases_by_backbone_vertices": dict(sorted(by_vertices.items())),
        "smallest_positive_Rayleigh": str(minimum_positive),
        "counterexamples": 0,
    }


def main():
    report = {
        "status": "PASS; finite exact audit, not the universal proof",
        "arithmetic": "fractions.Fraction only",
        "implementation": (
            "all original vertices retained; independent connectivity-"
            "partition skip/join DP; no author-checker imports"
        ),
        "exhaustive": exhaustive(),
        "seeded_random_rational": random_rational(),
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2), flush=True)


if __name__ == "__main__":
    main()
