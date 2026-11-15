"""Exact finite audit of the pair-slack extension in PROOF.md."""
import os
import resource
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import json

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))

def g(k):
    return (0,0,1,2,2)[k]

def c0(e):
    return (2-4*e)*(1-e**3/2)

def c1(e):
    return c0(e)-Q(17,630)*e**4*(Q(1,2)-e)**4

def c2(e):
    a = Q(1,2)-e
    return c1(e)-Q(4,15)*e**5*a**3-Q(16,81)*e**6*a**3

def expanded(e):
    # Independently hand-expanded C2(e)-1, by powers of e.
    return (1-4*e-e**3+Q(20143,10080)*e**4
            -Q(5,252)*e**5+Q(1529,11340)*e**6
            -Q(187,945)*e**7-Q(107,1890)*e**8+Q(16,81)*e**9)

def record(x):
    with localcontext() as ctx:
        ctx.prec = 50
        return {'exact': str(x),
                'decimal': str(Decimal(x.numerator)/Decimal(x.denominator))}

# Exact local gap; no geometric or probabilistic assumptions.
gap_by_m = {m:set() for m in range(5)}
pair_events = 0
local_cases = 0
for states in product(((0,0),(0,1),(1,1)), repeat=4):
    low, high = zip(*states)
    ds = [h-l for l,h in states]
    m = sum(ds)
    b = sum(ds[i] and any(all(states[j] == (v,v)
                         for j in range(4) if j != i) for v in (0,1))
            for i in range(4))
    events = sum(all(ds[j] for j in pair) and
                 any(all(states[j] == (v,v) for j in range(4)
                         if j not in pair) for v in (0,1))
                 for pair in combinations(range(4),2))
    assert events <= 1
    gap = m-b-(g(sum(high))-g(sum(low)))
    assert gap >= Q(comb(m,3),2)+events
    # Independent full gap characterization.
    assert gap == events+(m == 3)+2*(m == 4)
    gap_by_m[m].add(gap)
    pair_events += events
    local_cases += 1
assert local_cases == 81 and pair_events == 12

# Verify the rule by random deletion of one input, then a triple majority.
rule_checks = 0
for bits in product((0,1),repeat=4):
    majority = Q(sum(sum(bits[j] for j in tri)>=2
                     for tri in combinations(range(4),3)),4)
    for e in (Q(0),Q(1,5),Q(248076,10**6),Q(1,2)):
        p = (e,e,Q(1,2),1-e,1-e)[sum(bits)]
        assert p == e+(1-2*e)*majority
        assert p == e+(Q(1,2)-e)*g(sum(bits))
        rule_checks += 1

transmission = [g(2+u)-g(1+l) for l,u in ((0,0),(0,1),(1,1))]
assert transmission == [1,2,1]

# Build geometry from actual lattice coordinates, for all six pairs.
neighbors = ((0,1),(1,0),(0,-1),(-1,0))
diagonals = ((1,1),(1,-1),(-1,-1),(-1,1))
geometry = []
receiver_geometry_checks = 0
for pair in combinations(neighbors,2):
    helpers = [h for h in diagonals
               if any(abs(h[0]-r[0])+abs(h[1]-r[1])==1 for r in pair)]
    patterns = []
    for values in product((0,1), repeat=len(helpers)):
        if all(sorted(values[i] for i,h in enumerate(helpers)
                      if abs(h[0]-r[0])+abs(h[1]-r[1])==1) == [0,1]
               for r in pair):
            patterns.append(values)
    adjacent = sum(abs(pair[0][i]-pair[1][i]) for i in (0,1)) == 2 and (
        pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1])
    assert (len(helpers),len(patterns)) == ((3,2) if adjacent else (4,4))
    blockers = [v for v in neighbors if v not in pair]
    assert len(set([(0,0)]+helpers+list(pair)+blockers)) == 1+len(helpers)+4
    for receiver in pair:
        rx,ry = receiver
        actual_inputs = {(rx+1,ry),(rx-1,ry),(rx,ry+1),(rx,ry-1)}
        axial = (2*rx,2*ry)
        adjacent_helpers = {h for h in helpers if h in actual_inputs}
        assert len(adjacent_helpers) == 2
        assert actual_inputs == {(0,0),axial} | adjacent_helpers
        assert not actual_inputs.intersection(blockers)
        receiver_geometry_checks += 1
    geometry.append({'pair':pair,'type':'adjacent' if adjacent else 'opposite',
                     'helpers':helpers,'patterns':patterns})
assert sum(v['type']=='adjacent' for v in geometry) == 4

def order_count(n, edges):
    # Direct enumeration, retaining no permutation list.
    number = 0
    for order in permutations(range(n)):
        rank = [0]*n
        for i,v in enumerate(order):
            rank[v] = i
        number += all(rank[u]<rank[v] for u,v in edges)
    # Independent recursion through order ideals.
    ways = [0]*(1<<n)
    ways[0] = 1
    for mask in range(1<<n):
        for v in range(n):
            if not mask & (1<<v) and all(mask & (1<<u) for u,w in edges if w==v):
                ways[mask | (1<<v)] += ways[mask]
    assert ways[-1] == number
    return number

