import math
import numpy as np

rng = np.random.default_rng(2026092302)
max_gram = 0.0
max_energy = 0.0
max_q_relation = 0.0
max_reconstruction = 0.0
min_product_eigenvalue = 1.0
trials = 100

for _ in range(trials):
    c = 0.96 + 0.039 * rng.random()
    n = 12

    # Build a light-row matrix with exact Gram diag(1-c,1,1), so after
    # adjoining hub sqrt(c)e_1 the complete spectral frame is Parseval.
    B = rng.normal(size=(n, 3))
    G = B.T @ B
    vals, vecs = np.linalg.eigh(G)
    B = B @ vecs @ np.diag(vals ** -0.5) @ vecs.T
    Rlight = B @ np.diag([math.sqrt(1.0 - c), 1.0, 1.0])

    perm = rng.permutation(n)
    S = perm[: n // 2]
    T = perm[n // 2 :]

    def bank(J):
        s = Rlight[J, 0]
        w = Rlight[J, 1:]
        W = w.T @ w
        b = w.T @ s
        q = np.linalg.solve(W, b)
        eps = s - w @ q
        tau = float(eps @ eps)
        return s, w, W, q, eps, tau

    sS, wS, WS, qS, epsS, tauS = bank(S)
    sT, wT, WT, qT, epsT, tauT = bank(T)

    d = qS - qT
    product = WS @ WT
    pevals, Pbasis = np.linalg.eigh(product)
    min_product_eigenvalue = min(min_product_eigenvalue, float(pevals.min()))
    sqrt_product = Pbasis @ np.diag(np.sqrt(pevals)) @ Pbasis.T
    invsqrt_product = Pbasis @ np.diag(1.0 / np.sqrt(pevals)) @ Pbasis.T

    # P = WT Z_S - WS Z_T, represented as source-coordinate columns.
    Pcoeff = np.zeros((n, 2))
    Pcoeff[S] = wS @ WT
    Pcoeff[T] = -wT @ WS
    Ptilde_coeff = Pcoeff @ invsqrt_product

    Ecoeff = np.zeros(n)
    Ecoeff[S] = epsS
    Ecoeff[T] = epsT
    tau = tauS + tauT
    Ucoeff = Ecoeff / math.sqrt(tau)

    # [Z, Ptilde, U] must be a five-dimensional orthonormal projection.
    frame = np.column_stack([Rlight[:, 1:], Ptilde_coeff, Ucoeff])
    max_gram = max(max_gram, float(np.linalg.norm(frame.T @ frame - np.eye(5), ord=np.inf)))

    eta = np.r_[sqrt_product @ d, math.sqrt(tau)]
    max_energy = max(max_energy, abs(float(eta @ eta) - (1.0 - c)))
    max_q_relation = max(
        max_q_relation,
        float(np.linalg.norm(qS - WT @ d) + np.linalg.norm(qT + WS @ d)),
    )

    x = rng.normal(size=n)
    longitudinal = float(Rlight[:, 0] @ x)
    Ptilde = Ptilde_coeff.T @ x
    U = float(Ucoeff @ x)
    reconstructed = float((sqrt_product @ d) @ Ptilde + math.sqrt(tau) * U)
    max_reconstruction = max(max_reconstruction, abs(longitudinal - reconstructed))

assert max_gram < 1e-11
assert max_energy < 1e-11
assert max_q_relation < 1e-11
assert max_reconstruction < 1e-11

# Null-hub indefinite spectral control: eigenvalues {-1,-1,2}.
M = np.array([[0.0, 1.0, 1.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 0.0]])
eigs = np.linalg.eigvalsh(M)
b = M[0, 1:]
beta2 = float(b @ b)
v = np.array([1.0, -1.0]) / math.sqrt(2.0)
lambda_transverse = float(v @ M[1:, 1:] @ v)
assert np.max(np.abs(eigs - np.array([-1.0, -1.0, 2.0]))) < 1e-12
assert abs(np.linalg.det(M) + beta2 * lambda_transverse) < 1e-12

c0 = 63.0 / 64.0
hidden_norm = math.sqrt(1.0 - c0)
determinant_currency = c0 * abs(np.linalg.det(M))

print('trials', trials)
print('max_orthonormal_frame_error', max_gram)
print('max_energy_identity_error', max_energy)
print('max_q_relation_error', max_q_relation)
print('max_longitudinal_reconstruction_error', max_reconstruction)
print('minimum_WSWT_eigenvalue_sampled', min_product_eigenvalue)
print('control_spectral_eigenvalues', eigs)
print('control_beta_squared', beta2)
print('control_lambda_transverse', lambda_transverse)
print('near_coloop_hidden_norm_at_63_over_64', hidden_norm)
print('control_kappa2_abs_lambda_at_63_over_64', determinant_currency)
print('QFORM_B11_NEARCOLOOP_CANONICAL_CHECK_PASS')
