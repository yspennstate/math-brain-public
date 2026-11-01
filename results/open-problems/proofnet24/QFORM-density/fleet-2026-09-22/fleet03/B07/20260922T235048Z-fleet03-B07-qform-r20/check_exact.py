from fractions import Fraction
from itertools import combinations
import math


def det_frac(M):
    M = [list(map(Fraction, row)) for row in M]
    n = len(M)
    if n == 0:
        return Fraction(1)
    d = Fraction(1)
    for i in range(n):
        pivot = next((r for r in range(i, n) if M[r][i] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
            d = -d
        p = M[i][i]
        d *= p
        for j in range(i, n):
            M[i][j] /= p
        for r in range(i + 1, n):
            q = M[r][i]
            if q:
                for j in range(i, n):
                    M[r][j] -= q * M[i][j]
    return d


def sub(M, rows, cols):
    return [[M[i][j] for j in cols] for i in rows]


A = [[Fraction(x) for x in row] for row in [
    [2, 1, -1, 2, 0],
    [1, 3, 2, -1, 1],
    [-1, 2, 4, 1, -2],
    [2, -1, 1, 5, 1],
    [0, 1, -2, 1, 3],
]]
n = len(A)

Ws = []
for i in range(n):
    rest = [j for j in range(n) if j != i]
    a = A[i][i]
    b = [A[j][i] for j in rest]
    S = [[A[rest[r]][rest[c]] - b[r] * b[c] / a
          for c in range(n - 1)] for r in range(n - 1)]
    W = Fraction(0)
    M2 = Fraction(0)
    for Rpos in combinations(range(n - 1), 2):
        R = [rest[r] for r in Rpos]
        for Cpos in combinations(range(n - 1), 2):
            C = [rest[c] for c in Cpos]
            W += det_frac(sub(A, [i] + R, [i] + C)) ** 2
            M2 += det_frac(sub(S, Rpos, Cpos)) ** 2
    assert W == a * a * M2
    Ws.append(W)

E = [Fraction(0) for _ in range(4)]
for I in combinations(range(n), 3):
    for J in combinations(range(n), 3):
        q = len(set(I) & set(J))
        E[q] += det_frac(sub(A, I, J)) ** 2

assert sum(Ws) == E[1] + 2 * E[2] + 3 * E[3]
assert Ws == list(map(Fraction, [7877, 16736, 19581, 27032, 15619]))
assert E[1:] == list(map(Fraction, [2556, 36830, 3543]))
assert sum(Ws) == 86845

# Weak-L2 kernel constants in the proof:
# k_-(y)=|y^2-1|^{-1/2} has distribution <= 4 s^{-2};
# k_+(y)=(y^2+1)^{-1/2} has distribution <= 2 s^{-2}.
# We sample the exact formulas only as a finite sanity check; the report proves
# the inequalities analytically for all s.
for m in range(-12, 13):
    s = 2.0 ** (m / 2.0)
    delta = s ** -2
    if s > 1:
        mu_minus = 2 * (math.sqrt(1 + delta) - math.sqrt(1 - delta))
    else:
        mu_minus = 2 * math.sqrt(1 + delta)
    mu_plus = 0.0 if s >= 1 else 2 * math.sqrt(s ** -2 - 1)
    assert mu_minus <= 4 * s ** -2 + 1e-12
    assert mu_plus <= 2 * s ** -2 + 1e-12

c_zero = 16 * 3 ** (-0.25)
c_diffuse = 4 * math.sqrt(25.46)
assert abs(c_zero - 12.15737097042548) < 1e-12
assert abs(c_diffuse - 20.183161298468583) < 1e-12

print("pivot_W=", [int(x) for x in Ws])
print("overlap_E1_E2_E3=", [int(E[q]) for q in (1, 2, 3)])
print("weighted_overlap=", int(E[1] + 2 * E[2] + 3 * E[3]))
print("zero_self_composite_constant=", c_zero)
print("diffuse_twoeig_composite_constant=", c_diffuse)
print("STATUS=PASS")
