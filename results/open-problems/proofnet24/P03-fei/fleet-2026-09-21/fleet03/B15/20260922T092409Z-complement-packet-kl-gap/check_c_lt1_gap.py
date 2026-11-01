#!/usr/bin/env python3
"""
Stress test for B-PRODUCT-COMPLEMENT-GAP-v1.

The theorem in REPORT.md is analytic.  This script independently enumerates all
balanced Boolean functions through n=4, computes the nonempty-product
I-projection Q_r, and checks the coarse quantitative bound

    K_occ >= c^{-2} prod_i t_i(1-t_i) / ln(2)

on the c<1 branch.

Floating point is used only as a stress test; no proof sign depends on it.
"""
from itertools import combinations
import math


def fwht(a):
    a = [float(x) for x in a]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def positive_c(r):
    mu = sum(r)
    if mu <= 1.0 + 1e-12:
        return None
    def g(c):
        z = 1.0
        for rr in r:
            z *= 1.0-c*rr
        return 1.0-z-c
    if abs(g(1.0)) < 1e-12:
        return 1.0
    lo, hi = 1e-12, 1.0
    for _ in range(120):
        mid = (lo+hi)/2.0
        if g(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


print("STRESS_PASS (floating diagnostic; theorem is analytic)")
for n in (2, 3, 4):
    N = 1 << n
    total = 0
    c_lt_1 = 0
    min_gap = float("inf")
    min_ratio = float("inf")
    witness = None
    for neg in combinations(range(N), N//2):
        mask = 0
        for x in neg:
            mask |= 1 << x
        vals = [-1.0 if (mask >> x) & 1 else 1.0 for x in range(N)]
        ahat = [v/N for v in fwht(vals)]
        P = [z*z for z in ahat]
        r = [
            sum(P[S] for S in range(N) if (S >> i) & 1)
            for i in range(n)
        ]
        c = positive_c(r)
        total += 1
        if c is None or c >= 1.0-1e-10:
            continue
        c_lt_1 += 1
        t = [c*rr for rr in r]
        Q = [0.0]*N
        for S in range(1, N):
            q = 1.0
            for i in range(n):
                q *= t[i] if (S >> i) & 1 else (1.0-t[i])
            Q[S] = q/c
        K = sum(
            P[S]*math.log2(P[S]/Q[S])
            for S in range(1, N) if P[S] > 1e-16
        )
        d2 = 1.0/(c*c)
        for tt in t:
            if tt > 1e-14:
                d2 *= tt*(1.0-tt)
        lower = d2/math.log(2.0)
        if K + 1e-11 < lower:
            raise AssertionError((n, mask, K, lower))
        gap = K-lower
        ratio = K/lower if lower > 0.0 else float("inf")
        if gap < min_gap:
            min_gap = gap
            witness = (mask, sum(r), c, K, lower, ratio)
        min_ratio = min(min_ratio, ratio)
    if c_lt_1 == 0:
        print(f"n={n} balanced={total} c_lt_1=0")
    else:
        print(
            f"n={n} balanced={total} c_lt_1={c_lt_1} "
            f"min(K-lb)={min_gap:.15g} min_ratio={min_ratio:.15g}"
        )
        print(
            "  witness mask=0x%x mu=%.15g c=%.15g "
            "K=%.15g lb=%.15g ratio=%.15g" % witness
        )
