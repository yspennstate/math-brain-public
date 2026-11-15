#!/usr/bin/env python3
"""Exact finite-prefix concentration statistics; no infinite-depth inference."""

import os
os.environ["OMP_NUM_THREADS"] = "1"

from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import resource
import time


def prefixes(lam, n):
    values = [Q(0)]
    power = Q(1)
    for _ in range(n):
        values = [x + sign * power for x in values for sign in (-1, 1)]
        power *= lam
    return values


def sweep(lam, n):
    radius = lam**n / (1 - lam)
    events = defaultdict(int)
    for value in prefixes(lam, n):
        events[value - radius] += 1
        events[value + radius] -= 1
    count = 0
    previous = None
    lengths = defaultdict(Q)
    for x, change in sorted(events.items()):
        if previous is not None and count > 0:
            lengths[count] += x - previous
        count += change
        assert count >= 0
        previous = x
    assert count == 0
    normalizer = 2 * radius * 2**n
    assert sum(c * length for c, length in lengths.items()) == normalizer
    return lengths, normalizer


def cap(lengths, normalizer, delta):
    remaining = delta
    total = Q(0)
    for count in sorted(lengths, reverse=True):
        take = min(remaining, lengths[count])
        total += count * take
        remaining -= take
        if remaining == 0:
            break
    return total / normalizer


def independent_midpoint(lam, n, delta):
    """Enumerate signs directly; count covers without an endpoint sweep.

    Optimize by the dual formula inf_t (t*delta + integral(f-t)_+).
    Its minimum occurs at zero or at an attained density value.
    """
    powers = [lam**j for j in range(n)]
    values = [sum((s * p for s, p in zip(signs, powers)), Q(0))
              for signs in product((-1, 1), repeat=n)]
    radius = lam**n / (1 - lam)
    intervals = [(x - radius, x + radius) for x in values]
    endpoints = sorted({x for interval in intervals for x in interval})
    normalizer = 2 * radius * 2**n
    segments = []
    for left, right in zip(endpoints, endpoints[1:]):
        midpoint = (left + right) / 2
        count = sum(a < midpoint < b for a, b in intervals)
        if count:
            segments.append((Q(count) / normalizer, right - left))
    thresholds = {Q(0)} | {density for density, _ in segments}
    return min(t * delta + sum((max(density - t, Q(0)) * length
                               for density, length in segments), Q(0))
               for t in thresholds)


def main():
    start = time.monotonic()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])
    checks = 0
    for lam in (Q(1, 3), Q(1, 2), Q(2, 3)):
        for n in range(1, 7):
            lengths, normalizer = sweep(lam, n)
            for delta in (Q(1, 64), Q(1, 2), Q(3), Q(10)):
                actual = cap(lengths, normalizer, delta)
                assert actual == independent_midpoint(lam, n, delta)
                checks += 1
    print("independent midpoint/dual comparisons", checks, "passed")
    controls = 0
    for n in range(1, 15):
        for lam in (Q(1, 3), Q(1, 2)):
            lengths, normalizer = sweep(lam, n)
            support_length = 2 / (1 - lam) * (2 * lam)**n
            for delta in (Q(1, 64), Q(1, 2), Q(3), Q(10)):
                assert cap(lengths, normalizer, delta) == min(delta / support_length, Q(1))
                controls += 1
    print("disjoint/tiled exact formula comparisons", controls, "passed")
    delta = Q(1, 64)
    print("lambda n delta cap_exact cap_decimal max_density_decimal")
    for lam in (Q(1, 3), Q(1, 2), Q(2, 3)):
        for n in (4, 8, 12, 14):
            lengths, normalizer = sweep(lam, n)
            actual = cap(lengths, normalizer, delta)
            maximum = Q(max(lengths)) / normalizer
            print(lam, n, delta, actual, f"{float(actual):.12g}", f"{float(maximum):.12g}")
    # This is only arithmetic verification of the displayed exponent.
    # No infinite-depth concentration bound is being asserted at lambda=2/3.
    import math
    lam, delta, theta = Q(2, 3), Q(1, 64), Q(1, 36)
    diameter = 2 / (1 - lam)
    epsilon = delta * lam / (4 * diameter)
    denominator_a = 18 / epsilon
    denominator_b = 72 * diameter / (delta * lam)
    assert denominator_a == denominator_b == 41472
    p = 1 + math.log(1 / (18 * float(theta))) / math.log(float(denominator_a))
    print("conditional exponent arithmetic: epsilon", epsilon,
          "18/epsilon", denominator_a, "p", f"{p:.12g}")
    print("WARNING: the finite table proves no infinite-depth bound or new AC example")
    print("elapsed_seconds", f"{time.monotonic() - start:.3f}")
    # macOS reports ru_maxrss in bytes.
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == "__main__":
    main()
