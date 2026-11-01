#!/usr/bin/env python3
"""Exact certificate: the 30+45 cut-facet relaxation has bridge gap exactly 1/3.

No floating point or LP solver is used. Fractions certify a feasible point and
a coefficientwise dual inequality. SymPy is used only for an exact rank check
of the true bridge facet on the 90 deterministic colored perfect matchings.
"""
from fractions import Fraction as F
from itertools import combinations, product
import sympy as sp

V = tuple(range(6))
EDGES = list(combinations(V, 2))
EID = {e: i for i, e in enumerate(EDGES)}

def ix(c, e):
    return 15*c + EID[tuple(sorted(e))]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

# Affine equations: each color has one edge; each vertex is used once overall.
EQ = []
for c in range(3):
    row = [F(0)]*45
    for e in EDGES:
        row[ix(c, e)] = F(1)
    EQ.append(row)
for v in V:
    row = [F(0)]*45
    for c in range(3):
        for e in EDGES:
            if v in e:
                row[ix(c, e)] += F(1)
    EQ.append(row)
assert len(EQ) == 9

# The 30 balanced 3+3 cut facets used by the recent R7-01 theorem.
BAL = {}
for X in combinations(V, 3):
    Y = tuple(v for v in V if v not in X)
    if tuple(X) > tuple(Y):
        continue
    internal = [e for e in EDGES
                if set(e) <= set(X) or set(e) <= set(Y)]
    for singled in range(3):
        row = [F(0)]*45
        for e in internal:
            row[ix(singled, e)] += 1
            for c in range(3):
                if c != singled:
                    row[ix(c, e)] -= 1
        BAL[(tuple(X), singled)] = row
assert len(BAL) == 30

# The 45 2+4 crossing facets used by the recent R7-01 theorem.
CROSS = {}
for X in combinations(V, 2):
    crossing = [e for e in EDGES
                if ((e[0] in X) != (e[1] in X))]
    for singled in range(3):
        row = [F(0)]*45
        for e in crossing:
            row[ix(singled, e)] += 1
            for c in range(3):
                if c != singled:
                    row[ix(c, e)] -= 1
        CROSS[(tuple(X), singled)] = row
assert len(CROSS) == 45

# Exact fractional point x*. All unspecified coordinates are zero.
x = [F(0)]*45
support = {
    0: {
        (0,1): F(1,6), (1,3): F(1,6),
        (2,3): F(1,3), (4,5): F(1,3),
    },
    1: {
        (0,1): F(1,3), (0,2): F(1,12), (0,4): F(1,12),
        (0,5): F(1,6), (1,2): F(1,6), (2,3): F(1,12),
        (3,4): F(1,12),
    },
    2: {
        (0,2): F(1,12), (0,4): F(1,12), (1,2): F(1,6),
        (2,3): F(1,12), (3,4): F(1,12), (3,5): F(1,6),
        (4,5): F(1,3),
    },
}
for c, vals in support.items():
    for e, q in vals.items():
        x[ix(c, e)] = q

assert all(q >= 0 for q in x)
assert all(dot(row, x) == 1 for row in EQ)
assert all(dot(row, x) <= 0 for row in BAL.values())
assert all(dot(row, x) <= 0 for row in CROSS.values())

# A known exact bridge facet from the earlier cumulative C0034 work:
# L={0,3}, D={1,2}, R={4,5}.
# SA = E(L union D) minus {D}; SB = E(D union R) minus {D}.
SA = [(0,1), (0,2), (0,3), (1,3), (2,3)]
SB = [(1,4), (1,5), (2,4), (2,5), (4,5)]
BRIDGE = [F(0)]*45
for e in SA:
    BRIDGE[ix(0, e)] += 1
for e in SB:
    BRIDGE[ix(1, e)] -= 1
    BRIDGE[ix(2, e)] -= 1

# The 75-facet relaxation violates the true bridge inequality by exactly 1/3.
assert dot(BRIDGE, x) == F(1,3)

# Exact dual certificate for the sharp upper bound 1/3.
# Three cut facets, each with weight 1/6:
A1 = BAL[((0,1,3), 0)]
A2 = BAL[((0,2,3), 0)]
A3 = CROSS[((1,2), 0)]

# Multipliers for the 9 affine equations:
# color sums c=0,1,2, then vertex equations v=0,...,5.
nu = [
    F(-1,3), F(-2,3), F(-2,3),
    F(2,3), F(1,3), F(1,3), F(2,3), F(0), F(0),
]
assert sum(nu, F(0)) == F(1,3)

# Coefficientwise identity:
#   -BRIDGE + (A1+A2+A3)/6 + sum_j nu_j EQ_j = RED >= 0.
# Therefore, for every y>=0 satisfying EQ_j(y)=1 and all cut rows <=0,
#   BRIDGE(y) <= 1/3.
RED = []
for k in range(45):
    r = (-BRIDGE[k] + F(1,6)*(A1[k]+A2[k]+A3[k])
         + sum((nu[j]*EQ[j][k] for j in range(9)), F(0)))
    RED.append(r)
assert all(r >= 0 for r in RED)
assert set(RED) == {F(0), F(1,3)}

# Complementary sharpness: x* attains the upper bound.
assert dot(BRIDGE, x) == sum(nu, F(0))

# Independent exact re-check that BRIDGE is valid and facet-defining
# on the true 90-vertex colored perfect-matching polytope.
STATES = []
for coloring in product(range(3), repeat=6):
    if all(coloring.count(c) == 2 for c in range(3)):
        row = [F(0)]*45
        for c in range(3):
            pts = tuple(v for v in V if coloring[v] == c)
            row[ix(c, pts)] = 1
        STATES.append(row)
assert len(STATES) == 90
bridge_values = [dot(BRIDGE, s) for s in STATES]
assert set(bridge_values) == {F(-1), F(0)}
assert max(bridge_values) == 0
tight = [s for s, val in zip(STATES, bridge_values) if val == 0]
assert len(tight) == 60
M = sp.Matrix([[1] + [int(q) for q in s] for s in tight])
assert M.rank() == 37  # equality-face affine dimension 36

print("vertex_count=90")
print("candidate_cut_facets=75")
print("bridge_true_vertex_values={-1,0}")
print("bridge_tight_vertices=60")
print("bridge_equality_face_affine_dimension=36")
print("relaxation_witness_bridge_gap=1/3")
print("dual_cut_rows=bal013_color0,bal023_color0,cross12_color0")
print("dual_cut_weight_each=1/6")
print("dual_affine_multiplier_sum=1/3")
print("dual_reduced_cost_values={0,1/3}")
print("EXACT_RELAXATION_OPTIMUM=1/3")
print("ALL_EXACT_CHECKS_PASS")
