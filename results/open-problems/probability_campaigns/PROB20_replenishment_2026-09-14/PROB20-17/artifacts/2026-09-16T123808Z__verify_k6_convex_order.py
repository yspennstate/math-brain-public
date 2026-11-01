#!/usr/bin/env python3
"""
Exact certificate for PROB20-17 run 2026-09-16T123808Z.

Proof-path checks only; no floating point is used:
  1. enumerate all 2^15 labeled simple graphs on 6 vertices;
  2. compute the exact maximum number of directed Hamiltonian paths at
     each missing-edge count q;
  3. verify the rational convex majorant psi;
  4. construct Phi(T)=E psi(Bin(15,T/15)) exactly;
  5. verify (1-T/18)^5-Phi(T)=T Q(T), and certify Q>0 on
     [0,5], [5,10], [10,15] by positive Bernstein coefficients.

The script uses Python stdlib only.
"""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb

N = 6
VERTS = tuple(range(N))
EDGES = tuple(combinations(VERTS, 2))
EIDX = {e: i for i, e in enumerate(EDGES)}
assert len(EDGES) == 15


def edge_index(a, b):
    if a > b:
        a, b = b, a
    return EIDX[(a, b)]


# 360 undirected Hamiltonian path edge sets (reverse orientations identified).
PATH_MASKS = set()
for p in permutations(VERTS):
    if p > p[::-1]:
        continue
    mask = 0
    for a, b in zip(p, p[1:]):
        mask |= 1 << edge_index(a, b)
    PATH_MASKS.add(mask)
assert len(PATH_MASKS) == 360


# Exact finite extremal table by complete enumeration of all 32768 graphs.
max_directed = [0] * 16
witness_mask = [0] * 16
for graph_mask in range(1 << 15):
    q = 15 - graph_mask.bit_count()
    undirected_count = 0
    for pm in PATH_MASKS:
        if graph_mask & pm == pm:
            undirected_count += 1
    directed_count = 2 * undirected_count
    if directed_count > max_directed[q]:
        max_directed[q] = directed_count
        witness_mask[q] = graph_mask

EXPECTED = [720, 480, 336, 240, 152, 96, 72, 32,
            16, 12, 2, 0, 0, 0, 0, 0]
assert max_directed == EXPECTED, (max_directed, EXPECTED)


psi = [
    Fraction(1, 1),
    Fraction(2, 3),
    Fraction(7, 15),
    Fraction(1, 3),
    Fraction(19, 90),
    Fraction(7, 45),
    Fraction(1, 10),
    Fraction(2, 45),
    Fraction(11, 360),
    Fraction(1, 60),
    Fraction(1, 360),
    Fraction(0, 1),
    Fraction(0, 1),
    Fraction(0, 1),
    Fraction(0, 1),
    Fraction(0, 1),
]

# psi majorizes the exact deterministic extremal profile.
for q in range(16):
    assert Fraction(max_directed[q], 720) <= psi[q]

# Discrete convexity required by Hoeffding's convex-order theorem.
second_differences = [
    psi[q] - 2 * psi[q + 1] + psi[q + 2]
    for q in range(14)
]
assert all(x >= 0 for x in second_differences)
EXPECTED_SECOND = [
    Fraction(2, 15), Fraction(1, 15), Fraction(1, 90),
    Fraction(1, 15), Fraction(0), Fraction(0), Fraction(1, 24),
    Fraction(0), Fraction(0), Fraction(1, 90), Fraction(1, 360),
    Fraction(0), Fraction(0), Fraction(0),
]
assert second_differences == EXPECTED_SECOND


# Exact polynomial utilities, coefficient lists in ascending power order.
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return ptrim(out)


def pscale(a, c):
    return ptrim([x * c for x in a])


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def ppow(a, k):
    out = [Fraction(1)]
    for _ in range(k):
        out = pmul(out, a)
    return out


def affine_substitute(poly, left, right):
    """Return coefficients in u after T=left+(right-left)u."""
    out = [Fraction(0)]
    linear = [Fraction(left), Fraction(right - left)]
    for j, c in enumerate(poly):
        out = padd(out, pscale(ppow(linear, j), c))
    return out


def power_to_bernstein(poly, degree):
    """Power coefficients c_j -> Bernstein coefficients b_k on [0,1]."""
    poly = list(poly) + [Fraction(0)] * (degree + 1 - len(poly))
    out = []
    for k in range(degree + 1):
        b = Fraction(0)
        for j in range(k + 1):
            b += poly[j] * Fraction(comb(k, j), comb(degree, j))
        out.append(b)
    return out


# Phi(T)=sum psi(q) C(15,q) (T/15)^q (1-T/15)^(15-q).
t_over_15 = [Fraction(0), Fraction(1, 15)]
one_minus_t_over_15 = [Fraction(1), Fraction(-1, 15)]
Phi = [Fraction(0)]
for q in range(16):
    term = pmul(ppow(t_over_15, q), ppow(one_minus_t_over_15, 15 - q))
    term = pscale(term, psi[q] * comb(15, q))
    Phi = padd(Phi, term)

# Blakley-Roy target lower polynomial R(T)=(1-T/18)^5.
R = ppow([Fraction(1), Fraction(-1, 18)], 5)
Delta = padd(R, pscale(Phi, Fraction(-1)))
assert Delta[0] == 0
assert len(Delta) == 16

# Delta(T)=T Q(T).
Q = Delta[1:]
assert len(Q) == 15

# Positive Bernstein coefficients of Q on three intervals certify Q>0.
intervals = [(0, 5), (5, 10), (10, 15)]
expected_minima = [
    Fraction(82323881, 34437376800),
    Fraction(864233, 2152336050),
    Fraction(1, 116640),
]
mins = []
for left, right in intervals:
    in_u = affine_substitute(Q, left, right)
    bern = power_to_bernstein(in_u, 14)
    assert all(b > 0 for b in bern)
    mins.append(min(bern))
assert mins == expected_minima, (mins, expected_minima)


print("EXACT CERTIFICATE PASSED")
print("directed Hamiltonian maxima by missing-edge count q=0..15:")
print(max_directed)
print("convex second differences of psi:")
print([str(x) for x in second_differences])
print("minimum Bernstein coefficients for Q on [0,5],[5,10],[10,15]:")
print([str(x) for x in mins])
