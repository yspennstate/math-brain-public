#!/usr/bin/env python3
"""Exact finite certificate for R20 / KNSV Conjecture 8.2.

This checker verifies a sparse seven-vertex dual obstruction to the proposed
*linear local reconstruction* of the first hidden (4,3) block statistic h1.
It is NOT a counterexample to Conjecture 8.2.

For a simple 7-vertex graph G, ordinary U is stored exactly as the integer
coefficient dictionary keyed by
    (sorted component-size partition, total cyclomatic number)
over all spanning edge subsets.

For a 4-set B with complementary 3-set C, write
    C_G(B;q)=q^3 sum_j a_j(B)(1+q)^j.
Then h1(G)=sum a_0(B) over those B whose complement C is a triangle.
The code computes a_0(B) exactly as -C_G(B;-1).

It verifies an equality of *sums* of ordinary-U polynomials for two weighted
multisets of graph types, while the corresponding sums of h1 differ.  Hence
h1 is not a universal Q-linear combination of ordinary-U coefficient
functions on seven-vertex simple graphs.  This does not produce two graphs
with equal U and different h1.
"""
from collections import Counter, defaultdict
from itertools import combinations

LEFT = [
    ("F~{OO", 1),
    ("FG?`G", 3),
    ("FC_`G", 2),
    ("F`?GW", 1),
    ("F`G`G", 3),
    ("FetA?", 1),
    ("F`_pg", 1),
]
RIGHT = [
    ("FOg?G", 3),
    ("F@G`G", 3),
    ("FK_`G", 3),
    ("Fms?G", 2),
    ("F~|A?", 1),
]


def decode_graph6(s):
    vals = [ord(c) - 63 for c in s]
    n = vals[0]
    if not (0 <= n <= 62):
        raise ValueError("checker only supports short graph6 headers")
    bits = []
    for v in vals[1:]:
        bits.extend((v >> sh) & 1 for sh in range(5, -1, -1))
    edges = []
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                edges.append((i, j))
            k += 1
    return n, tuple(edges)


def u_dictionary(code):
    n, edges = decode_graph6(code)
    out = defaultdict(int)
    for mask in range(1 << len(edges)):
        par = list(range(n))
        sz = [1] * n
        ec = 0

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ec += 1
                a, b = find(u), find(v)
                if a != b:
                    if sz[a] < sz[b]:
                        a, b = b, a
                    par[b] = a
                    sz[a] += sz[b]
        roots = [find(v) for v in range(n)]
        comps = Counter(roots)
        lam = tuple(sorted(comps.values(), reverse=True))
        cyc = ec - n + len(comps)
        out[(lam, cyc)] += 1
    return dict(out)


def h1(code):
    n, edges = decode_graph6(code)
    if n != 7:
        raise ValueError("h1 certificate is specialized to n=7")
    E = set(edges)
    total = 0
    for B in combinations(range(7), 4):
        C = tuple(v for v in range(7) if v not in B)
        if not all(tuple(sorted(e)) in E for e in combinations(C, 2)):
            continue
        induced = [e for e in combinations(B, 2) if tuple(sorted(e)) in E]
        # a0(B) = - C_G(B;-1), since C_G(B;q)=q^3 A_B(1+q).
        a0 = 0
        for mask in range(1 << len(induced)):
            par = {v: v for v in B}

            def find(x):
                while par[x] != x:
                    par[x] = par[par[x]]
                    x = par[x]
                return x

            ec = 0
            for i, (u, v) in enumerate(induced):
                if (mask >> i) & 1:
                    ec += 1
                    a, b = find(u), find(v)
                    if a != b:
                        par[b] = a
            if len({find(v) for v in B}) == 1:
                a0 += -((-1) ** ec)
        total += a0
    return total


def weighted_u(side, cache):
    out = defaultdict(int)
    for code, mult in side:
        for key, coeff in cache[code].items():
            out[key] += mult * coeff
    return {k: v for k, v in out.items() if v}


def main():
    codes = [c for c, _ in LEFT + RIGHT]
    if len(set(codes)) != len(codes):
        raise AssertionError("graph types must be distinct")
    for code in codes:
        n, edges = decode_graph6(code)
        assert n == 7
        assert len(edges) == len(set(edges))
        assert all(u != v for u, v in edges)

    cache = {code: u_dictionary(code) for code in codes}
    UL = weighted_u(LEFT, cache)
    UR = weighted_u(RIGHT, cache)
    hL = sum(mult * h1(code) for code, mult in LEFT)
    hR = sum(mult * h1(code) for code, mult in RIGHT)

    print("R20 KNSV exact seven-vertex dual check")
    print("LEFT=", LEFT)
    print("RIGHT=", RIGHT)
    print("weighted_graph_copies_left=", sum(m for _, m in LEFT))
    print("weighted_graph_copies_right=", sum(m for _, m in RIGHT))
    print("ordinary_U_dictionary_terms_left=", len(UL))
    print("ordinary_U_dictionary_terms_right=", len(UR))
    print("ordinary_U_weighted_sums_equal=", UL == UR)
    print("h1_weighted_sum_left=", hL)
    print("h1_weighted_sum_right=", hR)
    print("h1_difference_left_minus_right=", hL - hR)
    print("per_graph=(code,edges,h1)")
    for code in codes:
        print(code, len(decode_graph6(code)[1]), h1(code))

    assert UL == UR
    assert hL == 1
    assert hR == 4
    assert hL != hR
    print("VERDICT=PASS: exact Z-certificate; h1 is not a universal linear combination of ordinary-U coefficient functions on seven-vertex simple graphs.")
    print("SCOPE=PARTIAL_ONLY: this is a dual obstruction to one proof architecture, not a pair of U-equal graphs and not a refutation of KNSV Conjecture 8.2.")


if __name__ == "__main__":
    main()
