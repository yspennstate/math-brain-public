#!/usr/bin/env python3
"""Exact finite self-check for Bensmail--Marcille--Orenga Conjecture 2.6 through n=8.

No random sampling and no numerical tolerance are used.

Coverage:
* NetworkX graph_atlas_g() supplies every unlabeled simple graph through order 7.
* Every connected 8-vertex graph is obtained by deleting one vertex, so it occurs among
  the graphs formed by taking one of the 1044 unlabeled 7-vertex graphs and adding a
  new vertex with a nonempty neighborhood subset of the old seven vertices.
* We generate all such connected augmentations.  We deduplicate only after an exact
  NetworkX graph-isomorphism test.  Degree sequence and Weisfeiler--Lehman hash are
  used only as safe pre-buckets: if an isomorphic pair were ever split by a bucket,
  this would merely retain a duplicate, never delete an uncovered graph.

For each connected nice graph G, exact DFS finds rho:V(G)->{0,...,Delta(G)} such that
sigma(u)=(1+rho(u))*d(u)+sum_{v~u}rho(v) is proper.  Integer arithmetic only.

Connected graphs suffice because constraints are componentwise and
Delta(component) <= Delta(whole graph).

SELF-CHECK ONLY / PARTIAL for the universal conjecture.
"""

from __future__ import annotations

import collections
import networkx as nx


def normalize(G: nx.Graph) -> nx.Graph:
    return nx.convert_node_labels_to_integers(G, ordering="sorted")


def sigma_values(G: nx.Graph, rho: list[int]) -> list[int]:
    G = normalize(G)
    return [
        (1 + rho[u]) * G.degree(u) + sum(rho[v] for v in G.neighbors(u))
        for u in range(G.number_of_nodes())
    ]


def verify_scheme(G: nx.Graph, rho: list[int]) -> bool:
    G = normalize(G)
    Delta = max(dict(G.degree()).values(), default=0)
    if len(rho) != G.number_of_nodes():
        return False
    if any((not isinstance(x, int)) or x < 0 or x > Delta for x in rho):
        return False
    sig = sigma_values(G, rho)
    return all(sig[u] != sig[v] for u, v in G.edges())


def edge_constraints(G: nx.Graph):
    """Exact linear forms sigma(u)-sigma(v)."""
    G = normalize(G)
    n = G.number_of_nodes()
    deg = [G.degree(i) for i in range(n)]
    cons = []
    for u, v in G.edges():
        coeff = [0] * n
        coeff[u] += deg[u]
        coeff[v] -= deg[v]
        for w in G.neighbors(u):
            coeff[w] += 1
        for w in G.neighbors(v):
            coeff[w] -= 1
        support = tuple(i for i, a in enumerate(coeff) if a)
        cons.append((deg[u] - deg[v], tuple(coeff), support, (u, v)))
    return cons, deg


def find_scheme(G: nx.Graph):
    G = normalize(G)
    n = G.number_of_nodes()
    if n == 0:
        return []
    Delta = max(dict(G.degree()).values(), default=0)
    if G.number_of_edges() == 0:
        return [0] * n

    cons, deg = edge_constraints(G)
    var_cons = [[] for _ in range(n)]
    for j, (_c, _coeff, support, _edge) in enumerate(cons):
        for i in support:
            var_cons[i].append(j)

    order = sorted(range(n), key=lambda i: (-len(var_cons[i]), -deg[i], i))
    assign = [None] * n
    partial = [c for c, _coeff, _support, _edge in cons]
    unassigned = [len(support) for _c, _coeff, support, _edge in cons]

    def dfs(k: int):
        if k == n:
            candidate = [int(x) for x in assign]
            return candidate if verify_scheme(G, candidate) else None
        i = order[k]
        for val in range(Delta + 1):
            bad = False
            touched = []
            for j in var_cons[i]:
                a = cons[j][1][i]
                partial[j] += a * val
                unassigned[j] -= 1
                touched.append((j, a))
                if unassigned[j] == 0 and partial[j] == 0:
                    bad = True
            if not bad:
                assign[i] = val
                ans = dfs(k + 1)
                if ans is not None:
                    return ans
                assign[i] = None
            for j, a in touched:
                partial[j] -= a * val
                unassigned[j] += 1
        return None

    return dfs(0)


