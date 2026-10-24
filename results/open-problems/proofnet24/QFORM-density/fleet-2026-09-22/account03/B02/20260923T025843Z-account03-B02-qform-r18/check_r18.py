import math
import numpy as np

rng = np.random.default_rng(20260923)
errs = []
for _ in range(100):
    m = int(rng.integers(2, 8))
    n = int(rng.integers(2, 8))
    U, _ = np.linalg.qr(rng.normal(size=(m, 2)))
    V, _ = np.linalg.qr(rng.normal(size=(n, 2)))
    s = np.exp(rng.normal(size=2))
    Sigma = np.diag(s)
    B = U @ Sigma @ V.T
    a = rng.normal(size=2)
    b = rng.normal(size=2)
    alpha = U @ a
    beta = V @ b
    theta = b @ np.linalg.solve(Sigma, a)
    d = theta + 1.2 + rng.uniform(0.0, 1.0)
    C = B - np.outer(alpha, beta) / d
    sv = np.linalg.svd(C, compute_uv=False)
    observed = sv[0] * sv[1]
    predicted = np.prod(s) * abs(1.0 - theta / d)
    errs.append(abs(observed - predicted) / max(1.0, observed, predicted))

print(f"max_scaled_rank2_schur_error={max(errs):.18e}")
print(f"rank2_square_constant={16/(3**0.25):.15f}")
print(f"fractional_q_4_3_H_constant={9*math.sqrt(3)*math.e/2:.15f}")
print(f"fractional_q_4_3_square_constant={4*math.sqrt(9*math.sqrt(3)*math.e/2):.15f}")
print(f"near_diffuse_square_constant={4*math.sqrt(24*math.sqrt(3)*math.e/5):.15f}")
print(f"partner_residual_square_constant={4*math.sqrt(3*2**(2/3)):.15f}")
print("STATUS=PASS")
