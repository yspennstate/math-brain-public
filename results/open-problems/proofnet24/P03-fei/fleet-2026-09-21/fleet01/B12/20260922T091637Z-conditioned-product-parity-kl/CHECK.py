#!/usr/bin/env python3
"""Deterministic diagnostics for B-CONDITIONED-PRODUCT-PARITY-KL-v1.

Finite enumeration is only a stress test; the proof is analytic in REPORT.md.
Standard library only.
"""

import itertools
import math


def fwht(values):
    a = [float(x) for x in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0.0)


def maxent_nonempty(r):
    mu = sum(r)
    n = len(r)
    if abs(mu - 1.0) < 1e-12:
        q = [0.0] * (1 << n)
        for i, ri in enumerate(r):
            q[1 << i] = ri
        return q, None, None

    def g(c):
        prod = 1.0
        for ri in r:
            prod *= 1.0 - c * ri
        return 1.0 - prod - c

    lo, hi = 1e-15, 1.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if g(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    c = (lo + hi) / 2.0
    t = [c * ri for ri in r]
    q = [0.0] * (1 << n)
    for S in range(1, 1 << n):
        z = 1.0
        for i, ti in enumerate(t):
            z *= ti if ((S >> i) & 1) else (1.0 - ti)
        q[S] = z / c
    return q, c, t


def metrics(n, ones):
    N = 1 << n
    chosen = set(ones)
    f = [1.0 if x in chosen else -1.0 for x in range(N)]
    ahat = fwht(f)
    P = [x * x for x in ahat]
    assert abs(P[0]) < 1e-12
    r = [sum(P[S] for S in range(N) if (S >> i) & 1) for i in range(n)]
    q, c, t = maxent_nonempty(r)
    K = entropy(q) - entropy(P)
    if c is None or c >= 1.0 - 1e-12:
        return K, c, None, None, r
    active = [i for i, ti in enumerate(t) if ti > 1e-14]
    d = 1.0 / c
    for i in active:
        d *= math.sqrt(t[i] * (1.0 - t[i]))
    kappa = -math.log1p(-(d * d)) / math.log(2.0)
    return K, c, d, kappa, r


def exhaustive(n):
    N = 1 << n
    count = 0
    conditioned = 0
    min_slack = float("inf")
    worst = None
    for ones in itertools.combinations(range(N), N // 2):
        count += 1
        K, c, d, kappa, r = metrics(n, ones)
        if c is not None and c < 1.0 - 1e-10:
            conditioned += 1
            slack = K - kappa
            if slack < min_slack:
                min_slack = slack
                worst = (ones, K, c, d, kappa)
            if slack < -2e-10:
                raise AssertionError((n, ones, K, kappa, slack))
    return count, conditioned, min_slack, worst


def main():
    print("B-CONDITIONED-PRODUCT-PARITY-KL-v1 finite stress test")
    for n in (2, 3, 4):
        count, conditioned, slack, worst = exhaustive(n)
        if conditioned:
            print(
                f"n={n} balanced={count} c_lt_1={conditioned} "
                f"min_K_minus_kappa={slack:.16g} "
                f"worst_K={worst[1]:.16g} worst_c={worst[2]:.16g} "
                f"worst_d={worst[3]:.16g} worst_kappa={worst[4]:.16g}"
            )
        else:
            print(f"n={n} balanced={count} c_lt_1=0 min_K_minus_kappa=NA")

    b0_ones = (0, 1, 2, 3, 4, 5, 8, 10)
    K, c, d, kappa, r = metrics(4, b0_ones)
    print(
        "B0 "
        f"r={','.join(f'{x:.12g}' for x in r)} "
        f"c={c:.15g} Kocc={K:.15g} d={d:.15g} kappa={kappa:.15g}"
    )
    assert K + 2e-10 >= kappa
    print("PASS")


if __name__ == "__main__":
    main()
