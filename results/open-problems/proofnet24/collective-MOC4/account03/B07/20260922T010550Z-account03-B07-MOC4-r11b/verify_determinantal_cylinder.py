from fractions import Fraction
from itertools import combinations, permutations

N = 4
PERMS = list(permutations(range(N)))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def event_vector(S, T):
    T = set(T)
    return [Fraction(int({p[i] for i in S} == T), 1) for p in PERMS]


def rank(M):
    A = [list(map(Fraction, row)) for row in M]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def det(M):
    n = len(M)
    if n == 0:
        return Fraction(1)
    ans = Fraction(0)
    for p in permutations(range(n)):
        z = Fraction(parity(p), 1)
        for i in range(n):
            z *= M[i][p[i]]
        ans += z
    return ans


events = []
for k in (1, 2, 3):
    for S in combinations(range(N), k):
        for T in combinations(range(N), k):
            if set(S) != set(T):
                events.append((S, T, event_vector(S, T)))
A = [[events[j][2][i] for j in range(len(events))] for i in range(len(PERMS))]


def separator(p):
    # One-based notation:
    # 1_{sigma(1)=2}+1_{sigma(2)=4}-1_{sigma({1,3})={2,3}}
    # +1_{sigma({1,4})={3,4}}.
    return (
        int(p[0] == 1)
        + int(p[1] == 3)
        - int({p[0], p[2]} == {1, 2})
        + int({p[0], p[3]} == {2, 3})
    )


s = [Fraction(separator(p), 1) for p in PERMS]
zeros = [i for i, x in enumerate(s) if x == 0]
Azero = [A[i] for i in zeros]

# Exact rational orthogonal matrix from the existing account04/B09 obstruction.
U = [
    [Fraction(492, 625), Fraction(-31, 625), Fraction(-48, 125), Fraction(12, 25)],
    [Fraction(-9, 25), Fraction(12, 25), Fraction(-4, 5), Fraction(0)],
    [Fraction(-36, 125), Fraction(48, 125), Fraction(9, 25), Fraction(4, 5)],
    [Fraction(-256, 625), Fraction(-492, 625), Fraction(-36, 125), Fraction(9, 25)],
]

mu = []
for p in PERMS:
    z = Fraction(parity(p), 1)
    for i in range(N):
        z *= U[i][p[i]]
    mu.append(z)


def minor(rows, cols):
    return det([[U[i][j] for j in cols] for i in rows])


# For this real orthogonal U, the general unitary cylinder identity reduces to
# sum_{sigma(S)=T} mu_sigma = det(U[S,T])^2.
for k in (1, 2, 3):
    for S in combinations(range(N), k):
        for T in combinations(range(N), k):
            lhs = sum(mu[j] for j, p in enumerate(PERMS) if {p[i] for i in S} == set(T))
            rhs = minor(S, T) ** 2
            assert lhs == rhs, (S, T, lhs, rhs)

print("event_columns", len(events))
print("event_span_rank", rank(A))
print("separator_values", {v: s.count(Fraction(v, 1)) for v in (0, 1, 2)})
print("separator_zero_rows", len(zeros))
print("zero_restriction_rank", rank(Azero))
print("mu_total", sum(mu))
print("separator_mu_expectation", sum(mu[i] * s[i] for i in range(len(PERMS))))
print("cylinder_identity_checks", "PASS")
