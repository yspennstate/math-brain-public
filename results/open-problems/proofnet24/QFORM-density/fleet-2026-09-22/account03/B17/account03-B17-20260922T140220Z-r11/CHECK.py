import itertools
import math
import numpy as np


def walsh_frame(d=4):
    n = 2**d
    bits = np.array([[(x >> k) & 1 for k in range(d)] for x in range(n)], dtype=int)
    R = np.column_stack([(-1.0) ** bits[:, k] / math.sqrt(n) for k in range(3)])
    chi4 = (-1) ** bits[:, 3]
    J = np.diag([1.0, 1.0, -1.0])
    A = R @ J @ R.T
    return R, chi4, J, A


R, chi4, J, A = walsh_frame(4)
n = R.shape[0]
assert np.max(np.abs(R.T @ R - np.eye(3))) < 1e-13

eig = np.linalg.eigvalsh(A)
assert np.max(np.abs(eig[-2:] - 1)) < 1e-12
assert abs(eig[0] + 1) < 1e-12
assert np.max(np.abs(eig[1:-2])) < 1e-12
assert np.max(np.abs(np.diag(A) - 1/n)) < 1e-13

count = 0
scaled_det = []
bad_inertia = 0
for inds in itertools.combinations(range(n), 3):
    B = A[np.ix_(inds, inds)]
    det = np.linalg.det(B)
    if abs(det) > 1e-10:
        count += 1
        scaled_det.append(abs(det) * n**3)
        ev = np.linalg.eigvalsh(B)
        if not (np.sum(ev > 1e-9) == 2 and np.sum(ev < -1e-9) == 1):
            bad_inertia += 1
assert count == n**3 // 16
assert max(abs(x - 16) for x in scaled_det) < 1e-9
assert bad_inertia == 0

I = np.where(chi4 == 1)[0]
K = np.where(chi4 == -1)[0]
assert np.max(np.abs(R[I].T @ R[I] - 0.5*np.eye(3))) < 1e-13
assert np.max(np.abs(R[K].T @ R[K] - 0.5*np.eye(3))) < 1e-13
Bcross = A[np.ix_(I, K)]
sv = np.linalg.svd(Bcross, compute_uv=False)
assert np.max(np.abs(sv[:3] - 0.5)) < 1e-12
assert np.max(sv[3:]) < 1e-12
P = R[I] @ np.linalg.inv(R[I].T @ R[I]) @ R[I].T
max_lev = float(np.max(np.diag(P)))
assert abs(max_lev - 6/n) < 1e-13

bound = 3*math.sqrt(2)*math.e
stress = 3*math.sqrt(2)
print('PASS')
print('n =', n)
print('spectrum = {-1, 1, 1, 0^(n-3)}')
print('physical diagonal =', 1/n)
print('nonsingular 3x3 principal triples =', count, '= n^3/16')
print('|det B_I| * n^3 =', scaled_det[0])
print('bad inertia count =', bad_inertia)
print('balanced-cut cross singular values =', sv[:3])
print('max range leverage =', max_lev, '= 6/n')
print('regularized-determinant q=1 density bound =', bound)
print('sharp Gaussian stress =', stress)
print('ratio =', bound/stress)
