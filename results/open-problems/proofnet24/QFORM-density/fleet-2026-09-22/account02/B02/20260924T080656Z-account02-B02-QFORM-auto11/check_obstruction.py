import itertools
import math
import numpy as np

A = np.array([
    [1,0,1,0,0],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,1,0,1,0],
    [0,0,0,0,1],
], dtype=float)

print('eigenvalues', np.linalg.eigvalsh(A).tolist())
counts = {r:0 for r in range(6)}
max_rank = 0
for lab in itertools.product((0,1,2), repeat=5):
    I = [k for k,a in enumerate(lab) if a == 1]
    J = [k for k,a in enumerate(lab) if a == 2]
    if not I or not J:
        continue
    r = int(np.linalg.matrix_rank(A[np.ix_(I,J)], tol=1e-12))
    counts[r] += 1
    max_rank = max(max_rank, r)
print('cross_rank_counts', counts)
print('max_disjoint_cross_rank', max_rank)

delta = 1/100
det_floor = 1/6 - 4*delta**2/3
C_pair = 128*det_floor**(-1/4)
C_pivot = 8*delta**(-1/2) + 16*math.sqrt(2)*3**0.25*delta**(-1/4)
print('det_floor', det_floor)
print('C_pair', C_pair)
print('C_pivot', C_pivot)
print('C4_claim', 201)
print('r47_a_gt_1_over_228_sigma_ge_1_over_100_bound', 201*math.sqrt(22800))
print('grouped_three_square_L1_bound', 50*math.pi)

assert np.allclose(np.linalg.eigvalsh(A), [0,0,1,2,2])
assert max_rank == 2
assert C_pair < 201 and C_pivot < 201
