#!/usr/bin/env python3
"""Corroborative checker for PROB20-17 report 2026-09-15T233655Z.

This script is NOT a proof.  It stress-tests:
  1. rho(AB) * ||A^2 B^2|| >= ||AB||^3;
  2. the piecewise pair-sum bound for ||A^2B^2||+||ABAB||;
  3. the Jensen aggregate Q_22 bound;
  4. the final scalar constant against direct n=4 word enumeration.

The report contains the mathematical proofs.
"""

import itertools
import math
import numpy as np

SEED = 20260915233655
rng = np.random.default_rng(SEED)


def op(a):
    return float(np.linalg.norm(a, 2))


def random_psd(d):
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    a /= op(a)
    a *= 10.0 ** rng.uniform(-1.0, 1.0)
    return a


def rho_product(a, b):
    vals, u = np.linalg.eigh(b)
    bs = (u * np.sqrt(np.maximum(vals, 0.0))) @ u.conj().T
    c = bs @ a @ bs
    c = (c + c.conj().T) / 2.0
    return float(np.max(np.linalg.eigvalsh(c)).real)


Z0 = 2.0 ** (-2.0 / 3.0)
PAIR_C = 3.0 / 2.0 ** (2.0 / 3.0)
E0 = 2.0 ** (2.0 / 3.0)
Q22_TAIL = 2.0 + 3.0 * 2.0 ** (1.0 / 3.0)
RS_CONSTANT = (
    11.0 / 2.0
    + 3.0 / 4.0 * 2.0 ** (1.0 / 3.0)
    + 3.0 / 6.0 ** (1.0 / 3.0)
)
NORMALIZED_CONSTANT = 3.0 * RS_CONSTANT / 32.0


def psi(z):
    if z <= Z0:
        return PAIR_C
    return z ** (-0.5) + z


def q22_coefficient(e):
    if e <= E0:
        return 2.0 * (1.0 + math.sqrt(e) + 1.0 / e)
    return Q22_TAIL


def pair_tests():
    min_interp = float("inf")
    min_pair = float("inf")
    for d in (2, 3, 4, 6):
        for _ in range(200):
            a = random_psd(d)
            b = random_psd(d)
            p = op(a @ b)
            if p < 1e-13:
                continue
            r = rho_product(a, b)
            x = op(a @ a @ b @ b)
            y = op(a @ b @ a @ b)
            min_interp = min(min_interp, r * x / p**3)
            z = p**2 / (op(a) ** 2 * op(b) ** 2)
            min_pair = min(min_pair, (x + y) / (p**2 * psi(z)))
    return min_interp, min_pair


def four_matrix_tests():
    min_q22 = float("inf")
    min_full = float("inf")
    for d in (2, 3, 4):
        for _ in range(100):
            mats = [random_psd(d) for _ in range(4)]
            p_sum = 0.0
            e_sum = 0.0
            q22 = 0.0
            for i in range(4):
                for j in range(i + 1, 4):
                    a, b = mats[i], mats[j]
                    p = op(a @ b)
                    p_sum += p**2
                    e_sum += op(a) ** 2 * op(b) ** 2
                    x = op(a @ a @ b @ b)
                    y = op(a @ b @ a @ b)
                    q22 += 2.0 * (x + y + p**2)
            e = e_sum / p_sum
            min_q22 = min(min_q22, q22 / (p_sum * q22_coefficient(e)))

            s = sum(
                op(mats[i] @ mats[j] @ mats[k] @ mats[l])
                for i, j, k, l in itertools.permutations(range(4))
            )
            r_all = sum(
                op(mats[i] @ mats[j] @ mats[k] @ mats[l])
                for i, j, k, l in itertools.product(range(4), repeat=4)
            )
            if s > 1e-13:
                min_full = min(min_full, (r_all / s) / RS_CONSTANT)
    return min_q22, min_full


if __name__ == "__main__":
    mi, mp = pair_tests()
    mq, mf = four_matrix_tests()
    print(f"seed={SEED}")
    print(f"pair interpolation min ratio = {mi:.15g}")
    print(f"pair piecewise min ratio     = {mp:.15g}")
    print(f"aggregate Q22 min ratio      = {mq:.15g}")
    print(f"direct R/S / theorem min     = {mf:.15g}")
    print(f"R/S theorem constant         = {RS_CONSTANT:.15g}")
    print(f"normalized theorem constant  = {NORMALIZED_CONSTANT:.15g}")
    assert mi >= 1.0 - 1e-10
    assert mp >= 1.0 - 1e-10
    assert mq >= 1.0 - 1e-10
    assert mf >= 1.0 - 1e-10
