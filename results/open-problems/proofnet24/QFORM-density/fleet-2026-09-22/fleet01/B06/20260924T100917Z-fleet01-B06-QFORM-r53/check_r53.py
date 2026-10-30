import math
import json
import numpy as np

rng = np.random.default_rng(202609241053)
max_recon = 0.0
max_pnorm = 0.0
max_qid = 0.0
min_spec_margin = float("inf")
count = 0

for n in [4, 5, 8, 12]:
    for _ in range(500):
        u = rng.normal(size=3)
        u /= np.linalg.norm(u)
        lam = rng.normal()
        if abs(lam) < 0.1:
            lam = math.copysign(0.1, lam if lam != 0 else 1.0)

        m = n - 3
        M = rng.normal(size=(3, m))
        C0 = rng.normal(size=(m, m))
        C0 = (C0 + C0.T) / 2
        K = lam * np.outer(u, u)
        A = np.block([[K, M], [M.T, C0]])

        # Exact orthonormal basis of u^perp from the SVD of the row u^T.
        _, _, Vt = np.linalg.svd(u.reshape(1, 3), full_matrices=True)
        Uperp = Vt[1:].T
        B = Uperp.T @ M
        Ub, s, _ = np.linalg.svd(B, full_matrices=True)

        # Smaller singular direction of the two-dimensional transverse map,
        # padded by zero if the tail has dimension one.
        if m >= 2:
            nu = s[-1]
            a = Ub[:, -1]
        else:
            nu = 0.0
            a = Ub[:, 1]

        w = Uperp @ a
        w /= np.linalg.norm(w)
        k = int(np.argmax(np.abs(w)))

        wfull = np.r_[w, np.zeros(m)]
        idx = [k] + [i for i in range(n) if i != k]
        Ap = A[np.ix_(idx, idx)]
        wp = wfull[idx]
        wk = wp[0]
        T = wp[1:] / wk
        C = Ap[1:, 1:]
        P = np.column_stack((-T, np.eye(n - 1)))

        rw = A @ wfull
        rp = rw[idx]
        q = rp[1:] / wk
        E = np.zeros((n, n))
        E[0, 1:] = q
        E[1:, 0] = q

        max_recon = max(
            max_recon,
            np.linalg.norm(Ap - (P.T @ C @ P + E), ord=2),
        )
        max_pnorm = max(
            max_pnorm,
            abs(np.linalg.norm(P, 2) ** 2 - 1 / (wk * wk)),
        )
        max_qid = max(
            max_qid,
            abs(np.linalg.norm(q) - nu / abs(wk)),
        )

        sA = np.linalg.svd(Ap, compute_uv=False)
        sC = np.linalg.svd(C, compute_uv=False)
        rhs = (wk * wk) * (sA[2] - np.linalg.norm(q))
        min_spec_margin = min(min_spec_margin, sC[2] - rhs)
        count += 1

results = {
    "seed": 202609241053,
    "trials": count,
    "dimensions": [4, 5, 8, 12],
    "max_reconstruction_op_error": max_recon,
    "max_P_norm_squared_identity_error": max_pnorm,
    "max_q_norm_identity_error": max_qid,
    "min_spectral_inequality_margin": min_spec_margin,
}
print(json.dumps(results, indent=2, sort_keys=True))
