"""Exact rational values of the two constants of s_inf at the uniform star K_{1,n-1}.

s_inf = (n-2) num/den - (n-1) lam + 2, with den = 2 tr(Pi G), num = 2 tr(Pi N Pi G), G = P (x) (lam I - L), where P is the
top spectral projector of L, Pi the orthogonal projector onto V = {symmetric, zero diagonal, zero row sums} in R^{n x n},
and N = sum_e w_e (I - K_e), K_e the conjugation by the transposition e. (Same quantity as parts() in t104_star_local.py:
sum_l g_l S_l S_l^* = (1/2)(I+F)(P (x) A)(I+F) and Pi F = Pi.) P and lam are expanded to second order by Kato's formulas,
in exact rationals.

c : the coefficient of |delta|^2 along delta = eps (e_1 - e_2) on the leaf weights (|delta|^2 = 2 eps^2).
c1: the first derivative along one leaf-leaf edge, with the weights renormalised to sum 1.

usage: python t104_star_exact.py nmin nmax
"""
import sys
from sympy import Matrix, Rational, eye, zeros, kronecker_product as kron


def lap(n, w):
    L = zeros(n, n)
    for (i, j), v in w.items():
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def proj_V(n):
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = [0] * (n * n); r[i * n + j] = 1; r[j * n + i] = -1; rows.append(r)
        r = [0] * (n * n); r[i * n + i] = 1; rows.append(r)
        r = [0] * (n * n)
        for j in range(n):
            r[i * n + j] = 1
        rows.append(r)
    ns = Matrix(rows).nullspace()
    assert len(ns) == n * (n - 3) // 2
    qs = []
    for v in ns:
        for q in qs:
            v = v - (q.dot(v) / q.dot(q)) * q
        qs.append(v)
    Pi = zeros(n * n, n * n)
    for q in qs:
        Pi += (q * q.T) / q.dot(q)
    return Pi


def Kop(n, i, j):
    P = eye(n); P[i, i] = 0; P[j, j] = 0; P[i, j] = 1; P[j, i] = 1
    return kron(P, P)


def series(n, Pi, Kall, w0, w1):
    """Second-order data of s along w0 + eps w1 (w1 a dict of weight changes)."""
    I = eye(n); I2 = eye(n * n)
    L0, L1 = lap(n, w0), lap(n, w1)
    N0 = zeros(n * n, n * n); N1 = zeros(n * n, n * n)
    for e, v in w0.items():
        N0 += v * (I2 - Kall[e])
    for e, v in w1.items():
        N1 += v * (I2 - Kall[e])
    lam0 = Rational(n, n - 1)
    u = Matrix([n - 1] + [-1] * (n - 1))
    P0 = (u * u.T) / u.dot(u)
    assert L0 * u == lam0 * u
    R = (lam0 * I - L0 + P0).inv() - P0
    lam1 = (P0 * L1).trace()
    lam2 = (P0 * L1 * R * L1).trace()
    P1 = R * L1 * P0 + P0 * L1 * R
    P2 = (P0 * L1 * R * L1 * R + R * L1 * P0 * L1 * R + R * L1 * R * L1 * P0
          - P0 * L1 * P0 * L1 * R * R - P0 * L1 * R * R * L1 * P0 - R * R * L1 * P0 * L1 * P0)
    A0 = lam0 * I - L0; A1 = lam1 * I - L1; A2 = lam2 * I
    G = [kron(P0, A0), kron(P1, A0) + kron(P0, A1), kron(P2, A0) + kron(P1, A1) + kron(P0, A2)]
    PG = [Pi * g for g in G]
    den = [2 * pg.trace() for pg in PG]
    PN0Pi, PN1Pi = Pi * N0 * Pi, Pi * N1 * Pi
    num = [2 * (PN0Pi * G[0]).trace(),
           2 * ((PN0Pi * G[1]).trace() + (PN1Pi * G[0]).trace()),
           2 * ((PN0Pi * G[2]).trace() + (PN1Pi * G[1]).trace())]
    f0 = num[0] / den[0]
    f1 = (num[1] - f0 * den[1]) / den[0]
    f2 = (num[2] - f0 * den[2] - f1 * den[1]) / den[0]
    s = [(n - 2) * f0 - (n - 1) * lam0 + 2, (n - 2) * f1 - (n - 1) * lam1, (n - 2) * f2 - (n - 1) * lam2]
    return s, (lam1, lam2)


for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    Pi = proj_V(n)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    Kall = {e: Kop(n, *e) for e in edges}
    a = Rational(1, n - 1)
    star = {(0, j): a for j in range(1, n)}
    # leaf-weight deviation delta = eps (e_1 - e_2); sum zero, so the total weight stays 1
    s_d, lam_d = series(n, Pi, Kall, star, {(0, 1): 1, (0, 2): -1})
    c = s_d[2] / 2
    # one leaf-leaf edge, renormalised: to first order the direction is e_12 - star
    w1 = {(1, 2): 1}
    for e, v in star.items():
        w1[e] = -v
    s_e, lam_e = series(n, Pi, Kall, star, w1)
    print("n %d  s(star) %s  s1(delta) %s  c %s  c1 %s  lam1(edge) %s" % (n, s_d[0], s_d[1], c, s_e[1], lam_e[0]), flush=True)
