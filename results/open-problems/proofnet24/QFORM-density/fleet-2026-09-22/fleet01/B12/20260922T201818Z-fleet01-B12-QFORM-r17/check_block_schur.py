import numpy as np

rng = np.random.default_rng(20260922)
max_identity_error = 0.0
max_det_error = 0.0
rank_violations = 0
cases = 0

for n in range(7, 11):
    for r in (2, 3):
        if r >= n:
            continue
        for k in (1, 2, 3):
            for _ in range(50):
                X = rng.normal(size=(n, n))
                B = (X + X.T) / 2
                B[:r, :r] += 4 * np.eye(r)
                U, _ = np.linalg.qr(rng.normal(size=(n, k)))
                vals = rng.uniform(-4.0, 4.0, size=k)
                vals[np.abs(vals) < 0.3] = 0.5
                C = np.diag(vals)
                A = B + U @ C @ U.T
                P = B[:r, :r]
                PA = A[:r, :r]
                if abs(np.linalg.det(P)) < 1e-8 or abs(np.linalg.det(PA)) < 1e-8:
                    continue
                F = B[:r, r:]
                U1, U2 = U[:r, :], U[r:, :]
                W = U2 - F.T @ np.linalg.inv(P) @ U1
                Cp = C - C @ U1.T @ np.linalg.inv(PA) @ U1 @ C

                def schur(M):
                    Pm = M[:r, :r]
                    Fm = M[:r, r:]
                    Dm = M[r:, r:]
                    return Dm - Fm.T @ np.linalg.inv(Pm) @ Fm

                update = schur(A) - schur(B)
                pred = W @ Cp @ W.T
                max_identity_error = max(max_identity_error, np.linalg.norm(update - pred, ord=2))
                if np.linalg.matrix_rank(update, tol=1e-8) > k:
                    rank_violations += 1
                max_det_error = max(
                    max_det_error,
                    abs(np.linalg.det(Cp) - np.linalg.det(C) * np.linalg.det(P) / np.linalg.det(PA)),
                )
                cases += 1

print(f"cases={cases}")
print(f"max_identity_error={max_identity_error:.17g}")
print(f"max_det_error={max_det_error:.17g}")
print(f"rank_violations={rank_violations}")
assert rank_violations == 0
assert max_identity_error < 1e-10
assert max_det_error < 1e-9
print("QFORM_B12_R17_BLOCK_CHECK_PASS")
