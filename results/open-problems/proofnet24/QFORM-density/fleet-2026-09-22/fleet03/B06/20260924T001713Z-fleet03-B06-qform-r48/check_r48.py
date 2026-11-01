#!/usr/bin/env python3
"""Finite sanity checks for fleet03/B06 r48.

These are only numerical checks of exact algebraic identities proved in REPORT.md.
They are not substitutes for the proofs.
"""

import math
import numpy as np

rng = np.random.default_rng(0)


def relerr(x, y):
    return abs(x-y) / max(1.0, abs(x), abs(y))


max_currency_err = 0.0
max_resonance_err = 0.0
accepted = 0
for _ in range(10_000):
    E = rng.normal(size=(2, 8))
    G = E @ E.T
    if abs(np.linalg.det(G)) < 1e-8:
        continue
    h = int(rng.integers(0, E.shape[1]))
    e = E[:, h]
    E0 = np.delete(E, h, axis=1)
    G0 = E0 @ E0.T
    alpha = float(e @ np.linalg.solve(G, e))
    if abs(1-alpha) < 1e-9:
        continue

    M = rng.normal(size=(2, 2))
    T = (M + M.T) / 2.0
    d0 = float(rng.normal())
    s = d0 + float(e @ T @ e)
    if abs(s) < 1e-8:
        continue
    T0 = T - np.outer(T @ e, T @ e) / s

    lhs = np.linalg.det(T0) * np.linalg.det(G0)
    rhs = np.linalg.det(T) * np.linalg.det(G) * (d0/s) * (1-alpha)
    max_currency_err = max(max_currency_err, relerr(lhs, rhs))

    Hraw = rng.normal(size=(2, 2))
    H = (Hraw + Hraw.T) / 2.0
    if abs(np.linalg.det(H)) < 1e-8:
        continue
    v = rng.normal(size=2)
    v /= np.linalg.norm(v)
    lam = float(rng.normal())
    U = np.linalg.inv(H) + lam * np.outer(v, v)
    lhs2 = np.linalg.det(U)
    rhs2 = (1.0 + lam * float(v @ H @ v)) / np.linalg.det(H)
    max_resonance_err = max(max_resonance_err, relerr(lhs2, rhs2))
    accepted += 1

print("accepted", accepted)
print("max_currency_normalized_error", repr(max_currency_err))
print("max_resonance_normalized_error", repr(max_resonance_err))
print("three_pivot_prefactor", repr(4 * 2 ** (5/8)))
print("rank1_resonance_prefactor", repr(3 * 2 ** (5/3)))

assert accepted > 9_000
assert max_currency_err < 1e-9
assert max_resonance_err < 1e-9
assert abs(4 * 2 ** (5/8) - 6.168843301631763) < 1e-12
assert abs(3 * 2 ** (5/3) - 9.524406311809198) < 1e-12

print("QFORM_B06_R48_CHECK_PASS")
