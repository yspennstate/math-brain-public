#!/usr/bin/env python3
"""Exact finite checks for the Walsh/block construction in PROOF.md."""
import itertools
import json
import os
from pathlib import Path
import signal
import time
from fractions import Fraction

signal.alarm(600)
data = json.loads(Path("counterexample.json").read_text())
base = data["patterns"]
core = data["sigma"]


def character(a, z):
    return (-1) ** ((a & z).bit_count())


def patterns(k, b):
    return [p + [character(a, z) for a in range(1, k) for _ in range(b)]
            for p in base for z in range(k)]


def q(s, rows):
    return sum(sum(x * y for x, y in zip(p, s)) ** 2 for p in rows)


def block_profile(k, b):
    # Exact maximum at every Hamming distance, using decoupled blocks.
    core_profile = [-1] * 13
    for s in itertools.product((-1, 1), repeat=12):
        d = s.count(-1)
        core_profile[d] = max(core_profile[d], q(s, base))
    result = [k * value for value in core_profile]
    for _ in range(k - 1):
        nxt = [-1] * (len(result) + b)
        for d, value in enumerate(result):
            for r in range(b + 1):
                nxt[d + r] = max(nxt[d + r], value + 11*k*(b - 2*r)**2)
        result = nxt
    return result


def direct_check():
    k, b = 4, 2
    rows = patterns(k, b)
    n = 12 + b*(k - 1)
    for i in range(n):
        for j in range(n):
            actual = sum(p[i]*p[j] for p in rows)
            if i < 12 and j < 12:
                expected = k * sum(p[i]*p[j] for p in base)
            elif i >= 12 and j >= 12 and (i - 12)//b == (j - 12)//b:
                expected = 11*k
            else:
                expected = 0
            assert actual == expected
    print("all Gram entries checked:", n, "neurons,", len(rows), "patterns")
    # Independently use the actual rows and one-spin Gray-code updates.
    profile = [-1] * (n + 1)
    s = [-1] * n
    projections = [sum(x*y for x, y in zip(p, s)) for p in rows]
    distance = n
    for step in range(1 << n):
        if step:
            i = (step & -step).bit_length() - 1
            old = s[i]
            for mu, p in enumerate(rows):
                projections[mu] -= 2 * p[i] * old
            s[i] = -old
            distance += old
        value = sum(v*v for v in projections)
        if step % 4096 == 0:
            assert value == q(s, rows)
        profile[distance] = max(profile[distance], value)
    assert profile == block_profile(k, b)
    print("all", 1 << n, "actual states: Gray-code profile equals block DP")
    # A local minimum near each actual pattern; direct full energy checks.
    smallest = None
    for p in rows:
        s = core + p[12:]
        initial = q(s, rows)
        for i in range(n):
            flipped = s.copy()
            flipped[i] *= -1
            change = initial - q(flipped, rows)
            assert change > 0
            smallest = change if smallest is None else min(smallest, change)
        assert sum(a != c for a, c in zip(s, p)) <= 12
    assert smallest == min(4*k, 44*k*(b - 1))
    print("strict local minima verified near all", len(rows), "patterns")
    print("minimum flip energy increase", Fraction(smallest, 2*n))


if __name__ == "__main__":
    started = time.monotonic()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))
    direct_check()
    b = 79
    assert Fraction(11, b) > Fraction(13820106, 100000000)
    print("B=79 limiting load", Fraction(11, b), "=", float(Fraction(11, b)))
    print("K N M profile_min profile_max proved_uniform_error_bound")
    for k in (2, 4, 8, 16):
        n, m = 12 + b*(k - 1), 11*k
        profile = block_profile(k, b)
        lower = 11*k*b*b*(k - 2)
        upper = k*1584 + 11*k*b*b*(k - 1)
        assert min(profile) >= lower and max(profile) <= upper
        exact_error = max(abs(Fraction(v, 2*n*n) - Fraction(11, 2))
                          for v in profile)
        bound = max(abs(Fraction(lower, 2*n*n) - Fraction(11, 2)),
                    abs(Fraction(upper, 2*n*n) - Fraction(11, 2)))
        assert exact_error <= bound
        print(k, n, m, round(min(profile)/(2*n*n), 9),
              round(max(profile)/(2*n*n), 9), round(float(bound), 9))
    print("elapsed_seconds", round(time.monotonic() - started, 3))
