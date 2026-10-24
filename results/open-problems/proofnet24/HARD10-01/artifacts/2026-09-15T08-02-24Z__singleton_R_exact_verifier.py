#!/usr/bin/env python3
"""HARD10-01 exact finite verifier for the singleton-R theorem.

For every simple graph on n=3,4,5 labelled vertices and every distinguished
edge pair e,f, this script:

  * enumerates all forests of H=G-{e,f};
  * forms the five exact classes N0, Ne, Nf, B, R;
  * when R consists of exactly one forest P, expands the FULL multivariate
    Rayleigh difference coefficient-by-coefficient; and
  * verifies

        Delta_{e,f}(y) = y^P * product_{g in P} (1+y_g).

The theorem is proved mathematically in the companion report.  This program is
only an exhaustive small-graph adversarial check; it is not the universal
proof.

Standard library only.  Polynomial monomials are encoded by (union,intersection):
an H-edge in union\intersection has exponent 1, an edge in intersection has
exponent 2, and an edge outside union has exponent 0.
"""
from collections import defaultdict
from itertools import combinations


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    return True


def five_classes(n, graph_edges, e_index, f_index):
    e = graph_edges[e_index]
    f = graph_edges[f_index]
    H = [g for k, g in enumerate(graph_edges) if k not in (e_index, f_index)]
    classes = {k: [] for k in ("N0", "Ne", "Nf", "B", "R")}

    for mask in range(1 << len(H)):
        A = [H[i] for i in range(len(H)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        e_ok = is_forest(n, A + [e])
        f_ok = is_forest(n, A + [f])
        ef_ok = is_forest(n, A + [e, f])
        if not e_ok and not f_ok:
            key = "N0"
        elif e_ok and not f_ok:
            key = "Ne"
        elif f_ok and not e_ok:
            key = "Nf"
        elif ef_ok:
            key = "B"
        else:
            key = "R"
        classes[key].append(mask)
    return H, classes


def add_product(coeff, left, right, sign):
    for x in left:
        for y in right:
            coeff[(x | y, x & y)] += sign


def rayleigh_polynomial(classes):
    """Expand Ne*Nf + R*(Ne+Nf+B+R) - B*N0 exactly."""
    coeff = defaultdict(int)
    add_product(coeff, classes["Ne"], classes["Nf"], +1)
    for key in ("Ne", "Nf", "B", "R"):
        add_product(coeff, classes["R"], classes[key], +1)
    add_product(coeff, classes["B"], classes["N0"], -1)
    return {m: c for m, c in coeff.items() if c}


def singleton_factor(P):
    """Polynomial y^P product_{g in P}(1+y_g)."""
    indices = [i for i in range(P.bit_length()) if (P >> i) & 1]
    ans = {}
    for s in range(1 << len(indices)):
        doubled = 0
        for j, i in enumerate(indices):
            if (s >> j) & 1:
                doubled |= 1 << i
        ans[(P, doubled)] = 1
    return ans


def exhaustive(n):
    complete_edges = list(combinations(range(n), 2))
    tested_pairs = 0
    singleton_pairs = 0

    for graph_mask in range(1 << len(complete_edges)):
        graph_edges = [
            complete_edges[i]
            for i in range(len(complete_edges))
            if (graph_mask >> i) & 1
        ]
        if len(graph_edges) < 2:
            continue
        for e_index, f_index in combinations(range(len(graph_edges)), 2):
            tested_pairs += 1
            H, classes = five_classes(n, graph_edges, e_index, f_index)
            if len(classes["R"]) != 1:
                continue
            singleton_pairs += 1
            P = classes["R"][0]
            got = rayleigh_polynomial(classes)
            want = singleton_factor(P)
            if got != want:
                raise AssertionError(
                    "counterexample to singleton factorization",
                    n,
                    graph_edges,
                    graph_edges[e_index],
                    graph_edges[f_index],
                    H,
                    classes,
                    got,
                    want,
                )
    return tested_pairs, singleton_pairs


def main():
    grand_pairs = grand_singletons = 0
    for n in (3, 4, 5):
        pairs, singletons = exhaustive(n)
        grand_pairs += pairs
        grand_singletons += singletons
        print(
            f"n={n}: distinguished graph/edge-pairs tested={pairs}; "
            f"singleton-R pairs={singletons}; all passed"
        )
    assert (grand_pairs, grand_singletons) == (11766, 1017)
    print("TOTAL pairs tested=11766")
    print("TOTAL singleton-R pairs=1017")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
