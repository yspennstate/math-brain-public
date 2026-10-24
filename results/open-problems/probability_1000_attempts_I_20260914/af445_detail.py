"""Detail of a lumping example for Aldous-Fill 4.45: print pi, the matrices A_ij = E_i T_j - E_pi T_j for the original and the induced chain, and the argmax."""
import numpy as np, sys
from mpmath import mp, mpf, matrix
mp.dps = 30
def analyse(W, p):
    n = len(W); W = [[mpf(x) for x in row] for row in W]
    w = [sum(r) for r in W]; pi = [w[i] / sum(w) for i in range(n)]
    Q = matrix(n, n)
    for i in range(n):
        for j in range(n):
            if i != j: Q[i, j] = W[i][j] / w[i]
        Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    def tau12(Q, pi):
        m = Q.rows; Pi = matrix(m, m)
        for i in range(m):
            for j in range(m): Pi[i, j] = pi[j]
        Z = (Pi - Q) ** -1 - Pi
        A = [[-Z[i, j] / pi[j] for j in range(m)] for i in range(m)]
        best = max((A[i][j], i, j) for i in range(m) for j in range(m))
        return best, A, Z
    (t0, i0, j0), A, Z = tau12(Q, pi)
    print("original: pi =", [mp.nstr(x, 6) for x in pi], " tau12 =", mp.nstr(t0, 10), "at (i,j) =", (i0, j0))
    for row in A: print("   ", [mp.nstr(x, 6) for x in row])
    m = max(p) + 1; hpi = [mpf(0)] * m; Qh = matrix(m, m)
    for i in range(n): hpi[p[i]] += pi[i]
    for i in range(n):
        for j in range(n):
            if i != j and p[i] != p[j]: Qh[p[i], p[j]] += pi[i] * Q[i, j]
    for a in range(m):
        for b in range(m):
            if a != b: Qh[a, b] = Qh[a, b] / hpi[a]
        Qh[a, a] = -sum(Qh[a, b] for b in range(m) if b != a)
    (t1, a0, b0), Ah, Zh = tau12(Qh, hpi)
    print("induced (partition %s): hat pi =" % p, [mp.nstr(x, 6) for x in hpi], " tau12 =", mp.nstr(t1, 10), "at", (a0, b0), " ratio =", mp.nstr(t1 / t0, 8))
    for row in Ah: print("   ", [mp.nstr(x, 6) for x in row])
    print("induced rates:");
    for a in range(m): print("   ", [mp.nstr(Qh[a, b], 6) for b in range(m)])
W = [[0, 0, 0.0001, 0], [0, 0.01174, 0.00012, 0.01087], [0.0001, 0.00012, 0, 0.00539], [0, 0.01087, 0.00539, 1.0]]
analyse(W, [0, 1, 2, 2])
print("\n--- simplified family: leaf 0 on 2 (weight a), 2-3 weight d, 1-3 weight c, 1-2 weight b, loop at 3 weight 1, loop at 1 weight e")
for (a, b, c, d, e) in [(1e-4, 1.2e-4, 0.0109, 0.0054, 0.0117), (1e-4, 0, 0.01, 0.005, 0.01), (1e-5, 0, 0.01, 0.005, 0), (1e-5, 0, 0.01, 0.005, 0.02), (1e-6, 0, 0.001, 0.0005, 0.002), (1e-6, 0, 0.01, 0.002, 0.02)]:
    W = [[0, 0, a, 0], [0, e, b, c], [a, b, 0, d], [0, c, d, 1.0]]
    print("params", (a, b, c, d, e)); analyse(W, [0, 1, 2, 2])
