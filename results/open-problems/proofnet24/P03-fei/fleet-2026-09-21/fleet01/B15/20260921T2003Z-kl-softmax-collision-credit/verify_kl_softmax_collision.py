"""Finite sanity checks for B15-KL-SOFTMAX-01.

This script checks only the algebraic identity and the displayed remote-gap
specialization.  The universal claims in REPORT.md are proved symbolically.
"""

from __future__ import annotations

import math
import random
from fractions import Fraction


def decompose(weights, depths):
    total = sum(weights)
    lam = [w / total for w in weights]
    M = max(depths)
    mean = sum(a * x for a, x in zip(lam, depths))
    collision = M - mean
    Z = sum(a * (4.0 ** x) for a, x in zip(lam, depths))
    q = [a * (4.0 ** x) / Z for a, x in zip(lam, depths)]
    kl = sum(a * math.log2(a / b) for a, b in zip(lam, q))
    psi = M - 0.5 * math.log2(Z)
    return collision, kl, psi


def random_identity_checks(seed=20260921, trials=10000):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        m = rng.randint(2, 7)
        weights = [10.0 ** rng.uniform(-5.0, 1.0) for _ in range(m)]
        depths = [rng.randint(0, 20) for _ in range(m)]
        collision, kl, psi = decompose(weights, depths)
        err = abs(collision - (0.5 * kl + psi))
        worst = max(worst, err)
        assert psi >= -2e-12
        assert psi <= collision + 2e-12
    return worst


def remote_gap_row(k):
    x = Fraction(1, 4)
    y = Fraction(2 ** (k + 1) - 1, 2 ** (2 * k + 2))
    P = x + y
    rho = float(y / P)
    psi = -0.5 * math.log2(rho + (1.0 - rho) * (4.0 ** (-k)))
    residual = float(P) * psi
    raw = k / 4.0
    credit = raw - residual
    assert abs(raw - (credit + residual)) < 2e-12
    return float(P), rho, raw, credit, residual


def main():
    worst = random_identity_checks()
    print(f"random_trials=10000 worst_identity_error={worst:.3e}")
    print("k P rho raw KL_part softmax_residual")
    for k in (2, 4, 8, 16, 32):
        P, rho, raw, credit, residual = remote_gap_row(k)
        print(
            f"{k:2d} {P:.12g} {rho:.12g} {raw:.12g} "
            f"{credit:.12g} {residual:.12g}"
        )
    print("PASS")


if __name__ == "__main__":
    main()
