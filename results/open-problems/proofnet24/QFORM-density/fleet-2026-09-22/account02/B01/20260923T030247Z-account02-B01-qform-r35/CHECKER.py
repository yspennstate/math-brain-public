import math
import numpy as np


def sylvester(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H


m = 8
eta = 0.2
c = 1.0 + eta
N = 2 * m
H = sylvester(N)
K = H / math.sqrt(N)
u = np.r_[np.ones(m) / math.sqrt(m), np.zeros(m)]
v = np.r_[np.zeros(m), np.ones(m) / math.sqrt(m)]
M = c * np.vstack([u, v])

Ares = np.zeros((2 + N, 2 + N))
Ares[0, 2:] = c * u
Ares[2:, 0] = c * u
Ares[1, 2:] = c * v
Ares[2:, 1] = c * v
Ares[2:, 2:] = eta * K

w = np.ones(m) / math.sqrt(m)
Aw = np.outer(w, w)
A = np.block([
    [Ares, np.zeros((2 + N, m))],
    [np.zeros((m, 2 + N)), Aw],
])

eig = np.linalg.eigvalsh(A)
maxdiag = float(np.max(np.abs(np.diag(A))))
maxpair = 0.0
for i in range(A.shape[0]):
    for j in range(i + 1, A.shape[0]):
        maxpair = max(maxpair, abs(float(A[i, i] * A[j, j] - A[i, j] ** 2)))

print(f"m={m}")
print(f"eta={eta}")
print(f"c={c}")
print(f"hadamard_orthogonality_error={np.max(np.abs(K @ K - np.eye(N))):.17g}")
print(f"gram_error={np.max(np.abs(M @ M.T - c*c*np.eye(2))):.17g}")
print(f"large_eig_count={int(np.sum(np.abs(eig) >= 1 - 1e-12))}")
print(f"eig_extremes={eig[0]:.17g},{eig[1]:.17g},{eig[-2]:.17g},{eig[-1]:.17g}")
print(f"max_abs_diagonal={maxdiag:.17g}")
print(f"max_abs_pair_determinant={maxpair:.17g}")
print(f"new_dense_leaf_bound={2**(13/4)/math.sqrt(c):.17g}")
print(f"source_H_eta0_bound={4/c:.17g}")
print(f"partner_plus_grouped_square_bound={8*math.sqrt(math.e)/math.sqrt(c):.17g}")
assert np.max(np.abs(K @ K - np.eye(N))) < 1e-12
assert np.max(np.abs(M @ M.T - c*c*np.eye(2))) < 1e-12
assert np.sum(np.abs(eig) >= 1 - 1e-12) >= 5
assert maxdiag < 0.2
assert maxpair < 0.2
print("STATUS=PASS")
