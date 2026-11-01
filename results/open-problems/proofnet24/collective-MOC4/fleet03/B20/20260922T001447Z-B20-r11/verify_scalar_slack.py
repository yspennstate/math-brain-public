from fractions import Fraction as F
from itertools import permutations

# Exact rational verifier for the example in REPORT.md.
# Complex numbers are pairs (real, imag) of Fractions.

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
    # Re(eta*z)
    return eta[0]*z[0] - eta[1]*z[1]

def det2(M, rows, cols):
    i, k = rows
    j, l = cols
    return M[i][j]*M[k][l] - M[i][l]*M[k][j]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]

def transpose(A):
    return [list(x) for x in zip(*A)]

U = [
    [F(492,625), -F(31,625), -F(48,125), F(12,25)],
    [-F(9,25), F(12,25), -F(4,5), F(0)],
    [-F(36,125), F(48,125), F(9,25), F(4,5)],
    [-F(256,625), -F(492,625), -F(36,125), F(9,25)],
]

a = [c(-2,-3), c(-2,0), c(3,1), c(-1,-2)]
b = [c(3,0), c(2,-1), c(3,-2), c(2,3)]
eta = c(-4,-5)

# Orthogonality.
UtU = matmul(transpose(U), U)
assert UtU == [[F(int(i == j)) for j in range(4)] for i in range(4)]

reps = [(0,1), (0,2), (0,3)]
comps = [(2,3), (1,3), (1,2)]
h = [
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
]
H = [[F(x,2) for x in row] for row in [
    [1,1,1,1],
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
]]

# Pair transport R and signed difference D.
R = [[F(0) for _ in range(3)] for _ in range(3)]
D = [[F(0) for _ in range(3)] for _ in range(3)]
for aa, Sset in enumerate(reps):
    for bb, Tset in enumerate(reps):
        Tc = comps[bb]
        m = det2(U, Sset, Tset)
        n = det2(U, Sset, Tc)
        q1, q2 = m*m, n*n
        R[aa][bb] = q1 + q2
        D[aa][bb] = q1 - q2
assert all(sum(row) == 1 for row in R)
assert all(sum(R[i][j] for i in range(3)) == 1 for j in range(3))

# Spectral complementary-pair arrays.
Aplus, Aminus, Bplus, Bminus = [], [], [], []
for Sset, Sc in zip(reps, comps):
    aS, aSc = prod([a[i] for i in Sset]), prod([a[i] for i in Sc])
    bT, bTc = prod([b[i] for i in Sset]), prod([b[i] for i in Sc])
    Aplus.append(add(aSc, aS))
    Aminus.append(sub(aSc, aS))
    Bplus.append(add(bT, bTc))
    Bminus.append(sub(bT, bTc))

X = [[re_eta(eta, mul(Aplus[i], Bplus[j])) for j in range(3)] for i in range(3)]
Y = [[re_eta(eta, mul(Aminus[i], Bminus[j])) for j in range(3)] for i in range(3)]

# W_ij = Re eta (a_{i^c} b_j + a_i b_{j^c}).
def prod_except(vals, i):
    return prod([vals[k] for k in range(4) if k != i])

ac = [prod_except(a, i) for i in range(4)]
bc = [prod_except(b, j) for j in range(4)]
W = [[re_eta(eta, add(mul(ac[i], b[j]), mul(a[i], bc[j])))
      for j in range(4)] for i in range(4)]

Z = [[F(1,8)*sum(F(h[aa][i]*h[bb][j])*Y[aa][bb]
                    for aa in range(3) for bb in range(3))
      for j in range(4)] for i in range(4)]
C = [[W[i][j] + Z[i][j] for j in range(4)] for i in range(4)]
HC = matmul(matmul(H, C), transpose(H))
G = [[HC[i+1][j+1] for j in range(3)] for i in range(3)]

assert G == [
    [F(755,2), F(755,2), -F(673,2)],
    [-F(1005,2), -F(801,2), F(975,2)],
    [-F(345,2), -F(345,2), F(1083,2)],
]
assert X == [
    [F(-284), F(-294), F(-148)],
    [F(-624), F(-430), F(-376)],
    [F(1110), F(1100), F(590)],
]

K = [[abs(G[i][j]) + X[i][j]/2 for j in range(3)] for i in range(3)]
perms = list(permutations(range(3)))

def aval(M, rho):
    return sum(M[i][rho[i]] for i in range(3))

def delta(rho):
    gs = [G[i][rho[i]] for i in range(3)]
    product = gs[0]*gs[1]*gs[2]
    return F(0) if product >= 0 else 2*min(abs(x) for x in gs)

Kvals = [aval(K, rho) for rho in perms]
deltas = [delta(rho) for rho in perms]
Kstar = max(Kvals)
Vstar = max(k - d for k, d in zip(Kvals, deltas))
Delta = Kstar - Vstar

A_slack = Kstar - sum(R[i][j]*K[i][j] for i in range(3) for j in range(3))

def sgn(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)

S_slack = sum(abs(G[i][j])*(R[i][j] - sgn(G[i][j])*D[i][j])
              for i in range(3) for j in range(3))

assert Kvals == [F(2515,2), F(2515,2), F(2515,2), F(2515,2), F(2351,2), F(2351,2)]
assert deltas == [F(755), F(345), F(755), F(345), F(345), F(345)]
assert Kstar == F(2515,2)
assert Vstar == F(1825,2)
assert Delta == F(345)
assert A_slack == F(2563648,390625)
assert S_slack == F(225456591,390625)
assert A_slack + S_slack == F(228020239,390625)
assert A_slack + S_slack - Delta == F(93254614,390625) > 0

# Exact scalar identity F0 = K* - A - S.
F0 = sum(D[i][j]*G[i][j] + R[i][j]*X[i][j]/2
         for i in range(3) for j in range(3))
assert F0 == Kstar - A_slack - S_slack
assert F0 <= Vstar

print("PASS")
print("K* =", Kstar)
print("V* =", Vstar)
print("Delta =", Delta)
print("A =", A_slack)
print("S =", S_slack)
print("A+S-Delta =", A_slack + S_slack - Delta)
