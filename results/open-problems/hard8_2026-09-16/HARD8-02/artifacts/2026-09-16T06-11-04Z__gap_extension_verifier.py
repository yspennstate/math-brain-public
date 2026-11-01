#!/usr/bin/env python3
"""Exact experiments for the rooted one-gap extension mechanism in graceful trees.

Requires networkx. All checks are integer/exhaustive; no floating point or SAT timeout
is used. For each unlabeled n-vertex tree and each chosen root, enumerate graceful
labelings and test whether one gap insertion can extend the tree by a leaf at that root.

Gap insertion at L sends each old vertex label x to x + 1[x >= L], leaving L unused.
The script checks the cut-suffix criterion proved in the accompanying report.
"""
from __future__ import annotations
import argparse
import time
import networkx as nx


def graceful_labelings(T):
    """Generate all graceful labelings T -> {0,...,m} exactly."""
    n = T.number_of_nodes()
    m = n - 1
    nodes = list(T.nodes())
    edges = list(T.edges())
    for a, b in edges:
        for x, y in ((a, b), (b, a)):
            lab = {x: 0, y: m}
            used_labels = {0, m}
            used_diffs = {m}

            def rec():
                if len(lab) == n:
                    yield dict(lab)
                    return
                unassigned = [v for v in nodes if v not in lab]
                v = max(unassigned, key=lambda z: sum(1 for w in T.neighbors(z) if w in lab))
                assigned_nei = [w for w in T.neighbors(v) if w in lab]
                for val in range(n):
                    if val in used_labels:
                        continue
                    new_diffs = []
                    ok = True
                    for w in assigned_nei:
                        d = abs(val - lab[w])
                        if d == 0 or d in used_diffs or d in new_diffs:
                            ok = False
                            break
                        new_diffs.append(d)
                    if not ok:
                        continue
                    lab[v] = val
                    used_labels.add(val)
                    used_diffs.update(new_diffs)
                    yield from rec()
                    for d in new_diffs:
                        used_diffs.remove(d)
                    used_labels.remove(val)
                    del lab[v]
            yield from rec()


def gap_certificates(T, lab, root):
    """Return all (L,k,c,shifted_root) one-gap extension certificates."""
    n = T.number_of_nodes()
    m = n - 1
    edge_by_d = {}
    for u, v in T.edges():
        d = abs(lab[u] - lab[v])
        if d in edge_by_d:
            return []
        edge_by_d[d] = (u, v)
    if set(edge_by_d) != set(range(1, m + 1)):
        return []
    out = []
    for L in range(m + 2):
        c = []
        for d in range(1, m + 1):
            u, v = edge_by_d[d]
            a, b = lab[u], lab[v]
            c.append(int((a < L <= b) or (b < L <= a)))
        if any(c[i] > c[i + 1] for i in range(m - 1)):
            continue
        k = 0
        while k < m and c[k] == 0:
            k += 1
        shifted_root = lab[root] + (1 if lab[root] >= L else 0)
        if abs(L - shifted_root) == k + 1:
            out.append((L, k, tuple(c), shifted_root))
    return out


def explicitly_verify_extension(T, lab, root, cert):
    """Construct the extended labeling and verify all differences exactly."""
    L, k, c, shifted_root = cert
    n = T.number_of_nodes()
    m = n - 1
    new_leaf = max(T.nodes()) + 1
    G = T.copy()
    G.add_edge(root, new_leaf)
    new_lab = {v: x + (1 if x >= L else 0) for v, x in lab.items()}
    new_lab[new_leaf] = L
    assert set(new_lab.values()) == set(range(m + 2))
    diffs = [abs(new_lab[u] - new_lab[v]) for u, v in G.edges()]
    assert sorted(diffs) == list(range(1, m + 2))
    assert abs(new_lab[root] - L) == k + 1
    return G, new_lab


def analyse_n(n):
    start = time.time()
    trees = rooted = endpoint_ok = gap_ok = gap_only = no_gap = 0
    first_gap_only = None
    max_labelings = 0
    for T in nx.generators.nonisomorphic_trees(n):
        trees += 1
        labs = list(graceful_labelings(T))
        max_labelings = max(max_labelings, len(labs))
        for root in T.nodes():
            rooted += 1
            endpoint = any(lab[root] in (0, n - 1) for lab in labs)
            found = None
            for lab in labs:
                certs = gap_certificates(T, lab, root)
                if certs:
                    found = (lab, certs[0])
                    break
            gap = found is not None
            endpoint_ok += int(endpoint)
            gap_ok += int(gap)
            gap_only += int(gap and not endpoint)
            no_gap += int(not gap)
            if gap and not endpoint and first_gap_only is None:
                lab, cert = found
                explicitly_verify_extension(T, lab, root, cert)
                first_gap_only = {
                    "edges": sorted(tuple(sorted(e)) for e in T.edges()),
                    "root": root,
                    "labeling": dict(sorted(lab.items())),
                    "certificate": cert,
                    "graceful_labelings_of_tree": len(labs),
                }
    return {
        "n": n,
        "trees": trees,
        "rooted_instances": rooted,
        "endpoint_extendable": endpoint_ok,
        "gap_extendable": gap_ok,
        "gap_only": gap_only,
        "no_gap": no_gap,
        "max_labelings_one_tree": max_labelings,
        "seconds": time.time() - start,
        "first_gap_only": first_gap_only,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=9)
    args = ap.parse_args()
    print("n trees rooted endpoint gap gap_only no_gap max_labelings")
    for n in range(2, args.max_n + 1):
        r = analyse_n(n)
        print(r["n"], r["trees"], r["rooted_instances"],
              r["endpoint_extendable"], r["gap_extendable"],
              r["gap_only"], r["no_gap"], r["max_labelings_one_tree"])
        if r["first_gap_only"]:
            print("  first_gap_only =", r["first_gap_only"])


if __name__ == "__main__":
    main()
