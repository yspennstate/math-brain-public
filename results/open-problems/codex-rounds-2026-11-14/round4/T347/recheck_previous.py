#!/usr/bin/env python3
"""Independent cut-form verification of the round-3 certificate; no writes."""
import itertools
import json
import os
from pathlib import Path
import signal
import time

signal.alarm(120)
started = time.monotonic()
source = Path('~/codex_op_1114r3/briefs/T347')
data = json.loads((source / 'counterexample.json').read_text())
base = data['patterns']
core = data['sigma']


def gram(rows):
    n = len(rows[0])
    return [[sum(p[i] * p[j] for p in rows) for j in range(n)]
            for i in range(n)]


def cut_profile(rows):
    # Q(s) = Q(1) - 4 times the weight of the cut of negative sites.
    a = gram(rows)
    n = len(a)
    q0 = sum(sum(row) for row in a)
    profile = [-1] * (n + 1)
    for mask in range(1 << n):
        negative = [i for i in range(n) if mask >> i & 1]
        positive = [j for j in range(n) if not (mask >> j & 1)]
        value = q0 - 4 * sum(a[i][j] for i in negative for j in positive)
        d = len(negative)
        profile[d] = max(profile[d], value)
    return profile, a


def direct_q(s, rows):
    return sum(sum(x * y for x, y in zip(p, s)) ** 2 for p in rows)


profile, a = cut_profile(base)
assert profile[:7] == [192, 236, 256, 284, 288, 300, 304]
assert profile == profile[::-1]
fields = [core[i] * sum(a[i][j] * core[j] for j in range(12) if j != i)
          for i in range(12)]
assert fields == [9, 9, 1, 9, 25, 1, 5, 5, 25, 5, 13, 1]
assert direct_q(core, base) == 240 < profile[2]
print('base cut enumeration:', profile[:7], 'fields:', fields)

# A different Walsh instance from the earlier verifier: K=2, B=4, N=16.
k, b = 2, 4
rows = [p + [(-1) ** z] * b for p in base for z in range(k)]
profile, a = cut_profile(rows)
n = len(rows[0])
assert n == 16 and len(rows) == 22
for i, j in itertools.product(range(n), repeat=2):
    expected = (k * sum(p[i] * p[j] for p in base) if i < 12 and j < 12
                else 11 * k if i >= 12 and j >= 12 else 0)
    assert a[i][j] == expected
lower = 11 * k * b * b * (k - 2)
upper = 1584 * k + 11 * k * b * b * (k - 1)
assert lower <= min(profile) <= max(profile) <= upper
costs = []
for p in rows:
    s = core + p[12:]
    initial = direct_q(s, rows)
    assert sum(x != y for x, y in zip(s, p)) <= 12
    for i in range(n):
        neighbor = s.copy()
        neighbor[i] *= -1
        diff = initial - direct_q(neighbor, rows)
        assert diff == 4 * s[i] * sum(a[i][j] * s[j] for j in range(n) if i != j)
        costs.append(diff)
assert min(costs) == 4 * k
print('Walsh actual Gram, all 65536 states, all flips near 22 patterns: PASS')
print('minimum energy increase:', min(costs), '/', 2 * n)
print('priority:', os.getpriority(os.PRIO_PROCESS, 0))
print('elapsed_seconds:', round(time.monotonic() - started, 3))
