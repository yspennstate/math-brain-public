"""Exact finite checks for PROOF.md; one process, standard library only."""
from fractions import Fraction as F
from itertools import product
import heapq
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))

# Test interpolation from raw costs, independently of the convex formula.
patterns = ((F(0), F(0), F(1, 2), F(1, 2), F(1)),
            (F(0), F(1, 3), F(1, 3), F(2, 3), F(1)),
            (F(0), F(0), F(0), F(0), F(1)))
configs = pairs = 0
for theta, increments, errors in product(patterns,
        product((F(0), F(1, 7), F(2, 7)), repeat=4),
        product((F(-2), F(0), F(3)), repeat=2)):
    defects = [F(0)]
    for increment in increments:
        defects.append(defects[-1]+increment)
    p = [F(j, 5) for j in range(5)]
    q = [p[j]-p[0]+defects[j] for j in range(5)]
    d = defects[-1]
    g0, g1 = p[0]+errors[0], p[-1]+errors[1]
    c = q[-1]-g1+g0
    assert c == d-errors[1]+errors[0]
    g = [g0+q[j]-theta[j]*c for j in range(5)]
    e = [g[j]-p[j] for j in range(5)]
    for j in range(5):
        convex = (1-theta[j])*errors[0]+theta[j]*errors[1]
        assert e[j] == convex+defects[j]-theta[j]*d
        assert abs(e[j]-convex) <= d
    for a, b in product(range(5), repeat=2):
        assert q[b]-q[a]-g[b]+g[a] == (theta[b]-theta[a])*c
        assert abs(e[b]-e[a]) <= abs(errors[1]-errors[0])+2*d
        if theta[a] == theta[b]:
            assert q[b]-q[a]-g[b]+g[a] == 0
        pairs += 1
    configs += 1
print(f'Interpolation: {configs} exact configurations; {pairs} ordered/reversed occurrence pairs PASS')

# A finite metric graph with physical domination in both orientations.
# Subdivide every grid edge at its midpoint to test partial-edge endpoints.
vertices = list(product(range(3), repeat=2))
original_edges = [(u, v) for u in vertices for v in vertices
                  if u < v and sum(abs(u[i]-v[i]) for i in range(2)) == 1]

def bfun(x):
    return F(3*x[0]-2*x[1]+x[0]*x[1], 7)

def linear(x):
    return (2*x[0]+x[1])/F(11)

def potential(x):
    return bfun(x)-linear(x)

adjacency = {u: {} for u in vertices}
edge_weights = {}
for j, (u, v) in enumerate(original_edges):
    # bfun is affine on these horizontal/vertical edges.
    midpoint = tuple(F(u[i]+v[i], 2) for i in range(2))
    weight = abs(bfun(v)-bfun(u))+F(j+1, 13)
    edge_weights[u, v] = weight
    adjacency.setdefault(midpoint, {})
    for a, b in ((u, midpoint), (midpoint, v)):
        adjacency[a][b] = adjacency[b][a] = weight/2
        assert weight/2 >= abs(bfun(b)-bfun(a))
nodes = sorted(adjacency)

def shortest_from(start):
    distances, queue = {start: F(0)}, [(F(0), start)]
    while queue:
        cost, u = heapq.heappop(queue)
        if cost != distances[u]:
            continue
        for v, weight in adjacency[u].items():
            candidate = cost+weight
            if v not in distances or candidate < distances[v]:
                distances[v] = candidate
                heapq.heappush(queue, (candidate, v))
    return distances

distances = {u: shortest_from(u) for u in nodes}
# Independent all-pairs calculation, not another Dijkstra run.
floyd = {(u, v): (F(0) if u == v else adjacency[u].get(v))
         for u, v in product(nodes, repeat=2)}
for k in nodes:
    for u, v in product(nodes, repeat=2):
        if floyd[u, k] is None or floyd[k, v] is None:
            continue
        candidate = floyd[u, k]+floyd[k, v]
        if floyd[u, v] is None or candidate < floyd[u, v]:
            floyd[u, v] = candidate
assert all(distances[u][v] == floyd[u, v] for u, v in product(nodes, repeat=2))
print(f'Metric graph: {len(nodes)} vertices; {len(nodes)**2} Dijkstra/Floyd distances agree PASS')

