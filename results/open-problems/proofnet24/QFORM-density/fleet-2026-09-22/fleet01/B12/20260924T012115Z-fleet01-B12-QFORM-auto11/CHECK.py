import math
import numpy as np

rng = np.random.default_rng(0)
max_gram_err = 0.0
product_violations = 0
woodbury_violations = 0
trials = 5000

for _ in range(trials):
    n, m, r = 10, 6, 3
    X = rng.normal(size=(n, n))
    A0 = (X + X.T) / 2
    P = np.eye(n)[:, :m]
    M0 = A0 @ P
    if np.linalg.matrix_rank(M0) < m:
        continue

    Uraw = rng.normal(size=(n, r))
    U, _ = np.linalg.qr(Uraw)
    theta = rng.choice([-1.0, 1.0], size=r) * rng.uniform(0.2, 20.0, size=r)
    Theta = np.diag(theta)

    V = P.T @ U
    M0dag = np.linalg.pinv(M0)
    R = M0dag @ U
    Pi = M0 @ M0dag
    Uperp = (np.eye(n) - Pi) @ U
    L = np.eye(m) + R @ Theta @ V.T

    M = (A0 + U @ Theta @ U.T) @ P
    G_direct = M.T @ M
    G_formula = (
        L.T @ (M0.T @ M0) @ L
        + V @ Theta @ Uperp.T @ Uperp @ Theta @ V.T
    )
    max_gram_err = max(max_gram_err, np.linalg.norm(G_direct - G_formula, 2))

    s = np.linalg.svd(M, compute_uv=False)
    s0 = np.linalg.svd(M0, compute_uv=False)
    sminL = np.linalg.svd(L, compute_uv=False)[-1]
    if np.any(s + 1e-9 < s0 * sminL):
        product_violations += 1

    K = np.linalg.inv(Theta) + V.T @ R
    if abs(np.linalg.det(K)) > 1e-10:
        Kinv = np.linalg.inv(K)
        lower = 1.0 / (
            1.0
            + np.linalg.norm(R, 2)
            * np.linalg.norm(Kinv, 2)
            * np.linalg.norm(V, 2)
        )
        if sminL + 1e-9 < lower:
            woodbury_violations += 1

# Partner-application arithmetic.
g = 125 / 64
m = 6
N = math.comb(m, 2)
s = g
terms = [
    8 * N * math.sqrt(6 * math.pi * m) / g,
    4 * math.pi * N / g,
    3 * (400 ** (1 / 3)) * ((4 * N / g) ** (5 / 6)) * (s ** (-1 / 6)),
    10 * math.sqrt(2 * math.e) / (math.sqrt(3) * g),
]

print({
    "trials": trials,
    "max_gram_operator_error": max_gram_err,
    "product_bound_violations": product_violations,
    "woodbury_bound_violations": woodbury_violations,
    "partner_terms": terms,
    "partner_max": max(terms),
})
