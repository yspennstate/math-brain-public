from fractions import Fraction as F
from itertools import permutations


def c(re=0, im=0):
    return (F(re), F(im))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])


def prod(vals):
    z = c(1, 0)
    for x in vals:
        z = mul(z, x)
    return z


def re_eta(eta, z):
    return eta[0]*z[0] - eta[1]*z[1]


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def vandermonde(vals):
    z = c(1, 0)
    for i in range(4):
        for j in range(i + 1, 4):
            z = mul(z, sub(vals[i], vals[j]))
    return z


a = [c(-1, 1), c(-3, 0), c(-1, -3), c(-1, -1)]
b = [c(2, -2), c(-2, -1), c(0, -3), c(-1, -1)]
eta = c(-1, 2)
assert len(set(a)) == 4 and len(set(b)) == 4

reps = [(0, 1), (0, 2), (0, 3)]
comps = [(2, 3), (1, 3), (1, 2)]
h = [
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
H = [[F(x, 2) for x in row] for row in [[1, 1, 1, 1], *h]]

Aplus, Aminus, Bplus, Bminus = [], [], [], []
for S, Sc in zip(reps, comps):
    aS, aSc = prod([a[i] for i in S]), prod([a[i] for i in Sc])
    bT, bTc = prod([b[i] for i in S]), prod([b[i] for i in Sc])
    Aplus.append(add(aSc, aS))
    Aminus.append(sub(aSc, aS))
    Bplus.append(add(bT, bTc))
    Bminus.append(sub(bT, bTc))

X = [[re_eta(eta, mul(Aplus[i], Bplus[j])) for j in range(3)]
     for i in range(3)]
Y = [[re_eta(eta, mul(Aminus[i], Bminus[j])) for j in range(3)]
     for i in range(3)]


def prod_except(vals, i):
    return prod([vals[k] for k in range(4) if k != i])


ac = [prod_except(a, i) for i in range(4)]
bc = [prod_except(b, j) for j in range(4)]
W = [[re_eta(eta, add(mul(ac[i], b[j]), mul(a[i], bc[j])))
      for j in range(4)] for i in range(4)]
Z = [[F(1, 8)*sum(F(h[aa][i]*h[bb][j])*Y[aa][bb]
                    for aa in range(3) for bb in range(3))
      for j in range(4)] for i in range(4)]
C = [[W[i][j] + Z[i][j] for j in range(4)] for i in range(4)]
HC = matmul(matmul(H, C), transpose(H))
G = [[HC[i + 1][j + 1] for j in range(3)] for i in range(3)]

assert G == [
    [-F(111, 4), -F(351, 4), -F(301, 4)],
    [ F(23, 4),   F(119, 4),  -F(99, 4)],
    [ F(159, 4),  F(239, 4),  -F(51, 4)],
]
assert X == [
    [F(22),  F(18),  F(15)],
    [F(108), F(112), F(65)],
    [F(202), F(118), F(155)],
]

K = [[abs(G[i][j]) + X[i][j]/2 for j in range(3)] for i in range(3)]
perms = list(permutations(range(3)))


def aval(M, rho):
    return sum(M[i][rho[i]] for i in range(3))


def delta(rho):
    gs = [G[i][rho[i]] for i in range(3)]
    p = gs[0]*gs[1]*gs[2]
    return F(0) if p >= 0 else 2*min(abs(x) for x in gs)


Kvals = [aval(K, rho) for rho in perms]
deltas = [delta(rho) for rho in perms]
Kstar = max(Kvals)
assert Kvals.count(Kstar) == 1
i0 = Kvals.index(Kstar)
rho0 = perms[i0]
assert rho0 == (2, 1, 0)
m = min(abs(G[i][rho0[i]]) for i in range(3))
Vstar = max(k - d for k, d in zip(Kvals, deltas))
Delta = Kstar - Vstar

candidates = []
for j, rho in enumerate(perms):
    if j == i0:
        continue
    q = sum(rho[i] != rho0[i] for i in range(3))
    candidates.append(((Kstar - Kvals[j])/q, j, q))
kappa, jstar, qstar = min(candidates)
tau = perms[jstar]

assert Kvals == [F(859,4), F(859,4), F(987,4), F(1179,4), F(1045,4), F(1237,4)]
assert deltas == [F(0), F(0), F(0), F(0), F(23,2), F(119,2)]
assert m == F(119,4)
assert kappa == F(29,4) < m
assert tau == (1,2,0) and qstar == 2 and deltas[jstar] == 0
assert Delta == F(29,2) == 2*kappa
assert 2*min(m, kappa) == Delta

Va = vandermonde(a)
Vb = vandermonde(b)
assert Va == c(240,160)
assert Vb == c(-76,-168)
peer_det = mul(c(-F(1,2),0), mul(Va,Vb))
assert peer_det == c(-4320,26240)

print('PASS')
print('rho0 =', rho0)
print('m =', m)
print('kappa =', kappa)
print('nearest competitor =', tau, 'q =', qstar, 'delta_tau =', deltas[jstar])
print('Delta =', Delta)
print('2 min(m,kappa) =', 2*min(m,kappa))
print('prior kappa>=m criterion =', kappa >= m)
print('new floor certificate =', Delta <= 2*min(m,kappa))
print('peer structured determinant =', peer_det)
