#!/usr/bin/env python3
"""P26 independent exact checker for R01/I0024 (Aldous-Fill Open Problem 3.44).

Checks the weighted-divergence/singular-value formulation on:
  (i) P4, K3, a weighted triangle (legacy P26 cases), and
  (ii) a nonuniform reversible three-state chain with self-loops.

All computations are exact SymPy rationals. This is only the finite core;
the universal singular-value proof is written in the P26 run report.
"""
import sympy as sp
Q = sp.Rational


def graph_data(weights):
    n = max(max(e) for e in weights) + 1
    deg = [sum(w for (i, j), w in weights.items() if i == v or j == v) for v in range(n)]
    W = sum(deg)
    pi = [sp.simplify(d / W) for d in deg]
    edges = sorted(weights)
    B = sp.zeros(n, len(edges))
    for k, (i, j) in enumerate(edges):
        B[i, k] = 1
        B[j, k] = -1
    C = sp.diag(*[sp.simplify(weights[e] / W) for e in edges])
    Pi = sp.diag(*pi)
    P = sp.zeros(n)
    for (i, j), w in weights.items():
        P[i, j] = sp.simplify(w / deg[i])
        P[j, i] = sp.simplify(w / deg[j])
    L = sp.simplify(B * C * B.T)
    assert L == sp.simplify(Pi * (sp.eye(n) - P))
    J = sp.ones(n, n)
    Lp = sp.simplify((L + J / Q(n)).inv() - J / Q(n))
    return n, pi, edges, B, C, Pi, P, L, Lp


def tau(P):
    ev = []
    for z, m in P.eigenvals().items():
        ev += [sp.simplify(z)] * m
    ev = sorted(ev, key=lambda z: float(sp.N(z)), reverse=True)
    return sp.simplify(1 / (1 - ev[1]))


def check_gram(name, weights):
    n, pi, edges, B, C, Pi, P, L, Lp = graph_data(weights)
    p = sp.Matrix(pi)
    Psi = sp.zeros(len(edges), n)
    R = sp.simplify(C * B.T * Lp)
    for x in range(n):
        b = sp.zeros(n, 1)
        b[x] = 1
        b -= p
        Psi[:, x] = sp.simplify(R * b)
        assert sp.simplify(B * Psi[:, x] - b) == sp.zeros(n, 1)
    assert sp.simplify(Psi * p) == sp.zeros(len(edges), 1)
    G = sp.simplify(Psi.T * C.inv() * Psi)
    H = sp.zeros(n, n - 1)
    for i in range(n - 1):
        H[i, i] = 1
        H[n - 1, i] = -pi[i] / pi[n - 1]
    lam = sp.symbols("lam")
    poly = sp.factor((H.T * Pi * G * Pi * H - lam * (H.T * Pi * H)).det())
    vals = [sp.simplify(x) for x in sp.solve(sp.Eq(poly, 0), lam)]
    t = tau(P)
    assert max(vals, key=lambda z: float(sp.N(z))) == t
    print(name, "tau=", t, "gram_eigs=", vals)


P4 = {(0, 1): Q(1), (1, 2): Q(1), (2, 3): Q(1)}
K3 = {(0, 1): Q(1), (0, 2): Q(1), (1, 2): Q(1)}
WT = {(0, 1): Q(1), (0, 2): Q(2), (1, 2): Q(3)}
check_gram("P4", P4)
check_gram("K3", K3)
check_gram("weighted_triangle_1_2_3", WT)

# Legacy exact antisymmetric-projection test.
pi0 = [Q(1, 6), Q(1, 3), Q(1, 2)]
D = sp.Matrix([
    [0, Q(2, 3), Q(-5, 4)],
    [-Q(2, 3), 0, Q(7, 5)],
    [Q(5, 4), -Q(7, 5), 0],
])
g = D * sp.Matrix(pi0)
var = sp.simplify(sum(pi0[i] * g[i] ** 2 for i in range(3)))
ed2 = sp.simplify(sum(pi0[i] * pi0[j] * D[i, j] ** 2 for i in range(3) for j in range(3)))
margin = sp.simplify(ed2 - 2 * var)
assert margin == Q(39601, 64800)
print("projection_ed2_minus_2var=", margin)

