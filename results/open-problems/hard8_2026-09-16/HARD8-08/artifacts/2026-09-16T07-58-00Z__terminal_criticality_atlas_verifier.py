#!/usr/bin/env python3
"""Exact finite sanity checks for HARD8-08 terminal-criticality lemmas.

Requires networkx only for graph_atlas_g(), which is an exhaustive list of
unlabeled simple graphs on at most 7 vertices. All colorability/color-relation
checks below are deterministic exhaustive backtracking.
"""
from itertools import combinations
import networkx as nx


def clique_number(G):
    V = list(G.nodes())
    best = 0
    for r in range(1, len(V) + 1):
        found = False
        for S in combinations(V, r):
            if all(G.has_edge(a, b) for a, b in combinations(S, 2)):
                best = r
                found = True
                break
        if not found:
            break
    return best


def colorings(G, k):
    V = list(G.nodes())
    order = sorted(V, key=lambda v: (-G.degree(v), v))
    col = {}
    out = []

    def rec(i):
        if i == len(order):
            out.append(tuple(col[v] for v in V))
            return
        v = order[i]
        used = {col[u] for u in G.neighbors(v) if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                rec(i + 1)
                del col[v]

    rec(0)
    return V, out


def k_colorable(G, k):
    order = sorted(G.nodes(), key=lambda v: (-G.degree(v), v))
    col = {}

    def rec(i):
        if i == len(order):
            return True
        v = order[i]
        used = {col[u] for u in G.neighbors(v) if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                if rec(i + 1):
                    return True
                del col[v]
        return False

    return rec(0)


def chromatic_number(G):
    for k in range(1, len(G) + 1):
        if k_colorable(G, k):
            return k
    raise AssertionError


def forced_equal_pairs(G, k):
    V, cols = colorings(G, k)
    if not cols:
        return []
    ans = []
    for i, u in enumerate(V):
        for j in range(i + 1, len(V)):
            v = V[j]
            if G.has_edge(u, v):
                continue
            if all(c[i] == c[j] for c in cols):
                ans.append((u, v))
    return ans


def deletion_remains_k_chromatic(G, v, k):
    H = G.copy()
    H.remove_node(v)
    return not k_colorable(H, k - 1)


def common_neighbors(G, u, v):
    return set(G.neighbors(u)).intersection(G.neighbors(v))


def main():
    atlas = nx.graph_atlas_g()

    # Universal finite sanity check of the theorem on the whole atlas:
    # every forced-equal terminal of a k-colorable graph has deletion that remains k-chromatic.
    checked_pairs = 0
    for G in atlas:
        if len(G) < 2:
            continue
        for k in range(2, min(5, len(G) + 1)):
            if not k_colorable(G, k):
                continue
            for u, v in forced_equal_pairs(G, k):
                checked_pairs += 1
                assert chromatic_number(G) == k
                assert deletion_remains_k_chromatic(G, u, k)
                assert deletion_remains_k_chromatic(G, v, k)
    print('atlas_forced_equal_pairs_checked', checked_pairs)

    # k=3: smallest equality gadget is K4 minus the terminal edge.
    k3 = []
    for G in atlas:
        if len(G) != 4 or not nx.is_connected(G):
            continue
        if chromatic_number(G) == 3:
            fp = forced_equal_pairs(G, 3)
            if fp:
                k3.append((G, fp))
    print('n4_connected_chi3_with_forced_equal_unlabeled', len(k3))
    assert len(k3) == 1
    G3, fp3 = k3[0]
    u3, v3 = fp3[0]
    print('k3_example_edges', sorted(tuple(sorted(e)) for e in G3.edges()))
    print('k3_forced_pair', (u3, v3), 'common_neighbors', len(common_neighbors(G3, u3, v3)))
    assert len(common_neighbors(G3, u3, v3)) == 2

    # k=4, clique number <=3 (necessary for planar unit-distance graphs):
    # no example through 6 vertices; exactly one unlabeled connected example at 7.
    for n in range(4, 8):
        examples = []
        for G in atlas:
            if len(G) != n or not nx.is_connected(G):
                continue
            if clique_number(G) > 3:
                continue
            if chromatic_number(G) != 4:
                continue
            fp = forced_equal_pairs(G, 4)
            if fp:
                examples.append((G, fp))
        print('k4_omega_le3_n', n, 'unlabeled_examples', len(examples))
        if n <= 6:
            assert len(examples) == 0
        if n == 7:
            assert len(examples) == 1
            G, fp = examples[0]
            u, v = fp[0]
            print('k4_n7_edges', sorted(tuple(sorted(e)) for e in G.edges()))
            print('k4_n7_forced_pair', (u, v), 'common_neighbors', len(common_neighbors(G, u, v)))
            assert len(common_neighbors(G, u, v)) == 5
            # Remove terminals; the remaining graph is C5.
            H = G.copy()
            H.remove_nodes_from([u, v])
            assert nx.is_isomorphic(H, nx.cycle_graph(5))
            # Each terminal is adjacent to all five cycle vertices.
            assert G.degree(u) == 5 and G.degree(v) == 5

    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
