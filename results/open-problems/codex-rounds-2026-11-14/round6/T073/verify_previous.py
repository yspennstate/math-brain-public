"""Independent reconstruction of round 5, without predecessor imports."""
import os
import resource
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
from fractions import Fraction as Q
from itertools import product, combinations, permutations
from math import comb, factorial
from decimal import Decimal, localcontext
import json

def record(x):
    with localcontext() as ctx:
        ctx.prec = 50
        return {'exact': str(x), 'decimal': str(Decimal(x.numerator)/Decimal(x.denominator))}

counts = [0]*5
e = Q(1, 5)
a = Q(1, 2)-e
p = (e, e, Q(1, 2), 1-e, 1-e)
for lower in product((0, 1), repeat=4):
    for upper in product((0, 1), repeat=4):
        if any(l > u for l, u in zip(lower, upper)):
            continue
        ds = [u-l for l, u in zip(lower, upper)]
        m = sum(ds)
        blocked = sum(ds[i] and len({lower[j] for j in range(4) if j != i}) == 1
                      and all(lower[j] == upper[j] for j in range(4) if j != i)
                      for i in range(4))
        pair = sum(all(ds[i] for i in pair) and any(
                   all(lower[j] == upper[j] == b for j in range(4) if j not in pair)
                   for b in (0, 1)) for pair in combinations(range(4), 2))
        assert (p[sum(upper)]-p[sum(lower)])/a == m-blocked-Q(comb(m, 3), 2)-pair-Q(m == 3, 2)
        counts[m] += 1
assert counts == [16, 32, 24, 8, 1]

def count_orders(n, edges):
    prerequisites = [sum(1 << u for u, w in edges if w == v) for v in range(n)]
    dp = [0]*(1 << n)
    dp[0] = 1
    for mask in range(1 << n):
        if not dp[mask]:
            continue
        for v in range(n):
            if not mask & (1 << v) and mask & prerequisites[v] == prerequisites[v]:
                dp[mask | (1 << v)] += dp[mask]
    return dp[-1]

def receiver_integral(k, helper_incidence):
    """Condition on receiver times; integrate helper minima over k! simplices."""
    answer = Q(0)
    for order in permutations(range(k)):
        ranks = {v: i for i, v in enumerate(order)}
        powers = [0]*k
        for incident in helper_incidence:
            earliest = min(incident, key=ranks.get)
            powers[ranks[earliest]] += 1
        denominator = 1
        cumulative = 0
        for j, power in enumerate(powers):
            cumulative += power+1
            denominator *= cumulative
        answer += Q(1, denominator)
    return answer

rows = []
for name, incidence, free, mark_count, expected in (
    ('triple', [(0,), (0, 1), (1, 2), (2,)], 0, 2, Q(17, 1260)),
    ('exact_three', [(0,), (0, 1), (1, 2), (2,)], 1, 4, Q(68, 2835)),
    ('adjacent_pair', [(0,), (0, 1), (1,)], 2, 4, Q(1, 15)),
    ('opposite_pair', [(0,), (0,), (1,), (1,)], 2, 8, Q(8, 81)),
):
    k = 1+max(max(s) for s in incidence)
    h = len(incidence)
    n = h+k+free
    edges = [(i, h+j) for i, incident in enumerate(incidence) for j in incident]
    number = count_orders(n, edges)
    probability = receiver_integral(k, incidence)
    assert probability == Q(number, factorial(n))
    integral = sum(Q((-1)**j*comb(n, j), j+1) for j in range(n+1))
    assert integral == Q(1, n+1)
    coefficient = mark_count*probability*integral
    assert coefficient == expected
    rows.append({'event': name, 'orders': number, 'coefficient': str(coefficient)})

def contraction(t):
    a = Q(1, 2)-t
    return ((2-4*t)*(1-t**3/2)-Q(17, 630)*t**4*a**4
            -Q(4, 15)*t**5*a**3-Q(16, 81)*t**6*a**3-Q(136, 2835)*t**5*a**4)

coefficients = [Q(1), -4, 0, -1, Q(20143, 10080), -Q(37, 1620),
                Q(1801, 11340), -Q(17, 63), Q(223, 5670), Q(424, 2835)]
def polynomial(t):
    ans = Q(0)
    for c in reversed(coefficients):
        ans = ans*t+c
    return ans

lo = Q(19193920498167976369215855, 77371252455336267181195264)
hi = Q(38387840996335952738431711, 154742504910672534362390528)
assert contraction(lo) > 1 > contraction(hi)
assert hi-lo == Q(1, 154742504910672534362390528)
endpoint = Q(24807562, 10**8)
assert contraction(endpoint) < 1
for t in (lo, hi, endpoint, Q(0), Q(1, 4), Q(1, 2)):
    assert contraction(t)-1 == polynomial(t)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 10**9
print(json.dumps({'status': 'all assertions passed', 'local_counts': counts,
                  'clock_checks_by_two_methods': rows,
                  'root_lower': record(lo), 'root_upper': record(hi),
                  'C3_at_endpoint': record(contraction(endpoint)),
                  'nice': os.getpriority(os.PRIO_PROCESS, 0),
                  'peak_rss_bytes_macos': rss}, indent=2))
