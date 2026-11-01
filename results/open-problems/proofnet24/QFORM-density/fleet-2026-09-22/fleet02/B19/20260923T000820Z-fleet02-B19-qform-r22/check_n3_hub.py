import itertools, math
import numpy as np


def star_square(m):
    assert m % 2 == 0
    g = np.ones(m) / math.sqrt(m)
    u = np.r_[np.ones(m//2), -np.ones(m//2)] / math.sqrt(m)
    A = np.zeros((m+1, m+1))
    A[0,1:] = g
    A[1:,0] = g
    A[1:,1:] = np.outer(u,u)
    return A

m = 8
A = star_square(m)
eigs = np.linalg.eigvalsh(A)
assert np.allclose(eigs[[0,-2,-1]], [-1,1,1], atol=1e-12)
assert np.max(np.abs(np.diag(A))) <= 1/m + 1e-12
max_pair_det = 0.0
for i in range(m+1):
    for j in range(i+1,m+1):
        d = abs(np.linalg.det(A[np.ix_([i,j],[i,j])]))
        max_pair_det = max(max_pair_det,d)
assert abs(max_pair_det - 1/m) < 1e-12

max_cross_rank = 0
n = m+1
for mask in range(1,2**n-1):
    P = [i for i in range(n) if (mask>>i)&1]
    Q = [i for i in range(n) if not ((mask>>i)&1)]
    max_cross_rank = max(max_cross_rank, np.linalg.matrix_rank(A[np.ix_(P,Q)], tol=1e-10))
assert max_cross_rank <= 2

H_const = 3 * 4**(2/3)
partner_const = 16 * math.sqrt(60) * 2**0.25
D5_gamma_64 = 5 * math.sqrt(2*math.e) * 64
print(f"spectrum_nonzero=-1,1,1")
print(f"max_pair_det_m8={max_pair_det:.12f}")
print(f"max_cross_rank_all_cuts_m8={max_cross_rank}")
print(f"theorem_H_constant={H_const:.12f}")
print(f"partner_bank_constant={partner_const:.12f}")
print(f"D5_gamma_1_over_64={D5_gamma_64:.12f}")
print("QFORM_B19_R22_N3_HUB_CHECK_PASS")
