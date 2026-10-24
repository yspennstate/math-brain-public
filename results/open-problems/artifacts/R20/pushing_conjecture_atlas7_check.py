#!/usr/bin/env python3
"""Exact finite self-check for Bensmail–Marcille–Orenga Conjecture 2.6.

Checks every connected unlabeled simple graph in NetworkX graph_atlas_g()
with 1..7 vertices, excluding connected K2 (which is not "nice").
For each graph G it finds rho:V(G)->{0,...,Delta(G)} such that

  sigma(u)=(1+rho(u))*d(u)+sum_{v~u} rho(v)

is proper on every edge.  All arithmetic is integer arithmetic.

Connected graphs suffice for the all-graphs statement through order 7:
the constraints split over connected components, and a component witness
bounded by Delta(component) is also bounded by Delta(whole graph).

This is a SELF-CHECK / finite PARTIAL result, not a proof of the universal
conjecture.
"""

from __future__ import annotations

import collections
import hashlib
import networkx as nx


def normalize(G: nx.Graph) -> nx.Graph:
    return nx.convert_node_labels_to_integers(G, ordering="sorted")


def sigma_values(G: nx.Graph, rho: list[int]) -> list[int]:
    G = normalize(G)
    out = []
    for u in range(G.number_of_nodes()):
        out.append((1 + rho[u]) * G.degree(u) + sum(rho[v] for v in G.neighbors(u)))
    return out


def verify_scheme(G: nx.Graph, rho: list[int]) -> bool:
    G = normalize(G)
    if len(rho) != G.number_of_nodes():
        return False
    Delta = max(dict(G.degree()).values(), default=0)
    if any((not isinstance(x, int)) or x < 0 or x > Delta for x in rho):
        return False
    sig = sigma_values(G, rho)
    return all(sig[u] != sig[v] for u, v in G.edges())


def edge_constraints(G: nx.Graph):
    """Return exact linear forms sigma(u)-sigma(v)."""
    G = normalize(G)
    n = G.number_of_nodes()
    deg = [G.degree(i) for i in range(n)]
    cons = []
    for u, v in G.edges():
        coeff = [0] * n
        # sigma(u)-sigma(v)
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
    """Exact DFS for one Delta-bounded proper pushing scheme, or None."""
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

    # Deterministic fail-first order: variables occurring in most edge forms first.
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
                # A fully assigned edge form equal to zero is forbidden.
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


def main() -> None:
    atlas = nx.graph_atlas_g()
    graphs = []
    for G in atlas:
        n = G.number_of_nodes()
        if 1 <= n <= 7 and nx.is_connected(G) and n != 2:
            graphs.append(normalize(G))

    # Stability check for the exact census used in this artifact.
    assert len(graphs) == 995, len(graphs)

    counts_by_order = collections.Counter()
    counts_by_delta = collections.Counter()
    graph6_codes = []
    failures = []
    max_witness_value = 0

    for G in graphs:
        n = G.number_of_nodes()
        Delta = max(dict(G.degree()).values(), default=0)
        code = nx.to_graph6_bytes(G, header=False).decode("ascii").strip()
        graph6_codes.append(code)
        counts_by_order[n] += 1
        counts_by_delta[Delta] += 1

        rho = find_scheme(G)
        if rho is None or not verify_scheme(G, rho):
            failures.append(code)
        else:
            max_witness_value = max(max_witness_value, max(rho, default=0))

    digest = hashlib.sha256(("\n".join(sorted(graph6_codes)) + "\n").encode()).hexdigest()

    print(f"connected_eligible_graphs={len(graphs)}")
    print("counts_by_order=" + repr(dict(sorted(counts_by_order.items()))))
    print("counts_by_Delta=" + repr(dict(sorted(counts_by_delta.items()))))
    print(f"graph6_sha256={digest}")
    print(f"failures={len(failures)}")
    if failures:
        print("failure_graph6=" + repr(failures))
        raise SystemExit(1)
    print(f"max_witness_value_seen={max_witness_value}")
    print("VERDICT=PASS_ALL_CONNECTED_NICE_GRAPHS_ORDER_AT_MOST_7")
    print("CONSEQUENCE=by_componentwise_combination_all_nice_simple_graphs_order_at_most_7_pass")
    print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_CONJECTURE_2_6")


if __name__ == "__main__":
    main()
