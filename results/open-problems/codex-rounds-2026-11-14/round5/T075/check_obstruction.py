#!/usr/bin/env python3
"""Exact finite checks of the obstruction in PROOF.md; standard library only."""

import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import product
import resource
import sys
import time


def interval_data(lam, n):
    """Enumerate sign words directly and integrate exact constant segments."""
    radius = lam**n / (1-lam)
    powers = [lam**j for j in range(n)]
    events = defaultdict(int)
    for signs in product((-1, 1), repeat=n):
        center = sum((s*p for s, p in zip(signs, powers)), Q(0))
        events[center-radius] += 1
        events[center+radius] -= 1
    normalizer = 2*radius*2**n
    R = 1/(1-lam)
    events[-R] += 0
    events[R] += 0
    density0 = (1-lam)/2
    count = 0
    previous = None
    pieces = []
    positive = Q(0)
    negative = Q(0)
    for endpoint, change in sorted(events.items()):
        if previous is not None:
            length = endpoint-previous
            density = Q(count)/normalizer
            pieces.append((density, length))
            positive += max(density-density0, Q(0))*length
            negative += max(density0-density, Q(0))*length
        count += change
        previous = endpoint
    assert count == 0
    assert sum(h*length for h, length in pieces) == 1
    assert positive == negative
    return pieces, positive


def sorted_cap(pieces, delta):
    mass = Q(0)
    remaining = delta
    for height, length in sorted(pieces, reverse=True):
        take = min(remaining, length)
        mass += height*take
        remaining -= take
        if remaining == 0:
            break
    return mass


def one_step_checks():
    cases = 0
    for j in range(1, 40):
        lam = Q(40+j, 80)
        pieces, tv = interval_data(lam, 1)
        a = 2*lam-1
        defect = a*(1-lam)/lam
        assert tv == defect
        center_length = 2*a/(1-lam)
        high = (1-lam)/(2*lam)
        low = (1-lam)/(4*lam)
        for delta in (Q(1, 64), Q(1, 2), Q(2), Q(5), Q(1000)):
            explicit = high*min(delta, center_length)
            explicit += low*min(max(delta-center_length, Q(0)), Q(4))
            assert sorted_cap(pieces, delta) == explicit
        cases += 1
    print("exact one-step positive/negative TV and explicit-cap cases", cases)


def prefix_checks():
    cases = 0
    cap_cases = 0
    max_ratio = Q(0)
    for lam in (Q(501, 1000), Q(17, 32), Q(3, 5), Q(5, 8),
                Q(2, 3), Q(3, 4), Q(9, 10), Q(99, 100)):
        defect = (2*lam-1)*(1-lam)/lam
        for n in range(9):
            pieces, tv = interval_data(lam, n)
            assert tv <= n*defect, (lam, n, tv, n*defect)
            if n:
                max_ratio = max(max_ratio, tv/(n*defect))
            for delta in (Q(1, 64), Q(1, 2), Q(3), Q(1000)):
                actual = sorted_cap(pieces, delta)
                sharp = min(Q(1), delta*(1-lam)/2+n*defect)
                simple = min(Q(1), delta/4+n*(2*lam-1))
                assert actual <= sharp <= simple
                cap_cases += 1
            cases += 1
    print("exact prefix TV checks", cases, "cap inequalities", cap_cases)
    print("maximum TV/(n*d) in grid", max_ratio)


def root_sum(x, k):
    result = Q(0)
    for _ in range(k):
        result = x*(1+result)
    return result


def root_bracket(k):
    lo, hi = Q(1, 2), Q(1, 2)+Q(1, 2**(k+1))
    assert root_sum(lo, k) < 1 < root_sum(hi, k)
    # Independent polynomial identity, evaluated exactly at the endpoint.
    assert (1-hi)*(root_sum(hi, k)-1) == 2*hi-1-hi**(k+1) > 0
    for _ in range(100):
        mid = (lo+hi)/2
        if root_sum(mid, k) < 1:
            lo = mid
        else:
            hi = mid
    assert root_sum(lo, k) < 1 < root_sum(hi, k)
    return lo, hi


def decimal_beta_root(k):
    """A second root computation: Newton in beta, not bisection in lambda."""
    beta = Decimal(2)
    for _ in range(100):
        val = sum((beta**(-j) for j in range(1, k+1)), Decimal(-1))
        deriv = sum((-Decimal(j)*beta**(-j-1) for j in range(1, k+1)),
                    Decimal(0))
        updated = beta-val/deriv
        if abs(updated-beta) < Decimal("1e-110"):
            return 1/updated
        beta = updated
    raise AssertionError("Newton iteration did not converge")


def root_and_horizon_checks():
    delta, theta = Q(1, 64), Q(1, 36)
    margin = theta-delta/4
    assert margin == Q(55, 2304)
    print("delta", delta, "theta", theta, "margin", margin)
    with localcontext() as context:
        context.prec = 120
        for k in range(2, 41):
            lo, hi = root_bracket(k)
            root = decimal_beta_root(k)
            low_decimal = Decimal(lo.numerator)/Decimal(lo.denominator)
            high_decimal = Decimal(hi.numerator)/Decimal(hi.denominator)
            assert low_decimal < root < high_decimal
            assert 0 < 2*hi-1 < Q(1, 2**k)
            # Strict N*2^-k < margin; no prefix enumeration is used here.
            N = (margin.numerator*2**k-1)//margin.denominator
            gap = theta-(delta/4+Q(N, 2**k))
            assert gap > 0
            assert Q(N+1, 2**k) >= margin
            if k in (8, 12, 20, 40):
                print("k", k, "lambda approx", f"{root:.30f}",
                      "certified depth", N, "threshold gap", gap)
            if k == 20:
                assert N == 25031 and gap == Q(1, 9437184)
    print("rational root brackets versus independent Decimal Newton", 39)
    print("WARNING: singular parameters here are algebraic; T075 remains open")
    print("WARNING: large certified depths use the theorem, not enumeration")


def main():
    start = time.monotonic()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])
    one_step_checks()
    prefix_checks()
    root_and_horizon_checks()
    print("elapsed_seconds", f"{time.monotonic()-start:.3f}")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    assert rss < 1_000_000_000
    print("peak_rss_bytes", rss)


if __name__ == "__main__":
    main()
