from fractions import Fraction as F
from itertools import permutations


def c(re=0, im=0):
    return (F(re), F(im))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def prod(vals):
    z = c(1, 0)
    for x in vals:
        z = mul(z, x)
    return z


def re_eta(eta, z):
    return eta[0] * z[0] - eta[1] * z[1]


def prod_except(vals, i):
    return prod([vals[k] for k in range(4) if k != i])


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


h = [
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
H = [[F(x, 2) for x in row] for row in [[1, 1, 1, 1], *h]]
reps = [(0, 1), (0, 2), (0, 3)]
comps = [(2, 3), (1, 3), (1, 2)]
perms = list(permutations(range(3)))

# Exact structured coefficient instance.  This is a coefficient-level stress
# point, not a counterexample to MOC4.
a = [c(0, 1), c(-1, 2), c(-2, 2), c(0, 2)]
b = [c(-1, -2), c(2, 2), c(-1, 0), c(-2, 2)]
eta = c(0, 1)
assert len(set(a)) == 4 and len(set(b)) == 4

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
ac = [prod_except(a, i) for i in range(4)]
bc = [prod_except(b, j) for j in range(4)]
W = [[re_eta(eta, add(mul(ac[i], b[j]), mul(a[i], bc[j])))
      for j in range(4)] for i in range(4)]
Z = [[F(1, 8) * sum((F(h[aa][i] * h[bb][j]) * Y[aa][bb]
                       for aa in range(3) for bb in range(3)), F(0))
      for j in range(4)] for i in range(4)]
Cmat = [[W[i][j] + Z[i][j] for j in range(4)] for i in range(4)]
HC = matmul(matmul(H, Cmat), transpose(H))
G = [[HC[i + 1][j + 1] for j in range(3)] for i in range(3)]

assert G == [
    [F(7), F(59, 2), F(21)],
    [F(-7), F(16), F(3)],
    [F(21), F(43), F(39)],
]
assert X == [
    [F(-28), F(-23), F(20)],
    [F(-32), F(-16), F(16)],
    [F(-8), F(-34), F(24)],
]

K = [[abs(G[i][j]) + X[i][j] / 2 for j in range(3)] for i in range(3)]


def aval(M, rho):
    return sum((M[i][rho[i]] for i in range(3)), F(0))


def parity_penalty(rho):
    vals = [G[i][rho[i]] for i in range(3)]
    return F(0) if vals[0] * vals[1] * vals[2] >= 0 else 2 * min(abs(x) for x in vals)


Kvals = [aval(K, rho) for rho in perms]
pen = [parity_penalty(rho) for rho in perms]
Kstar = max(Kvals)
assert Kvals.count(Kstar) == 1
rho0 = perms[Kvals.index(Kstar)]
m = min(abs(G[i][rho0[i]]) for i in range(3))
Delta = Kstar - max(Kvals[j] - pen[j] for j in range(6))
cands = []
for j, rho in enumerate(perms):
    if rho == rho0:
        continue
    q = sum(rho[i] != rho0[i] for i in range(3))
    cands.append(((Kstar - Kvals[j]) / q, j, q))
kappa, jstar, qstar = min(cands)
tau = perms[jstar]

assert rho0 == (1, 0, 2)
assert Kvals == [F(52), F(30), F(60), F(46), F(48), F(56)]
assert pen == [F(0), F(0), F(14), F(0), F(14), F(0)]
assert m == F(7)
assert kappa == F(4, 3)
assert tau == (2, 1, 0) and qstar == 3 and pen[jstar] == 0
assert Delta == F(4) > 2 * kappa

# Relabel columns so rho0 becomes the identity.
Kp = [[K[i][rho0[j]] for j in range(3)] for i in range(3)]
Gp = [[G[i][rho0[j]] for j in range(3)] for i in range(3)]

# Strengthened assignment dual.  If ell_ij are the reduced costs, then
# ell_ii=0 and ell_ij>=kappa off diagonal.  The three positive surpluses are
# exactly the extra assignment slack available to the Dual-Plucker bound.
alpha = [F(26, 3), F(0), F(82, 3)]
beta = [F(28, 3), F(-9), F(71, 3)]
ell = [[alpha[i] + beta[j] - Kp[i][j] for j in range(3)] for i in range(3)]
assert ell == [
    [F(0), F(20, 3), F(4, 3)],
    [F(4, 3), F(0), F(38, 3)],
    [F(32, 3), F(4, 3), F(0)],
]
for i in range(3):
    assert ell[i][i] == 0
    for j in range(3):
        if i != j:
            assert ell[i][j] >= kappa
surplus = [[F(0) if i == j else ell[i][j] - kappa for j in range(3)]
           for i in range(3)]
assert surplus == [
    [F(0), F(16, 3), F(0)],
    [F(0), F(0), F(34, 3)],
    [F(28, 3), F(0), F(0)],
]

# In the theorem, the cellwise AM-GM coefficient is
# c_ij=sqrt(delta_ij(delta_ij+2|G_ij|)).  Store its exact square.
c2 = {}
for i, j in [(0, 1), (1, 2), (2, 0)]:
    d = surplus[i][j]
    c2[(i, j)] = d * (d + 2 * abs(Gp[i][j]))
assert c2 == {
    (0, 1): F(928, 9),
    (1, 2): F(1768, 9),
    (2, 0): F(8008, 9),
}

print("PASS")
print("rho0 =", rho0)
print("Kvals =", Kvals)
print("parity_penalties =", pen)
print("m =", m)
print("kappa =", kappa)
print("normalized_gap_minimizer =", tau, "q =", qstar, "penalty =", pen[jstar])
print("Delta =", Delta)
print("old_two_slack_floor =", 2 * min(m, kappa))
print("dual_reduced_costs =", ell)
print("dual_surpluses =", surplus)
print("positive_plucker_coefficients_squared =", c2)
