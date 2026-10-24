#!/usr/bin/env python3
"""Regression checks for QFORM-OFFDIAGONAL-STABLERANK-v1.

This script is not a proof certificate.  It checks the explicit numerical
constant and finite-sample instances of the determinant chord inequality used
in REPORT.md.
"""
import math
import random

ALPHA = 4.0 / (math.pi**2 * math.e**2)
C_DENSITY = 2.0 * math.e * math.sqrt(8.0) * (math.sqrt(2.0 * math.pi) + 2.0)

assert C_DENSITY < 70.0
assert abs(math.sqrt(ALPHA) - 2.0 / (math.pi * math.e)) < 1e-15

rng = random.Random(20260922)
worst_margin = float("inf")
trials = 300
for _ in range(trials):
    m = rng.randint(8, 40)
    sigma = [rng.random() for _ in range(m)]
    sigma[0] = 1.0
    while sum(s*s for s in sigma) < 8.0:
        sigma[rng.randrange(m)] = 1.0
    L = max(sigma)
    stable_rank = sum(s*s for s in sigma) / (L*L)
    assert stable_rank >= 8.0 - 1e-12

    # log det(I + alpha t^2 C C^T) >= sr(C) log(1+alpha L^2 t^2)
    # for a grid of t.  The exact proof is concavity of log(1+xu).
    for j in range(-20, 41):
        t = 10.0 ** (j / 10.0)
        x = ALPHA * t*t * L*L
        logdet = sum(math.log1p(ALPHA * t*t * s*s) for s in sigma)
        lower = stable_rank * math.log1p(x)
        margin = logdet - lower
        worst_margin = min(worst_margin, margin)
        assert margin >= -1e-10

print(f"alpha={ALPHA:.17g}")
print(f"density_constant={C_DENSITY:.15f}")
print(f"random_singular_spectra={trials}")
print(f"worst_logdet_margin={worst_margin:.3e}")
print("QFORM_B19_STABLERANK_CROSSCUT_PASS")
