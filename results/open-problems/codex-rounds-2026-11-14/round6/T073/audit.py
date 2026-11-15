"""Exact audit of all common-diagonal triple broadcasts; standard library only."""
import os
import resource
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, factorial, lcm
from pathlib import Path
import json

def record(q):
    q = Q(q)
    with localcontext() as ctx:
        ctx.prec = 55
        return {'exact': str(q), 'decimal': str(Decimal(q.numerator)/Decimal(q.denominator))}

def orders(n, edges):
    pred = [sum(1 << u for u, w in edges if w == v) for v in range(n)]
    ways = [0]*(1 << n)
    ways[0] = 1
    for mask in range(1 << n):
        if not ways[mask]:
            continue
        for v in range(n):
            if not mask & (1 << v) and mask & pred[v] == pred[v]:
                ways[mask | (1 << v)] += ways[mask]
    return ways[-1]

def continuous_probability(k, incidence):
    """Integrate helper-time minima, conditional on the k receiver times."""
    ans = Q(0)
    for order in permutations(range(k)):
        ranks = {v: j for j, v in enumerate(order)}
        powers = [0]*k
        for receiver_set in incidence:
            powers[min(ranks[v] for v in receiver_set)] += 1
        cumulative = 0
        denominator = 1
        for exponent in powers:
            cumulative += exponent+1
            denominator *= cumulative
        ans += Q(1, denominator)
    return ans

# Abstract path h0-r0-h1-r1-h2-r2-h3. A bit in S adds an axial
# helper below that receiver. Both colorings for each S are accounted for.
table = []
P = defaultdict(Q)
R = defaultdict(Q)
for bits in product((0, 1), repeat=3):
    S = tuple(i for i, v in enumerate(bits) if v)
    m = len(S)
    incidence = [(0,), (0, 1), (1, 2), (2,)]+[(i,) for i in S]
    h = len(incidence)
    n = h+3
    edges = [(j, h+i) for j, receivers in enumerate(incidence) for i in receivers]
    number = orders(n, edges)
    probability = continuous_probability(3, incidence)
    assert probability == Q(number, factorial(n))
    integral = sum(Q((-1)**j*comb(n, j), j+1) for j in range(n+1))
    assert integral == Q(1, n+1)
    coefficient = 2*probability*integral
    P[4+m] += coefficient
    # An unrestricted omitted-neighbor clock, with either common value.
    number_free = orders(n+1, edges)
    assert number_free == (n+1)*number
    exact_coefficient = 4*Q(number_free, factorial(n+2))
    assert exact_coefficient == coefficient*2*Q(n+1, n+2)
    R[5+m] += exact_coefficient
    # Explicitly insert the source as a minimal clock vertex.
    assert orders(n+1, edges+[(n, j) for j in range(n)]) == number
    table.append({'S': S, 'm': m, 'n': n, 'orders': number,
                  'order_probability': str(probability),
                  'P_coefficient': str(coefficient), 'R_coefficient': str(exact_coefficient)})
assert P[4] == Q(17, 1260) and R[5] == Q(68, 2835)

# Geometry and every input case in all four orientations, independently
# constructed from lattice coordinates and all sixteen diagonal patterns.
N = ((0, 1), (1, 0), (0, -1), (-1, 0))
H = ((1, 1), (1, -1), (-1, -1), (-1, 1))
distance = lambda x, y: abs(x[0]-y[0])+abs(x[1]-y[1])
geometry_checks = transmission_checks = 0
g = (0, 0, 1, 2, 2)
for omitted in N:
    receivers = [r for r in N if r != omitted]
    p_coeff = defaultdict(Q)
    r_coeff = defaultdict(Q)
    for values in product((0, 1), repeat=4):
        monochromatic = []
        forcing = dict(zip(H, values))
        for r in receivers:
            near = [h for h in H if distance(h, r) == 1]
            axial = (2*r[0], 2*r[1])
            actual_inputs = {(r[0]+1, r[1]), (r[0]-1, r[1]),
                             (r[0], r[1]+1), (r[0], r[1]-1)}
            assert actual_inputs == {(0, 0), axial} | set(near)
            assert omitted not in actual_inputs
            if forcing[near[0]] == forcing[near[1]]:
                monochromatic.append(r)
                forcing[axial] = 1-forcing[near[0]]
                outside = [(forcing[axial], forcing[axial])]
            else:
                outside = [(0, 0), (0, 1), (1, 1)]
            for low, high in outside:
                lo = sum(forcing[h] for h in near)+low
                hi = sum(forcing[h] for h in near)+1+high
                assert g[hi]-g[lo] >= 1
                if r in monochromatic:
                    assert g[hi]-g[lo] == 1
                transmission_checks += 1
        helpers = list(forcing)
        sites = helpers+receivers+[omitted]
        assert len(set([(0, 0)]+sites)) == len(sites)+1
        edges = [(sites.index(h), sites.index(r)) for h in helpers for r in receivers
                 if distance(h, r) == 1]
        n = len(sites)-1
        # The omitted vertex is last in this indexing, and has no constraints.
        L = orders(n, edges)
        L_free = orders(n+1, edges)
        assert L_free == (n+1)*L
        m = len(monochromatic)
        p_coeff[4+m] += Q(L, factorial(n+1))
        r_coeff[5+m] += 2*Q(L_free, factorial(n+2))
        geometry_checks += 1
    assert dict(p_coeff) == dict(P) and dict(r_coeff) == dict(R)
