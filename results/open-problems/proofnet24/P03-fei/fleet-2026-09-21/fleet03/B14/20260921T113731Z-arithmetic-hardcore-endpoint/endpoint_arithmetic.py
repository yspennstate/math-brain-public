#!/usr/bin/env python3
"""Numerics for the B14 exact hard-core endpoint arithmetic lemma.

This script does not search Boolean functions and does not certify FEI.  It only
reproduces the discrete endpoint values r_m and the elementary link-degree
lower bound proved in REPORT.md.
"""

import math


def h2(q: float) -> float:
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)


def j(q: float) -> float:
    return 1.0 - h2(0.5 + math.sqrt(q * (1.0 - q)))


def kappa(q: float) -> float:
    return (h2(q) + j(q)) / q


print("m tau r_m min_fourier_coneighbor_degree min_link_size")
for m in range(2, 9):
    theta = 1.0 / (m * m)
    tau = theta / (1.0 + theta)
    r = kappa(tau)
    dmin = math.ceil(math.log(2.0) / math.log(1.0 + theta) - 1e-14)
    print(f"{m} {tau:.17g} {r:.15f} {dmin} {m*m+1}")
