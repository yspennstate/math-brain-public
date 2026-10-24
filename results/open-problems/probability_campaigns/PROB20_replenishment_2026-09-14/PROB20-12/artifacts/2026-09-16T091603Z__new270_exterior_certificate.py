#!/usr/bin/env python3
"""PROB20-12 reproducibility checks for the new 270-facet proof.

Exact assertions check the relabeling, 6+3+6 edge partition, four-space
Hodge-complement sets, and annihilation incidence used by the proof.
A seeded Haar-complex stress test then evaluates the stacked exterior operator
and the resulting facet inequality.  The numerical section is diagnostic only;
the universal proof is analytic and is archived in the same-run Markdown report.
"""

import itertools
import numpy as np
from numpy.linalg import svd


def edge(a, b):
    return tuple(sorted((a, b)))


# ---------------------------------------------------------------------------
# 1. Exact combinatorial checks in the shifted 1,...,6 labeling.
# ---------------------------------------------------------------------------
R = {edge(1,2), edge(1,3), edge(1,4), edge(1,5), edge(2,3), edge(2,4)}
MSET = {edge(1,6), edge(2,5), edge(3,4)}
T = {edge(2,6), edge(3,5), edge(3,6), edge(4,5), edge(4,6), edge(5,6)}
ALL = {edge(a,b) for a in range(1,7) for b in range(a+1,7)}
assert R | MSET | T == ALL
assert not (R & MSET or R & T or MSET & T)

# Previous 0-based representative:
# B0=B1={01,02,12,13,14,23,24,25,34},
# B2={02,12,13,14,23,24}.
# Relabeling (5,0,3,4,1,2) -> (1,2,3,4,5,6).
old_to_new = {5:1, 0:2, 3:3, 4:4, 1:5, 2:6}
B = {(0,1),(0,2),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4)}
B2 = {(0,2),(1,2),(1,3),(1,4),(2,3),(2,4)}
mapset = lambda ss: {edge(old_to_new[a], old_to_new[b]) for a,b in ss}
Bnew, B2new = mapset(B), mapset(B2)
assert ALL - Bnew == R
assert Bnew - B2new == MSET
assert ALL - B2new == R | MSET

# Complementary four-space C={2,3,4,5}.
C = [2,3,4,5]
E = {edge(2,3), edge(2,4)}
D = {edge(2,5), edge(3,4), edge(3,5), edge(4,5)}
S = {edge(3,5), edge(4,5)}
F = {edge(2,3), edge(2,4), edge(2,5), edge(3,4)}
CEDGES = {edge(a,b) for a,b in itertools.combinations(C,2)}
assert E | D == CEDGES and not (E & D)

def comp_in_C(e):
    return tuple(sorted(set(C) - set(e)))

# 4D Hodge complements, ignoring the harmless orientation sign.
assert {comp_in_C(e) for e in E} == S
assert {comp_in_C(e) for e in D} == F
# Every D edge meets every S edge, hence D wedge S=0.
assert all(set(d) & set(s) for d in D for s in S)


# ---------------------------------------------------------------------------
# 2. Seeded complex-Haar diagnostic of the stacked operator.
# ---------------------------------------------------------------------------
PAIRS6 = list(itertools.combinations(range(6),2))
PIDX = {p:i for i,p in enumerate(PAIRS6)}
C0 = [1,2,3,4]  # zero-based coordinates corresponding to physical 2,3,4,5
PAIRSC = list(itertools.combinations(C0,2))
E0 = [(1,2),(1,3)]
D0 = [(1,4),(2,3),(2,4),(3,4)]
F0 = [(1,2),(1,3),(1,4),(2,3)]


def wedge2(u, v):
    return np.array([u[a]*v[b] - u[b]*v[a] for a,b in PAIRS6], dtype=complex)


def haar_unitary(n, rng):
    z = (rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    phase = d / np.where(np.abs(d) > 0, np.abs(d), 1)
    return q * np.conj(phase)


def coeff(alpha, p):
    return alpha[PIDX[tuple(sorted(p))]]


def wedge_sign_pair(e, f):
    if set(e) & set(f):
        return 0
    seq = list(e) + list(f)
    inv = sum(seq[i] > seq[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv % 2 else 1


def stacked_M(alphas):
    """Matrix of the report's M:E+E+F -> C^2 in coordinate bases."""
    a0, a1, a2 = alphas
    cols = [('E0',p) for p in E0] + [('E1',p) for p in E0] + [('F2',p) for p in F0]
    out = np.zeros((2, len(cols)), dtype=complex)
    for j, (typ, p) in enumerate(cols):
        if typ == 'E1':
            for q in PAIRSC:
                sg = wedge_sign_pair(p,q)
                if sg:
                    out[0,j] += sg * coeff(a2,q)
        elif typ == 'E0':
            for q in PAIRSC:
                sg = wedge_sign_pair(p,q)
                if sg:
                    out[1,j] += sg * coeff(a2,q)
        else:
            for q in D0:
                sg = wedge_sign_pair(q,p)
                if sg:
                    out[0,j] += sg * coeff(a1,q)
                    out[1,j] += sg * coeff(a0,q)
    return out


def mu(alpha, p1based):
    p = tuple(x-1 for x in p1based)
    return abs(coeff(alpha,p))**2


rng = np.random.default_rng(20260916)
trials = 3000
max_singular_value = 0.0
max_facet_violation = -1e100

for _ in range(trials):
    U = haar_unitary(6, rng)
    alphas = [wedge2(U[:,2*i], U[:,2*i+1]) for i in range(3)]

    sv = svd(stacked_M(alphas), compute_uv=False)[0]
    max_singular_value = max(max_singular_value, float(sv))

    lhs = mu(alphas[0],(1,6)) + mu(alphas[1],(1,6))
    q23 = sum(mu(a,(2,3)) for a in alphas)
    q24 = sum(mu(a,(2,4)) for a in alphas)
    rhs = q23 + q24 + mu(alphas[2],(2,5)) + mu(alphas[2],(3,4))
    max_facet_violation = max(max_facet_violation, float(lhs-rhs))

assert max_singular_value <= 1 + 1e-10
assert max_facet_violation <= 1e-10

print('exact_edge_partition', True)
print('exact_relabeling_to_lower_roots_form', True)
print('exact_hodge_complement_sets', True)
print('exact_D_wedge_S_zero', True)
print('haar_complex_trials', trials)
print('max_stacked_operator_singular_value', repr(max_singular_value))
print('max_shared_capacity_lhs_minus_rhs', repr(max_facet_violation))
print('ALL CHECKS PASSED')
