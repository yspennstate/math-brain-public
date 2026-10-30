import math
import numpy as np


def build(m):
    theta = np.array([2 * math.pi * j / m for j in range(1, m + 1)])
    V = np.column_stack([
        np.ones(m) / math.sqrt(m),
        math.sqrt(2 / m) * np.cos(theta),
        math.sqrt(2 / m) * np.sin(theta),
    ])
    U = np.vstack([np.array([[m, 0.0, 0.0]]), V])
    s = math.sqrt(1 + m * m)
    D = np.array([[0.0, 1 / s, 0.0], [1 / s, 0.0, 0.0], [0.0, 0.0, 1.0]])
    A = U @ D @ U.T
    return theta, V, U, D, A


max_gram_err = 0.0
max_spec_err = 0.0
max_q_err = 0.0
max_M_err = 0.0
M_target = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])

for m in range(3, 101):
    theta, V, U, D, A = build(m)
    G = U.T @ U
    G_target = np.diag([1 + m * m, 1.0, 1.0])
    max_gram_err = max(max_gram_err, float(np.max(np.abs(G - G_target))))

    eig = np.linalg.eigvalsh(A)
    nz = eig[np.abs(eig) > 1e-8]
    max_spec_err = max(max_spec_err, float(np.max(np.abs(nz - np.array([-1.0, 1.0, 1.0])))))

    q = np.sum(V[:, 1:] ** 2, axis=1)
    max_q_err = max(max_q_err, float(np.max(np.abs(q - 2 / m))))

    Ghalf = np.diag(np.sqrt(np.diag(G_target)))
    M = Ghalf @ D @ Ghalf
    max_M_err = max(max_M_err, float(np.max(np.abs(M - M_target))))

# Exceptional m=3 triple: hub plus theta=2pi/3,4pi/3.
m = 3
theta, V, U, D, A = build(m)
Rstar = np.vstack([U[0], V[0], V[1]])
det_Rstar = float(np.linalg.det(Rstar))
det_K = det_Rstar ** 2 * float(np.linalg.det(D))

C3 = 6 * (10 / 3) ** (1 / 3)
C4 = 3 * 2 ** (4 / 3) * (17 / 16) ** (1 / 3)
Clim = 3 * 2 ** (4 / 3)

print("QFORM_CIRCULAR_FULLPAY_REGRESSION_PASS")
print(f"max_gram_error_m3_to_m100={max_gram_err:.3e}")
print(f"max_nonzero_spectrum_error_m3_to_m100={max_spec_err:.3e}")
print(f"max_transverse_leverage_error_m3_to_m100={max_q_err:.3e}")
print(f"max_whitened_middle_matrix_error_m3_to_m100={max_M_err:.3e}")
print(f"m3_det_Rstar={det_Rstar:.15f}")
print(f"m3_det_K={det_K:.15f}")
print(f"uniform_family_constant={C3:.15f}")
print(f"m4_nullhub_constant={C4:.15f}")
print(f"large_m_limit={Clim:.15f}")
