import numpy as np

rng = np.random.default_rng(0)
worst_reconstruction = 0.0
worst_error_bound_violation = 0.0
worst_spectral_violation = 0.0

for _ in range(1000):
    n = 8
    G = rng.normal(size=(n, n))
    A = (G + G.T) / 2
    H = rng.choice(n, size=3, replace=False)
    w = np.zeros(n)
    v = rng.normal(size=3)
    v /= np.linalg.norm(v)
    w[H] = v
    k = H[np.argmax(np.abs(v))]
    a = w[k]
    R = [j for j in range(n) if j != k]
    C = A[np.ix_(R, R)]
    T = w[R] / a

    P = np.zeros((n - 1, n))
    P[:, k] = -T
    for ii, j in enumerate(R):
        P[ii, j] = 1.0

    Aw = A @ w
    q = Aw[R] / a
    d = Aw[k] / a - q @ T
    E = np.zeros((n, n))
    E[k, k] = d
    E[k, R] = q
    E[R, k] = q

    worst_reconstruction = max(
        worst_reconstruction,
        np.linalg.norm(A - P.T @ C @ P - E, 2),
    )

    eps = np.linalg.norm(Aw)
    e_bound = eps * (2 / abs(a) + np.sqrt(1 - a * a) / (a * a))
    worst_error_bound_violation = max(
        worst_error_bound_violation,
        np.linalg.norm(E, 2) - e_bound,
    )

    sA = np.linalg.svd(A, compute_uv=False)
    sC = np.linalg.svd(C, compute_uv=False)
    lb = a * a * sA[2] - (2 * abs(a) + np.sqrt(1 - a * a)) * eps
    worst_spectral_violation = max(worst_spectral_violation, lb - sC[2])

print({
    "worst_reconstruction": worst_reconstruction,
    "worst_error_bound_violation": worst_error_bound_violation,
    "worst_spectral_violation": worst_spectral_violation,
})
