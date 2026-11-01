#!/usr/bin/env python3
"""Exact integer verifier for the HARD8-02 q=2 endpoint-rooted P3 absorber.

The theorem checked is:
    for every k>=0, c=2k+3 admits a suffix-root cutoff-k absorber.

The universal proof is symbolic in the accompanying report.  This script only
checks the closed form on the finite range h=1,...,2000 with h=k+1.

No floating point, randomness, external solver, or timeout inference is used.
"""


def construct_q2(h: int):
    assert h >= 1

    # Exceptional small parameter h=1 (k=0,c=3).
    if h == 1:
        # (root, middle, leaf)
        return [(8, 2, 0), (6, 1, 5), (7, 4, 3)]

    c = 2 * h + 1
    pi = [(2 * i) % c for i in range(c)]

    mids = [None] * c
    leaves = [None] * c
    root_index = [None] * c

    # Pair low i with high c+pi(i), reversing only i=h,h+1.
    for i in range(c):
        high = c + pi[i]
        if i in (h, h + 1):
            mids[i], leaves[i] = high, i
        else:
            mids[i], leaves[i] = i, high

    # Special reversed path i=h realizes root-edge difference h.
    root_index[h] = h - 1

    # Extra reversed path i=h+1 realizes root-edge difference 3h+2.
    root_index[h + 1] = h + 2

    # Ordinary paths are indexed by their base signed shifts.
    shift = {}
    for i in range(c):
        if i in (h, h + 1):
            continue
        d = i if i <= h - 1 else i - c
        shift[i] = d

    # For h=2 the base root-index omissions are already exactly the two
    # reserved root indices, so no trade is needed.
    if h >= 3:
        if h % 2 == 0:
            r = h // 2
            trade = {
                -(r + 1): r,
                +(r + 1): -r,
                -r: -(r + 1),
                +r: +(r + 1),
            }
        else:
            r = (h - 1) // 2
            trade = {
                -r: -(r + 1),
                +r: +(r + 1),
                -(r + 1): +r,
                +(r + 1): -r,
            }

        for old_d, new_d in trade.items():
            i = old_d if old_d >= 0 else c + old_d
            assert shift[i] == old_d
            shift[i] = new_d

    for i, d_new in shift.items():
        root_index[i] = mids[i] + d_new
        assert 0 <= root_index[i] <= 2 * h

    triples = []
    for i in range(c):
        assert root_index[i] is not None
        triples.append((2 * c + root_index[i], mids[i], leaves[i]))

    return triples


def verify_one(h: int):
    c = 2 * h + 1
    k = h - 1
    triples = construct_q2(h)

    labels = []
    roots = []
    edges = []
    leaf_edges = []
    root_edges = []

    for root, middle, leaf in triples:
        labels.extend((root, middle, leaf))
        roots.append(root)

        d_leaf = abs(middle - leaf)
        d_root = abs(root - middle)

        leaf_edges.append(d_leaf)
        root_edges.append(d_root)
        edges.extend((d_leaf, d_root))

    assert len(labels) == 3 * c
    assert len(set(labels)) == 3 * c
    assert set(labels) == set(range(3 * c))

    assert len(roots) == c
    assert len(set(roots)) == c
    assert set(roots) == set(range(2 * c, 3 * c))

    assert len(edges) == 2 * c
    assert len(set(edges)) == 2 * c
    assert set(edges) == set(range(k + 1, k + 2 * c + 1))

    if h >= 2:
        assert set(leaf_edges) == set(range(h + 1, 3 * h + 2))
        assert set(root_edges) == ({h} | set(range(3 * h + 2, 5 * h + 2)))

    return len(triples), len(edges)


def main():
    total_paths = 0
    total_edge_differences = 0

    for h in range(1, 2001):
        paths, edge_differences = verify_one(h)
        total_paths += paths
        total_edge_differences += edge_differences

    print("Q2_ABSORBERS_VERIFIED", 2000)
    print("TOTAL_PATHS_CHECKED", total_paths)
    print("TOTAL_EDGE_DIFFERENCES_CHECKED", total_edge_differences)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
