import numpy as np

rng = np.random.default_rng(20260922)

def sc_scalar(M):
    a = M[0, 0]
    return M[1:, 1:] - np.outer(M[1:, 0], M[0, 1:]) / a

max_identity_error = 0.0
max_det_error = 0.0
rank_violations = 0
sv_violations = 0
cases = 0

for n in range(5, 11):
    for k in range(1, min(4, n - 1)):
        for _ in range(100):
            R = rng.normal(size=(n, n))
            B = (R + R.T) / 2
            B[0, 0] += 3.0 if B[0, 0] >= 0 else -3.0
            U, _ = np.linalg.qr(rng.normal(size=(n, k)))
            vals = rng.uniform(-5.0, 5.0, size=k)
            vals[np.abs(vals) < 0.2] += np.where(vals[np.abs(vals) < 0.2] >= 0, 0.3, -0.3)
            C = np.diag(vals)
            A = B + U @ C @ U.T
            if abs(B[0, 0]) < 1e-8 or abs(A[0, 0]) < 1e-8:
                continue

            alpha = B[0, 0]
            b = B[0, 1:]
            u = U[0:1, :]
            V = U[1:, :]
            a = A[0, 0]
            W = V - np.outer(b / alpha, u.ravel())
            Cp = C - C @ u.T @ u @ C / a

            actual_update = sc_scalar(A) - sc_scalar(B)
            predicted_update = W @ Cp @ W.T
            max_identity_error = max(
                max_identity_error,
                np.linalg.norm(actual_update - predicted_update, ord=2),
            )
            if np.linalg.matrix_rank(actual_update, tol=1e-8) > k:
                rank_violations += 1

            max_det_error = max(
                max_det_error,
                abs(np.linalg.det(Cp) - np.linalg.det(C) * alpha / a),
            )

            p = (n - 1) // 2
            X = sc_scalar(B)[:p, p:]
            F = actual_update[:p, p:]
            Y = X + F
            sX = np.linalg.svd(X, compute_uv=False)
            sY = np.linalg.svd(Y, compute_uv=False)
            rk = np.linalg.matrix_rank(F, tol=1e-8)
            for j in range(max(0, min(len(sY), len(sX) - rk))):
                if sY[j] + 1e-8 < sX[j + rk]:
                    sv_violations += 1
            cases += 1

print(f"cases={cases}")
print(f"max_identity_error={max_identity_error:.17g}")
print(f"max_det_error={max_det_error:.17g}")
print(f"rank_violations={rank_violations}")
print(f"sv_violations={sv_violations}")
assert rank_violations == 0
assert sv_violations == 0
assert max_identity_error < 1e-10
assert max_det_error < 1e-9
print("QFORM_B12_R17_CHECK_PASS")
