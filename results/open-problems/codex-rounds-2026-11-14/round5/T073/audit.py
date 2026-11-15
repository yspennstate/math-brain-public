"""Exact checks for the exact-three disagreement extension; standard library only."""
import os
import resource
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import json

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))

def rec(q):
    q = Q(q)
    with localcontext() as ctx:
        ctx.prec = 55
        return {'exact':str(q), 'decimal':str(Decimal(q.numerator)/Decimal(q.denominator))}

def g(k):
    return min(2, max(0, k-1))

# Prove the new local formula by exhaustive evaluation, with independent
# encodings of the triple sum and the exact-three indicators.
histogram = Counter()
exact_three_cases = 0
for states in product(((0, 0), (0, 1), (1, 1)), repeat=4):
    lower, upper = zip(*states)
    ds = [u-l for l, u in states]
    m = sum(ds)
    b = sum(ds[i]*any(all(states[j] == (v, v) for j in range(4) if j != i)
                     for v in (0, 1)) for i in range(4))
    triples = sum(all(ds[i] for i in tri) for tri in combinations(range(4), 3))
    pair_events = sum(all(ds[i] for i in pair) and any(
        all(states[j] == (v, v) for j in range(4) if j not in pair)
        for v in (0, 1)) for pair in combinations(range(4), 2))
    exact_events = sum(all(ds[i] == int(i in tri) for i in range(4))
                       for tri in combinations(range(4), 3))
    assert exact_events == int(m == 3)
    assert g(sum(upper))-g(sum(lower)) == m-b-Q(triples, 2)-pair_events-Q(exact_events, 2)
    histogram[m] += 1
    exact_three_cases += exact_events
assert sum(histogram.values()) == 81 and exact_three_cases == 8

# Reconstruct the rule by deleting a uniformly chosen input and taking the
# majority of the remaining three, then reversing with probability e.
rule_checks = 0
for bits in product((0, 1), repeat=4):
    maj = Q(sum(sum(bits[j] for j in tri) >= 2 for tri in combinations(range(4), 3)), 4)
    for e in (Q(0), Q(1, 5), Q(24807562, 10**8), Q(1, 2)):
        assert e+(1-2*e)*maj == (e, e, Q(1, 2), 1-e, 1-e)[sum(bits)]
        rule_checks += 1

def perm_count(n, edges):
    total = 0
    for order in permutations(range(n)):
        rank = [0]*n
        for i, v in enumerate(order):
            rank[v] = i
        total += all(rank[u] < rank[v] for u, v in edges)
    return total

def recursive_count(n, edges):
    @lru_cache(None)
    def count(mask):
        if mask == (1 << n)-1:
            return 1
        return sum(count(mask | (1 << v)) for v in range(n)
                   if not mask & (1 << v)
                   and all(mask & (1 << u) for u, w in edges if w == v))
    return count(0)

# All rotations, built from coordinates. The omitted compass site has no
# edge to any receiver; its forced mark can occur before or after receivers.
neighbors = ((0, 1), (1, 0), (0, -1), (-1, 0))
diagonals = ((1, 1), (1, -1), (-1, -1), (-1, 1))
dist = lambda v, w: abs(v[0]-w[0])+abs(v[1]-w[1])
geometry = []
transmission_checks = 0
for blocker in neighbors:
    receivers = tuple(r for r in neighbors if r != blocker)
    sites = diagonals+receivers+(blocker,)
    assert len(set(((0, 0),)+sites)) == 9
    patterns = [bits for bits in product((0, 1), repeat=4)
                if all(sum(bits[j] for j, h in enumerate(diagonals) if dist(h, r) == 1) == 1
                       for r in receivers)]
    assert len(patterns) == 2
    for r in receivers:
        inputs = {(r[0]+1, r[1]), (r[0]-1, r[1]), (r[0], r[1]+1), (r[0], r[1]-1)}
        axial = (2*r[0], 2*r[1])
        helpers = {h for h in diagonals if dist(h, r) == 1}
        assert inputs == {(0, 0), axial} | helpers
        assert blocker not in inputs
        for bits in patterns:
            forced = [bits[j] for j, h in enumerate(diagonals) if h in helpers]
            for l, u in ((0, 0), (0, 1), (1, 1)):
                lo = sum(forced)+l
                hi = sum(forced)+1+u
                assert g(hi)-g(lo) == (2 if (l, u) == (0, 1) else 1)
                transmission_checks += 1
    edges = [(sites.index(h), sites.index(r)) for h in diagonals for r in receivers if dist(h, r) == 1]
    count = perm_count(8, edges)
    assert count == recursive_count(8, edges) == 2176
    # Include the source explicitly as the first of the nine last-ring times.
    assert recursive_count(9, edges+[(8, j) for j in range(8)]) == count
    geometry.append({'omitted':blocker, 'helper_patterns':patterns, 'clock_orders':count})

# Third count: seven-site alternating fence, with one unrestricted insertion.
cuts = (2, 4, 6)
fence7 = 0
for k in range(4):
    for selected in combinations(cuts, k):
        positions = (0,)+selected+(7,)
        denominator = 1
        for l, u in zip(positions, positions[1:]):
            denominator *= factorial(u-l)
        fence7 += (-1)**(3-k)*factorial(7)//denominator
