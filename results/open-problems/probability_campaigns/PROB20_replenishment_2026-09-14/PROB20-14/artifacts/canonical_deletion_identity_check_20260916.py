#!/usr/bin/env python3
"""Finite-support consistency checks for PROB20-14 2026-09-16T11:42Z.

This checks only the exact canonical deletion/retuning algebra from the report.
It is NOT evidence for the arbitrary infinite-variance theorem.

Test law: P(xi=0)=1/2, P(xi=1)=1/4, P(xi=3)=1/4 (critical, span one).
"""

import math
from collections import defaultdict

PI = {0: 0.5, 1: 0.25, 3: 0.25}


def tilt(theta):
    z = sum(p * math.exp(-theta * x) for x, p in PI.items())
    return {x: p * math.exp(-theta * x) / z for x, p in PI.items()}


def mean(dist):
    return sum(x * p for x, p in dist.items())


def canonical(target_mean):
    if abs(target_mean - 1.0) < 1e-14:
        return dict(PI), 0.0
    if abs(target_mean) < 1e-14:
        return {0: 1.0}, math.inf
    lo, hi = 0.0, 1.0
    while mean(tilt(hi)) > target_mean:
        hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if mean(tilt(mid)) > target_mean:
            lo = mid
        else:
            hi = mid
    theta = (lo + hi) / 2.0
    return tilt(theta), theta


def sum_prob(dist, n, target):
    dp = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for s, a in dp.items():
            for x, p in dist.items():
                nxt[s + x] += a * p
        dp = nxt
    return dp.get(target, 0.0)


def kl(p, q):
    ans = 0.0
    for x, a in p.items():
        if a <= 0.0:
            continue
        b = q.get(x, 0.0)
        if b <= 0.0:
            return math.inf
        ans += a * math.log(a / b)
    return ans


def check_case(m, b):
    p0, _ = canonical(1.0 - b / m)
    denominator = sum_prob(p0, m, m - b)
    assert denominator > 0.0
    c0 = -math.log(denominator)

    marginal = {}
    for d, pd in p0.items():
        target = m - b - d
        numerator = 0.0 if target < 0 else sum_prob(p0, m - 1, target)
        marginal[d] = pd * numerator / denominator
    assert abs(sum(marginal.values()) - 1.0) < 1e-10

    residual_average = 0.0
    max_identity_gap = 0.0
    checked_d = 0

    for d, md in marginal.items():
        if md < 1e-14:
            continue
        n = m - 1
        bp = b + d - 1
        target = n - bp
        if target == n:               # b'=0 endpoint
            p1 = dict(PI)
        elif target == 0:             # b'=n endpoint
            p1 = {0: 1.0}
        else:
            p1, _ = canonical(target / n)

        residual_atom = sum_prob(p1, n, target)
        assert residual_atom > 0.0
        c1 = -math.log(residual_atom)
        jcost = n * kl(p1, p0)

        lhs = math.log(md / p0[d])
        rhs = c0 - c1 - jcost
        gap = abs(lhs - rhs)
        max_identity_gap = max(max_identity_gap, gap)
        assert gap < 1e-9

        residual_average += md * (c1 + jcost)
        checked_d += 1

    marginal_kl = kl(marginal, p0)
    decomposition_gap = abs(c0 - marginal_kl - residual_average)
    assert decomposition_gap < 1e-9

    print(
        f"m={m:2d} b={b:2d} checked_d={checked_d} "
        f"max_identity_gap={max_identity_gap:.3e} "
        f"decomposition_gap={decomposition_gap:.3e}"
    )


def main():
    # (4,1) checks both b'=0 (d=0) and b'=N (d=3) endpoint conventions.
    cases = [(4, 1), (8, 1), (8, 2), (10, 3), (20, 1), (20, 5)]
    for m, b in cases:
        check_case(m, b)
    print("ALL_ASSERTIONS_PASSED")


if __name__ == "__main__":
    main()