adj_edges = [(0,3),(1,3),(1,4),(2,4)]  # two additional free blockers 5,6
opp_edges = [(0,4),(1,4),(2,5),(3,5)]  # free blockers 6,7
adj_count = order_count(7,adj_edges)
opp_count = order_count(8,opp_edges)
# Independently form clock edges from actual coordinates in every orientation.
for item in geometry:
    sites = item['helpers']+list(item['pair'])+[
        v for v in neighbors if v not in item['pair']]
    edges = [(sites.index(h),sites.index(r)) for h in item['helpers']
             for r in item['pair'] if abs(h[0]-r[0])+abs(h[1]-r[1])==1]
    actual_count = order_count(len(sites),edges)
    assert actual_count == (adj_count if item['type']=='adjacent' else opp_count)
    item['clock_orders_from_actual_geometry'] = actual_count
# Third derivation: alternating fence on 5 sites, freely interleave two blockers.
fence5 = order_count(5,adj_edges)
assert fence5 == 16
assert adj_count == fence5*comb(7,5)*factorial(2) == 672
# Opposite case: independent triples, each receiver must be last in its triple.
assert Q(opp_count,factorial(8)) == Q(1,3)**2
assert opp_count == 4480
clock = {}
for name,n,count in (('adjacent',7,adj_count),('opposite',8,opp_count)):
    integral = sum(Q((-1)**j*comb(n,j),j+1) for j in range(n+1))
    assert integral == Q(1,n+1)  # substitution u=1-exp(-s)
    constant = Q(count,factorial(n))*integral
    assert constant == Q(count,factorial(n+1))
    clock[name] = {'sites':n,'orders':count,'integral':record(integral),
                   'source_integrated_clock_probability':record(constant)}
assert Q(adj_count,factorial(8)) == Q(1,60)
assert Q(opp_count,factorial(9)) == Q(1,81)
adj_coefficient = 2*2*Q(adj_count,factorial(8))
opp_coefficient = 4*2*Q(opp_count,factorial(9))
assert adj_coefficient == Q(1,15)
assert opp_coefficient == Q(8,81)

# Algebra audit via polynomial multiplication, independent of hand expansion.
def multiply(p,q):
    result = [Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            result[i+j] += x*y
    return result

def power(p,n):
    ans = [Q(1)]
    for _ in range(n):
        ans = multiply(ans,p)
    return ans

poly = [Q(1),Q(-4),Q(0),Q(-1),Q(2)]+[Q(0)]*5
for coefficient,m,n in ((Q(17,630),4,4),(4*adj_coefficient,5,3),
                         (2*opp_coefficient,6,3)):
    term = [Q(0)]*m+power([Q(1,2),Q(-1)],n)
    for j,x in enumerate(term):
        poly[j] -= coefficient*x
for e in (Q(0),Q(1,10),Q(1,4),Q(1,2),Q(248076,10**6)):
    by_coefficients = sum(v*e**i for i,v in enumerate(poly))
    assert by_coefficients == expanded(e) == c2(e)-1

# Exact bisection, then independently chosen decimal-grid signs.
lo,hi = Q(0),Q(1,4)
for _ in range(85):
    mid = (lo+hi)/2
    if c2(mid)>1:
        lo = mid
    else:
        hi = mid
assert c2(lo)>1>c2(hi)
grid_lo,grid_hi = Q(2480756,10**7),Q(2480757,10**7)
assert expanded(grid_lo)>0>expanded(grid_hi)
assert grid_lo<lo<hi<grid_hi
endpoint = Q(248076,10**6)
assert c2(endpoint)<1<c1(endpoint)
old_lo = Q(146438707495522750369,590295810358705651712)
old_hi = Q(1171509659964182002953,4722366482869645213696)
assert c1(old_lo)>1>c1(old_hi)
assert hi<old_lo
for t in (lo,hi,endpoint):
    assert expanded(t)==c2(t)-1

result = {
    'status':'all assertions passed',
    'ordered_local_pairs':local_cases,
    'pair_slack_configurations':pair_events,
    'local_gap_by_disagreement_count':{m:sorted(s) for m,s in gap_by_m.items()},
    'rule_checks':rule_checks,
    'transmission_in_units_of_a':transmission,
    'receiver_geometry_checks':receiver_geometry_checks,
    'geometry':geometry,
    'clock':clock,
    'adjacent_pair_bound_coefficient_before_e5_a2':record(adj_coefficient),
    'opposite_pair_bound_coefficient_before_e6_a2':record(opp_coefficient),
    'expanded_C2_minus_one_coefficients':list(map(str,poly)),
    'root_lower':record(lo),'root_upper':record(hi),
    'root_width':record(hi-lo),
    'threshold_improvement_lower':record(old_lo-hi),
    'threshold_improvement_upper':record(old_hi-lo),
    'rational_endpoint':record(endpoint),
    'C2_at_endpoint':record(c2(endpoint)),
    'C1_at_endpoint':record(c1(endpoint)),
    'nice':os.getpriority(os.PRIO_PROCESS,0),
    'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS'],
    'cpu_time_limit_seconds':30,
    'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
assert result['peak_rss_bytes_macos'] < 10**9
output = json.dumps(result,indent=2,sort_keys=True)+'\n'
Path(__file__).with_name('audit_output.json').write_text(output)
print(output,end='')
