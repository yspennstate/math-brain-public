#!/usr/bin/env python3
"""Finite deterministic certificate for HARD10-03 COUNTEREXAMPLE-L43.

The six vertices are the cycle C6, embedded in Z^3 as the boundary of a
2-by-1 lattice rectangle.  We apply the listed nearest-neighbor
transpositions chronologically, track labels, and certify that the final
permutation has the 2-cycle (0 3) even though the chronological strands of
labels 0 and 3 are never nearest-neighbors at any time.

This is a finite combinatorial certificate, not evidence for the full
infinite-volume conjecture.
"""

import json

C6_EDGES = {
    frozenset((0, 1)),
    frozenset((1, 2)),
    frozenset((2, 3)),
    frozenset((3, 4)),
    frozenset((4, 5)),
    frozenset((5, 0)),
}

RINGS = [
    (2, 3),
    (5, 0),
    (4, 5),
    (5, 0),
    (1, 2),
    (3, 4),
    (0, 1),
    (4, 5),
]

EXPECTED_FINAL_LABEL_TO_POSITION = (3, 2, 5, 0, 1, 4)


def label_position(pos_to_label, label):
    return pos_to_label.index(label)


def adjacent_positions(a, b):
    return frozenset((a, b)) in C6_EDGES


def cycles_of_permutation(p):
    seen = [False] * len(p)
    cycles = []
    for x in range(len(p)):
        if seen[x]:
            continue
        cyc = []
        y = x
        while not seen[y]:
            seen[y] = True
            cyc.append(y)
            y = p[y]
        cycles.append(tuple(cyc))
    return cycles


def main():
    for e in RINGS:
        assert frozenset(e) in C6_EDGES, f"non-edge transposition: {e}"

    pos_to_label = list(range(6))
    states = [tuple(pos_to_label)]
    contact_0_3 = [
        adjacent_positions(
            label_position(pos_to_label, 0),
            label_position(pos_to_label, 3),
        )
    ]

    for u, v in RINGS:
        pos_to_label[u], pos_to_label[v] = pos_to_label[v], pos_to_label[u]
        states.append(tuple(pos_to_label))
        contact_0_3.append(
            adjacent_positions(
                label_position(pos_to_label, 0),
                label_position(pos_to_label, 3),
            )
        )

    label_to_position = [None] * 6
    for position, label in enumerate(pos_to_label):
        label_to_position[label] = position
    label_to_position = tuple(label_to_position)

    assert label_to_position == EXPECTED_FINAL_LABEL_TO_POSITION
    cycles = cycles_of_permutation(label_to_position)
    assert any(set(c) == {0, 3} and len(c) == 2 for c in cycles)
    assert not any(contact_0_3), "labels 0 and 3 became adjacent"

    result = {
        "status": "PASS",
        "rings": RINGS,
        "states_position_to_label": states,
        "final_label_to_position": label_to_position,
        "cycles": cycles,
        "labels_0_3_adjacent_at_any_checked_state": any(contact_0_3),
        "note": (
            "Positions are constant between consecutive rings, so absence of "
            "adjacency in the initial state and every post-ring state certifies "
            "absence of adjacency throughout the deterministic time interval."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
