#!/usr/bin/env python3
"""
R16/H0021 exact finite self-check.

Checks:
1. For every unlabeled subcubic tree on 2<=n<=14 vertices and 1<=k<=min(6,n-1),
   the explicit degree-2-chain packing constructed in the report has size at least
       ceil((n+3k+2-2(k+1)L)/(k+1))_+.
2. For every such tree, the degree-2 mass on the suppressed core has a matching
   carrying at least one third of the total degree-2 mass.
3. For the uniformly subdivided cubic-core obstruction family with 3<=L<=8 and
   2<=k<=7, the exact vertex-count formula holds and the longest bare path has
   length k-1, so there is no bare k-path.
"""
import math
import networkx as nx


def maximal_chains(T):
    endpoints = [v for v in T if T.degree(v) != 2]
    seen_edges = set()
    chains = []
    for u in endpoints:
        for w in T.neighbors(u):
            e = frozenset((u, w))
            if e in seen_edges:
                continue
            path = [u, w]
            seen_edges.add(e)
            prev, cur = u, w
            while T.degree(cur) == 2:
                nxt = next(x for x in T.neighbors(cur) if x != prev)
                seen_edges.add(frozenset((cur, nxt)))
                path.append(nxt)
                prev, cur = cur, nxt
            chains.append((path[0], path[-1], tuple(path[1:-1]), tuple(path)))
    assert len(seen_edges) == T.number_of_edges()
    return chains


def explicit_k_packing_count(T, k):
    # On each maximal degree-2 chain, take consecutive disjoint blocks
    # of k+1 degree-2 vertices; each block supports a bare k-edge path.
    return sum(len(internal) // (k + 1)
               for _, _, internal, _ in maximal_chains(T))


def proved_lower_bound(T, k):
    n = T.number_of_nodes()
    L = sum(1 for v in T if T.degree(v) == 1)
    numerator = n + 3*k + 2 - 2*(k+1)*L
    return max(0, math.ceil(numerator / (k + 1)))


def core_weight_matching(T):
    C = nx.Graph()
    total = 0
    for u, v, internal, _ in maximal_chains(T):
        w = len(internal)
        C.add_edge(u, v, weight=w)
        total += w
    M = nx.max_weight_matching(C, maxcardinality=False, weight="weight")
    matched = sum(C.edges[e]["weight"] for e in M)
    return total, matched


def cubic_core(L):
    assert L >= 2
    G = nx.Graph()
    if L == 2:
        G.add_edge("l0", "l1")
        return G
    if L == 3:
        for i in range(3):
            G.add_edge("v0", f"l{i}")
        return G
    m = L - 2
    for i in range(m - 1):
        G.add_edge(f"v{i}", f"v{i+1}")
    leaf = 0
    for v in ("v0", f"v{m-1}"):
        for _ in range(2):
            G.add_edge(v, f"l{leaf}")
            leaf += 1
    for i in range(1, m - 1):
        G.add_edge(f"v{i}", f"l{leaf}")
        leaf += 1
    assert leaf == L
    assert all(G.degree(v) in (1, 3) for v in G)
    return G


def subdivide_all_edges(G, r):
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    edge_id = 0
    for u, v in G.edges():
        prev = u
        for j in range(r):
            w = f"s{edge_id}_{j}"
            H.add_edge(prev, w)
            prev = w
        H.add_edge(prev, v)
        edge_id += 1
    return H


subcubic_counts = {}
tested_pairs = 0
for n in range(2, 15):
    count = 0
    for T in nx.generators.nonisomorphic_trees(n):
        if max(dict(T.degree()).values()) > 3:
            continue
        count += 1
        for k in range(1, min(7, n)):
            got = explicit_k_packing_count(T, k)
            need = proved_lower_bound(T, k)
            assert got >= need, (n, k, got, need, sorted(T.edges()))
            tested_pairs += 1
        total, matched = core_weight_matching(T)
        assert 3 * matched >= total, (n, total, matched, sorted(T.edges()))
    subcubic_counts[n] = count

hard_family_cases = 0
for L in range(3, 9):
    for k in range(2, 8):
        core = cubic_core(L)
        T = subdivide_all_edges(core, k - 2)
        n = T.number_of_nodes()
        assert n == 2*L*(k-1) - 3*k + 4
        longest = max(len(path)-1 for _, _, _, path in maximal_chains(T))
        assert longest == k - 1
        hard_family_cases += 1

print("subcubic_unlabeled_counts_n2_to_n14 =", subcubic_counts)
print("tree_k_pairs_checked =", tested_pairs)
print("uniform_subdivision_obstruction_cases =", hard_family_cases)
print("ALL_EXACT_CHECKS_PASS")
