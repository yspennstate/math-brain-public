#!/usr/bin/env python3
"""Exact checks for PROOF.md; finite calculations do not verify its hypothesis."""

import os
os.environ["OMP_NUM_THREADS"] = "1"

from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import combinations
import math
import resource
import time


def covering_checks():
    # Endpoints and intervening cells both matter for open-interval covers.
    points = [Q(i, 2) for i in range(11)]
    intervals = [(a, b) for a in range(6) for b in range(a + 1, 6)]
    masks = [sum(1 << k for k, x in enumerate(points) if a < x < b)
             for a, b in intervals]
    families = 0
    for size in range(1, 6):
        for indices in combinations(range(len(intervals)), size):
            original = 0
            for i in indices:
                original |= masks[i]
            selected = list(indices)
            changed = True
            while changed:
                changed = False
                for i in selected:
                    others = 0
                    for j in selected:
                        if j != i:
                            others |= masks[j]
                    if masks[i] & ~others == 0:
                        selected.remove(i)
                        changed = True
                        break
            union = 0
            for i in selected:
                union |= masks[i]
            assert union == original
            assert all(sum(bool(masks[i] & (1 << k)) for i in selected) <= 2
                       for k in range(len(points)))
            families += 1
    print("exact open-interval covering families", families, "passed")


def integer_cap(p, q, n, delta):
    """Integer coordinate implementation, with no fraction-valued endpoints.

    Common coordinate denominator L=(q-p)q^(n-1).
    The tail radius in these coordinates is p^n.
    The sorted-overlap formula is the one in the earlier proof.
    """
    weights = [p**j * q**(n - 1 - j) for j in range(n)]
    events = defaultdict(int)
    radius = p**n
    scale = (q - p) * q**(n - 1)
    for mask in range(2**n):
        numerator = sum(w if mask & (1 << j) else -w
                        for j, w in enumerate(weights))
        center = (q - p) * numerator
        events[center - radius] += 1
        events[center + radius] -= 1
    lengths = defaultdict(int)
    previous = None
    count = 0
    for x in sorted(events):
        if previous is not None and count:
            lengths[count] += x - previous
        count += events[x]
        assert count >= 0
        previous = x
    assert count == 0
    normalizer = 2 * radius * 2**n
    assert sum(k * length for k, length in lengths.items()) == normalizer
    remaining = delta * scale
    mass_units = Q(0)
    for k in sorted(lengths, reverse=True):
        take = min(remaining, lengths[k])
        mass_units += k * take
        remaining -= take
        if remaining == 0:
            break
    return mass_units / normalizer


def prefix_checks():
    # Exact values copied as verification targets from the earlier report.
    targets = {
        (1, 3): [Q(27, 1024), Q(2187, 16384),
                 Q(177147, 262144), Q(1)],
        (1, 2): [Q(1, 256)] * 4,
        (2, 3): [Q(81, 16384), Q(19683, 4194304),
                 Q(9794029, 2147483648), Q(153382733, 34359738368)],
    }
    checks = 0
    for (p, q), expected in targets.items():
        for n, target in zip((4, 8, 12, 14), expected):
            actual = integer_cap(p, q, n, Q(1, 64))
            assert actual == target, (p, q, n, actual, target)
            if 2 * p <= q:
                support = Q(2, 1 - Q(p, q)) * (2 * Q(p, q))**n
                assert actual == min(Q(1, 64) / support, Q(1))
            checks += 1
    print("integer-coordinate prefix cap comparisons", checks, "passed")


def recurrence_checks():
    # Second derivation of Gamma: dilation (2), cover multiplicity (2),
    # and the ratio c/(c-1) from splitting h at height t.
    count = 0
    for theta in (Q(1, 1000), Q(1, 36), Q(1, 18), Q(1, 10),
                  Q(1, 5), Q(249, 1000)):
        c = 2 / (1 - 4 * theta)
        direct = 4 * c * theta / (c - 1)
        factored = 2 * theta * (2 / (c - 1)) * c
        reduced = 8 * theta / (1 + 4 * theta)
        assert direct == factored == reduced
        assert 0 < direct < 1
        assert c > 1 / (1 - 4 * theta)
        for epsilon in (Q(1, 2304), Q(1, 100), Q(1, 4)):
            A = c / epsilon
            assert A > 1
            endpoint = math.log(1 / float(direct)) / math.log(float(A))
            exponent_gain = endpoint / 2
            multiplier = float(direct) * float(A)**exponent_gain
            assert math.isclose(multiplier, math.sqrt(float(direct)),
                                rel_tol=2e-14)
            assert multiplier < 1
            count += 1
    print("tunable recurrence/exponent checks", count, "passed")

    lam, delta, theta = Q(2, 3), Q(1, 64), Q(1, 36)
    D = 2 / (1 - lam)
    epsilon = delta * lam / (4 * D)
    assert D == 6 and epsilon == Q(1, 2304)
    H = 2 / epsilon
    gamma = 4 * 2 * theta / (2 - 1)
    assert H == 8 * D / (delta * lam) == 4608
    assert gamma == Q(2, 9)
    assert gamma / (12 * theta) == Q(2, 3)
    assert 18 / epsilon == 72 * D / (delta * lam) == 41472

    old = 1 + math.log(2) / math.log(41472)
    new = 1 + math.log(3) / math.log(4608)
    critical = 1 + math.log(Q(9, 2)) / math.log(4608)
    explicit_all = 1 + math.log(5) / (2 * math.log(5184))
    with localcontext() as context:
        context.prec = 60
        new_decimal = 1 + Decimal(3).ln() / Decimal(4608).ln()
        old_decimal = 1 + Decimal(2).ln() / Decimal(41472).ln()
        critical_decimal = 1 + (Decimal(9) / 2).ln() / Decimal(4608).ln()
        all_decimal = 1 + Decimal(5).ln() / (2 * Decimal(5184).ln())
        for ordinary, high_precision in ((new, new_decimal), (old, old_decimal),
                                         (critical, critical_decimal),
                                         (explicit_all, all_decimal)):
            assert abs(ordinary - float(high_precision)) < 3e-15
        print("example epsilon", epsilon, "H", H, "Gamma", gamma)
        print("earlier p", f"{old_decimal:.15f}")
        print("new p, formula (5)", f"{new_decimal:.15f}")
        print("fixed-c endpoint, excluded", f"{critical_decimal:.15f}")
        print("new p, formula (4)", f"{all_decimal:.15f}")
    assert 1 < old < new < critical
    assert math.isclose(float(gamma) * float(H)**(new - 1), 2 / 3,
                        rel_tol=2e-14)

    # Check strict exponent improvement throughout a rational grid.
    for j in range(1, 1001):
        th = Q(j, 18001)  # all strictly below 1/18
        old_gain = math.log(1 / (18 * float(th))) / math.log(41472)
        new_gain = math.log(1 / (12 * float(th))) / math.log(4608)
        assert new_gain > old_gain > 0
    print("exponent improvement grid", 1000, "passed")
    print("WARNING: no infinite-subsequence concentration bound was checked")


def main():
    start = time.monotonic()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])
    covering_checks()
    prefix_checks()
    recurrence_checks()
    print("elapsed_seconds", f"{time.monotonic() - start:.3f}")
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == "__main__":
    main()
