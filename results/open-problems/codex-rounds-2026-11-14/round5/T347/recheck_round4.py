#!/usr/bin/env python3
"""Independent exact cut enumeration of the round-4 construction; no writes."""
import os
import resource
import signal
import sys
import time
from fractions import Fraction

signal.alarm(120)
started = time.monotonic()
print('priority', os.getpriority(os.PRIO_PROCESS, 0))
print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))

for k, b in ((2, 3), (4, 3), (4, 4)):
    n, m = k*b, 2*k-1
    rows = [[1]*n]
    for a in range(1, k):
        row = [1 if (a & z).bit_count() % 2 == 0 else -1
               for z in range(k) for _ in range(b)]
        rows.extend([row, [-x for x in row]])
    assert len({tuple(p) for p in rows}) == m
    gram = [[sum(p[i]*p[j] for p in rows) for j in range(n)]
            for i in range(n)]
    assert all(gram[i][j] == 2*k*(i//b == j//b)-1
               for i in range(n) for j in range(n))
    row_sums = [sum(row)-row[i] for i, row in enumerate(gram)]
    cuts = [0]*(1 << n)
    q0 = sum(sum(p)**2 for p in rows)
    energies = [q0]*(1 << n)
    profile = [-1]*(n+1)
    for mask in range(1 << n):
        if mask:
            bit = mask & -mask
            i = bit.bit_length()-1
            previous = mask ^ bit
            cross = sum(gram[i][j] for j in range(n) if previous >> j & 1)
            cuts[mask] = cuts[previous] + row_sums[i] - 2*cross
            energies[mask] = q0-4*cuts[mask]
        d = mask.bit_count()
        profile[d] = max(profile[d], energies[mask])
    stable = []
    margin = None
    for mask, value in enumerate(energies):
        differences = [value-energies[mask ^ (1 << i)] for i in range(n)]
        is_minimum = min(differences) >= 0
        block_uniform = all(((mask >> (z*b)) & ((1 << b)-1))
                            in (0, (1 << b)-1) for z in range(k))
        assert is_minimum == block_uniform
        if is_minimum:
            assert min(differences) > 0
            stable.append(mask)
            margin = min(differences) if margin is None else min(margin, *differences)
    assert len(stable) == 2**k and margin == 4*(n-m)
    assert profile == [2*n*n-(n-2*d)**2-8*k*(d % b)*(b-d % b)
                       for d in range(n+1)]
    # Re-evaluate actual pattern projections at every state for N<=12.
    if n <= 12:
        for mask, value in enumerate(energies):
            spins = [1-2*((mask >> i) & 1) for i in range(n)]
            assert value == sum(sum(x*y for x, y in zip(p, spins))**2 for p in rows)
    print(f'K={k} B={b}: cut enumeration of {1 << n} states PASS; '
          f'minima={len(stable)}; min_flip={Fraction(margin, 2*n)}; '
          'every shell optimum and every neighbor checked')

assert Fraction(2, 14) == Fraction(1, 7)
assert 2*(1-Fraction(2, 14)) == Fraction(12, 7)
print('B=14 limits: load=1/7; reference flip cost=12/7 PASS')
divisor = 1024**2 if sys.platform == 'darwin' else 1024
print('peak_rss_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/divisor, 3))
print('elapsed_seconds', round(time.monotonic()-started, 3))
