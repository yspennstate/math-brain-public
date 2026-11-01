#!/usr/bin/env python3
"""
R05 / I0030 exact finite certificate for the 8-vertex regular sharpness witness.

This checker does NOT claim a counterexample to Aldous-Fill 7.30. It certifies
an unweighted connected cubic graph outside the arc-transitive class for which
an individual adjacent normalized heat ratio is eventually decreasing.

All spectral claims below are exact over Q(sqrt(5)).
"""
from __future__ import annotations
import sympy as sp

N = 8
D = 3
EDGES = [
    (0,1),(0,2),(0,3),(1,2),(1,3),(2,4),
    (3,5),(4,6),(4,7),(5,6),(5,7),(6,7),
]
X, Y = 2, 0  # adjacent witness

A = sp.zeros(N)
for u,v in EDGES:
    A[u,v] = A[v,u] = 1

# Basic exact graph checks.
assert A == A.T
assert all(A[i,i] == 0 for i in range(N))
assert all(sum(A[i,j] for j in range(N)) == D for i in range(N))
assert A[X,Y] == 1

# Connectivity by exact BFS.
adj = {i: [j for j in range(N) if A[i,j] == 1] for i in range(N)}
seen = {0}
frontier = [0]
while frontier:
    u = frontier.pop()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            frontier.append(v)
assert len(seen) == N

# Exact failure of edge transitivity: common-neighbor count is an invariant of an edge.
common_counts = {}
for u,v in EDGES:
    c = len(set(adj[u]).intersection(adj[v]))
    common_counts[(u,v)] = c
common_values = set(common_counts.values())
assert common_values == {0,1,2}
assert common_counts[(0,1)] == 2
assert common_counts[(2,4)] == 0

z = sp.symbols("z")
charpoly = sp.factor(A.charpoly(z).as_expr())
expected_charpoly = (z-3)*(z-1)*(z+1)**4*(z**2-5)
assert sp.expand(charpoly - expected_charpoly) == 0

sqrt5 = sp.sqrt(5)
roots = [sp.Integer(3), sqrt5, sp.Integer(1), sp.Integer(-1), -sqrt5]
I = sp.eye(N)

def spectral_projector(r):
    E = sp.eye(N)
    for s in roots:
        if s != r:
            E = sp.simplify(E * (A - s*I)/(r-s))
    E = E.applyfunc(sp.simplify)
    assert (E*E-E).applyfunc(sp.simplify) == sp.zeros(N)
    assert (A*E-r*E).applyfunc(sp.simplify) == sp.zeros(N)
    return E

expected = {
    sp.Integer(3): (sp.Rational(1,8), sp.Rational(1,8), sp.Integer(1)),
    sqrt5: (
        sp.Rational(1,8)-sqrt5/sp.Integer(40),
        sqrt5/sp.Integer(20),
        (sp.Integer(1)+sqrt5)/2,
    ),
    sp.Integer(1): (sp.Rational(1,4), sp.Integer(0), sp.Integer(0)),
    sp.Integer(-1): (sp.Rational(3,8), -sp.Rational(1,8), -sp.Rational(1,3)),
    -sqrt5: (
        sp.Rational(1,8)+sqrt5/sp.Integer(40),
        -sqrt5/sp.Integer(20),
        (sp.Integer(1)-sqrt5)/2,
    ),
}

rows = []
for r in roots:
    E = spectral_projector(r)
    alpha = sp.simplify(E[X,X])
    beta = sp.simplify(E[X,Y])
    phi = sp.simplify(beta/alpha)
    ea, eb, ep = expected[r]
    assert sp.simplify(alpha-ea) == 0
    assert sp.simplify(beta-eb) == 0
    assert sp.simplify(phi-ep) == 0
    rows.append((r, sp.trace(E), alpha, beta, phi))

# Rate-one normalized Laplacian L=I-A/3.
lambda_star = sp.simplify(1 - sqrt5/3)
alpha_star = expected[sqrt5][0]
phi_star = expected[sqrt5][2]
assert lambda_star > 0
assert phi_star > 1

# Connected 3-regular graph: stationary spectral projector is J/n, so the
# ratio tends to one. The first non-stationary local exponential is r=sqrt(5).
# Its exact coefficient in r_{20}(t)-1 is n*alpha_*(phi_*-1).
coefficient = sp.simplify(N * alpha_star * (phi_star - 1))
expected_coefficient = sp.simplify((3*sqrt5 - 5)/5)
assert sp.simplify(coefficient - expected_coefficient) == 0
assert coefficient > 0

derivative_leading_coefficient = sp.simplify(-lambda_star * coefficient)
assert derivative_leading_coefficient < 0

print("graph_order", N)
print("degree", D)
print("witness_arc", X, Y)
print("common_neighbor_values", sorted(common_values))
print("not_edge_transitive_certificate", "edge(0,1)=2 edge(2,4)=0")
print("charpoly", charpoly)
for r,tr,alpha,beta,phi in rows:
    print("projector", "adj_eigenvalue=", r, "mult=", tr,
          "alpha=", alpha, "beta=", beta, "phi=", phi)
print("lambda_star", lambda_star)
print("phi_star", phi_star)
print("ratio_asymptotic_coefficient", coefficient)
print("derivative_leading_coefficient", derivative_leading_coefficient)
print("eventual_derivative_sign", "NEGATIVE")
print("source_class_status", "OUTSIDE_ARC_TRANSITIVE_CLASS")
print("RESULT PASS")
