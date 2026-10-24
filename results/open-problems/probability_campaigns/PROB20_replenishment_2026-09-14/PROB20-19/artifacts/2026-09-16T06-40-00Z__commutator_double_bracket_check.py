import numpy as np
from scipy.linalg import expm

SEED = 20260916
N = 700_000
rng = np.random.default_rng(SEED)


def topd(X, d):
    n, p = X.shape
    sq = X * X
    idx = np.argpartition(sq, p - d, axis=1)[:, p - d:]
    I = np.zeros_like(sq)
    rr = np.arange(n)[:, None]
    I[rr, idx] = 1.0
    f = np.sum(sq * I, axis=1)
    return f, I


def sample_from_cov(C, Z):
    L = np.linalg.cholesky(C)
    return Z @ L.T


def selection_K(X, I):
    p = X.shape[1]
    K = np.zeros((p, p))
    for i in range(p):
        for j in range(i + 1, p):
            v = 2.0 * np.mean(X[:, i] * X[:, j] * (I[:, i] - I[:, j]))
            K[i, j] = v
            K[j, i] = -v
    return K


def score_objects(C, X, f):
    F = np.mean(f)
    M = np.einsum('n,ni,nj->ij', f, X, X) / X.shape[0]
    Ci = np.linalg.inv(C)
    J = Ci @ M @ Ci - F * Ci
    K = J @ C - C @ J
    return F, M, J, K


# Moderate SPD test for score/selection identities.
C = np.array([
    [3.0, .45, .20, .10],
    [.45, 2.0, .25, .15],
    [.20, .25, 1.3, .30],
    [.10, .15, .30, .8],
])
Z = rng.standard_normal((N, 4))
X = sample_from_cov(C, Z)
f, I = topd(X, 2)
K_sel = selection_K(X, I)
F, M, J, K_score = score_objects(C, X, f)
trace_error = abs(np.trace(C @ J) - 2 * F)
comm_equiv = np.linalg.norm(C @ M - M @ C, ord='fro')
score_sel_err = np.max(np.abs(K_score - K_sel))

# Common-random-number finite difference along the empirical coupled gradient.
eta = 2e-3
R = expm(eta * K_sel)
Fp = np.mean(topd(X @ R.T, 2)[0])
flow_rate_fd = (Fp - F) / eta
flow_rate_pred = 0.5 * np.sum(K_sel * K_sel)

# KL/diagonal basis should have zero gradient up to sampling error.
Cd = np.diag([3.0, 2.0, 1.3, .8])
Xd = sample_from_cov(Cd, Z)
fd, Id = topd(Xd, 2)
Kd = selection_K(Xd, Id)

# Previous explicit Jacobi obstruction: selection derivative K_12 should be positive.
eps = 1e-3
Cstar = np.array([
    [4.0, 0.0, 2.0],
    [0.0, 1.0, 1.0],
    [2.0, 1.0, 2.0 + eps ** 2],
])
Z3 = rng.standard_normal((N, 3))
Xs = sample_from_cov(Cstar, Z3)
fs, Is = topd(Xs, 2)
Ks = selection_K(Xs, Is)

print(f'seed={SEED} N={N}')
print('moderate SPD eigenvalues=', np.linalg.eigvalsh(C))
print(f'F={F:.9f}')
print(f'max_abs(K_score-K_selection)={score_sel_err:.6g}')
print(f'abs(trace(CJ)-2F)={trace_error:.6g}')
print('eig(J_sym)=', np.linalg.eigvalsh((J + J.T) / 2))
print(f'||CM-MC||_F={comm_equiv:.6g}')
print(f'flow_rate_pred_half_normK2={flow_rate_pred:.9f}')
print(f'flow_rate_common_random_fd={flow_rate_fd:.9f}')
print(f'flow_rate_abs_error={abs(flow_rate_fd-flow_rate_pred):.6g}')
print(f'diagonal_basis_max_abs_K={np.max(np.abs(Kd)):.6g}')
print(f'obstruction_Cstar_K12_MC={Ks[0, 1]:.9f}')
print('analytic archived lower bound for Cstar K12 is > 0.322')
print('PASS finite-step ascent=', Fp > F)
print('PASS Cstar sign=', Ks[0, 1] > 0)
print('NOTE score-vs-selection and diagonal-zero checks are Monte Carlo self-review, not proofs.')