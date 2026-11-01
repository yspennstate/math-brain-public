#!/usr/bin/env python3
"""Finite checks for QFORM-ARBITRARY-PIVOT-LOWRESIDUAL-RANK-v1.

These checks are regression tests only; the proof is exact algebra in REPORT.md.
"""
import math
import numpy as np

rng = np.random.default_rng(0)
max_eig_error = 0.0
rank_failures = 0

for typ in (1, 2):
    for _ in range(1000):
        m = 7
        Q, _ = np.linalg.qr(rng.normal(size=(m, 2)))
        u, v = Q[:, 0], Q[:, 1]

        if typ == 1:
            lam = rng.choice([-1.0, 1.0]) * (1.0 + 3.0 * rng.random())
            C = lam * np.outer(u, u)
            l = rng.normal() * u + (0.2 + rng.random()) * v
            a = rng.normal()
        else:
            vals = np.array([
                rng.choice([-1.0, 1.0]) * (1.0 + 3.0 * rng.random()),
                rng.choice([-1.0, 1.0]) * (1.0 + 3.0 * rng.random()),
            ])
            C = Q @ np.diag(vals) @ Q.T
            q = rng.normal(size=2)
            l = Q @ q
            kappa = q @ np.diag(1.0 / vals) @ q
            a = kappa + rng.choice([-1.0, 1.0]) * (0.2 + rng.random())

        A = np.block([[np.array([[a]]), l[None, :]], [l[:, None], C]])
        if np.linalg.matrix_rank(A, tol=1e-8) != 3:
            rank_failures += 1

        B = np.column_stack([
            np.r_[1.0, np.zeros(m)],
            np.r_[0.0, u],
            np.r_[0.0, v],
        ])
        T = B.T @ A @ B
        ambient = np.linalg.eigvalsh(A)
        ambient = ambient[np.abs(ambient) > 1e-8]
        core = np.linalg.eigvalsh(T)
        max_eig_error = max(
            max_eig_error,
            float(np.max(np.abs(np.sort(ambient) - np.sort(core)))),
        )

G0 = ((2.0 * math.pi) ** 1.5 * math.exp(0.5) * math.gamma(0.25)
      / (4.0 * math.sqrt(math.pi) * math.gamma(0.75)))
r = 0.848
R = math.sqrt(5.0 + (1.0 + 2.0 * r) ** 2 / (1.0 - r * r))
Bconst = 1.0 + 2.0 * (2.0 / math.sqrt(1.0 - r * r) + 2.0 + G0 * R)
scalar = 128.0 * r ** (-0.25)

print(f"rank_failures={rank_failures}")
print(f"max_eigenvalue_error={max_eig_error:.16e}")
print(f"G0={G0:.15f}")
print(f"B(0.848,2)={Bconst:.15f}")
print(f"scalar_branch={scalar:.15f}")
assert rank_failures == 0
assert max_eig_error < 1e-10
assert Bconst < 134.0
assert scalar < 134.0
print("QFORM_B11_LOWRESIDUAL_ARBITRARY_PIVOT_CHECK_PASS")
