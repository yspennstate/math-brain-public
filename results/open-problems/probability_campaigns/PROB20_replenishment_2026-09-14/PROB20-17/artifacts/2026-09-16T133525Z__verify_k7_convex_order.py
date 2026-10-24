#!/usr/bin/env python3
"""
Exact / deterministic certificate for PROB20-17, run 2026-09-16T133525Z.

New result certified here:
  * exact extremal profile of directed Hamiltonian-path counts for every
    labeled simple graph on 7 vertices, indexed by the number q of missing edges;
  * a discrete-convex majorant psi of that profile;
  * exact rational Bernstein-basis positivity proving the binomialized
    Hamiltonian upper bound is at most the Blakley--Roy lower bound.

The finite graph enumeration is exhaustive over all 2^21 labeled graphs.
The polynomial part uses fractions.Fraction only.  NumPy is used only for the
Boolean-lattice zeta transform that counts path masks inside every graph mask.
"""

from fractions import Fraction
from itertools import permutations
from math import comb
import numpy as np

NVERT = 7
EDGES = [(i,j) for i in range(NVERT) for j in range(i+1,NVERT)]
EINDEX = {e:k for k,e in enumerate(EDGES)}
NEDGE = len(EDGES)
assert NEDGE == 21

# ---------------------------------------------------------------------
# 1. Exhaustive exact graph certificate by subset zeta transform.
# ---------------------------------------------------------------------

path_masks = set()
for p in permutations(range(NVERT)):
    m = 0
    for r in range(NVERT-1):
        e = tuple(sorted((p[r], p[r+1])))
        m |= 1 << EINDEX[e]
    path_masks.add(m)

# Reversal gives the same undirected path, hence 7!/2 masks.
assert len(path_masks) == 2520

size = 1 << NEDGE
contained = np.zeros(size, dtype=np.uint16)
for m in path_masks:
    contained[m] = 1

# Subset zeta transform:
# after the loop, contained[G] is the number of undirected Hamiltonian
# path edge-sets P with P subseteq G.
for bit in range(NEDGE):
    step = 1 << bit
    a = contained.reshape(-1, 2*step)
    a[:, step:] += a[:, :step]

# Exact popcount for all graph masks.
idx = np.arange(size, dtype=np.uint32)
byte_view = idx.view(np.uint8).reshape(size, 4)
lut = np.array([bin(i).count("1") for i in range(256)], dtype=np.uint8)
pop = lut[byte_view].sum(axis=1)

max_directed_by_present = []
for m in range(NEDGE+1):
    vals = contained[pop == m]
    mx_undirected = int(vals.max()) if len(vals) else 0
    max_directed_by_present.append(2 * mx_undirected)

max_directed_by_missing = [
    max_directed_by_present[NEDGE-q] for q in range(NEDGE+1)
]

EXPECTED = [
    5040, 3600, 2640, 1968, 1392, 952, 672, 480, 304, 184, 120,
    72, 36, 18, 14, 2, 0, 0, 0, 0, 0, 0
]
assert max_directed_by_missing == EXPECTED

F = [Fraction(v, 5040) for v in EXPECTED]

# ---------------------------------------------------------------------
# 2. Convex majorant on q=0,...,21.
# ---------------------------------------------------------------------

psi = [
    Fraction(1,1),
    Fraction(5,7),
    Fraction(11,21),
    Fraction(41,105),
    Fraction(29,105),
    Fraction(17,90),
    Fraction(2,15),
    Fraction(2,21),
    Fraction(19,315),
    Fraction(23,630),
    Fraction(1,42),
    Fraction(1,70),
    Fraction(1,140),
    Fraction(5,1008),
    Fraction(1,360),
    Fraction(1,1680),
    Fraction(0,1),
    Fraction(0,1),
    Fraction(0,1),
    Fraction(0,1),
    Fraction(0,1),
    Fraction(0,1),
]

assert len(psi) == 22
assert all(psi[q] >= F[q] for q in range(22))
second = [psi[q] - 2*psi[q+1] + psi[q+2] for q in range(20)]
assert all(x >= 0 for x in second)

