#!/usr/bin/env python3
"""Exact finite sanity audit for the depth-3 collision classification.

This is NOT the proof of the universal theorem.  The universal classification
is proved in the accompanying immutable report by positivity and subset
containment.  This script exactly checks the induced subset-sum partitions for
all integer weights (1,a,b) in a large finite box, using integer arithmetic.
"""

from itertools import product

N = 200

TYPES = (
    "A_no_collision_k8",
    "B_one_sum_relation_k7",
    "C_one_equality_k6",
    "D_equal_plus_sum_k5",
    "E_all_equal_k4",
)

EXPECTED_K = {
    "A_no_collision_k8": 8,
    "B_one_sum_relation_k7": 7,
    "C_one_equality_k6": 6,
    "D_equal_plus_sum_k5": 5,
    "E_all_equal_k4": 4,
}


def support_size(a: int, b: int) -> int:
    weights = (1, a, b)
    values = set()
    for mask in range(8):
        values.add(sum(weights[i] for i in range(3) if (mask >> i) & 1))
    return len(values)


def theorem_type(a: int, b: int) -> str:
    x, y, z = 1, a, b
    if x == y == z:
        return "E_all_equal_k4"
    equality_pairs = int(x == y) + int(x == z) + int(y == z)
    sum_relations = int(x == y + z) + int(y == x + z) + int(z == x + y)
    if equality_pairs and sum_relations:
        return "D_equal_plus_sum_k5"
    if equality_pairs:
        return "C_one_equality_k6"
    if sum_relations:
        return "B_one_sum_relation_k7"
    return "A_no_collision_k8"


def main() -> None:
    counts = {t: 0 for t in TYPES}
    mismatches = []
    for a, b in product(range(1, N + 1), repeat=2):
        kind = theorem_type(a, b)
        counts[kind] += 1
        k = support_size(a, b)
        if k != EXPECTED_K[kind]:
            mismatches.append((a, b, kind, k))
            break

    print("NEUNHAEUSERER depth-3 collision audit")
    print(f"range: weights (1,a,b), 1 <= a,b <= {N}")
    print(f"triples checked: {N*N}")
    for kind in TYPES:
        print(f"{kind}: {counts[kind]}")
    print(f"classification mismatches: {len(mismatches)}")
    if mismatches:
        print("FAIL", mismatches[0])
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
