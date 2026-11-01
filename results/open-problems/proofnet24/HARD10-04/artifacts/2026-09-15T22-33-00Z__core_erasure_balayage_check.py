"""Finite algebra certificate for HARD10-04 core-erasure balayage.

This is NOT a DLA simulation and does not verify the open growth exponent.
It checks the finite probability identity used in the 2026-09-15T22:28Z report:

    nu_O = mu_O + mu_I H,
    TV(mu_K, nu_O extended by zero on I) = mu_K(I),

for random probability vectors mu and random stochastic continuation kernels H.
It also prints the deterministic error scales appearing in the sparse-edit theorem.
"""

from __future__ import annotations

import math
import numpy as np


def check_once(rng: np.random.Generator, n_inner: int, n_outer: int) -> float:
    raw = rng.random(n_inner + n_outer)
    mu = raw / raw.sum()

    H = rng.random((n_inner, n_outer))
    H /= H.sum(axis=1, keepdims=True)

    mu_inner = mu[:n_inner]
    mu_outer = mu[n_inner:]

    # Balayage: if the first hit of K is in I, continue to O using H.
    nu_outer = mu_outer + mu_inner @ H
    nu_extended = np.concatenate([np.zeros(n_inner), nu_outer])

    tv = 0.5 * np.abs(mu - nu_extended).sum()
    target = mu_inner.sum()

    errors = [
        abs(tv - target),
        abs(nu_outer.sum() - 1.0),
        max(0.0, -float((nu_outer - mu_outer).min())),
    ]
    return max(errors)


def sparse_edit_scales(R: float, L: float) -> tuple[float, float, float]:
    """Return cutoff radius, penetration term, and martingale term."""
    s = R * math.exp(-L)
    penetration = math.exp(-L / 2.0)
    martingale = R ** (-0.25)
    return s, penetration, martingale


def main() -> None:
    rng = np.random.default_rng(20260915)
    worst = 0.0
    for _ in range(10_000):
        n_inner = int(rng.integers(1, 6))
        n_outer = int(rng.integers(1, 9))
        worst = max(worst, check_once(rng, n_inner, n_outer))

    print(f"10,000 random finite balayage checks: worst algebra error = {worst:.3e}")

    for R in (1e6, 1e12, 1e24):
        L = math.log(max(math.log(R), 2.0))
        s, penetration, martingale = sparse_edit_scales(R, L)
        print(
            f"R={R:.1e}, L=log log R={L:.4f}, "
            f"s=R/log R={s:.4e}, "
            f"penetration~{penetration:.4e}, martingale~{martingale:.4e}"
        )

    assert worst < 1e-12


if __name__ == "__main__":
    main()