# New stress test: nonuniform reversible chain with self-loops.
pi = sp.Matrix([Q(1, 6), Q(1, 3), Q(1, 2)])
Pi = sp.diag(*list(pi))
# Stationary edge masses c_ij = pi_i P_ij = pi_j P_ji.
c01, c02, c12 = Q(1, 24), Q(1, 12), Q(1, 8)
c00, c11, c22 = Q(1, 24), Q(1, 6), Q(7, 24)
P = sp.Matrix([
    [c00 / pi[0], c01 / pi[0], c02 / pi[0]],
    [c01 / pi[1], c11 / pi[1], c12 / pi[1]],
    [c02 / pi[2], c12 / pi[2], c22 / pi[2]],
])
assert P == sp.Matrix([
    [Q(1, 4), Q(1, 4), Q(1, 2)],
    [Q(1, 8), Q(1, 2), Q(3, 8)],
    [Q(1, 6), Q(1, 4), Q(7, 12)],
])
assert P * sp.ones(3, 1) == sp.ones(3, 1)
assert sp.simplify((pi.T * P) - pi.T) == sp.zeros(1, 3)
assert sp.simplify(Pi * P - (Pi * P).T) == sp.zeros(3)

B = sp.Matrix([[1, 1, 0], [-1, 0, 1], [0, -1, -1]])
C = sp.diag(c01, c02, c12)
L = sp.simplify(B * C * B.T)
assert L == sp.simplify(Pi * (sp.eye(3) - P))

# Spectral relaxation time.
ev = sorted(
    [sp.simplify(x) for x, m in P.eigenvals().items() for _ in range(m)],
    key=lambda z: float(sp.N(z)),
    reverse=True,
)
assert ev == [Q(1), Q(1, 4), Q(1, 12)]
tau2 = sp.simplify(1 / (1 - ev[1]))
assert tau2 == Q(4, 3)

# Moore-Penrose Laplacian inverse and exact minimum-energy quotient.
J = sp.ones(3, 3)
Lp = sp.simplify((L + J / Q(3)).inv() - J / Q(3))
H = sp.Matrix([[1, 0], [0, 1], [-1, -1]])  # basis for sum-zero demands
Menergy = sp.simplify(H.T * Lp * H)
Mnorm = sp.simplify(H.T * Pi.inv() * H)
lam = sp.symbols("lam")
poly = sp.factor((Menergy - lam * Mnorm).det())
vals = sorted(
    [sp.simplify(x) for x in sp.solve(sp.Eq(poly, 0), lam)],
    key=lambda z: float(sp.N(z)),
)
assert vals == [Q(12, 11), Q(4, 3)]
assert vals[-1] == tau2

# Electrical right inverse on zero-sum demands.
R = sp.simplify(C * B.T * Lp)
assert sp.simplify(B * R * H - H) == sp.zeros(3, 2)
assert sp.simplify(H.T * R.T * C.inv() * R * H - Menergy) == sp.zeros(2)

# State-to-stationarity centered flow family and Gram quotient.
M = sp.eye(3) - pi * sp.ones(1, 3)  # columns e_x - pi
Psi = sp.simplify(R * M)
assert sp.simplify(B * Psi - M) == sp.zeros(3)
assert sp.simplify(Psi * pi) == sp.zeros(3, 1)

print("self_loop_chain_P=", P.tolist())
print("self_loop_chain_eigenvalues=", ev)
print("self_loop_chain_tau2=", tau2)
print("self_loop_generalized_energy_eigs=", vals)
print("ALL_EXACT_CHECKS_PASS")
