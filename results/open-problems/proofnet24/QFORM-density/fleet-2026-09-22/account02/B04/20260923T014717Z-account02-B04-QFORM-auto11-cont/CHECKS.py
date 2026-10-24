import math
import numpy as np


def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H

H = hadamard(8)
U0 = H[:, :3] / math.sqrt(8)
P0 = U0 @ U0.T
sin2 = 5 / 12
cos2 = math.sqrt(119) / 12
theta = 0.5 * math.atan2(sin2, cos2)
c, s = math.cos(theta), math.sin(theta)
R = np.eye(8)
R[0, 0], R[0, 4], R[4, 0], R[4, 4] = c, s, -s, c
P = R @ P0 @ R.T

delta = 1 / 100
M0 = delta * np.eye(8) + (1 - delta) * P
M = 2 * M0

eps = delta**2
Z0 = 1 + 15 * eps + 30 * eps**2 + 10 * eps**3
Z = 64 * Z0
pH = (1 + 10 * eps + 10 * eps**2) / Z0
pL = eps * (3 + 12 * eps + 6 * eps**2) / Z0
alpha = pL + (pH - pL) * (17 / 32)
qstar = 2 * alpha

Cq = lambda q: 3 * math.e / ((3 - 2 * q) * math.sqrt(q))
direct_q = Cq(qstar) * Z ** (-1 / 6)

t = (1 - alpha) / alpha
Zt = 2 * (1 - alpha)
KL = -0.5 * math.log(4 * alpha * (1 - alpha))
Gopt = Z * math.exp(-KL)
weighted_q1 = 3 * math.e * Gopt ** (-1 / 6)

gamma = 127 / 250
kH = 4 / (4 + gamma**2)
kL = 0.0004 / (0.0004 + gamma**2)
Kdiag = kL + (kH - kL) * np.diag(P)
theta_r = 3 * kH + 5 * kL
D = (1 + 4 / gamma**2) ** 3 * (1 + 0.0004 / gamma**2) ** 5
ridge = (
    math.e
    / (math.sqrt(2) * gamma)
    * theta_r
    / (theta_r - 2)
    * D ** (-1 / (2 * theta_r))
)

# Coupled 17x17 target matrix Q=(z+.01*x_1)^2+2 x^T M y.
tau = 0.01
e1 = np.zeros(8)
e1[0] = 1
A = np.zeros((17, 17))
A[0, 0] = 1
A[0, 1:9] = tau * e1
A[1:9, 0] = tau * e1
A[1:9, 1:9] = tau**2 * np.outer(e1, e1)
A[1:9, 9:17] = M
A[9:17, 1:9] = M

eigs = np.linalg.eigvalsh(A)
mstar = M[0, 0]
C_HR = 63.11383495773493
partner = C_HR / math.sqrt(mstar)

out = {
    "P_diag": np.diag(P).tolist(),
    "M_singular_values": np.linalg.svd(M, compute_uv=False).tolist(),
    "Z0": Z0,
    "Z": Z,
    "pH": pH,
    "pL": pL,
    "alpha_max": alpha,
    "qstar": qstar,
    "direct_fractional_q_bound": direct_q,
    "tilt_t": t,
    "tilt_normalizer": Zt,
    "KL_min": KL,
    "Gopt": Gopt,
    "weighted_q1_bound": weighted_q1,
    "ridge_gamma": gamma,
    "ridge_max_diag": float(Kdiag.max()),
    "ridge_theta": theta_r,
    "ridge_D": D,
    "ridge_bound": ridge,
    "target_eigenvalues": eigs.tolist(),
    "selected_pair_coefficient": mstar,
    "partner_bound": partner,
}

for k, v in out.items():
    print(k, v)
