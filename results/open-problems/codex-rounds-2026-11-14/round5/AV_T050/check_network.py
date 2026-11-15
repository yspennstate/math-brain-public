"""Exact finite checks for PROOF.md. One process, standard library only."""
from fractions import Fraction as F
from itertools import product
from math import ceil
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

# Rounding is implemented in hundredths, including negative half-integers.
route_checks = 0
for d in (0, 1, 2, 5, 20):
    values = sorted({x for x in (-100*d, -100*d+25, -50, -49,
                                0, 49, 50, 100*d-25, 100*d)
                     if abs(x) <= 100*d})
    offsets = list(product(values, repeat=2))
    maximum = 0
    for zprime in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
        for q, qprime_offset in product(offsets, repeat=2):
            qp = tuple(100*zprime[i]+qprime_offset[i] for i in range(2))
            anchor = tuple((x+50)//100 for x in q)
            anchorp = tuple((x+50)//100 for x in qp)
            m = sum(abs(anchor[i]-anchorp[i]) for i in range(2))
            assert 100*m <= sum(abs(q[i]-qp[i]) for i in range(2))+200
            assert m <= 4*d+3 <= 4*d+5
            assert 8+5*m+8 <= 20*d+41
            # Manhattan route and every queried nominal center lie within
            # D+5, then 20 conversion/locality + 2 assignment/padding.
            assert max(abs(x) for x in anchor+anchorp)+2 <= d+5
            assert d+5+20+2 <= d+30
            maximum = max(maximum, m)
            route_checks += 1
    assert 16+5*(4*d+5) == 20*d+41
    print(f'D={d}: sampled max grid length {maximum}; H={d+30}; K={20*d+41}; PASS')
print(f'Exact route/rounding checks: {route_checks} PASS')

# Endpoint levels, including one-sided extremes and shifted negative marks.
period_checks = 0
for delta in (F(1, 51), F(1, 100), F(1, 1000)):
    assert 6*delta < 1 and 4*delta < 1
    for mark in (-3, 0, 4):
        for half_offset, e1, e2 in product((F(-1, 2), F(0), F(1, 2)),
                                          (-3*delta, 0, 3*delta),
                                          (-3*delta, 0, 3*delta)):
            # Extra-road attachment: mark to nearest transverse crossing.
            t = mark+half_offset+e1
            assert mark-1 < t < mark+1
            # Canonical transverse interval: q2 to its nearest integer j.
            lo, hi = sorted((mark+half_offset+e1, mark+e2))
            assert mark-1 < lo <= hi < mark+1
            # Grid edge: its two selected nominal levels are ordered.
            u, v = mark+e1, mark+1+e2
            assert u < v and mark-1 < u < v < mark+2
            period_checks += 1
print(f'Rational endpoint/period containments: {period_checks} PASS')

# Exhaust all simple horizontal crossings of a small strip with <=8 edges.
# The vertical family is its coordinate transpose. A finite crossing test,
# not a replacement for the general planar argument.
paths = []
allowed = set(product(range(-2, 3), range(-1, 2)))
def visit(path, seen):
    x, y = path[-1]
    if x == 2:
        paths.append(tuple(path))
        return
    if len(path)-1 == 8:
        return
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nxt = x+dx, y+dy
        if nxt in allowed and nxt not in seen:
            visit(path+[nxt], seen | {nxt})
for y in range(-1, 2):
    visit([(-2, y)], {(-2, y)})
assert paths
sets = [set(p) for p in paths]
vertical = [{(y, x) for x, y in p} for p in paths]
crossings = 0
for horizontal, v in product(sets, vertical):
    common = horizontal & v
    assert common and all(abs(x) <= 1 and abs(y) <= 1 for x, y in common)
    crossings += 1
print(f'Planar strip check: {len(paths)} paths each direction; {crossings} intersecting pairs PASS')

# Insert a loop into each horizontal occurrence record. Selecting by
# occurrence indices stays unambiguous even with repeated vertices.
for p in paths:
    repeated = p[:2]+(p[0],)+p[1:]
    for vset in vertical[:12]:
        candidates = [i for i, vertex in enumerate(repeated) if vertex in vset]
        assert candidates and repeated[min(candidates)] in vset
print('Repeated-vertex occurrence selection PASS')

# Arbitrary rational potentials; Q increments carry nonnegative defects.
# Forward and reverse uses must telescope with the same sign on Q and P.
p = [F(3*i*i-5*i+7, 11) for i in range(9)]
defects = [F(2*i+1, 13) for i in range(8)]
q = [p[i+1]-p[i]+defects[i] for i in range(8)]
signed_checks = 0
for length in range(1, 8):
    for directions in product((-1, 1), repeat=length):
        pos = 4
        total = F(0)
        budget = F(0)
        for direction in directions:
            target = pos+direction
            if not 0 <= target < len(p):
                break
            edge = min(pos, target)
            total += direction*q[edge]
            budget += defects[edge]
            pos = target
        else:
            assert abs(total-(p[pos]-p[4])) <= budget
            signed_checks += 1
print(f'Exact signed telescoping checks: {signed_checks} PASS')

# Negative controls: physical reverse costs cannot be signed comparisons;
# pointwise maxima of many label errors do not keep a per-label L1 bound.
tau, linear, increment = F(5), F(2), F(1)
forward = tau-linear
physical_reverse = tau+linear
assert physical_reverse != -forward
assert abs(physical_reverse+increment) > abs(forward-increment)
for labels in (2, 7, 31):
    errors = [[F(labels if state == label else 0) for state in range(labels)]
              for label in range(labels)]
    assert all(sum(e)/labels == 1 for e in errors)
    assert sum(max(e[state] for e in errors) for state in range(labels))/labels == labels
print('Negative controls: physical reversal differs; selected-label maximum grows as label count PASS')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform == 'darwin' else 1024)
assert rss < 768
print(f'Elapsed {time.monotonic()-started:.3f} seconds; peak RSS {rss:.2f} MiB; inherited nice {os.getpriority(os.PRIO_PROCESS, 0)}')
