#!/usr/bin/env python3
"""Finite-support consistency checks for the 2026-09-16 PROB20-14 report.

This is NOT proof evidence for the universal infinite-variance theorem.  It checks
only exact algebra/indexing on a finite critical law, plus a numerical Chernoff
upper bound obtained from a finite grid of tilts.
"""
from collections import defaultdict
from fractions import Fraction
from math import exp, log

PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
R = 0.5
Q = 1.5
MAX_N = 81


def convolve(base, n):
    d = {0: Fraction(1)}
    for _ in range(n):
        nd = defaultdict(Fraction)
        for s, p in d.items():
            for x, px in base.items():
                nd[s + x] += p * px
        d = dict(nd)
    return d


S = {n: convolve(PI, n) for n in range(MAX_N + 1)}


def u(m):
    """P(U=m), U=X-1, via Dwass: P(X=n)=P(S_n=n-1)/n."""
    n = m + 1
    return S[n].get(n - 1, Fraction(0)) / n


def u_convolution(m, b):
    if m < 0:
        return Fraction(0)
    if b == 0:
        return Fraction(1) if m == 0 else Fraction(0)
    ud = {i: u(i) for i in range(m + 1)}
    d = {0: Fraction(1)}
    for _ in range(b):
        nd = defaultdict(Fraction)
        for s, p in d.items():
            for x, px in ud.items():
                if px and s + x <= m:
                    nd[s + x] += p * px
        d = dict(nd)
    return d.get(m, Fraction(0))


# Ordinary k=2 prefix law: A=1+Z_1 and B=Z_2.
PREFIX = defaultdict(Fraction)
for z1, pz1 in PI.items():
    for z2, pz2 in S[z1].items():
        PREFIX[(1 + z1, z2)] += pz1 * pz2

assert sum(PREFIX.values()) == 1
assert sum(Fraction(b) * p for (a, b), p in PREFIX.items()) == 1


def prefix_checks(m):
    um = u(m)
    assert um > 0
    norm = Fraction(0)
    l1 = 0.0
    for (a, b), p in PREFIX.items():
        c = a + b - 1  # span h=1
        rr = u_convolution(m - c, b) / um if m >= c else Fraction(0)
        norm += p * rr
        l1 += float(p) * abs(float(rr) - b)
    assert norm == 1, (m, norm)
    return 0.5 * l1


# Exact normalization dQ/dP=R and observed Scheffe-TV decay on this test law.
tvs = []
for m in (5, 10, 15, 20, 30, 40):
    tv = prefix_checks(m)
    tvs.append((m, tv))
assert all(tvs[i + 1][1] < tvs[i][1] for i in range(len(tvs) - 1))


# Total-progeny pgf T(z)=z f(T), and phi(t)=e^t T(e^-t) for U=X-1.
def f(s):
    return sum(float(p) * (s ** k) for k, p in PI.items())


def T_of_z(z):
    x = 0.0
    for _ in range(100000):
        nx = z * f(x)
        if abs(nx - x) < 1e-15:
            return nx
        x = nx
    raise RuntimeError("fixed point did not converge")


def K(t):
    z = exp(-t)
    phi = exp(t) * T_of_z(z)
    return -log(phi)


def I_grid(m, b):
    """A LOWER bound on I_M(b)=sup_t[bK(t)-Mt], hence safe in (4.3)."""
    best = 0.0
    for i in range(4000):
        lt = -16.0 + i * (18.0 / 3999.0)
        t = exp(lt)
        best = max(best, b * K(t) - m * t)
    return best


m = 30
um = u(m)
L = -log(float(um))
weighted_rows = []
for j in (1, 2, 3, 4, 5, 6):
    actual = 0.0
    tau = 0.0
    for (a, b), p in PREFIX.items():
        if b < j:
            continue
        pf = float(p)
        tau += pf * (b ** Q)
        c = a + b - 1
        rr = float(u_convolution(m - c, b) / um) if m >= c else 0.0
        actual += pf * (b ** R) * rr
    ig = I_grid(m, j)
    # Since ig <= I_M(j), replacing I_M(j) by ig makes the RHS larger.
    bound = (tau / j) * exp(L - ig)
    assert actual <= bound + 1e-12, (j, actual, bound)
    weighted_rows.append((j, actual, tau, ig, bound))

print("critical law:", {k: str(v) for k, v in PI.items()})
print("q=", Q, "r=", R)
print("k=2 prefix mass=", sum(PREFIX.values()), "E[B]=", sum(Fraction(b)*p for (a,b),p in PREFIX.items()))
print("TV(Q_M, Kesten-prefix) checks:")
for row in tvs:
    print("  M=%d TV=%.12g" % row)
print("weighted Cramer tail checks at M=30:")
for j, actual, tau, ig, bound in weighted_rows:
    print("  j=%d actual=%.12g tau=%.12g I_grid=%.12g bound=%.12g" % (j, actual, tau, ig, bound))
print("ALL ASSERTIONS PASSED")
