from fractions import Fraction as F
from itertools import permutations, combinations


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def det(A):
    n = len(A)
    if n == 0:
        return F(1)
    M = [row[:] for row in A]
    out = F(1)
    for i in range(n):
        p = next((k for k in range(i, n) if M[k][i]), None)
        if p is None:
            return F(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            out = -out
        q = M[i][i]
        out *= q
        for j in range(i + 1, n):
            M[i][j] /= q
        for k in range(i + 1, n):
            c = M[k][i]
            if c:
                for j in range(i + 1, n):
                    M[k][j] -= c * M[i][j]
    return out


def minor(A, I, J):
    return det([[A[i][j] for j in J] for i in I])


def givens(n, i, j, t):
    # Rational tangent-half-angle rotation.
    c = (1 - t*t)/(1 + t*t)
    s = 2*t/(1 + t*t)
    G = eye(n)
    G[i][i] = G[j][j] = c
    G[i][j] = s
    G[j][i] = -s
    return G


S4 = list(permutations(range(4)))
S3 = list(permutations(range(3)))
MATCHINGS = [
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
]


def rho(sig):
    ans = []
    for M in MATCHINGS:
        image = frozenset(frozenset((sig[a], sig[b])) for a, b in
                          (tuple(e) for e in M))
        ans.append(MATCHINGS.index(image))
    return tuple(ans)


def bvn3(R):
    """Exact greedy Birkhoff decomposition of a rational 3x3 DS matrix."""
    M = [row[:] for row in R]
    w = {p: F(0) for p in S3}
    total = F(0)
    while any(M[i][j] for i in range(3) for j in range(3)):
        p = next((p for p in S3
                  if all(M[i][p[i]] > 0 for i in range(3))), None)
        assert p is not None
        a = min(M[i][p[i]] for i in range(3))
        w[p] += a
        total += a
        for i in range(3):
            M[i][p[i]] -= a
    assert total == 1
    return w


def channels(U):
    P = [[U[i][j]*U[i][j] for j in range(4)] for i in range(4)]
    # R_{alpha,beta}: sum of the two complementary 2-minor squares.
    R = [[F(0) for _ in range(3)] for _ in range(3)]
    for a, M in enumerate(MATCHINGS):
        S = sorted(next(iter(M)))
        for b, N in enumerate(MATCHINGS):
            Ts = [sorted(e) for e in N]
            R[a][b] = sum(minor(U, S, T)**2 for T in Ts)
    return P, R


def canonical_weights(U):
    P, R = channels(U)
    mu = bvn3(R)
    nu = {}
    for sig in S4:
        A = sum(P[i][sig[i]] for i in range(4))
        nu[sig] = A/F(8) + mu[rho(sig)]/F(4) - F(1, 8)
    return P, R, mu, nu


def event(sig, I, J):
    return sorted(sig[i] for i in I) == list(J)


# (A) Pure group-combinatorial checks behind the canonical section.
for i in range(4):
    for j in range(4):
        # Every V4 coset has exactly one permutation sending i to j.
        counts = {r: 0 for r in S3}
        for sig in S4:
            if sig[i] == j:
                counts[rho(sig)] += 1
        assert set(counts.values()) == {1}

for alpha in range(3):
    for beta in range(3):
        good = [sig for sig in S4 if rho(sig)[alpha] == beta]
        assert len(good) == 8
        for i in range(4):
            for j in range(4):
                assert sum(sig[i] == j for sig in good) == 2

# (B) Dense exact rational SO(4) test, away from zero entry/minor faces.
U = eye(4)
for i, j, t in [
    (0, 1, F(1, 2)), (1, 2, F(1, 3)), (2, 3, F(1, 4)),
    (0, 2, F(1, 5)), (1, 3, F(1, 6)), (0, 3, F(1, 7))
]:
    U = mm(U, givens(4, i, j, t))

assert det(U) == 1
assert all(U[i][j] != 0 for i in range(4) for j in range(4))
assert all(minor(U, I, J) != 0
           for I in combinations(range(4), 2)
           for J in combinations(range(4), 2))

P, R, mu, nu = canonical_weights(U)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(4)) == 1 for j in range(4))
assert all(sum(row) == 1 for row in R)
assert all(sum(R[i][j] for i in range(3)) == 1 for j in range(3))
assert sum(mu.values()) == 1
assert sum(nu.values()) == 1

# P and R are exactly reproduced by nu.
for i in range(4):
    for j in range(4):
        assert sum(nu[s] for s in S4 if s[i] == j) == P[i][j]
for a in range(3):
    for b in range(3):
        assert sum(nu[s] for s in S4 if rho(s)[a] == b) == R[a][b]

# Every compound event, k=0,...,4, is exactly reproduced.
for k in range(5):
    for I in combinations(range(4), k):
        for J in combinations(range(4), k):
            lhs = sum(nu[s] for s in S4 if event(s, I, J))
            rhs = minor(U, I, J)**2
            assert lhs == rhs, (k, I, J, lhs, rhs)

# Pointwise 2-subset reconstruction identity.
for S in combinations(range(4), 2):
    Sc = tuple(i for i in range(4) if i not in S)
    alpha = next(a for a, M in enumerate(MATCHINGS)
                 if frozenset((frozenset(S), frozenset(Sc))) == M)
    for T in combinations(range(4), 2):
        Tc = tuple(i for i in range(4) if i not in T)
        beta = next(b for b, M in enumerate(MATCHINGS)
                    if frozenset((frozenset(T), frozenset(Tc))) == M)
        N = sum(P[i][j] for i in S for j in T)
        rhs = (N - 1 + R[alpha][beta])/2
        assert minor(U, S, T)**2 == rhs

# (C) Spectra-independent 4p+q certificate at the exact Hadamard point.
H = [[F(x, 2) for x in row] for row in
     [[1, 1, 1, 1], [1, -1, 1, -1],
      [1, 1, -1, -1], [1, -1, -1, 1]]]
PH, RH, muH, nuH = canonical_weights(H)
p = min(min(row) for row in PH)
q = min(min(row) for row in RH)
assert 4*p + q >= 1
assert min(nuH.values()) >= 0
for k in range(5):
    for I in combinations(range(4), k):
        for J in combinations(range(4), k):
            assert sum(nuH[s] for s in S4 if event(s, I, J)) == minor(H, I, J)**2

print("PASS MOC4-CANONICAL-PR-COMMON-LIFT-v1")
print("dense_test_detU =", det(U))
print("dense_test_min_nu =", min(nu.values()))
print("dense_test_p =", min(min(row) for row in P))
print("dense_test_q =", min(min(row) for row in R))
print("hadamard_4p_plus_q =", 4*p + q)
print("hadamard_min_nu =", min(nuH.values()))
