#!/usr/bin/env python3
"""Exact finite checks of the parameter-stability bound; standard library only."""

import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import resource
import signal
import sys
import time


def direct_intervals(lam, n):
    powers = [lam**j for j in range(n)]
    radius = lam**n / (1-lam)
    return [(sum((s*p for s, p in zip(signs, powers)), Q(0))-radius,
             sum((s*p for s, p in zip(signs, powers)), Q(0))+radius)
            for signs in product((-1, 1), repeat=n)]


def density_events(lam, n):
    # Independent prefix generation via affine iteration, reversing word order.
    centers = [Q(0)]
    for _ in range(n):
        centers = [sign+lam*x for x in centers for sign in (-1, 1)]
    radius = lam**n / (1-lam)
    height = Q(1, 2**n)/(2*radius)
    events = defaultdict(Q)
    for x in centers:
        events[x-radius] += height
        events[x+radius] -= height
    return events


def pieces(lam, n):
    events = density_events(lam, n)
    height = Q(0)
    prev = None
    out = []
    for endpoint, change in sorted(events.items()):
        if prev is not None:
            out.append((height, endpoint-prev))
        height += change
        assert height >= 0
        prev = endpoint
    assert height == 0
    assert sum(h*length for h, length in out) == 1
    return out


def tv_by_signed_integrals(lam, eta, n):
    difference = density_events(lam, n)
    for point, change in density_events(eta, n).items():
        difference[point] -= change
    prev = None
    height = pos = neg = Q(0)
    for point, change in sorted(difference.items()):
        if prev is not None:
            pos += max(height, Q(0))*(point-prev)
            neg += max(-height, Q(0))*(point-prev)
        height += change
        prev = point
    assert height == 0 and pos == neg
    return pos


def cap_sorted(data, delta):
    result = Q(0)
    for height, length in sorted(data, reverse=True):
        take = min(delta, length)
        result += height*take
        delta -= take
        if delta == 0:
            break
    return result


def cap_midpoint_dual(lam, n, delta):
    intervals = direct_intervals(lam, n)
    endpoints = sorted({x for interval in intervals for x in interval})
    normalizer = 2*(lam**n/(1-lam))*2**n
    data = []
    for left, right in zip(endpoints, endpoints[1:]):
        midpoint = (left+right)/2
        height = Q(sum(u < midpoint < v for u, v in intervals))/normalizer
        data.append((height, right-left))
    thresholds = {Q(0)} | {h for h, _ in data}
    return min(t*delta+sum(max(h-t, Q(0))*length for h, length in data)
               for t in thresholds)


def constant(a, b, n):
    return (1-a)/((1-b)**2*a**n)


def interval_tv(first, second):
    u, v = first
    x, y = second
    return 1-max(Q(0), min(v, y)-max(u, x))/max(v-u, y-x)


def check_grid():
    cases = caps = duals = words = 0
    max_ratio = Q(0)
    pairs = [(Q(1, 3), Q(1, 2)), (Q(49, 100), Q(51, 100)),
             (Q(1, 2), Q(501, 1000)), (Q(3, 5), Q(601, 1000)),
             (Q(61, 100), Q(62, 100)), (Q(2, 3), Q(67, 100)),
             (Q(3, 4), Q(751, 1000)), (Q(9, 10), Q(91, 100)),
             (Q(99, 100), Q(991, 1000))]
    for lam, eta in pairs:
        a, b = min(lam, eta), max(lam, eta)
        for n in range(9):
            bound = constant(a, b, n)*abs(lam-eta)
            actual = tv_by_signed_integrals(lam, eta, n)
            assert actual <= min(Q(1), bound)
            if bound:
                max_ratio = max(max_ratio, actual/bound)
            first, second = direct_intervals(lam, n), direct_intervals(eta, n)
            wordwise_tv = Q(0)
            endpoint_bound = abs(lam-eta)/(1-b)**2
            for I, J in zip(first, second):
                assert max(abs(I[0]-J[0]), abs(I[1]-J[1])) <= endpoint_bound
                value = interval_tv(I, J)
                assert value <= min(Q(1), bound)
                wordwise_tv += value/2**n
                words += 1
            assert actual <= wordwise_tv
            data1, data2 = pieces(lam, n), pieces(eta, n)
            for delta in (Q(1, 64), Q(1, 2), Q(3), Q(1000)):
                cap1, cap2 = cap_sorted(data1, delta), cap_sorted(data2, delta)
                assert abs(cap1-cap2) <= actual
                caps += 1
                if n <= 4:
                    assert cap1 == cap_midpoint_dual(lam, n, delta)
                    assert cap2 == cap_midpoint_dual(eta, n, delta)
                    duals += 2
            # Derivative identity, evaluated as rational functions independently.
            finite = sum((j*b**(j-1) for j in range(1, n)), Q(0))
            tail = n*b**(n-1)/(1-b)+b**n/(1-b)**2
            assert finite+tail == 1/(1-b)**2
            cases += 1
    print("exact parameter-pair/depth TV checks", cases)
    print("individual-word endpoint and TV checks", words)
    print("cap-difference checks", caps, "independent midpoint/dual caps", duals)
    print("largest TV / Lipschitz bound in grid", max_ratio)


