#!/usr/bin/env python3
"""Corroborative checks for PROB20-17 2026-09-16T010521Z.

Checks only; the Markdown report contains the analytic proofs.
No external packages beyond numpy are required.
"""

import itertools
import math
import numpy as np

SEED = 20260916010521
RNG = np.random.default_rng(SEED)


def opnorm(x):
    return float(np.linalg.norm(x, 2))


def psd(d):
    z = (RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))) / math.sqrt(2.0)
    x = z @ z.conj().T
    x /= opnorm(x)
    x *= 10.0 ** RNG.uniform(-1.0, 0.0)
    return x


def spectral_radius_ab(a, b):
    vals = np.linalg.eigvals(a @ b)
    # Products of PSD matrices have nonnegative real spectrum up to roundoff.
    return float(np.max(np.abs(vals)))


def selected_balanced_sum(a, b, m):
    """The eight selected (m,m) words used in Theorem 6.3, m>=3."""
    am = np.linalg.matrix_power(a, m)
    bm = np.linalg.matrix_power(b, m)
    ordered = 2.0 * opnorm(am @ bm)
    alternating = 2.0 * opnorm(np.linalg.matrix_power(a @ b, m))
    a1 = np.linalg.matrix_power(a, m - 1) @ bm @ a
    a2 = a @ bm @ np.linalg.matrix_power(a, m - 1)
    b1 = np.linalg.matrix_power(b, m - 1) @ am @ b
    b2 = b @ am @ np.linalg.matrix_power(b, m - 1)
    return ordered + alternating + opnorm(a1) + opnorm(a2) + opnorm(b1) + opnorm(b2)


def hierarchy_checks():
    min_power = {m: float("inf") for m in range(2, 7)}
    min_selected = {m: float("inf") for m in range(3, 7)}
    min_piecewise = {m: float("inf") for m in range(2, 7)}

    for d in (2, 3, 5):
        for _ in range(250):
            a = psd(d)
            b = psd(d)
            p = opnorm(a @ b)
            if p < 1e-12:
                continue
            r = spectral_radius_ab(a, b)
            na, nb = opnorm(a), opnorm(b)
            z = p * p / (na * na * nb * nb)

            for m in range(2, 7):
                xm = opnorm(np.linalg.matrix_power(a, m) @ np.linalg.matrix_power(b, m))
                lhs = (r ** (m - 1)) * xm / (p ** (2 * m - 1))
                min_power[m] = min(min_power[m], lhs)

                ym = opnorm(np.linalg.matrix_power(a @ b, m))
                q = (m - 1) / m
                t0 = q ** (1.0 / (2 * m - 1))
                z0 = t0 * t0
                cm = ((2 * m - 1) / m) * (m / (m - 1)) ** ((m - 1) / (2 * m - 1))
                psi = cm if z <= z0 else z ** (-(m - 1) / 2) + z ** (m / 2)
                ratio = (xm + ym) / (p ** m * psi)
                min_piecewise[m] = min(min_piecewise[m], ratio)

                if m >= 3:
                    sel = selected_balanced_sum(a, b, m)
                    min_selected[m] = min(min_selected[m], sel / (8.0 * p ** m))

    return min_power, min_piecewise, min_selected


def distinct_sum(mats):
    n = len(mats)
    total = 0.0
    for perm in itertools.permutations(range(n)):
        w = np.eye(mats[0].shape[0], dtype=complex)
        for i in perm:
            w = w @ mats[i]
        total += opnorm(w)
    return total


def perfect_matching_check_n6():
    # n=6 => m=3, only 720 distinct words, so direct enumeration is cheap.
    min_ratio = float("inf")
    min_collision_ratio = float("inf")
    for _ in range(10):
        mats = [psd(2) for _ in range(6)]
        p3 = 0.0
        q33_lower_direct = 0.0
        for i in range(6):
            for j in range(i + 1, 6):
                p = opnorm(mats[i] @ mats[j])
                p3 += p ** 3
                q33_lower_direct += selected_balanced_sum(mats[i], mats[j], 3)
        s6 = distinct_sum(mats)
        min_ratio = min(min_ratio, (48.0 * p3) / s6 if s6 else float("inf"))
        min_collision_ratio = min(
            min_collision_ratio,
            q33_lower_direct / (8.0 * p3) if p3 else float("inf"),
        )
    return min_ratio, min_collision_ratio


if __name__ == "__main__":
    power, piecewise, selected = hierarchy_checks()
    pm_ratio, collision_ratio = perfect_matching_check_n6()
    print("seed", SEED)
    print("min hierarchy ratios rho^(m-1)||A^mB^m|| / ||AB||^(2m-1):", power)
    print("min ordered+alternating / piecewise envelope:", piecewise)
    print("min selected balanced 8-word sum / (8||AB||^m):", selected)
    print("min n=6 perfect-matching RHS / S6:", pm_ratio)
    print("min n=6 selected (3,3) sum / (8 P3):", collision_ratio)

    assert min(power.values()) >= 1.0 - 1e-9
    assert min(piecewise.values()) >= 1.0 - 1e-9
    assert min(selected.values()) >= 1.0 - 1e-9
    assert pm_ratio >= 1.0 - 1e-9
    assert collision_ratio >= 1.0 - 1e-9