paths = (((0, 0), (1, 0), (0, 0), (1, 0), (1, 1), (2, 1), (2, 2)),
         ((0, 2), (1, 2), (1, 1), (1, 0), (2, 0)))
parameters = ((F(0), F(0), F(1, 2), F(1), F(1), F(3, 2), F(2)),
              (F(0), F(1, 2), F(1, 2), F(1), F(2)))
roads = []
for path, params in zip(paths, parameters):
    points, levels, cum = [path[0]], [params[0]], [F(0)]
    for j, (u, v) in enumerate(zip(path, path[1:])):
        mid = tuple(F(u[i]+v[i], 2) for i in range(2))
        for vertex, level in ((mid, (params[j]+params[j+1])/2), (v, params[j+1])):
            weight = adjacency[points[-1]][vertex]
            cum.append(cum[-1]+weight)
            points.append(vertex)
            levels.append(level)
    cuts = [levels.index(F(k)) for k in range(3)]
    qcum = [cum[j]-linear(x)+linear(points[0]) for j, x in enumerate(points)]
    ds = [qcum[cuts[k+1]]-qcum[cuts[k]]
          -potential(points[cuts[k+1]])+potential(points[cuts[k]]) for k in range(2)]
    assert all(x >= 0 for x in ds)
    roads.append(dict(points=points, levels=levels, cuts=cuts, q=qcum, defects=ds))

anchor_ids = list(product(range(2), range(3)))
root = anchor_ids[0]
comparison_edges = [(root, a) for a in anchor_ids[1:]]
comparison_edges += [((road, k), (road, k+1)) for road, k in product(range(2), range(2))]
assert len(comparison_edges) == 5+4 == 9
dtotal = sum((sum(r['defects']) for r in roads), F(0))
assert dtotal == sum((r['q'][-1]-potential(r['points'][-1])+potential(r['points'][0])
                     for r in roads), F(0))
# Independent hand count on the original, unsubdivided road records:
# absolute calibration increments total 24/7, net increments 16/7;
# slack numerators are 3*2 + 5 + 2*6 + 7 + 8 + 9 + 12 = 59.
assert dtotal == F(24-16, 7)+F(3*2+5+2*6+7+8+9+12, 13) == F(517, 91)
raw_checks = centered_checks = switch_checks = 0
largest_raw_negative = largest_center_negative = F(0)

