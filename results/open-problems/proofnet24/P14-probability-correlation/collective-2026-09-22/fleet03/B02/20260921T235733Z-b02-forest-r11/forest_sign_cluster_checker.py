#!/usr/bin/env python3
r"""Exact sanity check for the three-edge deletion/contraction Rayleigh identity.

For every labelled simple graph on n<=5 and every unordered marked pair e,f
plus a third edge g, enumerate all forests exactly and verify

    A B Delta_G(e,f)
      = B Z Delta_{G\g}(e,f) + A Z Delta_{G/g}(e,f)
        - Delta_G(g,e) Delta_G(g,f),

where A counts forests excluding g and B counts forests including g after
removing the compulsory g label.  The script also checks the quantitative
minimal-counterexample implication whenever the two conditional gaps are
nonnegative and the full marked gap is negative.
"""
from itertools import combinations


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return False
    return True


def verify_order(n):
    universe = list(combinations(range(n), 2))
    m = len(universe)
    graph_count = 0
    marked_triples = 0

    for graph_mask in range(1 << m):
        present = [i for i in range(m) if (graph_mask >> i) & 1]
        k = len(present)
        graph_count += 1
        if k < 3:
            continue

        forests = []
        for submask in range(1 << k):
            chosen_indices = [present[j] for j in range(k) if (submask >> j) & 1]
            chosen_edges = [universe[i] for i in chosen_indices]
            if is_forest(n, chosen_edges):
                mask = 0
                for i in chosen_indices:
                    mask |= 1 << i
                forests.append(mask)

        z = len(forests)
        one = {i: sum((f >> i) & 1 for f in forests) for i in present}
        two = {}
        for i, j in combinations(present, 2):
            two[(i, j)] = sum(
                bool((f >> i) & 1) and bool((f >> j) & 1) for f in forests
            )

        def pair_count(i, j):
            if i > j:
                i, j = j, i
            return two[(i, j)]

        for e, f in combinations(present, 2):
            for g in present:
                if g == e or g == f:
                    continue

                a = sum(1 for x in forests if not ((x >> g) & 1))
                b = sum(1 for x in forests if (x >> g) & 1)
                ae = sum(1 for x in forests if not ((x >> g) & 1) and ((x >> e) & 1))
                af = sum(1 for x in forests if not ((x >> g) & 1) and ((x >> f) & 1))
                aef = sum(
                    1
                    for x in forests
                    if not ((x >> g) & 1) and ((x >> e) & 1) and ((x >> f) & 1)
                )
                be = sum(1 for x in forests if ((x >> g) & 1) and ((x >> e) & 1))
                bf = sum(1 for x in forests if ((x >> g) & 1) and ((x >> f) & 1))
                bef = sum(
                    1
                    for x in forests
                    if ((x >> g) & 1) and ((x >> e) & 1) and ((x >> f) & 1)
                )

                d0 = ae * af - a * aef
                d1 = be * bf - b * bef
                d = one[e] * one[f] - z * pair_count(e, f)
                r_e = b * ae - a * be
                r_f = b * af - a * bf

                lhs = a * b * d
                rhs = b * z * d0 + a * z * d1 - r_e * r_f
                if lhs != rhs:
                    raise AssertionError(
                        ("identity", n, graph_mask, e, f, g, lhs, rhs)
                    )

                if d0 >= 0 and d1 >= 0 and d < 0:
                    threshold = z * (b * d0 + a * d1)
                    if not (r_e * r_f > threshold >= 0):
                        raise AssertionError(
                            (
                                "minimality implication",
                                n,
                                graph_mask,
                                e,
                                f,
                                g,
                                d,
                                d0,
                                d1,
                                r_e,
                                r_f,
                                threshold,
                            )
                        )
                marked_triples += 1

    return graph_count, marked_triples


def main():
    total_graphs = 0
    total_marked = 0
    for n in range(2, 6):
        graphs, marked = verify_order(n)
        total_graphs += graphs
        total_marked += marked
        print(f"n={n} graphs={graphs} marked_triples={marked}")
    print(f"TOTAL_GRAPHS={total_graphs}")
    print(f"TOTAL_MARKED_TRIPLES={total_marked}")
    print("IDENTITY_FAILURES=0")
    print("IMPLICATION_FAILURES=0")
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
