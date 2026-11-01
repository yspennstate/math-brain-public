#!/usr/bin/env python3
"""Reproducible finite checks, not a proof of the infinite-state theorem.
Run with Python 3.10+; numpy is required only for the numerical diagnostics.
"""
from fractions import Fraction as F
from itertools import product
import json
import numpy as np


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def six_state(e):
    states = list(product((-1, 1), (-1, 0, 1)))
    nu = {-1: e, 0: 1 - 2 * e, 1: e}
    pi = [nu[v] / 2 for u, v in states]
    p = [[pi[j] * (1 + u * vp) for j, (up, vp) in enumerate(states)]
         for u, v in states]
    assert all(x >= 0 for row in p for x in row)
    assert all(sum(row) == 1 for row in p)
    assert [sum(pi[i] * p[i][j] for i in range(6)) for j in range(6)] == pi
    assert matmul(p, p) == [pi] * 6
    phi = max(sum(abs(p[i][j] - pi[j]) for j in range(6)) / 2 for i in range(6))
    delta = max(sum(abs(p[i][j] - p[k][j]) for j in range(6)) / 2
                for i in range(6) for k in range(6))
    assert phi == e and delta == 2 * e
    for m in (F(-3, 4), F(-1, 3), F(0), F(2, 5), F(4, 5)):
        posterior_var = e*(1+m)*(1-m)**2 + e*(1-m)*(-1-m)**2
        assert posterior_var / (1 - m*m) == 2*e
    return {"epsilon": str(e), "phi": str(phi), "delta": str(delta), "rho_star_squared": str(2*e)}


def binary(r, n):
    vf = n+1 + 2*sum((n+1-h)*r**(2*h) for h in range(1, n+1))
    vg = n + 2*sum((n-h)*r**(2*h) for h in range(1, n))
    cov = 2*sum((n-h)*r**(2*h+1) for h in range(n))
    corr = cov / np.sqrt(vf*vg)
    target = 2*r/(1+r*r)
    bound = 2*r*np.sqrt(1-r*r) if r <= 2**(-0.5) else 1.
    assert corr <= target + 1e-12 and target <= bound + 1e-12
    assert abs(corr-target) < 1e-3
    return {"r": r, "N": n, "finite_sum_correlation": corr, "limiting_lower_bound": target, "arcsine_upper_bound": bound}


def channel_checks():
    rng = np.random.default_rng(20260918)
    max_excess = -1.0
    for _ in range(200):
        k = rng.dirichlet(np.ones(5), size=4)
        lam = rng.dirichlet(np.ones(4))
        nu = lam @ k
        normalized_joint = np.sqrt(lam)[:, None]*k/np.sqrt(nu)[None, :]
        rho2 = np.linalg.svd(normalized_joint, compute_uv=False)[1]**2
        delta = max(np.abs(a-b).sum()/2 for a in k for b in k)
        assert rho2 <= delta + 1e-12
        max_excess = max(max_excess, float(rho2-delta))
    return {"number_of_channels": 200, "seed": 20260918, "max_rho_squared_minus_delta": max_excess,
            "status": "floating_point_diagnostic_only"}


def path_checks():
    for m in range(2, 31):
        a = np.diag(np.ones(m-1), 1) + np.diag(np.ones(m-1), -1)
        assert abs(np.linalg.norm(a, 2)-2*np.cos(np.pi/(m+1))) < 1e-12
    return {"block_counts": [2, 30], "status": "floating_point_diagnostic_only"}


if __name__ == '__main__':
    result = {"exact_six_state": [six_state(e) for e in (F(1,100), F(1,20), F(1,8), F(1,4), F(2,5))],
              "binary_sums": [binary(r, 10000) for r in (0.01, 0.1, 0.3, 0.6)],
              "local_channel": channel_checks(), "path_norm": path_checks(), "status": "ALL_CHECKS_PASS"}
    print(json.dumps(result, indent=2))