EXPECTED_SECOND = [
    Fraction(2,21), Fraction(2,35), Fraction(2,105), Fraction(17,630),
    Fraction(2,63), Fraction(11,630), Fraction(1,315), Fraction(1,90),
    Fraction(1,90), Fraction(1,315), Fraction(1,420), Fraction(5,1008),
    Fraction(0,1), Fraction(0,1), Fraction(1,630), Fraction(1,1680),
    Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1),
]
assert second == EXPECTED_SECOND

# ---------------------------------------------------------------------
# 3. Exact polynomial arithmetic with Fraction.
# Polynomials are coefficient lists in increasing powers of T.
# ---------------------------------------------------------------------

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(p, q):
    n = max(len(p), len(q))
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)

def scale(p, c):
    return trim([c*x for x in p])

def mul(p, q):
    out = [Fraction(0) for _ in range(len(p)+len(q)-1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)

def pow_poly(p, k):
    out = [Fraction(1)]
    base = list(p)
    while k:
        if k & 1:
            out = mul(out, base)
        base = mul(base, base)
        k >>= 1
    return out

# Phi(T) = E psi(B), B~Bin(21,T/21).
phi = [Fraction(0)]
pT = [Fraction(0), Fraction(1,21)]         # T/21
one_minus_p = [Fraction(1), Fraction(-1,21)]
for q in range(22):
    term = mul(pow_poly(pT, q), pow_poly(one_minus_p, 21-q))
    term = scale(term, psi[q] * comb(21,q))
    phi = add(phi, term)

# Blakley--Roy lower polynomial b(T)=(1-2T/49)^6.
br = pow_poly([Fraction(1), Fraction(-2,49)], 6)

# delta = br - phi
delta = add(br, scale(phi, Fraction(-1)))
assert delta[0] == 0
Q = trim(delta[1:])  # delta(T)=T Q(T)
assert len(Q)-1 == 20

def affine_substitute(p, a, b):
    """Return p(a+(b-a)x), coefficient list in increasing powers of x."""
    out = [Fraction(0)]
    lin = [Fraction(a), Fraction(b-a)]
    for j, c in enumerate(p):
        out = add(out, scale(pow_poly(lin, j), c))
    return out

def bernstein_coefficients_on_interval(p, a, b):
    """Degree-n Bernstein coefficients of p on [a,b], exactly."""
    c = affine_substitute(p, a, b)
    n = len(p)-1
    c += [Fraction(0)] * (n+1-len(c))
    beta = []
    for k in range(n+1):
        s = Fraction(0)
        for j in range(k+1):
            s += c[j] * Fraction(comb(k,j), comb(n,j))
        beta.append(s)
    return beta

intervals = [(0,7), (7,14), (14,21)]
bernstein = [bernstein_coefficients_on_interval(Q, a, b) for a,b in intervals]
assert all(all(x > 0 for x in coeffs) for coeffs in bernstein)

mins = [min(coeffs) for coeffs in bernstein]
EXPECTED_MINS = [
    Fraction(647379695899759, 387654779603620305),
    Fraction(6357158903570, 77530955920724061),
    Fraction(1,2470629),
]
assert mins == EXPECTED_MINS

# Sanity: endpoint values of delta are nonnegative exactly.
def eval_poly(p, x):
    x = Fraction(x)
    s = Fraction(0)
    power = Fraction(1)
    for c in p:
        s += c*power
        power *= x
    return s

assert eval_poly(delta, 0) == 0
assert eval_poly(delta, 21) > 0

print("EXACT K7 EXTREMAL TABLE (q missing -> max directed Hamiltonian paths):")
print(max_directed_by_missing)
print("CONVEX MAJORANT psi:")
print([str(x) for x in psi])
print("SECOND DIFFERENCES:")
print([str(x) for x in second])
print("MIN BERNSTEIN COEFFICIENTS FOR Q=delta/T ON [0,7],[7,14],[14,21]:")
print([str(x) for x in mins])
print("ALL ASSERTIONS PASSED")
