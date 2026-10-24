from fractions import Fraction as F
from itertools import permutations, combinations


def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cscale(x, z):
    return (x * z[0], x * z[1])


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def parity(sig):
    inv = sum(sig[i] > sig[j] for i in range(len(sig)) for j in range(i + 1, len(sig)))
    return -1 if inv % 2 else 1


def detc(M):
    n = len(M)
    out = ZERO
    for sig in permutations(range(n)):
        z = ONE
        for i in range(n):
            z = cmul(z, M[i][sig[i]])
        out = cadd(out, cscale(F(parity(sig)), z))
    return out


def ddet(M, Y):
    n = len(M)
    out = ZERO
    for sig in permutations(range(n)):
        s = F(parity(sig))
        for r in range(n):
            z = Y[r][sig[r]]
            for i in range(n):
                if i != r:
                    z = cmul(z, M[i][sig[i]])
            out = cadd(out, cscale(s, z))
    return out


U = [
    [F(0), F(16, 25), F(-48, 65), F(69, 325)],
    [F(16, 25), F(-72, 125), F(-33, 65), F(-48, 1625)],
    [F(-69, 325), F(48, 1625), F(-16, 65), F(-1536, 1625)],
    [F(48, 65), F(33, 65), F(24, 65), F(-16, 65)],
]

a = [
    (F(131), F(475)),
    (F(228), F(-102)),
    (F(462), F(-650)),
    (F(-32), F(-241)),
]

b = [
    (F(-415), F(116)),
    (F(95), F(414)),
    (F(43), F(-27)),
    (F(242), F(-757)),
]

pairs = list(combinations(range(4), 2))
perms = list(permutations(range(4)))

# Exact true-unitary checks.
for i in range(4):
    for j in range(4):
        s = sum(U[k][i] * U[k][j] for k in range(4))
        assert s == (1 if i == j else 0)
assert U[0][0] == 0
assert all(U[i][j] != 0 for i in range(4) for j in range(4) if (i, j) != (0, 0))

P = [[U[i][j] * U[i][j] for j in range(4)] for i in range(4)]


def minor2(I, J):
    i, k = I
    j, l = J
    return U[i][j] * U[k][l] - U[i][l] * U[k][j]


Q = [[minor2(I, J) ** 2 for J in pairs] for I in pairs]
assert all(Q[i][j] > 0 for i in range(6) for j in range(6))

# Actual spectral product coefficient array c_{I,J}=Re(a_{I^c} b_J), eta=1.
c = [[F(0) for _ in range(6)] for __ in range(6)]
for ii, I in enumerate(pairs):
    Ic = tuple(k for k in range(4) if k not in I)
    ax = cmul(a[Ic[0]], a[Ic[1]])
    for jj, J in enumerate(pairs):
        by = cmul(b[J[0]], b[J[1]])
        c[ii][jj] = cmul(ax, by)[0]


def Csig(sig):
    val = F(0)
    for jj, J in enumerate(pairs):
        image = tuple(sorted(sig[j] for j in J))
        ii = pairs.index(image)
        val += c[ii][jj]
    return val


# Exact feasible dual for the Birkhoff-fiber degree-two roof.
alpha = [
    [126655448444, 0, -102457185513, 0],
    [0, 96351785232, -89339824904, 113074058088],
    [0, 147815794082, -97607125232, 0],
    [0, 135894792956, 4675143533, 68434297596],
]

slacks = []
for sig in perms:
    lhs = sum(F(alpha[sig[j]][j]) for j in range(4))
    slacks.append(lhs - Csig(sig))
assert min(slacks) >= 0

actual = sum(c[ii][jj] * Q[ii][jj] for ii in range(6) for jj in range(6))
roof_upper = sum(F(alpha[i][j]) * P[i][j] for i in range(4) for j in range(4))
gap = actual - roof_upper
assert actual == F(-23917095479166582022, 2231328125)
assert roof_upper == F(-2601689915707196, 203125)
assert gap == F(4662468244876966038, 2231328125)
assert gap > 0

# Build C=U diag(b) U^T and X=diag(a)+C exactly.
C = [[ZERO for _ in range(4)] for __ in range(4)]
for i in range(4):
    for j in range(4):
        z = ZERO
        for k in range(4):
            z = cadd(z, cscale(U[i][k] * U[j][k], b[k]))
        C[i][j] = z
X = [[C[i][j] for j in range(4)] for i in range(4)]
for i in range(4):
    X[i][i] = cadd(X[i][i], a[i])
D = detc(X)
assert D == (
    F(-157616417606899340822, 2231328125),
    F(-90596533868255638604, 2231328125),
)

# Exact strict target-hull certificate.
verts = []
for sig in perms:
    z = ONE
    for i in range(4):
        z = cmul(z, cadd(a[i], b[sig[i]]))
    verts.append(z)
tri = [(2, 1, 3, 0), (2, 3, 1, 0), (3, 2, 1, 0)]
w = [
    F(197311889666051743468319177889, 539561815388344699015446875000),
    F(171410687948426629095192719811, 539561815388344699015446875000),
    F(1708392377738663264519349773, 5395618153883446990154468750),
]
assert all(x > 0 for x in w) and sum(w) == 1
Dz = ZERO
for ww, sig in zip(w, tri):
    Dz = cadd(Dz, cscale(ww, verts[perms.index(sig)]))
assert Dz == D

# Genuine left pair derivative for K_01=E_01-E_10.
K = [[F(0) for _ in range(4)] for __ in range(4)]
K[0][1] = F(1)
K[1][0] = F(-1)


def matmul(A, B):
    n, m, q = len(A), len(B[0]), len(B)
    R = [[ZERO for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for j in range(m):
            z = ZERO
            for k in range(q):
                aa = A[i][k] if isinstance(A[i][k], tuple) else (A[i][k], F(0))
                bb = B[k][j] if isinstance(B[k][j], tuple) else (B[k][j], F(0))
                z = cadd(z, cmul(aa, bb))
            R[i][j] = z
    return R


KC = matmul(K, C)
CK = matmul(C, K)
dC = [[csub(KC[i][j], CK[i][j]) for j in range(4)] for i in range(4)]
dD = ddet(X, dC)
g01 = dD[0]
assert g01 == F(237314454727650397056, 2231328125)
assert g01 > 0

print("orthogonal_exact=PASS")
print("unique_zero_entry=PASS")
print("all_36_two_minors_nonzero=PASS")
print("spectral_coefficients_actual=PASS")
print("dual_min_slack=", min(slacks))
print("dual_max_slack=", max(slacks))
print("degree2_actual=", actual)
print("degree2_roof_upper=", roof_upper)
print("spectral_roof_gap=", gap)
print("determinant=", D)
print("triangle_weights=", w)
print("target_hull_strict_certificate=PASS")
print("pair_derivative_K01=", g01)
print("not_stationary=PASS")
print("PASS exact source-valid spectral-roof adversary")
