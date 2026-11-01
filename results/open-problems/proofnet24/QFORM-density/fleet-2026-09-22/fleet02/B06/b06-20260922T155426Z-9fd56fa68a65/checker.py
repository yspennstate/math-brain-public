from fractions import Fraction
from itertools import combinations
import math, json


def hadamard(n):
    H = [[1]]
    while len(H) < n:
        H = [row + row for row in H] + [row + [-x for x in row] for row in H]
    return H


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def det2(a, b, c, d):
    return a * d - b * c


# Exact Hadamard support-disjoint adversary.
n = 16
H = hadamard(n)
U = [row[:3] for row in H]
D = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
M = matmul(matmul(U, D), transpose(U))  # A = M/n
assert all(M[i][i] == 1 for i in range(n))

positive_plane_pairs = 0
support_disjoint = True
sum_w_num = 0
full_nonzero_count = 0

for i, j in combinations(range(n), 2):
    # Same-sign plane is columns 0,1.  Weight = minor^2/n^2.
    minor = U[i][0] * U[j][1] - U[i][1] * U[j][0]
    w_num = minor * minor
    # Full 2x2 principal determinant = full_det_num/n^2.
    full_det_num = M[i][i] * M[j][j] - M[i][j] * M[j][i]
    if w_num:
        positive_plane_pairs += 1
        sum_w_num += w_num
        if full_det_num != 0:
            support_disjoint = False
    if full_det_num != 0:
        full_nonzero_count += 1
        if w_num != 0:
            support_disjoint = False

assert sum_w_num == n * n
assert support_disjoint
assert positive_plane_pairs == 64
assert full_nonzero_count == 32

# Equal-leverage k=2 affine-fiber BL factor for this plane.
c = Fraction(n - 2, n)
assert Fraction(n, 2) * c == 7
bl_factor = (Fraction(8, 7)) ** 7
assert float(bl_factor) < math.e

# Exact nontrivial minority-pivot pseudodeterminant check in n=3.
R = [
    [Fraction(5, 13), Fraction(0), Fraction(12, 13)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(-12, 13), Fraction(0), Fraction(5, 13)],
]
Rt = transpose(R)
I = matmul(Rt, R)
assert I == [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
Lam = [[Fraction(2), 0, 0], [0, Fraction(1), 0], [0, 0, Fraction(-1)]]
A = matmul(matmul(R, Lam), Rt)
a = A[0][0]
assert a == Fraction(-94, 169)
S = [[A[i][j] - A[i][0] * A[0][j] / a for j in (1, 2)] for i in (1, 2)]
detS = det2(S[0][0], S[0][1], S[1][0], S[1][1])
detLam = Fraction(-2)
ell = Fraction(1)
rhs = detLam * ell / a
assert detS == rhs == Fraction(169, 47)
assert S[0][0] > 0 and S[1][1] > 0 and detS > 0

out = {
    "affine_fiber_BL_factor_exact": "(8/7)^7",
    "affine_fiber_BL_factor_float": float(bl_factor),
    "full_nonzero_pair_determinants": full_nonzero_count,
    "hadamard_n": n,
    "minority_pivot_a": str(a),
    "minority_pivot_schur_pdet": str(detS),
    "one_pivot_constant_2sqrt_2pie": 2 * math.sqrt(2 * math.pi * math.e),
    "one_pivot_pdet_identity_rhs": str(rhs),
    "pluecker_support_disjoint_from_nonzero_full_pair_determinants": support_disjoint,
    "positive_same_sign_pluecker_pairs": positive_plane_pairs,
    "same_sign_row_leverage": "2/16",
    "status": "PASS",
    "sum_same_sign_pluecker_weight": f"{sum_w_num}/{n*n}",
    "universal_projection_bound_e": math.e,
}
print(json.dumps(out, indent=2, sort_keys=True))
