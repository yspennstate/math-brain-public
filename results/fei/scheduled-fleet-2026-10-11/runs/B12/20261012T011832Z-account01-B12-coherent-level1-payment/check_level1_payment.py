#!/usr/bin/env python3
"""Deterministic finite audit for the A057 first-layer log payment.

Scope: all balanced Boolean truth tables on n<=4. Walsh coefficients and
influences are exact Fractions; only logarithm evaluation is floating point.
No random seed is used.
"""
from fractions import Fraction
from itertools import combinations
import math


def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for k in range(start, start + step):
                x, y = a[k], a[k + step]
                a[k], a[k + step] = x + y, x - y
        step *= 2
    return a


def audit_dimension(n):
    size = 1 << n
    best_ratio = -1.0
    best_data = None
    count = 0
    for negative_set in combinations(range(size), size // 2):
        values = [1] * size
        for index in negative_set:
            values[index] = -1
        walsh_integer = fwht(values)
        hats = [Fraction(x, size) for x in walsh_integer]
        masses = [x * x for x in hats]
        alpha = [hats[1 << i] for i in range(n)]
        influence_by_coordinate = [
            sum((masses[mask] for mask in range(size) if mask & (1 << i)), Fraction(0))
            for i in range(n)
        ]
        for a, d in zip(alpha, influence_by_coordinate):
            assert abs(a) <= d
        influence = sum(influence_by_coordinate, Fraction(0))
        log_cost = sum(
            float(a * a) * math.log(1.0 / float(a * a))
            for a in alpha if a
        )
        ratio = log_cost / float(influence) if influence else 0.0
        assert ratio <= 2.0 / math.e + 1e-14
        if ratio > best_ratio:
            best_ratio = ratio
            best_data = (negative_set, alpha, influence, log_cost)
        count += 1
    return count, best_ratio, best_data


def main():
    print("scope=all balanced Boolean truth tables n<=4")
    print("arithmetic=exact Fraction for Walsh/influence; float64 only for logs")
    print("seed=none (exhaustive deterministic enumeration)")
    for n in range(1, 5):
        count, ratio, data = audit_dimension(n)
        negative_set, alpha, influence, log_cost = data
        print(
            f"n={n} cases={count} max_L_over_I={ratio:.16f} "
            f"alpha={[str(x) for x in alpha]} I={influence} "
            f"L_nats={log_cost:.16f} negative_indices={negative_set}"
        )
    print(f"analytic_bound_2_over_e={2.0 / math.e:.16f}")
    print("result=PASS")


if __name__ == "__main__":
    main()

