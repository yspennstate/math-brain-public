from fractions import Fraction as F
from itertools import combinations, permutations

U = [
    [F(492,625), F(-31,625), F(-48,125), F(12,25)],
    [F(-9,25), F(12,25), F(-4,5), F(0)],
    [F(-36,125), F(48,125), F(9,25), F(4,5)],
    [F(-256,625), F(-492,625), F(-36,125), F(9,25)],
]
a = [F(1), F(2), F(3), F(7)]
b = [F(5), F(2), F(2), F(3)]


def det(M):
    n = len(M)
    if n == 0:
        return F(1)
    ans = F(0)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F(1)
        for i, j in enumerate(p):
            term *= M[i][j]
        ans += (-1 if inv % 2 else 1) * term
    return ans


def subdet(rows, cols):
    return det([[U[i][j] for j in cols] for i in rows])


def prod(xs):
    ans = F(1)
    for x in xs:
        ans *= x
    return ans


def pidx(vals, inds):
    return prod(vals[i] for i in inds)


# Exact orthogonality.
UtU = [[sum(U[k][i] * U[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
assert UtU == [[F(int(i == j)) for j in range(4)] for i in range(4)]

all4 = set(range(4))
pair_reps = [(0, 1), (0, 2), (0, 3)]

def comp(S):
    return tuple(sorted(all4 - set(S)))

P = [[U[i][j] ** 2 for j in range(4)] for i in range(4)]
q = {}
for S in combinations(range(4), 2):
    for T in combinations(range(4), 2):
        q[(S, T)] = subdet(S, T) ** 2

R = [[F(0) for _ in range(3)] for _ in range(3)]
D = [[F(0) for _ in range(3)] for _ in range(3)]
for alpha, S in enumerate(pair_reps):
    for beta, T in enumerate(pair_reps):
        R[alpha][beta] = q[(S, T)] + q[(S, comp(T))]
        D[alpha][beta] = q[(S, T)] - q[(S, comp(T))]

        # q(S,T)-q(S,T^c) = sum_{i in S,j in T}|u_ij|^2 - 1.
        z = sum(P[i][j] for i in S for j in T)
        assert D[alpha][beta] == z - 1

        # Exact common-unitary interval.
        assert abs(D[alpha][beta]) <= R[alpha][beta]
        assert R[alpha][beta] <= (1 + D[alpha][beta] ** 2) / 2

# R is doubly stochastic.
for row in R:
    assert sum(row) == 1
for beta in range(3):
    assert sum(R[alpha][beta] for alpha in range(3)) == 1

# Hadamard representation of D.
h = [
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
for alpha in range(3):
    for beta in range(3):
        rhs = F(1, 4) * sum(
            F(h[alpha][i] * h[beta][j]) * P[i][j]
            for i in range(4) for j in range(4)
        )
        assert D[alpha][beta] == rhs

# Exact Plucker relation in every oriented row plane.
for S in pair_reps:
    m = [(subdet(S, T), subdet(S, comp(T))) for T in pair_reps]
    assert m[0][0] * m[0][1] - m[1][0] * m[1][1] + m[2][0] * m[2][1] == 0

# Spectral coefficients for the exact support reduction (eta = 1 here).
Aplus, Aminus, Bplus, Bminus = [], [], [], []
for S in pair_reps:
    Aplus.append(pidx(a, comp(S)) + pidx(a, S))
    Aminus.append(pidx(a, comp(S)) - pidx(a, S))
for T in pair_reps:
    Bplus.append(pidx(b, T) + pidx(b, comp(T)))
    Bminus.append(pidx(b, T) - pidx(b, comp(T)))

W = [[
    pidx(a, [k for k in range(4) if k != i]) * b[j]
    + a[i] * pidx(b, [k for k in range(4) if k != j])
    for j in range(4)
] for i in range(4)]
X = [[Aplus[alpha] * Bplus[beta] for beta in range(3)] for alpha in range(3)]
Y = [[Aminus[alpha] * Bminus[beta] for beta in range(3)] for alpha in range(3)]
Z = [[
    F(1, 8) * sum(
        F(h[alpha][i] * h[beta][j]) * Y[alpha][beta]
        for alpha in range(3) for beta in range(3)
    )
    for j in range(4)
] for i in range(4)]
C = [[W[i][j] + Z[i][j] for j in range(4)] for i in range(4)]
C0 = prod(a) + prod(b)

mixed = (
    C0
    + sum(P[i][j] * C[i][j] for i in range(4) for j in range(4))
    + F(1, 2) * sum(R[alpha][beta] * X[alpha][beta] for alpha in range(3) for beta in range(3))
)

# Direct determinant.
Bmat = [[sum(U[i][k] * b[k] * U[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
M = [[Bmat[i][j] + (a[i] if i == j else 0) for j in range(4)] for i in range(4)]
direct = det(M)
assert mixed == direct

# Check the permutation support formula for all 24 permutations.
pair_class = {}
for idx, S in enumerate(pair_reps):
    pair_class[frozenset(S)] = idx
    pair_class[frozenset(comp(S))] = idx

max_perm = None
for sigma in permutations(range(4)):
    rho = [pair_class[frozenset(sigma[i] for i in S)] for S in pair_reps]
    reduced_vertex = (
        C0
        + sum(C[i][sigma[i]] for i in range(4))
        + F(1, 2) * sum(X[alpha][rho[alpha]] for alpha in range(3))
    )
    direct_vertex = prod(a[i] + b[sigma[i]] for i in range(4))
    assert reduced_vertex == direct_vertex
    if max_perm is None or direct_vertex > max_perm:
        max_perm = direct_vertex

print("PASS")
print("direct_det =", direct)
print("mixed_reduction =", mixed)
print("max_permutation_product =", max_perm)
print("example_support_gap =", max_perm - direct)