assert fence7 == 272 and 8*fence7 == 2176
integral = sum(Q((-1)**j*comb(8, j), j+1) for j in range(9))
assert integral == Q(1, 9)
clock = Q(2176, factorial(8))*integral
assert clock == Q(2176, factorial(9)) == Q(17, 2835)
event_coefficient = 4*clock
correction_coefficient = Q(1, 2)*4*event_coefficient
assert event_coefficient == Q(68, 2835)
assert correction_coefficient == Q(136, 2835)
# Independent ratio of the explicit coefficients: 2e for the blocker mark
# and 8/9 for its extra clock requirement. Receiver bounds remain uniform.
assert Q(17, 1260)*2*Q(8, 9) == event_coefficient

def c2(e):
    a = Q(1, 2)-e
    return (2-4*e)*(1-e**3/2)-Q(17, 630)*e**4*a**4-Q(4, 15)*e**5*a**3-Q(16, 81)*e**6*a**3

def c3(e):
    return c2(e)-correction_coefficient*e**5*(Q(1, 2)-e)**4

# Two algebra constructions: multiply each factored term, and use the old
# polynomial plus an independently binomial-expanded new term.
def multiply(p, q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out

poly = [Q(1), Q(-4), Q(0), Q(-1), Q(2)]+[Q(0)]*5
for coefficient, m, n in ((Q(17, 630), 4, 4), (Q(4, 15), 5, 3),
                           (Q(16, 81), 6, 3), (correction_coefficient, 5, 4)):
    term = [Q(1)]
    for _ in range(n):
        term = multiply(term, [Q(1, 2), Q(-1)])
    for j, x in enumerate(term):
        poly[m+j] -= coefficient*x
old_poly = [Q(1), Q(-4), Q(0), Q(-1), Q(20143, 10080), -Q(5, 252),
            Q(1529, 11340), -Q(187, 945), -Q(107, 1890), Q(16, 81)]
second_poly = old_poly[:]
for j, x in enumerate((Q(1, 16), -Q(1, 2), Q(3, 2), Q(-2), Q(1))):
    second_poly[5+j] -= Q(136, 2835)*x
assert poly == second_poly

def horner(e):
    val = Q(0)
    for coefficient in reversed(second_poly):
        val = val*e+coefficient
    return val

lo, hi = Q(0), Q(1, 4)
for _ in range(85):
    mid = (lo+hi)/2
    assert horner(mid) == c3(mid)-1
    if c3(mid) > 1:
        lo = mid
    else:
        hi = mid
assert c3(lo) > 1 > c3(hi)
grid_lo, grid_hi = Q(24807560, 10**8), Q(24807565, 10**8)
assert horner(grid_lo) > 0 > horner(grid_hi)
assert grid_lo < lo < hi < grid_hi
old_lo = Q(38387847911459845608705571, 154742504910672534362390528)
old_hi = Q(9596961977864961402176393, 38685626227668133590597632)
assert c2(old_lo) > 1 > c2(old_hi)
assert hi < old_lo
endpoint = Q(24807562, 10**8)
assert c3(endpoint) < 1 < c2(endpoint)
for t in (lo, hi, endpoint, Q(0), Q(1, 4), Q(1, 2)):
    assert horner(t) == c3(t)-1

# A second, decimal-grid root enclosure using only the integer polynomial.
denom = 10**18
left, right = 248075600000000000, 248075650000000000
def integer_sign_numerator(k):
    common = 1
    for v in poly:
        common = common*v.denominator//__import__('math').gcd(common, v.denominator)
    return sum((v*common).numerator*k**j*denom**(9-j) for j, v in enumerate(poly))
assert integer_sign_numerator(left) > 0 > integer_sign_numerator(right)
while right-left > 1:
    middle = (left+right)//2
    if integer_sign_numerator(middle) > 0:
        left = middle
    else:
        right = middle
assert Q(left, denom) < lo < hi < Q(right, denom)

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 10**9
result = {'status':'all assertions passed', 'ordered_local_pairs':sum(histogram.values()),
          'local_cases_by_M':dict(histogram), 'exact_three_local_cases':exact_three_cases,
          'rule_checks':rule_checks, 'transmission_checks':transmission_checks,
          'geometry':geometry, 'fence7_orders':fence7, 'eight_clock_orders':2176,
          'clock_order_probability':rec(Q(2176, factorial(8))), 'age_integral':rec(integral),
          'integrated_clock_coefficient':rec(clock), 'event_coefficient_before_e5_a3':rec(event_coefficient),
          'new_correction_coefficient_before_e5_a4':rec(correction_coefficient),
          'C3_minus_one_coefficients':list(map(str, poly)),
          'root_lower':rec(lo), 'root_upper':rec(hi), 'root_width':rec(hi-lo),
          'integer_grid_lower':rec(Q(left, denom)), 'integer_grid_upper':rec(Q(right, denom)),
          'threshold_improvement_lower':rec(old_lo-hi), 'threshold_improvement_upper':rec(old_hi-lo),
          'endpoint':rec(endpoint), 'C3_at_endpoint':rec(c3(endpoint)), 'C2_at_endpoint':rec(c2(endpoint)),
          'nice':os.getpriority(os.PRIO_PROCESS, 0), 'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS'],
          'cpu_limit_seconds':30, 'peak_rss_bytes_macos':rss}
output = json.dumps(result, indent=2, sort_keys=True)+'\n'
Path(__file__).with_name('audit_output.json').write_text(output)
print(output, end='')
