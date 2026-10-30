#!/usr/bin/env python3
"""Finite diagnostics for TWOANCHOR_L2_RELAY.md; not a proof certificate."""
import math
import numpy as np

C = 3 * math.pi ** (1/3) / (2 ** (4/3))
assert abs(C - 1.7436710272644393) < 1e-14
assert abs(2 * math.pi - 6.283185307179586) < 1e-14

# Check the optimized Fourier-splitting formula at several H values.
for H in (0.01, 0.1, 1.0, 10.0):
    tau = (math.pi * math.sqrt(math.pi) * H / 2) ** (2/3)
    l1 = 2 * tau + 2 * math.pi * math.sqrt(math.pi) * H / math.sqrt(tau)
    p = l1 / (2 * math.pi)
    closed = 3 * 2 ** (-2/3) * H ** (2/3)
    assert abs(p - closed) < 1e-12

# Diagnostic only: random symmetric B with ||B||_op <= 1/2.
# Weyl's theorem proves the exact >=3/2 carrier bound; this merely regression-tests it.
rng = np.random.default_rng(20260924)
min_abs = 10.0
for _ in range(10000):
    M = rng.normal(size=(2, 2))
    B = (M + M.T) / 2
    op = np.linalg.norm(B, 2)
    if op > 0:
        B *= (0.5 / op) * rng.random()
    A = np.block([[B, 2 * np.eye(2)], [2 * np.eye(2), np.zeros((2, 2))]])
    ev = np.linalg.eigvalsh(A)
    min_abs = min(min_abs, float(np.min(np.abs(ev))))
    assert np.min(np.abs(ev)) >= 1.5 - 1e-10

print(f"relay_control_constant={C:.15f}")
print(f"partner_definite_plane_constant={2*math.pi:.15f}")
print(f"sampled_min_abs_carrier_eigenvalue={min_abs:.15f}")
print("STATUS=PASS")
