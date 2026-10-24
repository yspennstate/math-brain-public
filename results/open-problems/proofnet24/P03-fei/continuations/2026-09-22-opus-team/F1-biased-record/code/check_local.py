"""Standalone exact checker for the local bias-stability of Numaro's gate g (numpy + fractions only).

Checks, in exact integer / rational arithmetic:
  1. the truth table hashes to the published SHA-256 f8a7bb2c...9c7839 and I(g) = 261/128, singletons 57/256, 1/256;
  2. the listed 72 coordinate permutations are automorphisms (g(sigma x) = g(x)) and the listed 72 are dual
     isomorphisms (g(pi x) = -g(-x)); the automorphisms act transitively on {0..8} and on {9..17};
  3. Lambda(v) = sum_i Inf_i v_i^2 - sum_{T: ghat(T) = 0} (sum_{i not in T} v_i ghat(T u i))^2 is positive definite
     on the balanced subspace {sum_i ghat({i}) v_i = 0}, and Lambda + c c^T (c_i = ghat({i})) is positive definite
     on R^18 (exact LDL^T, all pivots > 0).
Consequences (see the report): the one-input slack is even in the bias; all first derivatives of the flat slack
vanish at the centre; along any balanced direction the flat slack rises like eps^2 log2(1/eps^2) Lambda(v).
Usage: python check_local.py
"""
import os, hashlib, itertools
from fractions import Fraction as Fr
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
n = 18
t = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
sha = hashlib.sha256(",".join(map(str, t.tolist())).encode()).hexdigest()
assert sha == "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839", sha
T = t.astype(np.int64)


def fwht(a):
    a = a.copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        x, y = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y
        a = a.reshape(-1); h *= 2
    return a


W = fwht(T)                       # W[S] = 2^18 ghat(S), exact integers
D = 1 << n
assert int((W * W).sum()) == D * D
pc = np.array([bin(x).count("1") for x in range(D)], dtype=np.int64)
I = Fr(int((W * W * pc).sum()), D * D)
assert I == Fr(261, 128)
c = [Fr(int(W[1 << i]), D) for i in range(n)]
assert c[:9] == [Fr(57, 256)] * 9 and c[9:] == [Fr(1, 256)] * 9 and W[0] == 0
print("1. SHA-256 ok, I(g) = 261/128, ghat({i}) = 57/256 (core), 1/256 (aux), g balanced")

# 2. symmetries: search core permutations preserving the signed core graph; aux follow the core-aux zero matching
S = {(i, j): int(W[(1 << i) | (1 << j)]) for i in range(n) for j in range(n) if i != j}
match = {i: [j for j in range(9, 18) if S[(i, j)] == 0][0] for i in range(9)}
idx = np.arange(D, dtype=np.int64)
comp = idx ^ (D - 1)


def perm_index(perm):
    y = np.zeros_like(idx)
    for i in range(n):
        y |= ((idx >> perm[i]) & 1) << i
    return y


autos, duals = [], []
for pcore in itertools.permutations(range(9)):
    ok_a = all(S[(pcore[i], pcore[j])] == S[(i, j)] for i in range(9) for j in range(i + 1, 9))
    ok_d = all(S[(pcore[i], pcore[j])] == -S[(i, j)] for i in range(9) for j in range(i + 1, 9))
    if not (ok_a or ok_d):
        continue
    perm = list(pcore) + [0] * 9
    for i in range(9):
        perm[match[i]] = match[pcore[i]]
    y = perm_index(perm)
    if ok_a and np.array_equal(T[y], T):
        autos.append(perm)
    if ok_d and np.array_equal(T[y], -T[comp]):
        duals.append(perm)
orb0 = sorted({p[0] for p in autos}); orb9 = sorted({p[9] for p in autos})
assert len(autos) == 72 and len(duals) == 72 and orb0 == list(range(9)) and orb9 == list(range(9, 18))
print("2. 72 automorphisms (transitive on core and on aux), 72 dual isomorphisms g(pi x) = -g(-x)")

# 3. exact Lambda
zero = np.nonzero(W == 0)[0]
A = np.zeros((len(zero), n), dtype=np.int64)
for i in range(n):
    notin = ((zero >> i) & 1) == 0
    A[notin, i] = W[zero[notin] | (1 << i)]
AtA = A.T.astype(object) @ A.astype(object)
Lam = [[(c[i] if i == j else Fr(0)) - Fr(int(AtA[i, j]), D * D) for j in range(n)] for i in range(n)]


def ldl_pivots(M):
    M = [row[:] for row in M]; piv = []
    for k in range(len(M)):
        d = M[k][k]; piv.append(d)
        if d <= 0:
            return piv, False
        for i in range(k + 1, len(M)):
            f = M[i][k] / d
            for j in range(k, len(M)):
                M[i][j] -= f * M[k][j]
    return piv, True


B = []
for j in range(1, n):
    v = [Fr(0)] * n; v[j] = Fr(1); v[0] = -c[j] / c[0]; B.append(v)
Mb = [[sum(B[a][i] * sum(Lam[i][k] * B[b][k] for k in range(n)) for i in range(n)) for b in range(n - 1)] for a in range(n - 1)]
piv1, ok1 = ldl_pivots(Mb)
Lp = [[Lam[i][j] + c[i] * c[j] for j in range(n)] for i in range(n)]
piv2, ok2 = ldl_pivots(Lp)
assert ok1 and ok2
print("3. Lambda on the balanced subspace: 17 pivots > 0 (min %.6e); Lambda + c c^T: 18 pivots > 0 (min %.6e)"
      % (float(min(piv1)), float(min(piv2))))
print("   Lambda diagonal: core %s, aux %s" % (Lam[0][0], Lam[9][9]))
print("ALL CHECKS PASSED")
