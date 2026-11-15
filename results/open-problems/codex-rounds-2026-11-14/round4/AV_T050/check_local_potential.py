"""Small exact checks for the abstract lemma in PROOF.md; standard library only."""
from collections import deque
from fractions import Fraction as F
from itertools import product
from math import prod
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# The state spaces below are fixed and tiny; record peak RSS as well.
data_cap = 768 * 1024 * 1024
soft, hard = resource.getrlimit(resource.RLIMIT_DATA)
cap = data_cap if hard == resource.RLIM_INFINITY else min(data_cap, hard)
try:
    resource.setrlimit(resource.RLIMIT_DATA, (cap, hard))
    print('Data limit set to 768 MiB or below')
except (ValueError, OSError) as exc:
    print('macOS data-limit call unavailable:', str(exc))
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

for h in (2, 3, 5, 10, 20):
    r = 8*h + 20
    boundary = {(x, y) for x in range(-r, r+1) for y in (-r, r)}
    boundary |= {(x, y) for x in (-r, r) for y in range(-r, r+1)}
    distances = {(r, 0): 0}
    queue = deque([(r, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = x+dx, y+dy
            if v in boundary and v not in distances:
                distances[v] = distances[(x, y)]+1
                queue.append(v)
    assert len(distances) == len(boundary) == 8*r
    tail = [(x, 0) for x in range(r, r+4*h+11)]
    # Q_H(u) misses Q_(2H)(0) iff a coordinate of u is beyond 3H.
    assert all(max(abs(x), abs(y)) > 3*h for x, y in boundary | set(tail))
    maximum = max(distances.values())+len(tail)-1
    assert maximum == 4*r+4*h+10
    print(f'H={h}: {len(boundary)} boundary vertices; max detour={maximum}; B={maximum+1}; support separation PASS')

h = 2
r, m, q, b = 8*h+20, (2*h+1)**2, (4*h+1)**2, 4*(8*h+20)+4*h+11
n = (2*r+1)**2 * 2**q
c_direct = 2+2*n*b*2**m
c_expanded = 2+1737254*2**106
assert c_direct == c_expanded
print('C_2 =', c_direct, '= 2 + 1737254 * 2^106')

# Nonuniform cells prevent accidental reliance on fair-bit orthogonality.
p = (F(1, 3), F(2, 5), F(3, 7), F(4, 9))
states = list(product((0, 1), repeat=4))
weights = {x: prod(p[i] if x[i] else 1-p[i] for i in range(4)) for x in states}
assert sum(weights.values()) == 1
masks = range(16)

def cond_atom(x, atom, mask):
    if any(x[i] != atom[i] for i in range(4) if mask >> i & 1):
        return F(0)
    return prod(p[i] if atom[i] else 1-p[i] for i in range(4) if not mask >> i & 1)

def projection_atom(x, atom, mask):
    return sum(((-1)**(mask.bit_count()-sub.bit_count()) * cond_atom(x, atom, sub)
                for sub in masks if sub & mask == sub), F(0))

for atom in states:
    projections = {mask: {x: projection_atom(x, atom, mask) for x in states} for mask in masks}
    for x in states:
        assert sum(projections[mask][x] for mask in masks) == int(x == atom)
    for mask in range(1, 16):
        assert sum(weights[x]*projections[mask][x] for x in states) == 0
        # Checking all atom columns proves this operator bound on this product.
        assert sum(weights[x]*abs(projections[mask][x]) for x in states) <= 2**mask.bit_count()*weights[atom]
print('Biased four-cell product: decomposition and zero means on all 16 atom-basis functions PASS; L1 bounds PASS')

# Directly check cancellation on functions of fewer than all four cells.
checks = 0
for support in masks:
    for atom in states:
        # The marginal cylinder atom: sum full atom projections over free bits.
        compatible = [y for y in states if all(y[i] == atom[i] for i in range(4) if support >> i & 1)]
        for mask in range(1, 16):
            if mask & support != mask:
                for x in states:
                    assert sum(projection_atom(x, y, mask) for y in compatible) == 0
                checks += 1
print(f'Support-cancellation checks: {checks} PASS')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_mib = rss / (1024**2 if sys.platform == 'darwin' else 1024)
assert rss_mib < 768
print(f'Elapsed: {time.monotonic()-started:.3f} seconds; peak RSS {rss_mib:.2f} MiB; one process, standard library')
