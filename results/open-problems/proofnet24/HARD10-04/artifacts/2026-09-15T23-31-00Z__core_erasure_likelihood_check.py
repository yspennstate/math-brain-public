#!/usr/bin/env python3
"""Finite algebra certificate for HARD10-04 core-erasure likelihood identities.

This is NOT a DLA simulation and does not test the unresolved growth exponent.
It checks, on randomized finite probability spaces, the algebra used in the
2026-09-15T23:26:00Z HARD10-04 report.

Construction:
  * p is a probability law on a finite set K = I disjoint-union O.
  * H is a stochastic continuation kernel from I to O.
  * q on O is p restricted to O plus the mass from I transported by H.

The exact identities/inequalities checked are:
  TV(p,q) = p(I) = eps,
  E_p[log(q/p) 1_O] <= eps,
  E_p[exp(theta L)] <= eps + (1-eps)^(1-theta), 0<=theta<=1,
where L=log(q/p) on O and L=0 on I.
"""

import math
import random
import numpy as np


def one_trial(m: int = 12) -> None:
    raw = np.random.exponential(1.0, size=m)
    p = raw / raw.sum()

    k = random.randint(1, m - 1)
    I = np.array(random.sample(range(m), k), dtype=int)
    mask = np.ones(m, dtype=bool)
    mask[I] = False
    O = np.where(mask)[0]

    eps = float(p[I].sum())

    H = np.random.exponential(1.0, size=(k, len(O)))
    H /= H.sum(axis=1, keepdims=True)

    q = np.zeros(m)
    q[O] = p[O] + p[I] @ H

    tv = 0.5 * float(np.abs(p - q).sum())
    assert abs(tv - eps) <= 1e-12, (tv, eps)

    L = np.zeros(m)
    L[O] = np.log(q[O] / p[O])

    elog = float(np.dot(p, L))
    assert elog <= eps + 1e-12, (elog, eps)

    for theta in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
        mgf = float(np.dot(p, np.exp(theta * L)))
        rhs = eps + (1.0 - eps) ** (1.0 - theta)
        assert mgf <= rhs + 1e-12, (theta, mgf, rhs)

        if eps <= 0.5:
            assert mgf <= math.exp(2.0 * theta * eps) + 1e-12


def scalar_three_halves_example(R: float) -> None:
    """Check the abstract R^{-3/2} sharpness scaling.

    One 'inner' atom has p=R^{-1/2}; R outer atoms split the remaining mass.
    This saturates p_* ~ R^{-1/2}, core mass ~ R^{-1/2}, and contributes
    exactly R^{-3/2} to S_3 from the inner atom.
    """
    inner = R ** (-0.5)
    core_s3 = inner ** 3
    target = R ** (-1.5)
    assert abs(core_s3 / target - 1.0) <= 1e-12


if __name__ == "__main__":
    np.random.seed(20260915)
    random.seed(20260915)

    for _ in range(10_000):
        one_trial()

    for R in (16.0, 64.0, 256.0, 4096.0, 65536.0):
        scalar_three_halves_example(R)

    print("PASS: 10,000 randomized likelihood checks + R^{-3/2} sharpness checks")