def check_interval_cases():
    # Nested, shifted, disjoint, coincident, and opposite endpoint motions.
    intervals = [(Q(u), Q(v)) for u in range(-2, 3) for v in range(u+1, 4)]
    count = 0
    for I in intervals:
        for J in intervals:
            e = max(abs(I[0]-J[0]), abs(I[1]-J[1]))
            expected = interval_tv(I, J)
            endpoints = sorted(set(I+J))
            full_l1 = Q(0)
            for lft, rgt in zip(endpoints, endpoints[1:]):
                x = (lft+rgt)/2
                h1 = Q(int(I[0] < x < I[1]), I[1]-I[0])
                h2 = Q(int(J[0] < x < J[1]), J[1]-J[0])
                full_l1 += abs(h1-h2)*(rgt-lft)
            assert expected == full_l1/2
            assert expected <= min(Q(1), 2*e/max(I[1]-I[0], J[1]-J[0]))
            count += 1
    print("uniform-interval formula and endpoint-bound checks", count)


def check_polynomial_exclusions():
    # An independent exact demonstration of the finite-polynomial subinterval step.
    # This interval is only a check of that algebra; it is not a late-cap certificate.
    t, r = Q(3, 5), Q(1, 100000)
    polynomials = [coeff for degree in range(4)
                   for coeff in product((-1, 0, 1), repeat=degree+1)
                   if coeff[-1] != 0]
    for coeff in polynomials:
        val = sum((c*t**j for j, c in enumerate(coeff)), Q(0))
        H = sum(j*abs(c) for j, c in enumerate(coeff))
        assert val != 0 and r*H <= abs(val)/2
        for x in (t-r, t, t+r):
            at_x = sum((c*x**j for j, c in enumerate(coeff)), Q(0))
            assert abs(at_x) >= abs(val)/2
    print("finite-polynomial exclusion checks", len(polynomials))


def check_old_numbers():
    delta, theta = Q(1, 64), Q(1, 36)
    margin = theta-delta/4
    assert margin == Q(55, 2304)
    k, N = 20, 25031
    gap = margin-Q(N, 2**k)
    assert gap == Q(1, 9437184)
    # Separate integer calculation, with no Fraction subtraction.
    assert 55*2**12-9*N == 1
    a, b = Q(1, 2), Q(1, 2)+margin/(2*N)
    assert a < a+Q(1, 2**(k+1)) < b < 1
    assert delta/4+N*(2*b-1) == theta
    # Illustrative finite stability certificate, entirely rational.
    a, b, n = Q(3, 5), Q(601, 1000), 8
    K = constant(a, b, n)
    h = Q(1, 1000000)
    assert K == Q(156250000000, 1044517761)
    print("round-5 depth and margin rechecked", N, gap)
    print("example a", a, "b", b, "n", n, "C_n", K,
          "bound for parameter change 1e-6", K*h)
    print("WARNING: no late depth m or singular transcendental parameter computed")


def main():
    signal.alarm(120)
    if sys.platform != "darwin" and hasattr(resource, "RLIMIT_AS"):
        resource.setrlimit(resource.RLIMIT_AS, (900_000_000, 900_000_000))
    start = time.monotonic()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])
    check_interval_cases()
    check_grid()
    check_polynomial_exclusions()
    check_old_numbers()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    assert rss < 1_000_000_000
    print("elapsed_seconds", f"{time.monotonic()-start:.3f}")
    print("peak_rss_bytes", rss)


if __name__ == "__main__":
    main()
