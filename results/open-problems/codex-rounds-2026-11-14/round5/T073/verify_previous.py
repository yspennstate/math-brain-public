"""Independent finite reconstruction of round 4; no predecessor imports."""
import os
import resource
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial
import json

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))

# Use the update probabilities directly, rather than the earlier g table.
e = F(1, 5)
a = F(1, 2)-e
p = (e, e, F(1, 2), 1-e, 1-e)
counts = Counter()
residuals = {m:set() for m in range(5)}
for low in product((0, 1), repeat=4):
    for high in product((0, 1), repeat=4):
        if any(l > h for l, h in zip(low, high)):
            continue
        d = [h-l for l, h in zip(low, high)]
        m = sum(d)
        blocked = sum(d[i] and any(all(low[j] == high[j] == b
                      for j in range(4) if i != j) for b in (0, 1))
                      for i in range(4))
        pairs = sum(all(d[i] for i in pair) and any(
                    all(low[j] == high[j] == b for j in range(4)
                        if j not in pair) for b in (0, 1))
                    for pair in combinations(range(4), 2))
        rhs = a*(m-blocked-F(comb(m, 3), 2)-pairs)
        gap = (rhs-(p[sum(high)]-p[sum(low)]))/a
        assert gap >= 0
        assert gap == F(m == 3, 2)
        residuals[m].add(str(gap))
        counts[m] += 1
assert list(counts[m] for m in range(5)) == [16, 32, 24, 8, 1]

def extension_count(vertices, edges):
    """Remove maximal vertices, independently of chronological enumeration."""
    vertices = tuple(vertices)
    @lru_cache(None)
    def count(mask):
        if not mask:
            return 1
        return sum(count(mask ^ (1 << v)) for v in vertices
                   if mask & (1 << v)
                   and all(not (mask & (1 << w)) for u, w in edges if u == v))
    return count((1 << len(vertices))-1)

neighbors = ((0, 1), (1, 0), (0, -1), (-1, 0))
diagonals = ((1, 1), (1, -1), (-1, -1), (-1, 1))
dist = lambda v, w: sum(abs(v[i]-w[i]) for i in (0, 1))
clock_checks = []
for receivers in list(combinations(neighbors, 2))+list(combinations(neighbors, 3)):
    helpers = tuple(h for h in diagonals if any(dist(h, r) == 1 for r in receivers))
    blockers = tuple(r for r in neighbors if r not in receivers) if len(receivers) == 2 else ()
    sites = helpers+receivers+blockers
    edges = [(sites.index(h), sites.index(r)) for h in helpers for r in receivers
             if dist(h, r) == 1]
    marks = sum(all(sum(v[i] for i, h in enumerate(helpers) if dist(h, r) == 1) == 1
                    for r in receivers) for v in product((0, 1), repeat=len(helpers)))
    n = len(sites)
    count = extension_count(range(n), edges)
    # Count source before all nonsource sites in the same partial order.
    with_source = extension_count(range(n+1), edges+[(n, j) for j in range(n)])
    assert with_source == count
    integral = sum(F((-1)**j*comb(n, j), j+1) for j in range(n+1))
    assert F(count, factorial(n))*integral == F(with_source, factorial(n+1))
    clock = F(count, factorial(n+1))
    coefficient = marks*(2 if blockers else 1)*clock
    if len(receivers) == 3:
        assert (count, marks, clock, coefficient) == (272, 2, F(17, 2520), F(17, 1260))
    elif len(helpers) == 3:
        assert (count, marks, clock, coefficient) == (672, 2, F(1, 60), F(1, 15))
    else:
        assert (count, marks, clock, coefficient) == (4480, 4, F(1, 81), F(8, 81))
    clock_checks.append({'receivers':receivers, 'orders':count, 'coefficient':str(coefficient)})
assert 2*sum(F((-1)**j*comb(3, j), j+1) for j in range(4)) == F(1, 2)

def c2(t):
    a = F(1, 2)-t
    return (2-4*t)*(1-t**3/2)-F(17, 630)*t**4*a**4-F(4, 15)*t**5*a**3-F(16, 81)*t**6*a**3

def expanded(t):
    return (1-4*t-t**3+F(20143, 10080)*t**4-F(5, 252)*t**5
            +F(1529, 11340)*t**6-F(187, 945)*t**7-F(107, 1890)*t**8+F(16, 81)*t**9)

lo = F(38387847911459845608705571, 154742504910672534362390528)
hi = F(9596961977864961402176393, 38685626227668133590597632)
assert c2(lo) > 1 > c2(hi)
endpoint = F(248076, 10**6)
expected = F(3337855398443582394496741255036654301312159321701,
             3337860107421875000000000000000000000000000000000)
assert c2(endpoint) == expected < 1
for t in (lo, hi, endpoint, F(0), F(1, 4), F(1, 2)):
    assert c2(t)-1 == expanded(t)

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 10**9
print(json.dumps({'status':'all assertions passed', 'ordered_pairs':sum(counts.values()),
                  'residual_by_M':{m:sorted(v) for m, v in residuals.items()},
                  'clock_checks':clock_checks, 'C2_at_previous_endpoint':str(expected),
                  'root_bracket':'both exact signs verified',
                  'nice':os.getpriority(os.PRIO_PROCESS, 0), 'peak_rss_bytes_macos':rss}, indent=2))
