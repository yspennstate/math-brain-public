#!/usr/bin/env python3
"""Exact finite self-check for R14 C199/C201.

Exhaustively enumerates every labeled simple graph on n=4 and n=6,
filters regular graphs, and verifies:
  (i) the centered complement antisymmetry for balanced min/max cuts;
  (ii) the exact equal-size swap formula for every balanced cut and every
       U subset S, V subset T with |U|=|V| (all admissible p).

Integer/rational arithmetic only.
"""
from itertools import combinations
from fractions import Fraction


def edges_complete(n):
    return list(combinations(range(n), 2))


def cut_size(E, S):
    S = set(S)
    return sum(((u in S) != (v in S)) for u, v in E)


def degrees(n, E):
    deg = [0] * n
    for u, v in E:
        deg[u] += 1
        deg[v] += 1
    return deg


def extrema(n, E):
    vals = [cut_size(E, S) for S in combinations(range(n), n // 2)]
    return min(vals), max(vals)


def verify_graph(n, E, allE):
    deg = degrees(n, E)
    if len(set(deg)) != 1:
        return 0
    d = deg[0]
    Ec = [e for e in allE if e not in E]
    mn, mx = extrema(n, E)
    mnc, mxc = extrema(n, Ec)
    B = Fraction(mn + mx, 1) - Fraction(d * n * n, 2 * (n - 1))
    dc = n - 1 - d
    Bc = Fraction(mnc + mxc, 1) - Fraction(dc * n * n, 2 * (n - 1))
    assert B + Bc == 0, (n, d, E, B, Bc)

    Vset = set(range(n))
    for St in combinations(range(n), n // 2):
        S = set(St)
        T = Vset - S
        r = [0] * n
        for u, v in E:
            if ((u in S) != (v in S)):
                r[u] += 1
                r[v] += 1
        base = cut_size(E, S)
        for p in range(1, n // 2 + 1):
            for Ut in combinations(sorted(S), p):
                U = set(Ut)
                for Vt in combinations(sorted(T), p):
                    V = set(Vt)
                    W = U | V
                    ecross = esame = 0
                    for u, v in E:
                        if u in W and v in W:
                            if ((u in U and v in V) or (v in U and u in V)):
                                ecross += 1
                            else:
                                esame += 1
                    Sp = (S - U) | V
                    delta = cut_size(E, Sp) - base
                    rhs = (
                        2 * p * d
                        - 2 * sum(r[w] for w in W)
                        + 2 * ecross
                        - 2 * esame
                    )
                    assert delta == rhs, (n, d, E, S, U, V, delta, rhs)
    return 1


def main():
    total_reg = 0
    by_nd = {}
    for n in (4, 6):
        allE = edges_complete(n)
        m = len(allE)
        for mask in range(1 << m):
            E = [allE[i] for i in range(m) if (mask >> i) & 1]
            deg = degrees(n, E)
            if len(set(deg)) != 1:
                continue
            d = deg[0]
            verify_graph(n, E, allE)
            total_reg += 1
            by_nd[(n, d)] = by_nd.get((n, d), 0) + 1
    print("R14_C199_C201_EXACT_CHECK_PASS")
    print("regular_graphs_checked", total_reg)
    for key in sorted(by_nd):
        print("n_d_count", key[0], key[1], by_nd[key])
    print("all_balanced_cuts_and_all_equal_size_swaps_checked_for_each_regular_graph")


if __name__ == "__main__":
    main()
