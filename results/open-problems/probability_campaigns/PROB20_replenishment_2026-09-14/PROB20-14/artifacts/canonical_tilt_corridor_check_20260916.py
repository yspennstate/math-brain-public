#!/usr/bin/env python3
"""Finite-support algebra checker for the PROB20-14 canonical-tilt checkpoint.

This is a consistency/indexing certificate only.  The test law has finite
variance and therefore does NOT constitute evidence for the target infinite-
variance theorem.
"""

import itertools
import math
from collections import defaultdict

PI = {0: 0.5, 1: 0.25, 3: 0.25}
Q = 1.5
R = Q - 1.0


def tilt(theta):
    z = sum(p * math.exp(-theta * d) for d, p in PI.items())
    return {d: p * math.exp(-theta * d) / z for d, p in PI.items()}


def mean(dist):
    return sum(d * p for d, p in dist.items())


def find_theta(alpha):
    target = 1.0 - alpha
    lo, hi = 0.0, 1.0
    while mean(tilt(hi)) > target:
        hi *= 2.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if mean(tilt(mid)) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def convolution(dist, n):
    cur = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for s, ps in cur.items():
            for d, pd in dist.items():
                nxt[s + d] += ps * pd
        cur = dict(nxt)
    return cur


def conditioned_marginal(dist, m, target):
    den = convolution(dist, m).get(target, 0.0)
    assert den > 0.0
    rest = convolution(dist, m - 1)
    mu = {
        d: p * rest.get(target - d, 0.0) / den
        for d, p in dist.items()
    }
    return mu, den


def kl(mu, p):
    return sum(mu[d] * math.log(mu[d] / p[d]) for d in mu if mu[d] > 0.0)


def run():
    beta = 2.0 / Q - 1.0
    rows = []
    for m in (8, 10, 12, 20, 30):
        for b in (1, max(1, m // 4), m // 2):
            if b > m // 2:
                continue
            alpha = b / m
            theta = find_theta(alpha)
            ptheta = tilt(theta)
            target = m - b

            mu_tilt, den_tilt = conditioned_marginal(ptheta, m, target)
            mu_orig, _ = conditioned_marginal(PI, m, target)

            # Exact conditioning is invariant under exponential tilting.
            assert max(abs(mu_tilt[d] - mu_orig[d]) for d in PI) < 1e-10

            # Reference and conditioned marginal have the exact target mean.
            assert abs(mean(ptheta) - (1.0 - alpha)) < 1e-10
            assert abs(mean(mu_tilt) - (1.0 - alpha)) < 1e-10

            c = -math.log(den_tilt)
            dkl = kl(mu_tilt, ptheta)

            # Tensorization consequence m D(mu||P_theta) <= central exponent.
            assert m * dkl <= c + 1e-10

            # Exact first-moment tail balance at K=1.
            K = 1
            tail_mu = sum(d * p for d, p in mu_tilt.items() if d > K)
            tail_p = sum(d * p for d, p in ptheta.items() if d > K)
            low_mu = sum(d * p for d, p in mu_tilt.items() if d <= K)
            low_p = sum(d * p for d, p in ptheta.items() if d <= K)
            assert abs((tail_mu - tail_p) + (low_mu - low_p)) < 1e-10

            # Uniform q-tail domination P_theta <= PI / PI(0).
            for k2 in (0, 1, 2):
                qt = sum((d ** Q) * p for d, p in ptheta.items() if d > k2)
                qt_pi = sum((d ** Q) * p for d, p in PI.items() if d > k2)
                assert qt <= qt_pi / PI[0] + 1e-12

            rows.append((m, b, theta, c, m * dkl, c / (m ** beta)))

    # Deterministic moving-tilt zero-surplus identity.
    zero_checks = 0
    for m in range(3, 9):
        for b in range(1, m // 2 + 1):
            alpha = b / m
            theta = find_theta(alpha)
            ptheta = tilt(theta)
            p0 = ptheta[0]
            ey = sum(max(d - 1, 0) * p for d, p in ptheta.items())
            assert abs(ey - (p0 - alpha)) < 1e-10
            n = m - 1
            for dsel in PI:
                target = m - b - dsel
                if target < 0:
                    continue
                for tup in itertools.product(PI.keys(), repeat=n):
                    if sum(tup) != target:
                        continue
                    n0 = sum(1 for x in tup if x == 0)
                    sy = sum(max(x - 1, 0) for x in tup)
                    assert n0 == b + dsel - 1 + sy
                    centered = dsel - 1 + alpha + sum(
                        max(x - 1, 0) - ey for x in tup
                    )
                    assert abs((n0 - n * p0) - centered) < 1e-9
                    zero_checks += 1

    print("ALL_ASSERTIONS_PASSED")
    print(f"tilt/entropy rows checked: {len(rows)}")
    print(f"zero-surplus configurations checked: {zero_checks}")
    print("sample rows: m b theta central_exponent m*KL c/m^beta")
    for row in rows[:8]:
        print(" ".join(f"{x:.12g}" if isinstance(x, float) else str(x) for x in row))


if __name__ == "__main__":
    run()
