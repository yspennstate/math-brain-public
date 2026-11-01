#!/usr/bin/env python3
"""Exact exhaustive certificate for HARD10-01, n=6.

Standard library only.

For every labelled simple graph on six vertices and every pair of disjoint
present distinguished edges e,f, classify the five-class R family after
deleting e,f.  Among pairs with exactly two R forests, verify:

  * comparable and incomparable case counts;
  * every incomparable pair has opposite terminal-pairing type;
  * every incomparable pair has symmetric difference of exactly four edges;
  * every 3-vertex-connected incomparable case is exactly K4 on its
    non-isolated support (the remaining vertices are isolated).

The calculation is a finite adversarial check.  It is not a proof of the
universal theorem; the proofs are in the corresponding Markdown report.
"""

from itertools import combinations
from collections import Counter

NVERT = 6
EDGES = list(combinations(range(NVERT), 2))
M = len(EDGES)                  # 15
NMASK = 1 << M                  # 32768


def precompute_forests_and_components():
    forest = [False] * NMASK
    comps = [None] * NMASK

    for mask in range(NMASK):
        parent = list(range(NVERT))
        rank = [0] * NVERT

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        for i, (u, v) in enumerate(EDGES):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                if rank[ru] < rank[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                if rank[ru] == rank[rv]:
                    rank[ru] += 1

        if not ok:
            continue

        forest[mask] = True
        roots = [find(v) for v in range(NVERT)]
        renumber = {}
        labels = []
        for r in roots:
            if r not in renumber:
                renumber[r] = len(renumber)
            labels.append(renumber[r])
        comps[mask] = tuple(labels)

    return forest, comps


def is_R(mask, e, f, forest, comps):
    if not forest[mask]:
        return None
    cc = comps[mask]
    a, b = e
    c, d = f
    if cc[a] == cc[b] or cc[c] == cc[d]:
        return None
    if {cc[a], cc[b]} != {cc[c], cc[d]}:
        return None
    # Two cross-pairing types.
    return 0 if cc[a] == cc[c] else 1


def list_R_submasks(Hmask, e, f, forest, comps):
    out = []
    sub = Hmask
    while True:
        typ = is_R(sub, e, f, forest, comps)
        if typ is not None:
            out.append((sub, typ))
        if sub == 0:
            break
        sub = (sub - 1) & Hmask
    return out


def support_graph(mask):
    vertices = set()
    edge_list = []
    for i, (u, v) in enumerate(EDGES):
        if (mask >> i) & 1:
            vertices.add(u)
            vertices.add(v)
            edge_list.append((u, v))
    return sorted(vertices), edge_list


def connected_after_deleting(vertices, edge_list, deleted):
    live = [v for v in vertices if v not in deleted]
    if len(live) <= 1:
        return True
    adj = {v: [] for v in live}
    live_set = set(live)
    for u, v in edge_list:
        if u in live_set and v in live_set:
            adj[u].append(v)
            adj[v].append(u)
    seen = {live[0]}
    stack = [live[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(live)


def vertex_connectivity_class(mask):
    """Return 0,1,2,or >=3 for the non-isolated support graph."""
    vertices, edge_list = support_graph(mask)
    if not vertices or not connected_after_deleting(vertices, edge_list, set()):
        return 0
    for v in vertices:
        if not connected_after_deleting(vertices, edge_list, {v}):
            return 1
    for u, v in combinations(vertices, 2):
        if not connected_after_deleting(vertices, edge_list, {u, v}):
            return 2
    return 3


def is_K4_on_support(mask):
    vertices, edge_list = support_graph(mask)
    return len(vertices) == 4 and len(edge_list) == 6


def main():
    forest, comps = precompute_forests_and_components()

    distinguished_pairs = [
        (i, j, EDGES[i], EDGES[j])
        for i in range(M)
        for j in range(i + 1, M)
        if set(EDGES[i]).isdisjoint(EDGES[j])
    ]
    assert len(distinguished_pairs) == 45

    stats = Counter()

    for ie, jf, e, f in distinguished_pairs:
        banned = (1 << ie) | (1 << jf)

        # Indicator of R on all edge subsets not using e or f.
        r_indicator = [0] * NMASK
        for mask in range(NMASK):
            if mask & banned:
                continue
            if is_R(mask, e, f, forest, comps) is not None:
                r_indicator[mask] = 1

        # Subset-zeta transform: z[H] = number of R subsets of H.
        z = r_indicator[:]
        for bit in range(M):
            step = 1 << bit
            for mask in range(NMASK):
                if mask & step:
                    z[mask] += z[mask ^ step]

        # Scan every graph containing the distinguished edges.
        for Gmask in range(NMASK):
            if (Gmask & banned) != banned:
                continue
            Hmask = Gmask & ~banned
            if z[Hmask] != 2:
                continue

            rsets = list_R_submasks(Hmask, e, f, forest, comps)
            assert len(rsets) == 2
            (P, ptype), (Q, qtype) = rsets

            comparable = (P & ~Q) == 0 or (Q & ~P) == 0
            if comparable:
                stats["comparable"] += 1
                continue

            stats["incomparable"] += 1
            assert ptype != qtype, (
                "same-pairing incomparable counterexample",
                Gmask, e, f, rsets,
            )
            stats["opposite_pairing"] += 1

            diff_size = (P ^ Q).bit_count()
            assert diff_size == 4, (
                "symmetric difference not four edges",
                Gmask, e, f, rsets, diff_size,
            )
            stats["diff4"] += 1

            kappa = vertex_connectivity_class(Gmask)
            stats[f"connectivity_{kappa}"] += 1
            if kappa >= 3:
                assert is_K4_on_support(Gmask), (
                    "3-connected exact-two case not K4 on support",
                    Gmask, e, f, rsets,
                )
                stats["3conn_is_K4"] += 1

    expected = {
        "comparable": 16830,
        "incomparable": 4725,
        "opposite_pairing": 4725,
        "diff4": 4725,
        "connectivity_2": 4680,
        "connectivity_3": 45,
        "3conn_is_K4": 45,
    }
    for key, value in expected.items():
        assert stats[key] == value, (key, stats[key], value)

    print("EXACT n=6 HARD10-01 TWO-R CERTIFICATE")
    for key in (
        "comparable",
        "incomparable",
        "opposite_pairing",
        "diff4",
        "connectivity_2",
        "connectivity_3",
        "3conn_is_K4",
    ):
        print(f"{key}: {stats[key]}")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