assert geometry_checks == 64 and transmission_checks == 384

def eval_terms(terms, e):
    return sum((c*e**j for j, c in terms.items()), Q(0))

def old(e):
    a = Q(1, 2)-e
    return ((2-4*e)*(1-e**3/2)-Q(17, 630)*e**4*a**4
            -Q(4, 15)*e**5*a**3-Q(16, 81)*e**6*a**3-Q(136, 2835)*e**5*a**4)

def new(e):
    a = Q(1, 2)-e
    return ((2-4*e)*(1-e**3/2)-Q(4, 15)*e**5*a**3-Q(16, 81)*e**6*a**3
            -2*a**4*(eval_terms(P, e)+eval_terms(R, e)))

# Construct the expanded polynomial from the event coefficients. Its second
# construction starts with the predecessor's polynomial and just adds deltas.
def multiply(p, q):
    ans = [Q(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            ans[i+j] += x*y
    return ans

poly = [Q(1), -4, 0, -1, 2]+[Q(0)]*8
terms = [(Q(4, 15), 5, 3), (Q(16, 81), 6, 3)]
terms += [(2*c, j, 4) for t in (P, R) for j, c in t.items()]
for c, j, k in terms:
    factor = [Q(1)]
    for _ in range(k):
        factor = multiply(factor, [Q(1, 2), -1])
    for i, x in enumerate(factor):
        poly[j+i] -= c*x
second = [Q(1), -4, 0, -1, Q(20143, 10080), -Q(37, 1620),
          Q(1801, 11340), -Q(17, 63), Q(223, 5670), Q(424, 2835)]+[Q(0)]*3
for t, first in ((P, 4), (R, 5)):
    for j, c in t.items():
        if j == first:
            continue
        for k in range(5):
            second[j+k] -= 2*c*Q((-1)**k*comb(4, k), 2**(4-k))
assert poly == second
while poly[-1] == 0:
    poly.pop()

def horner(e):
    out = Q(0)
    for c in reversed(poly):
        out = out*e+c
    return out

lo, hi = Q(0), Q(1, 4)
for _ in range(85):
    mid = (lo+hi)/2
    assert horner(mid) == new(mid)-1
    if new(mid) > 1:
        lo = mid
    else:
        hi = mid
assert new(lo) > 1 > new(hi)
old_lo = Q(19193920498167976369215855, 77371252455336267181195264)
old_hi = Q(38387840996335952738431711, 154742504910672534362390528)
assert old(old_lo) > 1 > old(old_hi)
assert hi < old_lo
endpoint = Q(hi.numerator*10**8//hi.denominator+1, 10**8)
assert new(endpoint) < 1 < old(endpoint)

# Root enclosure using integer polynomial arithmetic on a separate grid.
denom = 10**18
degree = len(poly)-1
common = lcm(*(Q(c).denominator for c in poly))
int_coeff = [int(c*common) for c in poly]
def grid_numerator(k):
    return sum(c*k**i*denom**(degree-i) for i, c in enumerate(int_coeff))
left, right = 248070000000000000, 248080000000000000
assert grid_numerator(left) > 0 > grid_numerator(right)
while right-left > 1:
    mid = (left+right)//2
    if grid_numerator(mid) > 0:
        left = mid
    else:
        right = mid
assert Q(left, denom) < lo < hi < Q(right, denom)
for t in (lo, hi, endpoint, Q(0), Q(1, 4), Q(1, 2)):
    assert new(t)-1 == horner(t)

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 10**9
result = {'status': 'all assertions passed', 'clock_table': table,
          'P_coefficients': {j: str(c) for j, c in sorted(P.items())},
          'R_coefficients': {j: str(c) for j, c in sorted(R.items())},
          'geometry_pattern_checks': geometry_checks, 'transmission_cases': transmission_checks,
          'C4_minus_one_coefficients': list(map(str, poly)),
          'root_lower': record(lo), 'root_upper': record(hi), 'root_width': record(hi-lo),
          'integer_grid_lower': record(Q(left, denom)), 'integer_grid_upper': record(Q(right, denom)),
          'threshold_improvement_lower': record(old_lo-hi), 'threshold_improvement_upper': record(old_hi-lo),
          'endpoint': record(endpoint), 'C4_at_endpoint': record(new(endpoint)), 'C3_at_endpoint': record(old(endpoint)),
          'contraction_improvement_at_old_root_midpoint': record(old((old_lo+old_hi)/2)-new((old_lo+old_hi)/2)),
          'nice': os.getpriority(os.PRIO_PROCESS, 0), 'OMP_NUM_THREADS': os.environ['OMP_NUM_THREADS'],
          'cpu_limit_seconds': 30, 'peak_rss_bytes_macos': rss}
output = json.dumps(result, indent=2, sort_keys=True)+'\n'
Path(__file__).with_name('audit_output.json').write_text(output)
print(output, end='')
