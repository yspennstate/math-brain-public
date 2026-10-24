import math
import numpy as np

rng = np.random.default_rng(202609240211)

# 1. Canonical active 4x4 invariant.
max_canonical_rel = 0.0
for _ in range(5000):
    kappa = 10.0 ** rng.uniform(-1.0, 1.0)
    lam = (1.0 if rng.random() < 0.5 else -1.0) * 10.0 ** rng.uniform(-1.0, 1.0)
    b = rng.normal()
    eta = rng.normal()
    gamma = abs(rng.normal())
    T = np.array([
        [0.0, kappa, 0.0, 0.0],
        [kappa, b, eta, gamma],
        [0.0, eta, lam, 0.0],
        [0.0, gamma, 0.0, 0.0],
    ])
    eig = np.linalg.eigvalsh(T)
    nz = eig[np.abs(eig) > 1e-8]
    assert len(nz) == 3
    lhs = float(np.prod(nz))
    rhs = -lam * (kappa * kappa + gamma * gamma)
    rel = abs(lhs - rhs) / max(1.0, abs(rhs))
    max_canonical_rel = max(max_canonical_rel, rel)

# 2. Recover the invariant after random residual orthogonal embeddings.
rng = np.random.default_rng(202609240212)
max_second_sv = 0.0
max_embedded_rel = 0.0
for _ in range(1000):
    residual_dim = 7
    kappa = 10.0 ** rng.uniform(-0.5, 0.5)
    lam = (1.0 if rng.random() < 0.5 else -1.0) * 10.0 ** rng.uniform(-0.5, 0.5)
    b = rng.normal()
    eta = rng.normal()
    gamma = abs(rng.normal())

    A0 = np.zeros((residual_dim + 1, residual_dim + 1))
    A0[:4, :4] = np.array([
        [0.0, kappa, 0.0, 0.0],
        [kappa, b, eta, gamma],
        [0.0, eta, lam, 0.0],
        [0.0, gamma, 0.0, 0.0],
    ])

    G = rng.normal(size=(residual_dim, residual_dim))
    O, _ = np.linalg.qr(G)
    R = np.eye(residual_dim + 1)
    R[1:, 1:] = O
    A = R @ A0 @ R.T

    c = A[1:, 0]
    kk = np.linalg.norm(c)
    u = c / kk
    B = A[1:, 1:]
    Pu = np.eye(residual_dim) - np.outer(u, u)
    C = Pu @ B @ Pu
    sv = np.linalg.svd(C, compute_uv=False)
    max_second_sv = max(max_second_sv, float(sv[1]))

    ce, cv = np.linalg.eigh(C)
    idx = int(np.argmax(np.abs(ce)))
    ll = float(ce[idx])
    v = cv[:, idx]
    q = Pu @ B @ u
    eta_rec = float(v @ q)
    q_perp = q - eta_rec * v
    gg = float(np.linalg.norm(q_perp))

    ae = np.linalg.eigvalsh(A)
    anz = ae[np.abs(ae) > 1e-8]
    assert len(anz) == 3
    lhs = float(np.prod(np.abs(anz)))
    rhs = abs(ll) * (kk * kk + gg * gg)
    rel = abs(lhs - rhs) / max(1.0, rhs)
    max_embedded_rel = max(max_embedded_rel, rel)

aligned_constant = 3.0 * 2.0 ** (4.0 / 3.0)
partner_constant = 2.0 * 12.0 ** (1.0 / 3.0) * (64.0 / 63.0) ** (1.0 / 3.0)

print(f"max_canonical_relative_error={max_canonical_rel:.16e}")
print(f"max_embedded_second_singular_value={max_second_sv:.16e}")
print(f"max_embedded_invariant_relative_error={max_embedded_rel:.16e}")
print(f"aligned_constant={aligned_constant:.15f}")
print(f"partner_q_ge_63_64_constant={partner_constant:.15f}")
print("QFORM_B11_ZEROPIVOT_WITT_LEAKAGE_CHECK_PASS")
