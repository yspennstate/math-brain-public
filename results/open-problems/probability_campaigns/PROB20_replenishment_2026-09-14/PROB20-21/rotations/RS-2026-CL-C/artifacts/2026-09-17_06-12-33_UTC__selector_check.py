#!/usr/bin/env python3
"""Exact self-checks for RS-2026-CL-C first successor report.

Checks:
1. B14 finite counterexample: deterministic averaging under S_2 can destroy
   Wein threshold success.
2. B19 selector polynomial semantics for all graphs on n=4,k=2 and n=5,k=3.
All arithmetic is integer/rational; no floating point is used in decisions.
"""
from itertools import combinations
from fractions import Fraction

def all_edges(n):
    return list(combinations(range(n), 2))

def first_clique_selector(n, k, bits):
    E = all_edges(n)
    eidx = {e:i for i,e in enumerate(E)}
    sets = list(combinations(range(n), k))
    M = len(sets)
    R = 8 * M * M
    weights = [2 * (R ** (M - 1 - j)) for j in range(M)]

    I = []
    for S in sets:
        val = 1
        for e in combinations(S, 2):
            val *= bits[eidx[tuple(sorted(e))]]
        I.append(val)

    prefix = 0
    g = []
    for j in range(M):
        gj = weights[j] * I[j] * (1 - 2 * prefix)
        g.append(gj)
        prefix += I[j]

    f = [sum(g[j] for j,S in enumerate(sets) if i in S)
         for i in range(n)]
    A = tuple(i for i,x in enumerate(f) if x >= 1)
    B = tuple(i for i,x in enumerate(f)
              if Fraction(1,2) < Fraction(x,1) < 1)
    cliques = [S for S,ind in zip(sets,I) if ind]
    expected = cliques[0] if cliques else tuple()
    return A, B, expected, f

def exhaust(n, k):
    E = all_edges(n)
    for mask in range(1 << len(E)):
        bits = [(mask >> i) & 1 for i in range(len(E))]
        A, B, expected, f = first_clique_selector(n, k, bits)
        assert A == expected, (n,k,mask,A,expected,f)
        assert B == tuple(), (n,k,mask,B,f)
    return 1 << len(E)

def b14_average_counterexample():
    f = (Fraction(1), Fraction(0))
    f_swap = (Fraction(0), Fraction(1))
    avg = tuple((x+y)/2 for x,y in zip(f,f_swap))
    A_original = tuple(i for i,x in enumerate(f) if x >= 1)
    A_average = tuple(i for i,x in enumerate(avg) if x >= 1)
    assert A_original == (0,)
    assert avg == (Fraction(1,2), Fraction(1,2))
    assert A_average == tuple()
    return avg

if __name__ == "__main__":
    avg = b14_average_counterexample()
    print("B14_AVERAGING_COUNTEREXAMPLE_PASS", avg)
    for n,k in [(4,2),(5,3)]:
        total = exhaust(n,k)
        print(f"B19_SELECTOR_EXHAUSTIVE_PASS n={n} k={k} graphs={total}")
    print("ALL_EXACT_CHECKS_PASS")
