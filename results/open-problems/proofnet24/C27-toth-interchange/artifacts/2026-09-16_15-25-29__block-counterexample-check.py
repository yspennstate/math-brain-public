#!/usr/bin/env python3
"""
C27 exact finite counterexample / random-cut optimality checker.

No floating point is used. The P3 continuous-time interchange law is
computed from exact rational spectral projectors of its integer generator;
after substituting x=e^t, positivity is a polynomial statement over Z.
"""
from fractions import Fraction
from math import comb, ceil
import itertools
import sympy as sp


def cycle_cut_tail(k, s):
    # Directed simple k-cycle, iid fair block colors.
    # If N=# red->blue transitions, then exactly 2*C(k,2j) colorings have N=j.
    return Fraction(sum(2 * comb(k, 2*j) for j in range(s, k//2 + 1)), 2**k)


def maximal_median_threshold(k):
    return max(s for s in range(k//2 + 1)
               if cycle_cut_tail(k, s) >= Fraction(1, 2))


print("RANDOM-CUT SIMPLE-CYCLE CHECK")
for k in range(2, 65):
    expected = ceil((k - 1) / 4)
    got = maximal_median_threshold(k)
    assert got == expected, (k, expected, got)
    if expected + 1 <= k//2:
        assert cycle_cut_tail(k, expected + 1) < Fraction(1, 2)
print("PASS k=2..64: maximal threshold with tail >=1/2 is ceil((k-1)/4).")

# Exact P3 interchange generator.
perms = list(itertools.permutations(range(3)))
idx = {p: i for i, p in enumerate(perms)}


def left_swap(p, a, b):
    return tuple(b if z == a else a if z == b else z for z in p)


Q = sp.zeros(6)
for p in perms:
    i = idx[p]
    for a, b in [(0, 1), (1, 2)]:
        Q[i, idx[left_swap(p, a, b)]] += 1
        Q[i, i] -= 1

I = sp.eye(6)
lams = [0, -1, -3, -4]
projectors = {}
for lam in lams:
    P = sp.eye(6)
    for mu in lams:
        if mu != lam:
            P = P * (Q - mu*I) / sp.Rational(lam - mu)
    P = sp.simplify(P)
    assert sp.simplify(P*P - P) == sp.zeros(6)
    assert sp.simplify(Q*P - lam*P) == sp.zeros(6)
    projectors[lam] = P
assert sp.simplify(sum(projectors.values(), sp.zeros(6)) - I) == sp.zeros(6)

e0 = sp.zeros(1, 6)
e0[0, idx[(0, 1, 2)]] = 1
x = sp.symbols('x', positive=True)
# exp(tQ)=sum P_lam*exp(lam t); x=e^t gives x^lam.
dist = sp.zeros(1, 6)
for lam, P in projectors.items():
    dist += e0 * P * x**lam
dist = sp.simplify(dist)
assert sp.simplify(sum(dist[0, j] for j in range(6)) - 1) == 0


def root_cycle(p):
    s = set()
    u = 0
    while u not in s:
        s.add(u)
        u = p[u]
    return s


A = sp.factor(sum(dist[0, j] for j, p in enumerate(perms) if 1 in root_cycle(p)))
B = sp.factor(sum(dist[0, j] for j, p in enumerate(perms) if 2 in root_cycle(p)))
AB = sp.factor(sum(dist[0, j] for j, p in enumerate(perms)
                   if {1, 2}.issubset(root_cycle(p))))
D = sp.factor(AB - A*B)
target = ((x - 1)**2 * (x**2 + x + 1)
          * (3*x**4 + 6*x**3 + 2*x**2 + 2*x - 1) / (36*x**8))
assert sp.simplify(D - target) == 0
last = 3*x**4 + 6*x**3 + 2*x**2 + 2*x - 1
assert sp.expand(last.subs(x, 1)) == 12
assert all(c > 0 for c in sp.Poly(sp.diff(last, x), x).all_coeffs())

print("P3 DEPENDENCE CHECK")
print("P(1 in C0) =", A)
print("P(2 in C0) =", B)
print("P({1,2} subset C0) =", AB)
print("joint-product =", D)
print("PASS: for x=e^t>1, all covariance factors are positive; final polynomial is increasing and equals 12 at x=1.")
print("Therefore the two cycle-membership events are strictly positively correlated for every t>0.")
print("ALL_EXACT_CHECKS_PASS")
