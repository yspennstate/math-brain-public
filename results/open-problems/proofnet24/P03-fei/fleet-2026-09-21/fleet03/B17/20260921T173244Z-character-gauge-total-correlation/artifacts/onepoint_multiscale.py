#!/usr/bin/env python3
"""Balanced block-tree decomposition of total correlation for the one-point Boolean family."""
from math import log2


def h2(q):
    if q == 0.0 or q == 1.0:
        return 0.0
    return -q*log2(q)-(1-q)*log2(1-q)


def H_marginal(n, k):
    if k == 0:
        return 0.0
    # For f_n=+1 except at one input, every nonzero k-bit spectral pattern
    # has the same marginal probability alpha.
    alpha = 2.0**(2-n-k)
    v = (2**k-1)*alpha
    return h2(v) + v*log2(2**k-1)


def run(n):
    assert n > 0 and n & (n-1) == 0
    q = 2.0**(1-n)
    tc = n*h2(q)-H_marginal(n,n)
    print(f"n={n} TC={tc:.17g}")
    cum = 0.0
    m = 2
    while m <= n:
        mi = 2*H_marginal(n,m//2)-H_marginal(n,m)
        nodes = n//m
        contribution = nodes*mi
        cum += contribution
        print(f"block={m:2d} nodes={nodes:2d} per_node_MI={mi:.17g} level={contribution:.17g} fraction={contribution/tc:.12f} cumulative={cum/tc:.12f}")
        m *= 2
    assert abs(cum-tc) <= max(1e-18,1e-9*tc)


run(16)
run(32)
print("checks: PASS; binary block-tree mutual informations telescope exactly to total correlation")