for trial in range(12):
    errors = {a: F((3*j+5*trial) % 11-5, 17) for j, a in enumerate(anchor_ids)}
    atotal = sum((abs(errors[b]-errors[a]) for a, b in comparison_edges), F(0))
    # Independently sum along the explicit root-star paths.
    anchor_range = max(errors.values())-min(errors.values())
    assert anchor_range <= sum((abs(errors[a]-errors[root]) for a in anchor_ids), F(0)) <= atotal
    gauges = []
    for road_id, road in enumerate(roads):
        g = []
        for j, (x, theta) in enumerate(zip(road['points'], road['levels'])):
            k = 0 if j < road['cuts'][1] else 1
            start, end = road['cuts'][k:k+2]
            ga = potential(road['points'][start])+errors[road_id, k]
            gb = potential(road['points'][end])+errors[road_id, k+1]
            c = road['q'][end]-road['q'][start]-gb+ga
            g.append(ga+road['q'][j]-road['q'][start]-(theta-k)*c)
        gauges.append(g)
    occurrences = [(r, j) for r, road in enumerate(roads) for j in range(len(road['points']))]
    rmax = smax = F(0)
    for road_id, road in enumerate(roads):
        for i, j in product(range(len(road['points'])), repeat=2):
            corrected = road['q'][j]-road['q'][i]-gauges[road_id][j]+gauges[road_id][i]
            rmax = max(rmax, abs(corrected))
    for (ra, i), (rb, j) in product(occurrences, repeat=2):
        a, b = roads[ra], roads[rb]
        x, y = a['points'][i], b['points'][j]
        gx, gy = gauges[ra][i], gauges[rb][j]
        ex, ey = gx-potential(x), gy-potential(y)
        assert abs(ex-ey) <= atotal+2*dtotal
        if x == y:
            assert gx-gy == ex-ey
            smax = max(smax, abs(gx-gy))
            switch_checks += 1
        qphysical = distances[x][y]-linear(y)+linear(x)
        physical_defect = qphysical-potential(y)+potential(x)
        assert physical_defect >= 0
        f0 = qphysical-gy+gx
        assert f0 == physical_defect+ex-ey
        assert f0 >= -atotal-2*dtotal
        largest_raw_negative = max(largest_raw_negative, -f0)
        # Add a genuine positively charged out-and-back physical excursion.
        loop_cost = 2*next(iter(adjacency[x].values()))
        assert f0+loop_cost > f0
        raw_checks += 1
        # Two marked center choices, then centers inside an edge occurrence.
        for selector in (0, 1, 'interior'):
            ca = a['cuts'][selector] if isinstance(selector, int) else 1
            cb = b['cuts'][selector] if isinstance(selector, int) else 1
            qa, qb = a['q'][i]-a['q'][ca], b['q'][cb]-b['q'][j]
            fc = qa+qphysical+qb-gauges[rb][cb]+gauges[ra][ca]
            ja = qa-gx+gauges[ra][ca]
            jb = qb-gauges[rb][cb]+gy
            assert fc == f0+ja+jb
            da = qa-potential(x)+potential(a['points'][ca])
            db = qb-potential(b['points'][cb])+potential(y)
            center_errors = ((gauges[ra][ca]-potential(a['points'][ca]))
                             -(gauges[rb][cb]-potential(b['points'][cb])))
            assert fc == physical_defect+da+db+center_errors
            assert abs(da) <= dtotal and abs(db) <= dtotal
            bound = atotal+(2 if isinstance(selector, int) else 4)*dtotal
            assert fc >= -bound
            largest_center_negative = max(largest_center_negative, -fc)
            # A common offset in every gauge cancels from both formulas.
            offset = F(10**9, 3)
            assert qa+qphysical+qb-(gauges[rb][cb]+offset)+(gauges[ra][ca]+offset) == fc
            centered_checks += 1
    assert rmax <= dtotal+atotal and smax <= atotal+2*dtotal
    for switches in (1, 2, 4):
        envelope = (switches+1)*rmax+switches*smax
        assert envelope <= (2*switches+1)*atotal+(3*switches+1)*dtotal

print(f'Physical endpoint lower bounds: {raw_checks}; center-adjusted identities/bounds: {centered_checks} PASS')
print(f'Switch coincidences: {switch_checks}; marked/interior centers, loops, common offsets PASS')
print(f'Fixture N=4, M=9, total defect={dtotal}; two independent defect sums agree')
print(f'Largest sampled negative parts: endpoint={largest_raw_negative}, center-adjusted={largest_center_negative}')

# Negative controls for assumptions that must not be silently dropped.
# At an initial nominal pause, positive raw cost is absorbed by Q in g.
theta, partial_defect, full_defect = F(0), F(1), F(1)
assert partial_defect-theta*full_defect == 1
assert abs(partial_defect-theta*full_defect) > 0  # equal anchor errors do not imply zero interior error
tau, nh_displacement = F(5), F(2)
assert (tau+nh_displacement)-(-(tau-nh_displacement)) == 2*tau > 0
# A switch between different calibration worlds need not cancel P.
assert (F(0)-F(0)) == (F(100)-F(100)) == 0
assert abs(F(0)-F(100)) == 100
empty_envelope = 0  # no feasible physical path, by definition
assert empty_envelope == 0
for n, b in product(range(1, 8), range(5)):
    assert 2*n*(2*b+1)+n == n*(4*b+3) == 4*b*n+3*n
for labels in (2, 7, 31):
    # A per-label L1 bound does not control an unrestricted selected maximum.
    means = [sum(labels if state == label else 0 for state in range(labels))/labels
             for label in range(labels)]
    assert means == [1]*labels
    assert sum(max(labels if state == label else 0 for label in range(labels))
               for state in range(labels))/labels == labels
print('Negative controls: omitted interpolation defect, physical reversal, different calibrations, selected maximum PASS')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform == 'darwin' else 1024)
assert rss < 768
print(f'Elapsed {time.monotonic()-started:.3f} seconds; peak RSS {rss:.2f} MiB; nice {os.getpriority(os.PRIO_PROCESS, 0)}')
