#!/usr/bin/env python3
"""Finite-support consistency check for the PROB20-14 random-prefix identity.

This is an algebraic/numerical certificate only.  It does NOT prove the
infinite-variance theorem.  It checks the exact probability decomposition for
k=2 under a critical finite-support offspring law and r=1/2.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import isclose

PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
R = 0.5
MAX_N = 30

assert sum(Fraction(d) * p for d, p in PI.items()) == 1


def convolve(a, b, cutoff=None):
    out = defaultdict(Fraction)
    for x, px in a.items():
        for y, py in b.items():
            z = x + y
            if cutoff is None or z <= cutoff:
                out[z] += px * py
    return dict(out)


def iid_sum(n, cutoff):
    law = {0: Fraction(1)}
    for _ in range(n):
        law = convolve(law, PI, cutoff)
    return law


def total_progeny_pmf(n):
    """Dwass: P(|T|=n)=P(S_n=n-1)/n."""
    return iid_sum(n, n - 1).get(n - 1, Fraction(0)) / n


U = {n: total_progeny_pmf(n) for n in range(1, MAX_N + 1)}


def forest_pmf(number_of_trees, total):
    if number_of_trees == 0:
        return Fraction(1) if total == 0 else Fraction(0)
    law = {0: Fraction(1)}
    base = {n: p for n, p in U.items() if p and n <= total}
    for _ in range(number_of_trees):
        law = convolve(law, base, total)
    return law.get(total, Fraction(0))


# Enumerate the first two levels.  N=Z_0+Z_1=1+root_degree and
# L=Z_2=sum of offspring counts of the root's children.
prefix = defaultdict(Fraction)
for root_degree, p_root in PI.items():
    if root_degree == 0:
        prefix[(1, 0)] += p_root
        continue
    for child_degrees in product(PI.keys(), repeat=root_degree):
        p = p_root
        for d in child_degrees:
            p *= PI[d]
        N = 1 + root_degree
        L = sum(child_degrees)
        prefix[(N, L)] += p

assert sum(prefix.values()) == 1

m_kr = sum(float(p) * (L ** R if L else 0.0) for (N, L), p in prefix.items())
E_B = (
    sum(float(p) * (L ** (1 + R) if L else 0.0) for (N, L), p in prefix.items())
    / m_kr
)
E_A = (
    sum(float(p) * (N * L ** R if L else 0.0) for (N, L), p in prefix.items())
    / m_kr
)

assert m_kr > 0
assert E_A < float("inf") and E_B < float("inf")


def conditioned_width_moment(n):
    numerator = 0.0
    for (N, L), p_prefix in prefix.items():
        if L == 0 or n < N:
            continue
        numerator += float(p_prefix * forest_pmf(L, n - N)) * (L ** R)
    return numerator / float(U[n])


def tilted_prefix_rhs(n):
    probability = 0.0
    for (N, L), p_prefix in prefix.items():
        if L == 0 or n < N:
            continue
        p_tilted = float(p_prefix) * (L ** R) / m_kr
        probability += p_tilted * float(forest_pmf(L, n - N))
    return m_kr * probability / float(U[n])


for n in (5, 8, 10, 15, 20):
    lhs = conditioned_width_moment(n)
    rhs = tilted_prefix_rhs(n)
    assert isclose(lhs, rhs, rel_tol=1e-13, abs_tol=1e-13), (n, lhs, rhs)
    print(f"n={n:2d}  conditioned_E[Z2^r]={lhs:.15f}  random_prefix_rhs={rhs:.15f}")

print(f"m_2,r={m_kr:.15f}")
print(f"E[A_2]={E_A:.15f}")
print(f"E[B_2]={E_B:.15f}")
print("all random-prefix identity checks passed")
