#!/usr/bin/env python3
"""R20 exact finite sanity checks for the modulo-3 unicyclic proof.

This is NOT the proof of the infinite theorem.  It checks:
  (i) the explicit C6+leaf independent-set residue table used in the proof;
  (ii) every connected unicyclic graph in NetworkX's complete graph atlas
       (all such graphs through order 7) has an exact rho in {0,1,2};
  (iii) the proof's signless-Laplacian determinant/kernel predictions on
        those finite cases.
All arithmetic deciding the claims is integer / mod 3.
"""
from itertools import product
import networkx as nx

P = 3


def bareiss_det(a):
    a = [list(map(int, r)) for r in a]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[-1][-1]


def rank_mod3(a):
    a = [[x % P for x in r] for r in a]
    m, n = len(a), len(a[0]) if a else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = 1 if a[r][c] == 1 else 2
        a[r] = [(inv * x) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [(a[i][j] - f * a[r][j]) % P for j in range(n)]
        r += 1
    return r


def q_matrix(G):
    nodes = sorted(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    q = [[0] * len(nodes) for _ in nodes]
    for v in nodes:
        i = idx[v]
        q[i][i] = G.degree(v)
        for w in G.neighbors(v):
            q[i][idx[w]] = 1
    return q, nodes


def proper_push_exists_012(G):
    nodes = sorted(G.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    for rho in product(range(3), repeat=len(nodes)):
        sig = []
        for v in nodes:
            i = idx[v]
            sig.append((1 + rho[i]) * G.degree(v) +
                       sum(rho[idx[w]] for w in G.neighbors(v)))
        if all(sig[idx[u]] != sig[idx[v]] for u, v in G.edges()):
            return rho
    return None


def cycle_length(G):
    cb = nx.cycle_basis(G)
    assert len(cb) == 1
    return len(cb[0])


def check_c6_leaf_table():
    G = nx.cycle_graph(6)
    G.add_edge(0, 6)
    h = {0: 0, 1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0}
    sets = [set(), {0}, {1}, {2}, {0, 3}, {1, 3}, {0, 2},
            {1, 3, 6}, {1, 4, 6}]
    residues = set()
    for T in sets:
        assert all(not (u in T and v in T) for u, v in G.edges())
        residues.add((len(T) % 3, sum(h[v] for v in T) % 3))
    assert residues == {(a, b) for a in range(3) for b in range(3)}
    return sorted(residues)


def main():
    residues = check_c6_leaf_table()
    print("c6_plus_leaf_independent_set_residues=", residues)
    print("c6_plus_leaf_covers_all_F3_squared=True")

    counts, odd_det_bad, even_nullity_bad, failures = {}, [], [], []
    witnesses = 0
    for H in nx.graph_atlas_g():
        n = H.number_of_nodes()
        if n == 0 or not nx.is_connected(H) or H.number_of_edges() != n:
            continue
        if len(nx.cycle_basis(H)) != 1:
            continue
        G = nx.convert_node_labels_to_integers(H, ordering="sorted")
        ell = cycle_length(G)
        counts[n] = counts.get(n, 0) + 1
        q, nodes = q_matrix(G)
        if ell % 2:
            detq = bareiss_det(q)
            if detq != 4:
                odd_det_bad.append((nx.to_graph6_bytes(G, header=False).decode().strip(), ell, detq))
        else:
            nullity = len(nodes) - rank_mod3(q)
            predicted = 1 + (1 if ell % 3 == 0 else 0)
            if nullity != predicted:
                even_nullity_bad.append((nx.to_graph6_bytes(G, header=False).decode().strip(), ell, nullity, predicted))
        rho = proper_push_exists_012(G)
        if rho is None:
            failures.append(nx.to_graph6_bytes(G, header=False).decode().strip())
        else:
            witnesses += 1

    print("connected_unicyclic_atlas_counts=", counts)
    print("connected_unicyclic_atlas_total=", sum(counts.values()))
    print("exact_012_witnesses_found=", witnesses)
    print("odd_cycle_detQ_not_4=", odd_det_bad)
    print("even_cycle_kernel_prediction_failures=", even_nullity_bad)
    print("proper_012_failures=", failures)
    ok = not odd_det_bad and not even_nullity_bad and not failures
    print("VERDICT=PASS" if ok else "VERDICT=FAIL")


if __name__ == "__main__":
    main()
