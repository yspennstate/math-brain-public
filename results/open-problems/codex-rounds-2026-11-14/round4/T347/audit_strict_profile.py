#!/usr/bin/env python3
"""Exact integer checks of PROOF.md; standard library, one process, no writes."""
import math
import os
from fractions import Fraction
import resource
import signal
import sys
import time

signal.alarm(180)


def patterns(k, b):
    assert k >= 2 and k & (k - 1) == 0
    return [[1] * (k * b)] + [
        [sign * (-1) ** ((a & z).bit_count())
         for z in range(k) for _ in range(b)]
        for a in range(1, k) for sign in (1, -1)]


def direct_q(s, rows):
    return sum(sum(x * y for x, y in zip(p, s)) ** 2 for p in rows)


def shell_formula(k, b, d):
    n = k * b
    r = d % b
    return 2 * n * n - (n - 2 * d) ** 2 - 8 * k * r * (b - r)


def block_dp(k, b):
    # Separate shell optimization, with no remainder or exchange argument.
    best = [0]
    for _ in range(k):
        nxt = [-1] * (len(best) + b)
        for d, value in enumerate(best):
            for r in range(b + 1):
                nxt[d + r] = max(nxt[d + r], value + (b - 2 * r) ** 2)
        best = nxt
    n = k * b
    return [2 * k * value - (n - 2 * d) ** 2 for d, value in enumerate(best)]


def exhaustive(k, b):
    rows = patterns(k, b)
    n, m = k * b, 2 * k - 1
    assert len(rows) == m and len({tuple(p) for p in rows}) == m
    a = [[sum(p[i] * p[j] for p in rows) for j in range(n)]
         for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert a[i][j] == 2 * k * (i // b == j // b) - 1
    energies = []
    best = [-1] * (n + 1)
    for mask in range(1 << n):
        s = [1 - 2 * ((mask >> i) & 1) for i in range(n)]
        value = direct_q(s, rows)
        sums = [sum(s[z * b:(z + 1) * b]) for z in range(k)]
        assert value == 2 * k * sum(v * v for v in sums) - sum(s) ** 2
        energies.append(value)
        d = mask.bit_count()
        best[d] = max(best[d], value)
    assert best == [shell_formula(k, b, d) for d in range(n + 1)]
    assert best == block_dp(k, b)
    stable = []
    minimum_diff = None
    for mask, value in enumerate(energies):
        diffs = [value - energies[mask ^ (1 << i)] for i in range(n)]
        if min(diffs) >= 0:
            stable.append(mask)
            assert min(diffs) > 0
            for z in range(k):
                block = (mask >> (z * b)) & ((1 << b) - 1)
                assert block in (0, (1 << b) - 1)
            minimum_diff = (min(diffs) if minimum_diff is None
                            else min(minimum_diff, min(diffs)))
    assert len(stable) == 2 ** k
    assert minimum_diff == 4 * (n - m)
    for p in rows:
        mask = sum(1 << i for i, value in enumerate(p) if value < 0)
        assert mask in stable
    # Direct energies along a block-reversal path, independently of shell maxima.
    q0 = direct_q([1] * n, rows)
    for r in range(b + 1):
        s = [-1] * r + [1] * (n - r)
        assert q0 - direct_q(s, rows) == 4 * r * (n - m * r)
    error = max(abs(Fraction(value, 2 * n * n)
                    - (1 - Fraction((n - 2 * d) ** 2, 2 * n * n)))
                for d, value in enumerate(best))
    assert error <= Fraction(1, k)
    print(f'K={k} B={b} N={n} M={m}: all {1 << n} states, actual Gram, '
          f'profiles, all neighbors PASS; minima={len(stable)}; '
          f'min_flip={Fraction(minimum_diff, 2*n)}; uniform_error={error}')


def larger_instance(k=16, b=14):
    rows = patterns(k, b)
    n, m = k * b, 2 * k - 1
    assert len({tuple(p) for p in rows}) == m
    # Check every stored pattern's signed fields from actual projections.
    worst = None
    for s in rows:
        projections = [sum(x * y for x, y in zip(p, s)) for p in rows]
        q0 = sum(v * v for v in projections)
        for i in range(n):
            field = s[i] * sum(p[i] * value for p, value in zip(rows, projections)) - m
            assert field > 0
            worst = field if worst is None else min(worst, field)
            if i in (0, b - 1, n - 1):
                neighbor = s.copy()
                neighbor[i] *= -1
                assert q0 - direct_q(neighbor, rows) == 4 * field
    assert worst == n - m
    best = block_dp(k, b)
    assert best == [shell_formula(k, b, d) for d in range(n + 1)]
    print(f'K={k} B={b} N={n} M={m}: every stored pattern strictly stable '
          f'by actual projections; all {n+1} shell optima match separate DP')
    print('finite_load', Fraction(m, n), '=', float(Fraction(m, n)))
    print('finite_min_flip', Fraction(2 * worst, n), '=', float(Fraction(2 * worst, n)))
    print('limiting_load', Fraction(2, b), '=', float(Fraction(2, b)))
    print('limiting_min_flip', 2 * (1 - Fraction(2, b)))
    # Second arithmetic route: no fractions or the Gram expansion.
    assert math.isclose(2 / b, 1 / 7, rel_tol=0, abs_tol=1e-16)
    assert 2 * (1 - Fraction(2, b)) == Fraction(12, 7)
    barrier = max(Fraction(2 * r) - Fraction(2 * m * r * r, n)
                  for r in range(b + 1))
    print('one-block-path_max_excess', barrier, 'continuous_upper_bound', Fraction(n, 2*m))


def boundary_checks():
    # B=2 still has strict minima, but its reference margin tends to zero.
    for b in (1, 2):
        k = 4
        rows = patterns(k, b)
        n = k * b
        reference = [1] * n
        one_flip = [-1] + [1] * (n - 1)
        diff = Fraction(direct_q(reference, rows) - direct_q(one_flip, rows), 2 * n)
        assert diff == 2 * (1 - Fraction(2 * k - 1, n))
        assert (diff > 0) == (b >= 2)
        print(f'boundary B={b} K=4 reference flip cost={diff}')


if __name__ == '__main__':
    started = time.monotonic()
    print('priority', os.getpriority(os.PRIO_PROCESS, 0))
    print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))
    for k, b in ((2, 3), (4, 3), (4, 4)):
        exhaustive(k, b)
    larger_instance()
    boundary_checks()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    divisor = 1024 * 1024 if sys.platform == 'darwin' else 1024
    print('peak_rss_MiB', round(peak / divisor, 3))
    print('elapsed_seconds', round(time.monotonic() - started, 3))
