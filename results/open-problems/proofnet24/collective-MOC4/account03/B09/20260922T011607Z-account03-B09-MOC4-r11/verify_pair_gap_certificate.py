from fractions import Fraction
from itertools import permutations

S4 = list(permutations(range(4)))
S3 = list(permutations(range(3)))
PAIR_REPS = [(0, 1), (0, 2), (0, 3)]
PAIR_CLASSES = [
    {frozenset((0, 1)), frozenset((2, 3))},
    {frozenset((0, 2)), frozenset((1, 3))},
    {frozenset((0, 3)), frozenset((1, 2))},
]


def pair_class(S):
    F = frozenset(S)
    for k, C in enumerate(PAIR_CLASSES):
        if F in C:
            return k
    raise AssertionError(F)


def rho(sig):
    return tuple(pair_class((sig[i], sig[j])) for i, j in PAIR_REPS)


# Exact coefficients for the genuinely complex example
# a=(-2+i,-3+3i,3-3i,i), b=(3+i,-3i,-3+2i,-1-i), eta=1.
C0 = Fraction(60)
C = [
    [Fraction(41, 4), Fraction(-167, 4), Fraction(59, 4), Fraction(-101, 4)],
    [Fraction(103, 4), Fraction(-313, 4), Fraction(157, 4), Fraction(-475, 4)],
    [Fraction(-545, 4), Fraction(359, 4), Fraction(301, 4), Fraction(413, 4)],
    [Fraction(209, 4), Fraction(-487, 4), Fraction(251, 4), Fraction(-173, 4)],
]
X = [
    [Fraction(0), Fraction(-48), Fraction(54)],
    [Fraction(0), Fraction(48), Fraction(-54)],
    [Fraction(120), Fraction(-82), Fraction(-84)],
]

x = {p: sum(X[i][p[i]] for i in range(3)) for p in S3}
c = {s: sum(C[i][s[i]] for i in range(4)) for s in S4}
endpoint = {s: c[s] + Fraction(1, 2) * x[rho(s)] for s in S4}

x_order = sorted(x.items(), key=lambda kv: kv[1], reverse=True)
rho0, x0 = x_order[0]
x1 = x_order[1][1]
gamma = x0 - x1
cmax = max(c.values())
M = max(endpoint.values())
kappa = cmax + Fraction(1, 2) * x0 - M
assert rho0 == (2, 1, 0)
assert x0 == 222 and x1 == 18 and gamma == 204
assert cmax == 156 and M == 264 and kappa == 3
assert gamma >= 6 * kappa

# Verify endpoint reconstruction against all 24 direct Gaussian-integer products.
a = [(-2, 1), (-3, 3), (3, -3), (0, 1)]
b = [(3, 1), (0, -3), (-3, 2), (-1, -1)]


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gprod(zs):
    z = (1, 0)
    for w in zs:
        z = gmul(z, w)
    return z


for s in S4:
    direct_real = gprod([gadd(a[i], b[s[i]]) for i in range(4)])[0]
    assert C0 + endpoint[s] == direct_real

# Verify the Hadamard representation of S4 is exactly the 24 W(D3)
# signed permutation matrices and the nonidentity relative trace bound is 1.
hrows = [
    [1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def transpose(A):
    return [list(row) for row in zip(*A)]


H = [[Fraction(v, 2) for v in row] for row in hrows]
HT = transpose(H)
Ws = []
for s in S4:
    P = [[Fraction(int(s[i] == j)) for j in range(4)] for i in range(4)]
    HPHT = matmul(matmul(H, P), HT)
    assert HPHT[0][0] == 1
    assert all(HPHT[0][j] == 0 for j in range(1, 4))
    assert all(HPHT[i][0] == 0 for i in range(1, 4))
    W = tuple(tuple(HPHT[i][j] for j in range(1, 4)) for i in range(1, 4))
    nz = []
    cols = []
    for i in range(3):
        row = [j for j in range(3) if W[i][j] != 0]
        assert len(row) == 1 and abs(W[i][row[0]]) == 1
        cols.append(row[0])
        nz.append(W[i][row[0]])
    assert len(set(cols)) == 3
    assert nz[0] * nz[1] * nz[2] == 1
    Ws.append(W)
assert len(set(Ws)) == 24


def frob(A, B):
    return sum(A[i][j] * B[i][j] for i in range(3) for j in range(3))


W0 = Ws[0]
assert frob(W0, W0) == 3
assert max(frob(W, W0) for W in Ws if W != W0) == 1

print("PAIR_GAP_CERTIFICATE_EXACT_CHECK=PASS")
print("rho0=", rho0)
print("x0=", x0, "x1=", x1, "gamma=", gamma)
print("cmax=", cmax, "mixed_endpoint_M=", M, "kappa=", kappa)
print("gamma_minus_6kappa=", gamma - 6 * kappa)
print("full_support_endpoint_max=", C0 + M)
print("independent_assignment_upper=", C0 + cmax + Fraction(1, 2) * x0)
print("weyl_elements_checked=", len(Ws))
