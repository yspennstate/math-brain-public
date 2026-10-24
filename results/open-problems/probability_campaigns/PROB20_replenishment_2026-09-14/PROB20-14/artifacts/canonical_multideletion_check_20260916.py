#!/usr/bin/env python3
"""Finite-support consistency checks for the PROB20-14 canonical multi-deletion identities.

This is an algebra/indexing certificate only.  The test law has finite support and finite
variance, so passing these assertions is not evidence for the target infinite-variance theorem.
"""

import itertools
import math

PI = {0: 0.5, 1: 0.25, 3: 0.25}  # critical, span one
TOL = 2e-9


def convolve(a, b):
    out = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power_pmf(P, n):
    base = [P.get(i, 0.0) for i in range(max(P) + 1)]
    out = [1.0]
    for _ in range(n):
        out = convolve(out, base)
    return out


def mean_at_theta(theta):
    weights = {d: p * math.exp(-theta * d) for d, p in PI.items()}
    z = sum(weights.values())
    return sum(d * w for d, w in weights.items()) / z


def canonical_for_mean(mu):
    if abs(mu - 1.0) < 1e-14:
        return dict(PI), 0.0
    if mu <= 0.0:
        return {0: 1.0}, math.inf
    lo, hi = 0.0, 1.0
    while mean_at_theta(hi) > mu:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if mean_at_theta(mid) > mu:
            lo = mid
        else:
            hi = mid
    theta = 0.5 * (lo + hi)
    weights = {d: p * math.exp(-theta * d) for d, p in PI.items()}
    z = sum(weights.values())
    return {d: w / z for d, w in weights.items()}, theta


def kl(P, Q):
    ans = 0.0
    for d, p in P.items():
        if p == 0.0:
            continue
        q = Q.get(d, 0.0)
        if q <= 0.0:
            return math.inf
        ans += p * math.log(p / q)
    return ans


def central(m, b):
    mu = 1.0 - b / m
    P, _ = canonical_for_mean(mu)
    pmf = power_pmf(P, m)
    target = m - b
    prob = pmf[target] if 0 <= target < len(pmf) else 0.0
    if prob <= 0.0:
        return math.inf, P
    return -math.log(prob), P


def direct_ratio(m, b, vec):
    ell = len(vec)
    N = m - ell
    b1 = b + sum(d - 1 for d in vec)
    if not (0 <= b1 <= N):
        return None
    c0, P0 = central(m, b)
    c1, P1 = central(N, b1)
    s = m - b
    t = N - b1
    pmf_m = power_pmf(P0, m)
    pmf_N = power_pmf(P0, N)
    base = math.prod(P0.get(d, 0.0) for d in vec)
    if base == 0.0 or pmf_m[s] == 0.0 or pmf_N[t] == 0.0:
        return None
    conditioned_joint = base * pmf_N[t] / pmf_m[s]
    lhs = conditioned_joint / base
    J = N * kl(P1, P0)
    rhs = math.exp(c0 - c1 - J)
    return lhs, rhs, c0, c1, J


def adaptive_path_ratio(m, b, vec):
    c0, _ = central(m, b)
    current_m, current_b = m, b
    log_ref = 0.0
    sum_J = 0.0
    for d in vec:
        Pprev, _ = canonical_for_mean(1.0 - current_b / current_m)
        log_ref += math.log(Pprev[d])
        next_m = current_m - 1
        next_b = current_b + d - 1
        if not (0 <= next_b <= next_m):
            return None
        Pnext, _ = canonical_for_mean(1.0 - next_b / next_m)
        sum_J += next_m * kl(Pnext, Pprev)
        current_m, current_b = next_m, next_b
    cend, _ = central(current_m, current_b)

    # Exact conditioned joint computed under the initial canonical product law.
    _, Pinit = central(m, b)
    ell = len(vec)
    N = m - ell
    s = m - b
    target = s - sum(vec)
    pmf_m = power_pmf(Pinit, m)
    pmf_N = power_pmf(Pinit, N)
    base_init = math.prod(Pinit[d] for d in vec)
    qjoint = base_init * pmf_N[target] / pmf_m[s]

    lhs = math.log(qjoint) - log_ref
    rhs = c0 - cend - sum_J
    return lhs, rhs


def main():
    max_direct_error = 0.0
    max_path_error = 0.0
    direct_cases = 0
    path_cases = 0

    for m, b in [(10, 1), (12, 2), (20, 1), (20, 4)]:
        for ell in (1, 2, 3):
            for vec in itertools.product((0, 1, 3), repeat=ell):
                got = direct_ratio(m, b, vec)
                if got is not None:
                    lhs, rhs, *_ = got
                    err = abs(lhs - rhs)
                    max_direct_error = max(max_direct_error, err)
                    direct_cases += 1
                    assert err < TOL, (m, b, vec, lhs, rhs, err)

                got2 = adaptive_path_ratio(m, b, vec)
                if got2 is not None:
                    lhs2, rhs2 = got2
                    err2 = abs(lhs2 - rhs2)
                    max_path_error = max(max_path_error, err2)
                    path_cases += 1
                    assert err2 < TOL, (m, b, vec, lhs2, rhs2, err2)

    # Central atom anti-concentration diagnostic on bounded deficit fractions.
    anti_cases = 0
    worst_scaled_atom = 0.0
    for m in (20, 40, 80, 120):
        for b in range(1, max(2, m // 3), max(1, m // 12)):
            c, _ = central(m, b)
            atom = math.exp(-c)
            worst_scaled_atom = max(worst_scaled_atom, math.sqrt(m) * atom)
            anti_cases += 1

    print("ALL_ASSERTIONS_PASSED")
    print(f"direct_identity_cases={direct_cases}")
    print(f"adaptive_path_cases={path_cases}")
    print(f"anti_concentration_diagnostic_cases={anti_cases}")
    print(f"max_direct_abs_error={max_direct_error:.3e}")
    print(f"max_adaptive_log_error={max_path_error:.3e}")
    print(f"max_sqrt_n_central_atom={worst_scaled_atom:.6f}")
    print("FINITE_SUPPORT_CHECK_ONLY")


if __name__ == "__main__":
    main()
