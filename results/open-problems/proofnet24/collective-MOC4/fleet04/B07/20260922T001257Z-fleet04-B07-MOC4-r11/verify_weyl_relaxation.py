from fractions import Fraction as F
from itertools import permutations

# Exact arithmetic counterexample to the naive Birkhoff/S6 relaxation only.
# It is NOT a counterexample to MOC4.  Spectra are real and eta=1.
a = [F(4), F(5), F(-4), F(2)]
b = [F(2), F(5), F(-3), F(3)]
pairs = [(0, 1), (0, 2), (0, 3)]
comps = [(2, 3), (1, 3), (1, 2)]
h = [[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
# Six two-subsets, grouped into the three complement pairs.
allpairs = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]


def prod(xs):
    z = F(1)
    for x in xs:
        z *= x
    return z


atri = [prod(a[k] for k in range(4) if k != i) for i in range(4)]
btri = [prod(b[k] for k in range(4) if k != i) for i in range(4)]
W = [[atri[i] * b[j] + a[i] * btri[j] for j in range(4)] for i in range(4)]

Aplus, Aminus, Bplus, Bminus = [], [], [], []
for S, Sc in zip(pairs, comps):
    ps, pc = prod(a[i] for i in S), prod(a[i] for i in Sc)
    qs, qc = prod(b[i] for i in S), prod(b[i] for i in Sc)
    Aplus.append(pc + ps)
    Aminus.append(pc - ps)
    Bplus.append(qs + qc)
    Bminus.append(qs - qc)

X = [[Aplus[i] * Bplus[j] for j in range(3)] for i in range(3)]
Y = [[Aminus[i] * Bminus[j] for j in range(3)] for i in range(3)]
Z = [[
    sum(F(h[al][i]) * Y[al][be] * h[be][j]
        for al in range(3) for be in range(3)) / 8
    for j in range(4)] for i in range(4)]
C = [[W[i][j] + Z[i][j] for j in range(4)] for i in range(4)]
# Lower 3x3 block of H C H^T for normalized 4x4 Walsh-Hadamard H.
G = [[
    sum(F(h[al][i]) * C[i][j] * h[be][j]
        for i in range(4) for j in range(4)) / 4
    for be in range(3)] for al in range(3)]

# A complement-symmetric 6x6 squared-minor matrix has each 2x2 block
# [[q+,q-],[q-,q+]].  This cost makes its block contribution equal
# G*(q+-q-) + (X/2)*(q++q-), i.e. the nonconstant part of (MI).
K = [[F(0) for _ in range(6)] for _ in range(6)]
for al in range(3):
    for be in range(3):
        same = G[al][be] + X[al][be] / 2
        flip = -G[al][be] + X[al][be] / 2
        block = [[same / 2, flip / 2], [flip / 2, same / 2]]
        for u in range(2):
            for v in range(2):
                K[2 * al + u][2 * be + v] = block[u][v]


def score(p):
    return sum(K[i][p[i]] for i in range(6))


idx = {tuple(sorted(S)): i for i, S in enumerate(allpairs)}


def induced(sig):
    return tuple(idx[tuple(sorted((sig[S[0]], sig[S[1]])))] for S in allpairs)


weyl = set(induced(sig) for sig in permutations(range(4)))
comp = [1, 0, 3, 2, 5, 4]
centralizer = [
    p for p in permutations(range(6))
    if all(p[comp[i]] == comp[p[i]] for i in range(6))
]

best6 = max((score(p), p) for p in permutations(range(6)))
best48 = max((score(p), p) for p in centralizer)
best24 = max((score(p), p) for p in weyl)

print("S4_Weyl_size", len(weyl))
print("complement_centralizer_size", len(centralizer))
print("best_S6", best6)
print("best_centralizer48", best48)
print("best_Weyl24", best24)
print("relaxation_gap", best48[0] - best24[0])

assert len(weyl) == 24
assert len(centralizer) == 48
assert best6 == best48
assert best48[0] > best24[0]
