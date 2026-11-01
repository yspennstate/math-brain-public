"""Exact rational check that the leading small-bias form Lambda is positive definite on the balanced subspace.
Lambda(v) = sum_i Inf_i v_i^2 - sum_{T: ghat(T)=0} (sum_{i not in T} v_i ghat(T u i))^2 (T = empty included).
Balanced subspace: sum_i ghat({i}) v_i = 0.  Basis: v = e_j - (c_j/c_0) e_0, j = 1..17.  Positive definiteness of
the 17x17 Gram matrix is checked by an exact LDL^T (all pivots > 0)."""
from fractions import Fraction as Fr
import numpy as np
from gate import load_table, biased_spectrum, N

t = load_table(); c = biased_spectrum(t, [0.5] * N)
W = np.rint(c * (1 << N)).astype(np.int64)
D = 1 << N
zero = np.nonzero(W == 0)[0]
L = [[Fr(0)] * N for _ in range(N)]
for i in range(N):
    L[i][i] += Fr(int(W[1 << i]), D)
# accumulate A^T A exactly with integers (numerators over D^2)
A = np.zeros((len(zero), N), dtype=np.int64)
for i in range(N):
    notin = ((zero >> i) & 1) == 0
    A[notin, i] = W[zero[notin] | (1 << i)]
AtA = A.T.astype(object) @ A.astype(object)
for i in range(N):
    for j in range(N):
        L[i][j] -= Fr(int(AtA[i, j]), D * D)
cvec = [Fr(int(W[1 << i]), D) for i in range(N)]
B = []
for j in range(1, N):
    v = [Fr(0)] * N; v[j] = Fr(1); v[0] = -cvec[j] / cvec[0]
    B.append(v)
M = [[sum(B[a][i] * sum(L[i][k] * B[b][k] for k in range(N)) for i in range(N)) for b in range(len(B))] for a in range(len(B))]
# exact LDL^T
n = len(M); piv = []
Mw = [row[:] for row in M]
for k in range(n):
    d = Mw[k][k]
    piv.append(d)
    if d <= 0:
        print("non-positive pivot at", k, d); break
    for i in range(k + 1, n):
        f = Mw[i][k] / d
        for j in range(k, n):
            Mw[i][j] -= f * Mw[k][j]
print("pivots (float):", [float(x) for x in piv])
print("all pivots > 0:", all(x > 0 for x in piv), "; min pivot = %.6e" % float(min(piv)))
Lf = np.array([[float(x) for x in row] for row in L])
print("Lambda diagonal: core %s, aux %s" % (L[0][0], L[9][9]))

# Lambda' = Lambda + c c^T on all of R^18 (the T = empty term removed): exact LDL^T
Lp = [[L[i][j] + cvec[i] * cvec[j] for j in range(N)] for i in range(N)]
Mw = [row[:] for row in Lp]; piv2 = []
for k in range(N):
    d = Mw[k][k]; piv2.append(d)
    if d <= 0:
        print("Lambda': non-positive pivot at", k); break
    for i in range(k + 1, N):
        f = Mw[i][k] / d
        for j in range(k, N):
            Mw[i][j] -= f * Mw[k][j]
print("Lambda' = Lambda + c c^T: all 18 pivots > 0:", all(x > 0 for x in piv2), "; min pivot = %.6e" % float(min(piv2)))
