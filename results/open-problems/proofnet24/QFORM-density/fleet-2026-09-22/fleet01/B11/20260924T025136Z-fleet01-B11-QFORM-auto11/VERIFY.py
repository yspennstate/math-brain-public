import math
import numpy as np

rng = np.random.default_rng(20260924)
max_prod_rel = 0.0
max_lev_err = 0.0
max_kernel = 0.0

for _ in range(5000):
    kappa = float(10 ** rng.uniform(-2, 2))
    gamma = float((1 if rng.random() < 0.5 else -1) * 10 ** rng.uniform(-2, 2))
    lam = float((1 if rng.random() < 0.5 else -1) * 10 ** rng.uniform(-2, 2))
    b = float(rng.normal() * 5)
    eta = float(rng.normal() * 5)

    A = np.array([
        [0.0, kappa, 0.0, 0.0],
        [kappa, b, eta, gamma],
        [0.0, eta, lam, 0.0],
        [0.0, gamma, 0.0, 0.0],
    ])

    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-9]
    assert len(nz) == 3
    prod = float(np.prod(nz))
    target_prod = -lam * (kappa * kappa + gamma * gamma)
    max_prod_rel = max(max_prod_rel, abs(prod - target_prod) / max(1.0, abs(target_prod)))

    n = np.array([gamma, 0.0, 0.0, -kappa])
    n /= np.linalg.norm(n)
    max_kernel = max(max_kernel, float(np.linalg.norm(A @ n)))
    P = np.eye(4) - np.outer(n, n)
    leverage = float(P[0, 0])
    target_leverage = kappa * kappa / (kappa * kappa + gamma * gamma)
    max_lev_err = max(max_lev_err, abs(leverage - target_leverage))

near_coloop_constant = 3 * 2 ** (4 / 3) * (64 / 63) ** (1 / 3)
partner_constant = 2 * 12 ** (1 / 3) * (64 / 63) ** (1 / 3)

print(f"max_product_relative_error={max_prod_rel:.16e}")
print(f"max_leverage_error={max_lev_err:.16e}")
print(f"max_kernel_residual={max_kernel:.16e}")
print(f"near_coloop_constant={near_coloop_constant:.15f}")
print(f"fleet02_B11_partner_constant={partner_constant:.15f}")
print("QFORM_B11_WITT_LEVERAGE_COMPILER_CHECK_PASS")
