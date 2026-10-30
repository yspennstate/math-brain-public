from fractions import Fraction
import math
import numpy as np

# Exact rational constants for the clean tau=3/10 corollary.
tau = Fraction(3, 10)
m = 1 - tau
detgap = m*m - 4*tau*tau
assert m == Fraction(7, 10)
assert detgap == Fraction(13, 100)

indefinite_bound = 50 * float(m) ** (-3/4)
definite_bound = math.pi / math.sqrt(float(detgap))
assert indefinite_bound < 66
assert definite_bound < 66

# Independent numerical regression of the exact rank-two Schur identity
# A-diag(0_2,S) has rank <=2 and hence s3(A)<=s1(S).
rng = np.random.default_rng(1729)
max_rank = 0
for n in range(3, 9):
    for _ in range(100):
        M = rng.normal(size=(n, n))
        A = (M + M.T) / 2
        B = A[:2, :2]
        if abs(np.linalg.det(B)) < 1e-8:
            continue
        K = A[:2, 2:]
        C = A[2:, 2:]
        S = C - K.T @ np.linalg.inv(B) @ K
        E = A.copy()
        E[2:, 2:] -= S
        rank = np.linalg.matrix_rank(E, tol=1e-8)
        max_rank = max(max_rank, int(rank))
        assert rank <= 2
        sA = np.linalg.svd(A, compute_uv=False)
        sS = np.linalg.svd(S, compute_uv=False)
        assert sA[2] <= sS[0] + 1e-8

print("tau=3/10")
print("m=7/10")
print("detgap=13/100")
print(f"opposite-sign bound={indefinite_bound:.12f}")
print(f"same-sign bound={definite_bound:.12f}")
print(f"max observed Schur correction rank={max_rank}")
print("QFORM_LOW_OFFDIAG_3OVER10_CHECK_PASS")