def generate_connected_n8_exact(base7: list[nx.Graph]):
    """Complete isomorph-free representative list of connected n=8 graphs.

    Correctness does not depend on the WL pre-bucket being complete: it is used only
    to avoid unnecessary exact isomorphism tests.  Exact deletion happens only after
    nx.is_isomorphic returns True.
    """
    buckets: dict[tuple, list[nx.Graph]] = {}
    reps: list[nx.Graph] = []
    connected_candidates = 0
    iso_tests = 0

    for B in base7:
        B = normalize(B)
        for mask in range(1, 1 << 7):
            G = B.copy()
            G.add_node(7)
            for i in range(7):
                if (mask >> i) & 1:
                    G.add_edge(7, i)
            if not nx.is_connected(G):
                continue
            connected_candidates += 1
            degseq = tuple(sorted((d for _, d in G.degree()), reverse=True))
            wl = nx.weisfeiler_lehman_graph_hash(G, iterations=3, digest_size=8)
            key = (degseq, wl)
            same_bucket = buckets.setdefault(key, [])
            duplicate = False
            for R in same_bucket:
                iso_tests += 1
                if nx.is_isomorphic(G, R):
                    duplicate = True
                    break
            if not duplicate:
                H = normalize(G)
                same_bucket.append(H)
                reps.append(H)

    return reps, connected_candidates, iso_tests, len(buckets)


def check_family(graphs: list[nx.Graph]):
    by_order = collections.Counter()
    by_delta = collections.Counter()
    failures = []
    max_witness = 0
    for G in graphs:
        G = normalize(G)
        n = G.number_of_nodes()
        Delta = max(dict(G.degree()).values(), default=0)
        by_order[n] += 1
        by_delta[Delta] += 1
        rho = find_scheme(G)
        if rho is None or not verify_scheme(G, rho):
            failures.append(nx.to_graph6_bytes(G, header=False).decode("ascii").strip())
        else:
            max_witness = max(max_witness, max(rho, default=0))
    return by_order, by_delta, failures, max_witness


def main() -> None:
    atlas = nx.graph_atlas_g()
    base7 = [normalize(G) for G in atlas if G.number_of_nodes() == 7]
    assert len(base7) == 1044, len(base7)

    connected_le7 = [
        normalize(G)
        for G in atlas
        if 1 <= G.number_of_nodes() <= 7 and nx.is_connected(G) and G.number_of_nodes() != 2
    ]
    assert len(connected_le7) == 995, len(connected_le7)

    n8, candidate_count, iso_tests, bucket_count = generate_connected_n8_exact(base7)

    # McKay's standard connected-graph count is an independent sanity check.
    # The coverage proof above does not require trusting this count.
    assert len(n8) == 11117, len(n8)

    b1, d1, f1, w1 = check_family(connected_le7)
    b8, d8, f8, w8 = check_family(n8)

    print(f"atlas_unlabeled_order7={len(base7)}")
    print(f"connected_eligible_order_le7={len(connected_le7)}")
    print("counts_order_le7=" + repr(dict(sorted(b1.items()))))
    print(f"n8_connected_augmentation_candidates={candidate_count}")
    print(f"n8_WL_degree_buckets={bucket_count}")
    print(f"n8_exact_isomorphism_tests={iso_tests}")
    print(f"n8_connected_isomorphism_classes={len(n8)}")
    print("n8_counts_by_Delta=" + repr(dict(sorted(d8.items()))))
    print(f"failures_order_le7={len(f1)}")
    print(f"failures_order8={len(f8)}")
    if f1 or f8:
        print("failure_graph6=" + repr(f1 + f8))
        raise SystemExit(1)
    print(f"max_witness_value_seen={max(w1, w8)}")
    print("VERDICT=PASS_ALL_NICE_SIMPLE_GRAPHS_ORDER_AT_MOST_8")
    print("METRIC=n_all=8")
    print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_CONJECTURE_2_6")


if __name__ == "__main__":
    main()
