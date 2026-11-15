#!/usr/bin/env python3
"""Exact circuit-repair audits; one process, standard-library arithmetic."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json
import os
import resource
import signal
import time

ROOT = Path(__file__).resolve().parent
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
START = time.monotonic()


def ldlt_solve(a, b):
    """Exact symmetric LDL^T factorization of a grounded Laplacian."""
    n = len(b)
    lower = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        dj = a[j][j] - sum(lower[j][k]**2 * diagonal[k] for k in range(j))
        assert dj > 0
        diagonal.append(dj)
        for i in range(j+1, n):
            lower[i][j] = (a[i][j] - sum(lower[i][k] * lower[j][k] * diagonal[k]
                                        for k in range(j))) / dj
    z = []
    for i in range(n):
        z.append(b[i] - sum(lower[i][j] * z[j] for j in range(i)))
    w = [z[i]/diagonal[i] for i in range(n)]
    x = [F(0)] * n
    for i in reversed(range(n)):
        x[i] = w[i] - sum(lower[j][i] * x[j] for j in range(i+1, n))
    assert all(sum(a[i][j]*x[j] for j in range(n)) == b[i] for i in range(n))
    return x


def components(edges, extra=()):
    vs = set(extra) | {u for u,v,r in edges} | {v for u,v,r in edges}
    adj = {v: set() for v in vs}
    for u,v,r in edges:
        adj[u].add(v)
        adj[v].add(u)
    result = []
    while vs:
        comp = {min(vs)}
        todo = list(comp)
        while todo:
            for w in adj[todo.pop()] - comp:
                comp.add(w)
                todo.append(w)
        vs -= comp
        result.append(comp)
    return result


def divergence(edges, flow, extra=()):
    d = {v: F(0) for comp in components(edges, extra) for v in comp}
    for (u,v,r), f in zip(edges, flow):
        d[u] += f
        d[v] -= f
    return d


def energy(edges, flow):
    return sum((F(r)*f*f for (u,v,r),f in zip(edges,flow)), F(0))


def current(edges, demand, extra=()):
    """Prescribed divergence, grounding separately in every component."""
    potential = {}
    for comp in components(edges, set(extra) | set(demand)):
        assert sum(demand.get(v,0) for v in comp) == 0, (comp, demand)
        ground = min(comp)
        free = sorted(comp - {ground})
        ix = {v:i for i,v in enumerate(free)}
        matrix = [[F(0) for _ in free] for _ in free]
        for u,v,r in edges:
            if u not in comp or u == v:
                continue
            c = 1/F(r)
            if u != ground:
                matrix[ix[u]][ix[u]] += c
            if v != ground:
                matrix[ix[v]][ix[v]] += c
            if u != ground and v != ground:
                matrix[ix[u]][ix[v]] -= c
                matrix[ix[v]][ix[u]] -= c
        values = ldlt_solve(matrix, [F(demand.get(v,0)) for v in free])
        potential[ground] = F(0)
        potential.update(zip(free, values))
    flow = [(potential[u]-potential[v])/F(r) for u,v,r in edges]
    d = divergence(edges, flow, extra)
    assert all(d.get(v,0) == demand.get(v,0) for v in set(d) | set(demand))
    return flow


def wired(edges, left, right):
    left, right = set(left), set(right)
    assert left.isdisjoint(right)
    vs = {v for comp in components(edges, left | right) for v in comp}
    rename = {v: '@L' if v in left else '@R' if v in right else v for v in vs}
    quotient = [(rename[u],rename[v],r) for u,v,r in edges if rename[u] != rename[v]]
    quotient_flow = iter(current(quotient, {'@L':F(1),'@R':F(-1)}, rename.values()))
    flow = [next(quotient_flow) if rename[u] != rename[v] else F(0) for u,v,r in edges]
    d = divergence(edges,flow,left | right)
    assert sum(d[v] for v in left) == 1
    assert sum(d[v] for v in right) == -1
    assert all(d[v] == 0 for v in vs - left - right)
    return flow


def diameter(edges, boundary):
    if len(components(edges,boundary)) > 1:
        comp = next(comp for comp in components(edges,boundary) if boundary[0] in comp)
        if not set(boundary) <= comp:
            return None  # infinity, never silently drop isolated interface vertices
    return max((energy(edges,current(edges,{u:F(1),v:F(-1)}))
                for u,v in combinations(boundary,2)), default=F(0))


def layer_data(pieces, boundaries):
    local = [wired(edges,left,right) for edges,left,right
             in zip(pieces,boundaries,boundaries[1:])]
    scalar = sum(energy(e,f) for e,f in zip(pieces,local))
    whole_edges = sum(pieces,[])
    whole = wired(whole_edges,boundaries[0],boundaries[-1])
    resistance = energy(whole_edges,whole)
    correction = F(0)
    offset = 0
    for edges,theta in zip(pieces,local):
        eta = [f-t for f,t in zip(whole[offset:offset+len(edges)],theta)]
        offset += len(edges)
        assert sum(F(r)*t*h for (u,v,r),t,h in zip(edges,theta,eta)) == 0
        correction += energy(edges,eta)
    assert resistance == scalar+correction
    mismatch = []
    for i,s in enumerate(boundaries[1:-1]):
        da = divergence(pieces[i],local[i],s)
        db = divergence(pieces[i+1],local[i+1],s)
        delta = {v:-da[v]-db[v] for v in s}
        assert sum(delta.values()) == 0
        assert min(-da[v] for v in s) >= 0
        assert min(db[v] for v in s) >= 0
        mismatch.append(delta)
    return scalar,resistance,correction,local,mismatch


def tv(h):
    return sum(abs(v) for v in h)/2


def circuit_formula(weights, h):
    assert sum(h) == 0
    cumulative = []
    total = F(0)
    for value in h:
        total += value
        cumulative.append(total)
    weight_sum = sum(weights)
    mean = sum(r*z for r,z in zip(weights,cumulative))/weight_sum
    flow = [z-mean for z in cumulative]
    q = sum(r*f*f for r,f in zip(weights,flow))
    pairwise = sum(weights[i]*weights[j]*(cumulative[i]-cumulative[j])**2
                   for i,j in combinations(range(len(h)),2))/weight_sum
    assert q == pairwise
    assert q <= F(weight_sum,4)*tv(h)**2
    return q,flow


def circuit_audit(pieces, boundaries, circuits):
    a,r,d,local,mismatch = layer_data(pieces,boundaries)
    repair = {}
    q_sum = F(0)
    coarse = F(0)
    for (vs,weights),delta in zip(circuits,mismatch):
        h = [delta[v] for v in vs]
        q,flow = circuit_formula(weights,h)
        q_sum += q
        coarse += F(sum(weights),4)*tv(h)**2
        for j,f in enumerate(flow):
            key = (vs[j],vs[(j+1)%len(vs)])
            assert key not in repair
            repair[key] = f
    candidate = []
    edges_all = sum(pieces,[])
    for edges,theta in zip(pieces,local):
        for (u,v,w),f in zip(edges,theta):
            extra = repair.get((u,v),-repair.get((v,u),F(0)))
            if (u,v) in repair or (v,u) in repair:
                assert f == 0  # wired optima vanish on all interface edges
            candidate.append(f+extra)
    div = divergence(edges_all,candidate, sum(boundaries,[]))
    assert div[boundaries[0][0]] == 1
    assert sum(div[v] for v in boundaries[-1]) == -1
    assert all(div[v] == 0 for v in div if v not in boundaries[0]+boundaries[-1])
    assert energy(edges_all,candidate) == a+q_sum
    assert 0 <= d <= q_sum <= coarse
    return a,r,d,q_sum,coarse


# Independent rerun of all 255 configurations underlying round 3.
old_count = old_positive = 0
s = ['u','v','w']
for lm,rm,owners in product(range(1,8),range(1,8),product(range(3),repeat=3)):
    a = [('x',v,1) for i,v in enumerate(s) if lm >> i & 1]
    b = [(v,'y',1) for i,v in enumerate(s) if rm >> i & 1]
    for (u,v),owner in zip(combinations(s,2),owners):
        if owner == 1: a.append((u,v,1))
        if owner == 2: b.append((u,v,1))
    if len(components(a,['x']+s)) != 1 or len(components(b,s+['y'])) != 1:
        continue
    scalar,r,d,_,delta = layer_data([a,b],[['x'],s,['y']])
    da,db = diameter(a,s),diameter(b,s)
    bound = da*db/(da+db)*tv(delta[0].values())**2
    assert d <= bound
    old_count += 1
    old_positive += int(d > 0)
assert (old_count,old_positive) == (255,210)

weighted_count = 0
for weights in product([1,2,5],repeat=6):
    a = [('x',v,w) for v,w in zip(s,weights[:3])]
    b = [(v,'y',w) for v,w in zip(s,weights[3:])]
    _,_,d,_,delta = layer_data([a,b],[['x'],s,['y']])
    da,db = diameter(a,s),diameter(b,s)
    assert d <= da*db/(da+db)*tv(delta[0].values())**2
    weighted_count += 1

sharpness = []
for length in [1,2,4,8,16,32,64,128,256,512,1024]:
    k = length**2
    pieces = [[('x','u',1),('x','v',k)],
              [('u','p',1),('v','q',1),('p','q',length)],
              [('p','y',k),('q','y',1)]]
    _,r,d,_,delta = layer_data(pieces,[['x'],['u','v'],['p','q'],['y']])
    t = F(k-1,2*(k+1))
    assert all(tv(h.values()) == t for h in delta)
    bnd = t*t*(F((k+1)*(length+2),k+length+3)+F((k+1)*length,k+length+1))
    assert d <= 2*bnd
    assert 1/(F(1,length)+F(2,k)) <= r <= length+3
    sharpness.append({'L':length,'R':str(r),'D':str(d),
                      'D_over_previous_sum':str(d/bnd) if bnd else None})
assert F(sharpness[-1]['D_over_previous_sum']) > F(199,100)

# Exact demand tests: cumulative formula, pairwise variance, and Kirchhoff
# equations; rotate and reverse weighted circuits to test indexing.
cycle_count = 0
for n in range(3,8):
    vs = [f'v{j}' for j in range(n)]
    for weights in ([1]*n,[1+j%3 for j in range(n)]):
        edges = [(vs[j],vs[(j+1)%n],weights[j]) for j in range(n)]
        for h0 in product([-1,0,1],repeat=n):
            if sum(h0):
                continue
            h = list(map(F,h0))
            q,flow = circuit_formula(weights,h)
            solved = current(edges,dict(zip(vs,h)))
            assert flow == solved
            assert q == energy(edges,solved)
            assert circuit_formula(weights[1:]+weights[:1],h[1:]+h[:1])[0] == q
            reverse_weights = weights[:-1][::-1]+weights[-1:]
            assert circuit_formula(reverse_weights,h[::-1])[0] == q
            cycle_count += 1

oscillations = []
for n in [4,6,8,12,16,20]:
    oscillatory,_ = circuit_formula([1]*n,[F(2*(-1)**j,n) for j in range(n)])
    dipole = [F(0)]*n
    dipole[0],dipole[n//2] = F(1),F(-1)
    concentrated,_ = circuit_formula([1]*n,dipole)
    assert oscillatory == F(1,n)
    assert concentrated == F(n,4)
    assert concentrated/oscillatory == F(n*n,4)
    oscillations.append({'N':n,'alternating_Q':str(oscillatory),
                         'antipodal_Q':str(concentrated)})

# Exhaust a square interface: all nonempty source/sink neighbor sets and
# every assignment of the four circuit edges to its two sides.
square_count = square_equality = square_both_infinite = square_zero = 0
square_extreme = None
vs = [f'v{j}' for j in range(4)]
for lm,rm,owners in product(range(1,16),range(1,16),product([0,1],repeat=4)):
    pieces = [[('x',v,1) for j,v in enumerate(vs) if lm >> j & 1],
              [(v,'y',1) for j,v in enumerate(vs) if rm >> j & 1]]
    for j,owner in enumerate(owners):
        pieces[owner].append((vs[j],vs[(j+1)%4],1))
    a,r,d,q,coarse = circuit_audit(pieces,[['x'],vs,['y']],[(vs,[1]*4)])
    square_count += 1
    square_equality += int(d == q)
    square_zero += int(d == 0)
    disconnected_a = len({frozenset(c & set(vs)) for c in components(pieces[0],vs)
                          if c & set(vs)}) > 1
    disconnected_b = len({frozenset(c & set(vs)) for c in components(pieces[1],vs)
                          if c & set(vs)}) > 1
    square_both_infinite += int(disconnected_a and disconnected_b)
    if lm == 1 and rm == 4 and owners == (0,1,0,1):
        assert diameter(pieces[0],vs) is None
        assert diameter(pieces[1],vs) is None
        assert (a,r,d,q) == (F(2),F(3),F(1),F(1))
        square_extreme = {'A':str(a),'R':str(r),'D':str(d),'Q':str(q),
                          'inner_diameter':'infinity','outer_diameter':'infinity'}
assert square_count == 3600 and square_extreme is not None

# Independent count checks, without network linear solves.
def square_blocks(owners, side):
    """Union-find on the interface alone, separate from components()."""
    parent = list(range(4))
    def root(j):
        while parent[j] != j:
            j = parent[j]
        return j
    for j,owner in enumerate(owners):
        if owner == side:
            parent[root(j)] = root((j+1)%4)
    groups = {}
    for j in range(4):
        groups.setdefault(root(j),[]).append(j)
    return list(groups.values())


independent_both_infinite = 0
for owners in product([0,1],repeat=4):
    connected_counts = []
    for side in [0,1]:
        count = 1
        for block in square_blocks(owners,side):
            count *= 2**len(block)-1
        connected_counts.append(count)
    independent_both_infinite += (15-connected_counts[0])*(15-connected_counts[1])
assert square_both_infinite == independent_both_infinite == 328
assert square_zero == 15*16 == 240

# The explicit circuit repair is the global optimum iff its circuit
# potential is constant on each hub's neighbor set. Then the prescribed
# equal spoke currents extend to a potential at that hub. This criterion
# counts equality cases without using any global network resistance.
independent_equality_pairs = 0
for lm,rm in product(range(1,16),repeat=2):
    left = [j for j in range(4) if lm >> j & 1]
    right = [j for j in range(4) if rm >> j & 1]
    h = [F(int(j in left),len(left))-F(int(j in right),len(right)) for j in range(4)]
    _,flow = circuit_formula([1]*4,h)
    potential = [F(0)]
    for f in flow[:3]:
        potential.append(potential[-1]-f)
    if len({potential[j] for j in left}) == len({potential[j] for j in right}) == 1:
        independent_equality_pairs += 1
assert square_equality == 16*independent_equality_pairs == 656

independent_demand_count = 2*sum(
    sum(factorial(n)//(factorial(j)**2*factorial(n-2*j)) for j in range(n//2+1))
    for n in range(3,8))
assert cycle_count == independent_demand_count == 1222


def necklace(lengths, bridges, ownership):
    k = len(lengths)
    circuits = [([f'c{i}v{j}' for j in range(n)],[1]*n) for i,n in enumerate(lengths)]
    boundaries = [['x']]+[vs for vs,w in circuits]+[['y']]
    pieces = [[] for _ in range(k+1)]
    for i,w in enumerate(bridges):
        u = 'x' if i == 0 else circuits[i-1][0][lengths[i-1]//2]
        v = 'y' if i == k else circuits[i][0][0]
        pieces[i].append((u,v,w))
    for i,(vs,weights) in enumerate(circuits):
        for j,w in enumerate(weights):
            owner = i+(j%2 if ownership == 'alternating' else 0)
            pieces[owner].append((vs[j],vs[(j+1)%len(vs)],w))
    # Components disjoint from both terminal sets must also be harmless.
    pieces[0].append(('detached0','detached1',3))
    return pieces,boundaries,circuits


necklace_count = 0
for k in [1,2,3]:
    for lengths,bridges,ownership in product(product([4,6],repeat=k),
                                             product([1,3],repeat=k+1),
                                             ['inner','alternating']):
        pieces,boundaries,circuits = necklace(lengths,bridges,ownership)
        a,r,d,q,coarse = circuit_audit(pieces,boundaries,circuits)
        series = sum(F(n,4) for n in lengths)
        assert a == sum(bridges)
        assert d == q == coarse == series
        assert r == sum(bridges)+series
        necklace_count += 1
assert necklace_count == 336
assert necklace_count == 2*sum(2**k*2**(k+1) for k in [1,2,3])

growth = []
for length in [2,3,4,8,16]:
    pieces,boundaries,circuits = necklace([2*length]*2,[1]*3,'inner')
    a,r,d,q,coarse = circuit_audit(pieces,boundaries,circuits)
    assert (a,r,d,q) == (F(3),F(length+3),F(length),F(length))
    growth.append({'L':length,'A':str(a),'R':str(r),'D':str(d),
                   'R_over_A':str(r/a)})

df = F(91,48)
assert df/2 == F(91,96)
assert df+df/2 == F(91,32)
assert 2*df/(df+df/2) == F(4,3)

summary = {'earlier_interface_cases':old_count,'earlier_positive':old_positive,
           'earlier_weighted_star_cases':weighted_count,'earlier_sharpness':sharpness,
           'weighted_circuit_demand_cases':cycle_count,'oscillations':oscillations,
           'square_networks':square_count,'square_equal_upper_bound':square_equality,
           'square_zero_correction':square_zero,
           'square_both_diameters_infinite':square_both_infinite,
           'both_infinite_example':square_extreme,'nested_circuit_cases':necklace_count,
           'nested_circuit_growth':growth,'effective_nice':os.getpriority(os.PRIO_PROCESS,0),
           'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS'],
           'peak_RSS_bytes_macOS':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           'elapsed_seconds':round(time.monotonic()-START,4),
           'result':'all exact checks passed'}
assert summary['peak_RSS_bytes_macOS'] < 1024**3
(ROOT/'circuit_results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
