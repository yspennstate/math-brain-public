from fractions import Fraction
from itertools import combinations


def det(M):
    M = [row[:] for row in M]
    n = len(M)
    ans = Fraction(1)
    for k in range(n):
        p = next((r for r in range(k, n) if M[r][k] != 0), None)
        if p is None:
            return Fraction(0)
        if p != k:
            M[k], M[p] = M[p], M[k]
            ans = -ans
        pivot = M[k][k]
        ans *= pivot
        for r in range(k + 1, n):
            factor = M[r][k] / pivot
            for c in range(k + 1, n):
                M[r][c] -= factor * M[k][c]
            M[r][k] = 0
    return ans


# Full target stress matrix: A=I_4-(1/3)J_4.
n = 4
A = [[Fraction(int(i == j)) - Fraction(1, 3) for j in range(n)] for i in range(n)]
ones_image = tuple(sum(row) for row in A)
assert ones_image == (Fraction(-1, 3),) * 4

# First three columns of a normalized Hadamard matrix span the eigenvalue-1 space.
H = [
    [1, 1, 1, 1],
    [1, -1, 1, -1],
    [1, 1, -1, -1],
    [1, -1, -1, 1],
]
U = [[Fraction(H[i][j], 2) for j in range(3)] for i in range(4)]

for j in range(3):
    col = [U[i][j] for i in range(4)]
    image = [sum(A[i][k] * col[k] for k in range(4)) for i in range(4)]
    assert image == col

weights = {}
triple_dets = {}
for I in combinations(range(4), 3):
    UI = [[U[i][j] for j in range(3)] for i in I]
    AI = [[A[i][j] for j in I] for i in I]
    weights[I] = det(UI) ** 2
    triple_dets[I] = det(AI)

assert set(weights.values()) == {Fraction(1, 4)}
assert sum(weights.values()) == 1
assert set(triple_dets.values()) == {Fraction(0)}

cross_dets = []
for I in combinations(range(4), 2):
    J = tuple(j for j in range(4) if j not in I)
    B = [[A[i][j] for j in J] for i in I]
    cross_dets.append(det(B))
assert set(cross_dets) == {Fraction(0)}

# H=A-diag(A) has eigenvalues -1,1/3,1/3,1/3, hence stable rank 4/3.
h_frob_sq = sum(A[i][j] ** 2 for i in range(4) for j in range(4) if i != j)
assert h_frob_sq == Fraction(4, 3)

print("A_ones=", ones_image)
print("core_pluecker_weights=", sorted(weights.values()))
print("physical_triple_determinants=", sorted(triple_dets.values()))
print("two_plus_two_cross_determinants=", sorted(cross_dets))
print("offdiag_frobenius_squared=", h_frob_sq)
print("offdiag_stable_rank=", Fraction(4, 3))
print("QFORM_PLUCKER_STRATUM_CANCELLATION_CHECK_PASS")
