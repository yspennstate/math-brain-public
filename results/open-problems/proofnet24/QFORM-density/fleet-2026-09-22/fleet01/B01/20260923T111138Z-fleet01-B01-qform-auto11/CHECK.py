import numpy as np

rng = np.random.default_rng(20260923)
max_err = 0.0
for _ in range(500):
    m = 7
    K = rng.normal(size=(2, m))
    alpha = rng.normal(size=2)
    M = np.vstack([K, alpha @ K])
    X = rng.normal(size=(3, 3))
    B = (X + X.T) / 2
    v = np.array([-alpha[0], -alpha[1], 1.0])
    n = v / np.linalg.norm(v)
    S = M @ M.T
    e2 = 0.5 * (np.trace(S) ** 2 - np.trace(S @ S))
    lhs = np.linalg.det(K @ K.T) * abs(v @ B @ v)
    rhs = e2 * abs(n @ B @ n)
    denom = max(1.0, abs(lhs), abs(rhs))
    max_err = max(max_err, abs(lhs - rhs) / denom)

Cstar = (15.0 / 4.0) * 12.0 ** (1.0 / 5.0)
print(f"max_normalized_identity_error={max_err:.17g}")
print(f"Cstar={Cstar:.16f}")
print("STATUS=PASS" if max_err < 1e-12 else "STATUS=FAIL")
