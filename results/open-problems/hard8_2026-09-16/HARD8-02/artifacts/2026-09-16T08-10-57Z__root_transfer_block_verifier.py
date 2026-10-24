#!/usr/bin/env python3
"""Exact verifier for HARD8-02 root-transfer / block-obstruction lemmas.

No floating point and no solver timeout.  The script:
  * enumerates graceful labelings of every non-isomorphic tree through --max-n;
  * finds every one-gap certificate on every root;
  * for each certificate and K=k,...,k+--delta, applies the closed-form
    balanced-broom construction and checks both gracefulness and the new
    one-gap certificate exactly;
  * checks the component lower bound on every constructed absorber;
  * checks the connected-graft necessity arithmetic for all tested k,s.

The exhaustive tree sweep is a finite consistency check; the accompanying
report contains the symbolic proofs for arbitrary sizes.
"""
from __future__ import annotations
import argparse
import networkx as nx


def is_graceful(T, lab):
    m = T.number_of_edges()
    if set(lab) != set(T.nodes()):
        return False
    if set(lab.values()) != set(range(m + 1)):
        return False
    diffs = [abs(lab[u] - lab[v]) for u, v in T.edges()]
    return sorted(diffs) == list(range(1, m + 1))


def edge_by_difference(T, lab):
    out = {}
    for u, v in T.edges():
        d = abs(lab[u] - lab[v])
        if d in out:
            return None
        out[d] = (u, v)
    return out


def graceful_labelings(T):
    n = T.number_of_nodes()
    m = n - 1
    nodes = list(T.nodes())
    edges = list(T.edges())
    seen = set()
    for a, b in edges:
        for x, y in ((a, b), (b, a)):
            lab = {x: 0, y: m}
            used_labels = {0, m}
            used_diffs = {m}

            def rec():
                if len(lab) == n:
                    key = tuple(lab[v] for v in nodes)
                    if key not in seen:
                        seen.add(key)
                        yield dict(lab)
                    return
                unassigned = [v for v in nodes if v not in lab]
                v = max(unassigned,
                        key=lambda z: sum(1 for w in T.neighbors(z) if w in lab))
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


def certificates(T, lab, root):
    m = T.number_of_edges()
    ebd = edge_by_difference(T, lab)
    assert ebd is not None and set(ebd) == set(range(1, m + 1))
    for L in range(m + 2):
        c = []
        for d in range(1, m + 1):
            u, v = ebd[d]
            a, b = lab[u], lab[v]
            c.append(int((a < L <= b) or (b < L <= a)))
        if any(c[i] > c[i + 1] for i in range(len(c) - 1)):
            continue
        k = 0
        while k < m and c[k] == 0:
            k += 1
        if lab[root] == L - k - 1:
            yield (L, k, "low")
        if lab[root] == L + k:
            yield (L, k, "high")


def verify_certificate(T, lab, root, L, k, branch):
    assert is_graceful(T, lab)
    m = T.number_of_edges()
    ebd = edge_by_difference(T, lab)
    cross = []
    for d in range(1, m + 1):
        u, v = ebd[d]
        a, b = lab[u], lab[v]
        cross.append(int((a < L <= b) or (b < L <= a)))
    assert cross == [0] * k + [1] * (m - k)
    if branch == "low":
        assert lab[root] == L - k - 1
    else:
        assert branch == "high"
        assert lab[root] == L + k


def transfer(T, lab, root, L, k, branch, K):
    assert K >= k
    verify_certificate(T, lab, root, L, k, branch)
    s = K + 1
    base_max = max(T.nodes()) if T.nodes() else -1
    u = base_max + 1
    p = [u + i for i in range(1, k + 1)]
    q = [u + k + j for j in range(1, K - k + 1)]

    G = T.copy()
    G.add_edge(root, u)
    for v in p:
        G.add_edge(root, v)
    for v in q:
        G.add_edge(u, v)

    new_lab = {v: x + (s if x >= L else 0) for v, x in lab.items()}
    if branch == "low":
        new_lab[u] = L + K
        for j, v in enumerate(q, start=1):
            new_lab[v] = L + j - 1
        for i, v in enumerate(p, start=1):
            new_lab[v] = L + K - k + i - 1
        L2 = L
        branch2 = "high"
    else:
        new_lab[u] = L
        for i, v in enumerate(p, start=1):
            new_lab[v] = L + i
        for j, v in enumerate(q, start=1):
            new_lab[v] = L + k + j
        L2 = L + K + 1
        branch2 = "low"

    assert is_graceful(G, new_lab)
    verify_certificate(G, new_lab, u, L2, K, branch2)

    U = {u, *p, *q}
    F = G.subgraph(U)
    c = nx.number_connected_components(F)
    assert c == k + 1
    assert c >= min(s, k + 1)
    return G, new_lab, (u, L2, K, branch2)


def arithmetic_component_bound(max_k=20, max_s=20):
    for k in range(max_k + 1):
        for s in range(1, max_s + 1):
            B = list(range(k + 1, k + s + 1))
            high = [d for d in B if d >= s]
            assert len(high) == min(s, k + 1)
            if s >= 2 and k > 0:
                assert len(high) >= 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=8)
    ap.add_argument("--delta", type=int, default=2)
    args = ap.parse_args()

    arithmetic_component_bound()
    tree_count = 0
    labeling_count = 0
    certificate_count = 0
    transfer_count = 0
    low = high = 0

    for n in range(2, args.max_n + 1):
        for T in nx.generators.nonisomorphic_trees(n):
            tree_count += 1
            for lab in graceful_labelings(T):
                labeling_count += 1
                for root in T.nodes():
                    for cert in certificates(T, lab, root):
                        certificate_count += 1
                        L, k, branch = cert
                        low += branch == "low"
                        high += branch == "high"
                        for K in range(k, k + args.delta + 1):
                            transfer(T, lab, root, L, k, branch, K)
                            transfer_count += 1

    print("PASS")
    print("trees", tree_count)
    print("graceful_labelings", labeling_count)
    print("certificates", certificate_count)
    print("low_certificates", low)
    print("high_certificates", high)
    print("verified_transfers", transfer_count)
    print("max_n", args.max_n)
    print("delta", args.delta)


if __name__ == "__main__":
    main()
