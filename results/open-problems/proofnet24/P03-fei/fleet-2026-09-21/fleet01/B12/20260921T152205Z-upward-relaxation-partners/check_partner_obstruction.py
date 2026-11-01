#!/usr/bin/env python3
"""Sanity checks for the B12 FEI factorial-shadow/partner report.

The mathematical proofs are in REPORT.md.  This file only checks the explicit
rational shell+spike instance and exact integer Walsh autocorrelation on a
fixed deterministic random sample of Boolean functions.
"""

from fractions import Fraction
from math import comb, isqrt, log2
import random


def shell_spike(n=200, m=3):
    assert m == 3 and n % 2 == 0 and (n - m) % 2 == 1
    N = comb(n, m)
    t = isqrt(N)
    eps = Fraction(1, 4 * t)
    p = (1 - eps) / N

    # Squared granular upward-mass inequality p_A <= 4^(|A|-1) nu_A^2.
    shell_ok = p <= Fraction(4 ** (m - 1)) * (p + eps) ** 2
    full_ok = eps <= Fraction(4 ** (n - 1)) * eps ** 2

    I = Fraction(m) * (1 - eps) + Fraction(n) * eps
    H = -(1 - float(eps)) * log2(float(p)) - float(eps) * log2(float(eps))
    return {
        "n": n,
        "m": m,
        "N": N,
        "floor_sqrt_N": t,
        "epsilon": str(eps),
        "shell_atom_mass": str(p),
        "shell_upward_exact": shell_ok,
        "full_upward_exact": full_ok,
        "influence_exact": str(I),
        "influence_float": float(I),
        "entropy_bits": H,
        "entropy_over_influence": H / float(I),
    }


def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def partner_checks(n=6, trials=200, seed=120921):
    rng = random.Random(seed)
    N = 1 << n
    max_abs_autocorrelation = 0
    polygon_failures = 0
    translations_checked = 0

    for _ in range(trials):
        f = [1 if rng.getrandbits(1) else -1 for _ in range(N)]
        W = fwht_int(f)  # normalized coefficients are W/N; common scaling cancels
        for U in range(1, N):
            autocorrelation = sum(W[A] * W[A ^ U] for A in range(N))
            max_abs_autocorrelation = max(max_abs_autocorrelation, abs(autocorrelation))
            if autocorrelation != 0:
                raise AssertionError("Boolean autocorrelation identity failed")

            weights = []
            signed = []
            for A in range(N):
                B = A ^ U
                if A < B:
                    weights.append(abs(W[A] * W[B]))
                    signed.append(W[A] * W[B])
            if sum(signed) != 0:
                raise AssertionError("unordered-pair autocorrelation failed")
            if weights:
                total = sum(weights)
                largest = max(weights)
                if largest > total - largest:
                    polygon_failures += 1
            translations_checked += 1

    return {
        "n": n,
        "trials": trials,
        "seed": seed,
        "translations_checked": translations_checked,
        "max_abs_integer_autocorrelation": max_abs_autocorrelation,
        "partner_polygon_failures": polygon_failures,
    }


if __name__ == "__main__":
    print(shell_spike())
    print(partner_checks())
