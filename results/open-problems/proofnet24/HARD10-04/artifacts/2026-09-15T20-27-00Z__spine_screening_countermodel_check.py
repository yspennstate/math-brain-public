#!/usr/bin/env python3
"""Finite algebra certificate for the HARD10-04 spine screening countermodel.

This is NOT a DLA simulation and NOT evidence about the value of the DLA exponent.
It verifies the exact finite-dimensional identities used in the report
proofnet24/HARD10-04/runs/2026-09-15/2026-09-15T20-22-30Z__report.md:

1. nu_n = nu_{n+1} P_n for the deterministic reverse kernel;
2. TV(nu_{n+1}, nu_n extended by zero) = q_{n+1};
3. fixed old-shell posterior variance stays constant (zero screening);
4. on an N-step constant-q plateau with q=N^{-1/2}, first pair-overlap
   moment is 1 while the exact second moment is N.
"""

from __future__ import annotations

import math
import numpy as np


def spine_measure(q: list[float | None], n: int) -> np.ndarray:
    """Return nu_n on {1,...,n}; q is 1-indexed with q[0]=None."""
    out = np.zeros(n, dtype=float)
    for j in range(1, n):
        out[j - 1] = float(q[j] - q[j + 1])
    out[n - 1] = float(q[n])
    return out


def check_projectivity(max_n: int = 500) -> None:
    q: list[float | None] = [None] + [1.0 / math.sqrt(n) for n in range(1, max_n + 2)]

    for n in range(1, max_n):
        nu_n = spine_measure(q, n)
        nu_np1 = spine_measure(q, n + 1)

        # P_n is identity on {1,...,n}; n+1 is sent deterministically to n.
        pushed = nu_np1[:n].copy()
        pushed[n - 1] += nu_np1[n]
        assert np.allclose(pushed, nu_n, atol=1e-13, rtol=0.0)

        extended = np.concatenate([nu_n, np.array([0.0])])
        tv = 0.5 * np.abs(nu_np1 - extended).sum()
        assert abs(tv - float(q[n + 1])) < 1e-13


def check_zero_screening(k: int = 11, max_n: int = 500) -> None:
    q: list[float | None] = [None] + [1.0 / math.sqrt(n) for n in range(1, max_n + 2)]
    delta = float(q[k + 1])

    for n in range(k + 1, max_n + 1):
        nu_n = spine_measure(q, n)
        # Deterministic ancestry: a present state j descends through shell k
        # iff j >= k+1.
        posterior = np.array([1.0 if j >= k + 1 else 0.0 for j in range(1, n + 1)])
        mean = float(np.dot(nu_n, posterior))
        variance = float(np.dot(nu_n, (posterior - delta) ** 2))
        assert abs(mean - delta) < 1e-13
        assert abs(variance - delta * (1.0 - delta)) < 1e-13


def check_plateau_pair_clock() -> None:
    for n_steps in (10, 100, 1000, 10000):
        q = n_steps ** -0.5
        first_moment = n_steps * q * q
        # In the spine plateau, c_{k,l}=q for every k<l, so the pair-clock
        # second moment is N q^2 + 2*C(N,2) q^2 = N.
        second_moment = n_steps * q * q + 2.0 * (n_steps * (n_steps - 1) / 2.0) * q * q
        assert abs(first_moment - 1.0) < 1e-12
        assert abs(second_moment - n_steps) < 1e-9


def main() -> None:
    check_projectivity()
    check_zero_screening()
    check_plateau_pair_clock()
    print("PASS: projectivity, TV increments, zero screening, and plateau pair-clock identities verified.")


if __name__ == "__main__":
    main()
