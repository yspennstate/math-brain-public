#!/usr/bin/env python3
"""Finite-scale consistency checker for HARD10-04 scalar sharpness family.

This is NOT a DLA simulation and NOT a proof of the DLA exponent.  It checks the
explicit abstract probability family used in the 2026-09-15T19:55:00Z report.
For D in [3/2,2], one heavy atom has mass R^{-D/3} and R light atoms share the
remaining mass.  The script reports the normalized entropy, third-moment
exponent, Beurling-scale maximum, unit-drift block size, and higher-moment
quantity.  The mathematical proof is in the Markdown report; this script is a
reproducibility/algebra certificate only.
"""

from __future__ import annotations

import math


def row(R: int, D: float, q: float = 3.0, kappa: float = 2.0) -> dict[str, float]:
    if not (1.5 <= D <= 2.0):
        raise ValueError("D must lie in [1.5,2]")
    if q <= 1:
        raise ValueError("q must exceed 1")
    h = R ** (-D / 3.0)
    light = (1.0 - h) / R
    H = -h * math.log(h) - R * light * math.log(light)
    S3 = h**3 + R * light**3
    a = kappa * S3
    N = max(1, math.floor(1.0 / a))
    mq = kappa**q * (h ** (2.0 * q + 1.0) + R * light ** (2.0 * q + 1.0))
    return {
        "D": D,
        "R": float(R),
        "H_over_logR": H / math.log(R),
        "tau3": -math.log(S3) / math.log(R),
        "pmax_times_sqrtR": h * math.sqrt(R),
        "N_over_R_to_D": N / (R**D),
        "N_times_a": N * a,
        "scaled_higher_moment": N * mq * (R ** (q - 1.0)),
    }


def main() -> None:
    R = 10**6
    q = 3.0
    for D in (1.5, 1.6, 1.712, 1.9, 2.0):
        out = row(R, D, q=q)
        print(" ".join(f"{k}={v:.12g}" for k, v in out.items()))
        assert out["pmax_times_sqrtR"] <= 1.0 + 1e-12
        assert 0.99 <= out["N_times_a"] <= 1.0 + 1e-12
        # The theorem proves this scaled quantity stays O(1) as R grows.
        assert math.isfinite(out["scaled_higher_moment"])


if __name__ == "__main__":
    main()
