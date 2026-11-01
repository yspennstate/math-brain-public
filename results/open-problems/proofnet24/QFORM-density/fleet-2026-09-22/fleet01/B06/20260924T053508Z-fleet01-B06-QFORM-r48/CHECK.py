import numpy as np
from math import sqrt, pi, exp
from mpmath import gamma, cos

rng = np.random.default_rng(260924)
max_schur = 0.0
max_s_norm = 0.0
count = 0

for n in [5, 8, 12, 25]:
    for _ in range(100):
        R, _ = np.linalg.qr(rng.normal(size=(n, 3)))
        H = rng.normal(size=(3, 3))
        Lam = (H + H.T) / 2
        if abs(np.linalg.det(Lam)) < 0.1:
            continue

        good = None
        for h in range(n):
            for j in range(h + 1, n):
                U = R[[h, j], :]
                delta = np.linalg.det(U @ U.T)
                if delta < 1e-6:
                    continue
                B = U @ Lam @ U.T
                if abs(np.linalg.det(B)) < 1e-4:
                    continue
                good = (h, j, U, delta, B)
                break
            if good is not None:
                break
        if good is None:
            continue

        h, j, U, delta, B = good
        K = [k for k in range(n) if k not in (h, j)]
        d = rng.normal(size=len(K))
        D = np.zeros((n, n))
        for k, val in zip(K, d):
            D[k, k] = val

        A = D + R @ Lam @ R.T
        pair = [h, j]
        Schur = (
            A[np.ix_(K, K)]
            - A[np.ix_(K, pair)]
            @ np.linalg.inv(A[np.ix_(pair, pair)])
            @ A[np.ix_(pair, K)]
        )

        eta = np.cross(U[0], U[1])
        eta /= np.linalg.norm(eta)
        s = R[K, :] @ eta
        tau = np.linalg.det(Lam) * delta / np.linalg.det(B)
        target = np.diag(d) + tau * np.outer(s, s)

        max_schur = max(max_schur, float(np.linalg.norm(Schur - target)))
        max_s_norm = max(max_s_norm, abs(float(s @ s - 1.0)))
        count += 1

C2 = 8 * pi ** 0.25 * exp(0.25) / (float(gamma(0.25)) * float(cos(pi / 8)))
Cdiff = 2 * sqrt(3) * C2 * (4 / sqrt(3)) ** 0.25
Cscaled = Cdiff * (64 / 7) ** 0.25 * 64 ** 0.125

print({
    "accepted_cases": count,
    "max_schur_fro_error": max_schur,
    "max_s_norm_sq_error": max_s_norm,
    "C2": C2,
    "Cdiff": Cdiff,
    "Cscaled": Cscaled,
})
