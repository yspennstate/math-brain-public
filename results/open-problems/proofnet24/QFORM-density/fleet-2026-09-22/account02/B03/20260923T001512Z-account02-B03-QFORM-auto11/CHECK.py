import itertools
import math
import numpy as np


def matrix(m, a=1.0, b=1.0):
    n = 1 + 2*m
    A = np.zeros((n, n))
    A[0, 1:m+1] = a / math.sqrt(m)
    A[1:m+1, 0] = a / math.sqrt(m)
    A[m+1:, m+1:] = b / m
    return A


def check(m):
    A = matrix(m)
    n = len(A)
    eig = np.linalg.eigvalsh(A)
    nz = eig[np.abs(eig) > 1e-10]
    max_diag = max(abs(A[i, i]) for i in range(n))
    max_pair_det = 0.0
    for i, j in itertools.combinations(range(n), 2):
        max_pair_det = max(max_pair_det,
                           abs(np.linalg.det(A[np.ix_([i, j], [i, j])])))
    max_cross_rank = None
    if n <= 7:
        max_cross_rank = 0
        # label each coordinate 0=unused, 1=I, 2=J; exhaustive for m=2,3
        for lab in itertools.product(range(3), repeat=n):
            I = [i for i, z in enumerate(lab) if z == 1]
            J = [i for i, z in enumerate(lab) if z == 2]
            if I and J:
                r = np.linalg.matrix_rank(A[np.ix_(I, J)], tol=1e-10)
                max_cross_rank = max(max_cross_rank, r)
    return nz, max_diag, max_pair_det, max_cross_rank


for m in [2, 3, 4, 5, 10, 100]:
    nz, md, mp, mr = check(m)
    print(f"m={m} nonzero_eigs={np.array2string(nz, precision=12)} "
          f"max_diag={md:.12g} max_pairdet={mp:.12g} "
          f"max_cut_rank={mr if mr is not None else 'analytic<=2'}")

print(f"C_hub={3*4**(2/3):.15f}")
print(f"C_partner={3*2**(8/3):.15f}")
