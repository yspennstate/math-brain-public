from fractions import Fraction as F
from itertools import permutations
from math import factorial, log, pi

# -----------------------------------------------------------------------------
# Part A: exact finite self-check for the Z^4 critical Green-overlap calculation.
# -----------------------------------------------------------------------------

def p_return_4d(n: int) -> F:
    if n < 0 or n % 2:
        return F(0, 1)
    m = n // 2
    fac = [factorial(j) for j in range(m + 1)]
    s = F(0, 1)
    for a in range(m + 1):
        for b in range(m - a + 1):
            for c in range(m - a - b + 1):
                d = m - a - b - c
                s += F(1, fac[a]**2 * fac[b]**2 * fac[c]**2 * fac[d]**2)
    return F(factorial(2*m), 8**(2*m)) * s


def critical_overlap_partial_sum(T: int) -> F:
    # By the exact convolution identity this is
    # sum_{n=0}^T (n+1) P_0(X_n=0).
    return sum((n + 1) * p_return_4d(n) for n in range(T + 1))

Ts = [8, 16, 32, 64]
K = {T: critical_overlap_partial_sum(T) for T in Ts}
assert all(K[T] > 0 for T in Ts)
assert all(K[Ts[j+1]] > K[Ts[j]] for j in range(len(Ts)-1))

print('I0005_Z4_OVERLAP_EXACT_SELF_CHECK=PASS')
for T in Ts:
    v = K[T]
    print(f'T={T}: K_T(0)={v.numerator}/{v.denominator}')
for j in range(1, len(Ts)):
    T = Ts[j]
    inc = K[T] - K[T//2]
    print(f'T={T}: dyadic_increment={inc.numerator}/{inc.denominator} ~= {float(inc):.15f}')
print(f'asymptotic_dyadic_target_decimal_only={(4/pi**2)*log(2):.15f}')

# -----------------------------------------------------------------------------
# Part B: independent exact arithmetic audit of P02's unsigned-matching no-go.
# The data are re-entered here; this script does not import or execute P02 code.
# -----------------------------------------------------------------------------

def inv(A):
    n = len(A)
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        pivot_row = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[pivot_row] = M[pivot_row], M[col]
        pivot = M[col][col]
        M[col] = [x / pivot for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            z = M[r][col]
            if z:
                M[r] = [M[r][j] - z*M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]


def det(A):
    A = [row[:] for row in A]
    ans = F(1)
    n = len(A)
    for col in range(n):
        pivot_row = next((r for r in range(col, n) if A[r][col] != 0), None)
        if pivot_row is None:
            return F(0)
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            ans = -ans
        pivot = A[col][col]
        ans *= pivot
        for r in range(col + 1, n):
            if A[r][col]:
                z = A[r][col] / pivot
                for j in range(col + 1, n):
                    A[r][j] -= z*A[col][j]
    return ans


def permanent(A):
    total = F(0)
    for sig in permutations(range(len(A))):
        term = F(1)
        for i, j in enumerate(sig):
            term *= A[i][j]
        total += term
    return total

P = [
    [F(1,2), F(1,2), F(0),   F(0)],
    [F(1,2), F(0),   F(1,2), F(0)],
    [F(0),   F(1,2), F(0),   F(1,2)],
    [F(0),   F(0),   F(1,2), F(1,2)],
]
assert all(P[i][j] == P[j][i] for i in range(4) for j in range(4))
assert all(sum(row) == 1 for row in P)

stationary = [F(1,4)] * 4
Pi = [[stationary[j] for j in range(4)] for _ in range(4)]
I = [[F(int(i == j)) for j in range(4)] for i in range(4)]
B = [[I[i][j] - P[i][j] + Pi[i][j] for j in range(4)] for i in range(4)]
Binv = inv(B)
Z = [[Binv[i][j] - Pi[i][j] for j in range(4)] for i in range(4)]

i, j, k, l = 0, 1, 2, 3
D = [
    [Z[k][k], Z[l][k], -stationary[k]],
    [Z[k][l], Z[l][l], -stationary[l]],
    [F(1),    F(1),     F(0)],
]
N = [
    [Z[k][k], Z[l][k], -stationary[k], Z[i][k]],
    [Z[k][l], Z[l][l], -stationary[l], Z[i][l]],
    [F(1),    F(1),     F(0),           F(1)],
    [Z[k][j], Z[l][j], -stationary[j], Z[i][j]],
]

# Direct killed occupation on transient states {0,1} before hitting {2,3}.
Q = [[P[a][b] for b in (0,1)] for a in (0,1)]
I2 = [[F(int(a == b)) for b in range(2)] for a in range(2)]
G = inv([[I2[a][b] - Q[a][b] for b in range(2)] for a in range(2)])
direct = G[0][1]
signed = det(N) / det(D)
unsigned = permanent(N) / permanent(D)

assert direct == F(2)
assert signed == direct
assert unsigned == F(1,24)
assert unsigned != direct
print('P02_D4_UNSIGNED_MATCHING_INDEPENDENT_AUDIT=PASS')
print(f'direct={direct}; detD={det(D)}; detN={det(N)}; signed={signed}')
print(f'permD={permanent(D)}; permN={permanent(N)}; unsigned={unsigned}')
print('ALL_EXACT_ASSERTIONS_PASS')
