"""Exact rational certificate for Aldous-Fill Open Problem 4.45 (K = 1 fails): a reversible 4-state chain with integer weights whose
stationary-flow lumping of two states has a LARGER stopping-rule mixing time tau_1^(2) = max_{i,j} (E_i T_j - E_pi T_j) = max_{ij} (-Z_ij / pi_j)."""
from fractions import Fraction as F
import sympy as sp
def chain(W):
    n = len(W); w = [sum(map(F, r)) for r in W]; tot = sum(w); pi = [x / tot for x in w]
    Q = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i != j: Q[i, j] = sp.Rational(F(W[i][j]) / w[i])
        Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    return Q, [sp.Rational(p) for p in pi]
def tau12(Q, pi):
    n = Q.rows; Pi = sp.Matrix(n, n, lambda i, j: pi[j])
    Z = (Pi - Q).inv() - Pi
    A = [[-Z[i, j] / pi[j] for j in range(n)] for i in range(n)]
    best = max((A[i][j], i, j) for i in range(n) for j in range(n))
    return best, A
def induced(Q, pi, p):
    n = Q.rows; m = max(p) + 1
    hpi = [sp.Integer(0)] * m; Qh = sp.zeros(m, m)
    for i in range(n): hpi[p[i]] += pi[i]
    for i in range(n):
        for j in range(n):
            if i != j and p[i] != p[j]: Qh[p[i], p[j]] += pi[i] * Q[i, j]
    for a in range(m):
        for b in range(m):
            if a != b: Qh[a, b] = Qh[a, b] / hpi[a]
        Qh[a, a] = -sum(Qh[a, b] for b in range(m) if b != a)
    return Qh, hpi
# integer weights: W_02 = 1, W_12 = 1, W_11 = 117 (holding), W_13 = 109, W_23 = 54, W_33 = 10000 (holding)
W = [[0, 0, 1, 0], [0, 117, 1, 109], [1, 1, 0, 54], [0, 109, 54, 10000]]
Q, pi = chain(W)
(t0, i0, j0), A = tau12(Q, pi)
Qh, hpi = induced(Q, pi, [0, 1, 2, 2])
(t1, a0, b0), Ah = tau12(Qh, hpi)
print("original pi =", [str(p) for p in pi])
print("original tau_1^(2) =", t0, "=", float(t0), "attained at (i,j) =", (i0, j0))
print("induced hat pi =", [str(p) for p in hpi])
print("induced rates matrix:"); sp.pprint(Qh)
print("induced tau_1^(2) =", t1, "=", float(t1), "attained at", (a0, b0))
print("ratio =", sp.nsimplify(t1 / t0), "=", float(t1 / t0))
# also the same for the raw optimiser weights scaled by 10^5 (rounded), as a second witness
W2 = [[0, 0, 10, 0], [0, 1174, 12, 1087], [10, 12, 0, 539], [0, 1087, 539, 100000]]
Q, pi = chain(W2); (t0, _, _), _ = tau12(Q, pi); Qh, hpi = induced(Q, pi, [0, 1, 2, 2]); (t1, _, _), _ = tau12(Qh, hpi)
print("second witness ratio =", float(t1 / t0))
