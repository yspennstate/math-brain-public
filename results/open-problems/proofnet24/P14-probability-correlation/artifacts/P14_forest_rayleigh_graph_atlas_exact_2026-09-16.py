#!/usr/bin/env python3
"""Exact finite certificate for Grimmett Conjecture 4.2 on all unlabeled simple graphs n<=7.

Uses NetworkX's graph_atlas_g() (all non-isomorphic simple graphs with <=7 vertices)
and enumerates every acyclic edge subset exactly using rollback union-find.
For each graph G and each distinct present edge pair e,f, it computes integer counts
  Z    = # forests of G,
  Z_e  = # forests containing e,
  Z_f  = # forests containing f,
  Z_ef = # forests containing e and f,
and checks the exact Rayleigh difference
  Delta = Z_e Z_f - Z Z_ef >= 0.
No floating point arithmetic is used in the certificate inequality.
"""
from __future__ import annotations
import hashlib
import json
import platform
import sys
import time
from collections import defaultdict
from pathlib import Path

import networkx as nx

EXPECTED_UNLABELED_COUNTS = {1: 1, 2: 2, 3: 4, 4: 11, 5: 34, 6: 156, 7: 1044}


def exact_forest_moments(G: nx.Graph):
    """Return (edges, Z, Z1, Z2) with exact Python integers."""
    G = nx.convert_node_labels_to_integers(G, ordering="sorted")
    n = G.number_of_nodes()
    edges = sorted((min(u, v), max(u, v)) for u, v in G.edges())
    m = len(edges)
    Z = 0
    Z1 = [0] * m
    Z2 = [[0] * m for _ in range(m)]
    chosen: list[int] = []
    parent = list(range(n))
    size = [1] * n

    def find(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x

    def dfs(k: int) -> None:
        nonlocal Z
        if k == m:
            Z += 1
            L = len(chosen)
            for a in range(L):
                i = chosen[a]
                Z1[i] += 1
                for b in range(a + 1, L):
                    j = chosen[b]
                    if i < j:
                        Z2[i][j] += 1
                    else:
                        Z2[j][i] += 1
            return

        # Exclude edge k.
        dfs(k + 1)

        # Include edge k exactly when it does not create a cycle.
        u, v = edges[k]
        ru, rv = find(u), find(v)
        if ru == rv:
            return
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        old_size_ru = size[ru]
        parent[rv] = ru
        size[ru] += size[rv]
        chosen.append(k)
        dfs(k + 1)
        chosen.pop()
        size[ru] = old_size_ru
        parent[rv] = rv

    dfs(0)
    return edges, Z, Z1, Z2


def main() -> int:
    t0 = time.time()
    atlas = nx.graph_atlas_g()
    by_n = defaultdict(list)
    for G in atlas:
        n = G.number_of_nodes()
        if 1 <= n <= 7:
            by_n[n].append(G)

    observed_counts = {n: len(by_n[n]) for n in range(1, 8)}
    if observed_counts != EXPECTED_UNLABELED_COUNTS:
        raise AssertionError((observed_counts, EXPECTED_UNLABELED_COUNTS))

    summary = {}
    global_pair_checks = 0
    global_negative = 0
    global_zero = 0
    global_positive = 0
    global_min_positive = None
    global_min_positive_witness = None
    graph_digest = hashlib.sha256()

    for n in range(1, 8):
        pair_checks = negative = zero = positive = 0
        min_positive = None
        min_positive_witness = None
        max_edges = 0
        forest_count_max = 0
        for atlas_index, G in enumerate(by_n[n]):
            H = nx.convert_node_labels_to_integers(G, ordering="sorted")
            edges, Z, Z1, Z2 = exact_forest_moments(H)
            max_edges = max(max_edges, len(edges))
            forest_count_max = max(forest_count_max, Z)
            # Durable graph identity independent of atlas object memory addresses.
            graph_digest.update(f"n={n};edges={edges}\n".encode("utf-8"))
            m = len(edges)
            for i in range(m):
                for j in range(i + 1, m):
                    pair_checks += 1
                    delta = Z1[i] * Z1[j] - Z * Z2[i][j]
                    if delta < 0:
                        negative += 1
                        print("COUNTEREXAMPLE", n, atlas_index, edges, edges[i], edges[j], Z, Z1[i], Z1[j], Z2[i][j], delta)
                        return 2
                    if delta == 0:
                        zero += 1
                    else:
                        positive += 1
                        if min_positive is None or delta < min_positive:
                            min_positive = delta
                            min_positive_witness = {
                                "atlas_n_local_index": atlas_index,
                                "edges": edges,
                                "pair": [edges[i], edges[j]],
                                "Z": Z,
                                "Z_e": Z1[i],
                                "Z_f": Z1[j],
                                "Z_ef": Z2[i][j],
                                "delta": delta,
                            }
        summary[str(n)] = {
            "unlabeled_graphs": len(by_n[n]),
            "max_edges": max_edges,
            "edge_pair_checks": pair_checks,
            "negative_deltas": negative,
            "zero_deltas": zero,
            "positive_deltas": positive,
            "minimum_positive_delta": min_positive,
            "minimum_positive_witness": min_positive_witness,
            "maximum_forest_count_seen": forest_count_max,
        }
        global_pair_checks += pair_checks
        global_negative += negative
        global_zero += zero
        global_positive += positive
        if min_positive is not None and (global_min_positive is None or min_positive < global_min_positive):
            global_min_positive = min_positive
            global_min_positive_witness = {"n": n, **min_positive_witness}

    elapsed = time.time() - t0
    manifest = {
        "problem": "Grimmett Conjecture 4.2: uniform-all-forests pairwise edge negative correlation",
        "scope": "all unlabeled finite simple graphs with 1<=n<=7; all distinct present edge pairs; unit weights",
        "arithmetic": "exact Python integers only for Z, Z_e, Z_f, Z_ef and Delta",
        "networkx_version": nx.__version__,
        "python_version": platform.python_version(),
        "expected_unlabeled_counts": EXPECTED_UNLABELED_COUNTS,
        "observed_unlabeled_counts": observed_counts,
        "graph_catalog_sha256": graph_digest.hexdigest(),
        "per_n": summary,
        "totals": {
            "unlabeled_graphs": sum(observed_counts.values()),
            "edge_pair_checks": global_pair_checks,
            "negative_deltas": global_negative,
            "zero_deltas": global_zero,
            "positive_deltas": global_positive,
            "minimum_positive_delta": global_min_positive,
            "minimum_positive_witness": global_min_positive_witness,
        },
        "result": "PASS" if global_negative == 0 else "FAIL",
        "elapsed_seconds": elapsed,
    }
    print(json.dumps(manifest, sort_keys=True, indent=2))
    return 0 if global_negative == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
