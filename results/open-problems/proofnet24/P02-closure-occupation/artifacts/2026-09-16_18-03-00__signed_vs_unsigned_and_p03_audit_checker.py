from fractions import Fraction as F
from itertools import permutations


def inv(A):
    n = len(A)
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pivot = M[c][c]
        M[c] = [x / pivot for x in M[c]]
        for r in range(n):
            if r == c:
                continue
            z = M[r][c]
            if z:
                M[r] = [M[r][j] - z * M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]


def det(A):
    A = [row[:] for row in A]
    n = len(A)
    ans = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            ans = -ans
        pivot = A[c][c]
        ans *= pivot
        for r in range(c+1, n):
            if A[r][c] != 0:
                z = A[r][c] / pivot
                for j in range(c+1, n):
                    A[r][j] -= z * A[c][j]
    return ans


def permanent(A):
    total = F(0)
    for sig in permutations(range(len(A))):
        term = F(1)
        for i, j in enumerate(sig):
            term *= A[i][j]
        total += term
    return total


# Reversible four-state chain: symmetric, irreducible, aperiodic.
P = [
    [F(1,2), F(1,2), F(0),   F(0)],
    [F(1,2), F(0),   F(1,2), F(0)],
    [F(0),   F(1,2), F(0),   F(1,2)],
    [F(0),   F(0),   F(1,2), F(1,2)],
]
n = 4
pi = [F(1,4)] * n
Pi = [[pi[j] for j in range(n)] for _ in range(n)]
I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
B = [[I[i][j] - P[i][j] + Pi[i][j] for j in range(n)] for i in range(n)]
Binv = inv(B)
Z = [[Binv[i][j] - Pi[i][j] for j in range(n)] for i in range(n)]

# Aldous--Fill four-mark example with i=0, j=1, A={2,3}.
i, j, k, l = 0, 1, 2, 3
D = [
    [Z[k][k], Z[l][k], -pi[k]],
    [Z[k][l], Z[l][l], -pi[l]],
    [F(1),    F(1),     F(0)],
]
N = [
    [Z[k][k], Z[l][k], -pi[k], Z[i][k]],
    [Z[k][l], Z[l][l], -pi[l], Z[i][l]],
    [F(1),    F(1),     F(0),  F(1)],
    [Z[k][j], Z[l][j], -pi[j], Z[i][j]],
]
signed_ratio = det(N) / det(D)
unsigned_ratio = permanent(N) / permanent(D)

# Direct killed-chain occupation on transient states {0,1}.
Q = [[P[a][b] for b in (0,1)] for a in (0,1)]
I2 = [[F(int(a == b)) for b in range(2)] for a in range(2)]
G = inv([[I2[a][b] - Q[a][b] for b in range(2)] for a in range(2)])
direct = G[0][1]

assert direct == F(2)
assert signed_ratio == direct
assert unsigned_ratio == F(1,24)
assert unsigned_ratio != direct

print("D4_exact_reversible_counterexample=PASS")
print("P_symmetric_reversible=True")
print("direct_occupation_E0_visits1_before_T_{2,3}=", direct)
print("signed_det_denominator=", det(D))
print("signed_det_numerator=", det(N))
print("signed_ratio=", signed_ratio)
print("unsigned_permanent_denominator=", permanent(D))
print("unsigned_permanent_numerator=", permanent(N))
print("unsigned_ratio=", unsigned_ratio)

# Independent exact arithmetic for P03 n=6 high-boundary comparison:
# 96*(C6* - (16/3) h_2(3/16))
# = 3072 + 96 log2 3 + 416 log2 13 - 961 log2 31 > 0
# iff 2^3072 * 3^96 * 13^416 > 31^961.
lhs = (1 << 3072) * (3 ** 96) * (13 ** 416)
rhs = 31 ** 961
assert lhs > rhs
diff = lhs - rhs
print("P03_C6_high_boundary_exact_integer_comparison=PASS")
print("lhs_digits=", len(str(lhs)))
print("rhs_digits=", len(str(rhs)))
print("difference_digits=", len(str(diff)))
print("difference_prefix=", str(diff)[:80])
print("difference_suffix=", str(diff)[-80:])
print("ALL_EXACT_CHECKS_PASS")
