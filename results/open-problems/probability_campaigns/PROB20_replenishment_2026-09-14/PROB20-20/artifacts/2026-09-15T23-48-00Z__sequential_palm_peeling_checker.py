#!/usr/bin/env python3
"""Finite exact-enumeration sanity checks for PROB20-20 sequential Palm peeling.

This is a bookkeeping/numerical certificate only.  It checks:
  1. normalization of the one-step size-biased removal kernel;
  2. the exact one-step KL decrement identity;
  3. the exact two-step path KL telescope.

It is not evidence for the universal asymptotic conjecture.
"""

from collections import defaultdict
from math import log

PI = {0: 0.30, 1: 0.25, 2: 0.20, 3: 0.15, 5: 0.10}
NU = sum(k * p for k, p in PI.items())
QBAR = {k: k * p / NU for k, p in PI.items() if k > 0}
TOL = 2e-12


def convolution_law(n):
    law = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for s, ps in law.items():
            for k, pk in PI.items():
                nxt[s + k] += ps * pk
        law = dict(nxt)
    return law


CACHE = {n: convolution_law(n) for n in range(9)}


def prob(n, m):
    return CACHE[n].get(m, 0.0)


def cost(n, m):
    z = prob(n, m)
    if z <= 0:
        return float("inf")
    return -log(z)


def palm_kernel(n, m):
    den = m * prob(n, m)
    out = {}
    for k, pk in PI.items():
        if k == 0:
            continue
        rem = prob(n - 1, m - k) if m >= k else 0.0
        if rem > 0:
            out[k] = n * k * pk * rem / den
    return out


def kl_kernel_to_qbar(kernel):
    return sum(v * log(v / QBAR[k]) for k, v in kernel.items())


def check_one_step(n, m):
    kernel = palm_kernel(n, m)
    norm = sum(kernel.values())
    lhs = cost(n, m) - sum(
        v * cost(n - 1, m - k) for k, v in kernel.items()
    )
    rhs = kl_kernel_to_qbar(kernel) + log((m / n) / NU)
    err = lhs - rhs
    assert abs(norm - 1.0) < TOL
    assert abs(err) < TOL
    return norm, lhs, rhs, err


def path_distribution(n, m, r):
    states = {((), n, m): 1.0}
    for _ in range(r):
        nxt = defaultdict(float)
        for (path, nj, mj), pr in states.items():
            assert nj > 0 and mj > 0
            for k, pk in palm_kernel(nj, mj).items():
                nxt[(path + (k,), nj - 1, mj - k)] += pr * pk
        states = dict(nxt)
    return states


def check_path(n, m, r):
    states = path_distribution(n, m, r)
    total = sum(states.values())
    kl = 0.0
    expected_terminal_cost = 0.0
    expected_density_premium = 0.0

    for (path, nf, mf), pr in states.items():
        q = 1.0
        nj, mj = n, m
        path_premium = 0.0
        for k in path:
            q *= QBAR[k]
            path_premium += log((mj / nj) / NU)
            nj -= 1
            mj -= k
        kl += pr * log(pr / q)
        expected_terminal_cost += pr * cost(nf, mf)
        expected_density_premium += pr * path_premium

    rhs = cost(n, m) - expected_terminal_cost - expected_density_premium
    err = kl - rhs
    assert abs(total - 1.0) < TOL
    assert abs(err) < TOL
    return total, kl, rhs, err


def main():
    print(f"nu={NU:.17g}")
    print("ONE-STEP CHECKS")
    for n, m in [(5, 8), (6, 10), (5, 10), (7, 12)]:
        norm, lhs, rhs, err = check_one_step(n, m)
        print(
            f"N={n} M={m} norm={norm:.17g} "
            f"lhs={lhs:.17g} rhs={rhs:.17g} error={err:.3e}"
        )

    print("TWO-STEP PATH CHECKS")
    for n, m, r in [(6, 10, 2), (7, 10, 2), (7, 12, 2)]:
        total, kl, rhs, err = check_path(n, m, r)
        print(
            f"N={n} M={m} r={r} total={total:.17g} "
            f"path_KL={kl:.17g} telescope={rhs:.17g} error={err:.3e}"
        )

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
