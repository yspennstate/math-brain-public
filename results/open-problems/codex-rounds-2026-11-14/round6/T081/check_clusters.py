"""Exact graph and fixed-background polymer checks; standard library only."""
import itertools
import json
import math
import os
import resource
import signal
import time
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('180s limit')))
signal.alarm(180)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()


def connected(n, edges):
    seen = {0}
    while True:
        new = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if new == seen:
            return len(seen) == n
        seen = new


def prufer_trees(n):
    if n == 1:
        return [frozenset()]
    trees = []
    for code in itertools.product(range(n), repeat=n-2):
        degree = [1+code.count(v) for v in range(n)]
        edges = []
        for v in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.append(tuple(leaves))
        trees.append(frozenset(edges))
    return trees


def optional_penrose_edges(n, tree, edges):
    levels, parents = {0: 0}, {}
    while len(levels) < n:
        for u, v in tree:
            if u in levels and v not in levels:
                parents[v], levels[v] = u, levels[u]+1
            elif v in levels and u not in levels:
                parents[u], levels[u] = v, levels[v]+1
    optional = []
    for u, v in edges-tree:
        if levels[u] == levels[v]:
            optional.append((u, v))
        elif abs(levels[u]-levels[v]) == 1:
            early, late = (u, v) if levels[u] < levels[v] else (v, u)
            if early >= parents[late]:
                optional.append((u, v))
    return optional


graph_cases = 0
for n in range(1, 6):
    all_edges = list(itertools.combinations(range(n), 2))
    trees = prufer_trees(n)
    connected_signed = {}
    for mask in range(1 << len(all_edges)):
        edges = frozenset(e for j, e in enumerate(all_edges) if mask >> j & 1)
        if connected(n, edges):
            connected_signed[mask] = (-1)**len(edges)
    for mask in range(1 << len(all_edges)):
        edges = frozenset(e for j, e in enumerate(all_edges) if mask >> j & 1)
        # First way: enumerate every connected spanning subgraph.
        coefficient = sum(sign for sub, sign in connected_signed.items() if sub & mask == sub)
        # Second way: sum the alternating Penrose intervals over Prufer trees.
        spanning = [tree for tree in trees if tree <= edges]
        intervals = sum((-1)**(n-1) for tree in spanning
                        if not optional_penrose_edges(n, tree, edges))
        assert coefficient == intervals
        assert abs(coefficient) <= len(spanning)
        assert (-1)**(n-1)*coefficient >= 0
        graph_cases += 1
assert graph_cases == 1099


def box(radius, center=(0, 0)):
    return frozenset((x+center[0], y+center[1])
                     for x, y in itertools.product(range(-radius, radius+1), repeat=2))


def enlarge(s):
    return frozenset((x+dx, y+dy) for x, y in s
                     for dx, dy in itertools.product((-1, 0, 1), repeat=2))


# Four geometric contours and a second code on the first support.
supports = [box(1), box(1, (4, 0)), box(1, (2, 0)), box(4)-box(2), box(1)]
enlargements = [enlarge(s) for s in supports]
sizes = list(map(len, supports))
incompatible = [[bool(enlargements[i] & supports[j]) for j in range(5)] for i in range(5)]
assert all(incompatible[i][i] for i in range(5))
assert not incompatible[0][1] and len(enlargements[0] & enlargements[1]) == 5
assert not incompatible[0][3] and enlargements[0] <= box(2)
assert incompatible[0][2] and incompatible[1][2]
assert incompatible[0][4]  # different codes on the same support
universe = frozenset().union(*enlargements)
sites = sorted(universe)
bits = {p: 1 << j for j, p in enumerate(sites)}
assigned = [sum(bits[p] for p in e) for e in enlargements]


@lru_cache(None)
def coefficient(labels):
    """Root-component recurrence, independent of connected-edge enumeration."""
    n = len(labels)
    full = (1 << n)-1

    @lru_cache(None)
    def all_graphs(mask):
        vertices = [i for i in range(n) if mask >> i & 1]
        return int(not any(incompatible[labels[i]][labels[j]]
                           for i, j in itertools.combinations(vertices, 2)))

    @lru_cache(None)
    def conn(mask):
        root = mask & -mask
        total = all_graphs(mask)
        sub = (mask-1) & mask
        while sub:
            if sub & root:
                total -= conn(sub)*all_graphs(mask ^ sub)
            sub = (sub-1) & mask
        return total

    return conn(full)


order = 6
multisets = []
for n in range(1, order+1):
    for labels in itertools.combinations_with_replacement(range(5), n):
        phi = coefficient(labels)
        if phi:
            support = 0
            for i in labels:
                support |= assigned[i]
            divisor = math.prod(math.factorial(labels.count(i)) for i in range(5))
            multisets.append((n, labels, phi, divisor, support))


def log_coefficients(poly):
    result = [F(0)]*(order+1)
    for n in range(1, order+1):
        an = poly[n] if n < len(poly) else 0
        result[n] = an - sum(F(i, n)*result[i]*(poly[n-i] if n-i < len(poly) else 0)
                            for i in range(1, n))
    return result


def subset_polynomial(catalog, weights):
    poly = [F(0)]*(len(catalog)+1)
    for mask in range(1 << len(catalog)):
        family = [catalog[j] for j in range(len(catalog)) if mask >> j & 1]
        if any(incompatible[i][j] for i, j in itertools.combinations(family, 2)):
            continue
        poly[len(family)] += math.prod(weights[i] for i in family)
    return poly


def deletion_polynomial(catalog, weights):
    if not catalog:
        return [F(1)]
    first, rest = catalog[0], catalog[1:]
    left = deletion_polynomial(rest, weights)
    right = deletion_polynomial(tuple(j for j in rest if not incompatible[first][j]), weights)
    ans = [F(0)]*max(len(left), len(right)+1)
    for i, x in enumerate(left):
        ans[i] += x
    for i, x in enumerate(right):
        ans[i+1] += weights[first]*x
    return ans


domains = [universe, enlargements[0], enlargements[1], enlargements[2], enlargements[3],
           enlargements[0] | enlargements[1], box(3), box(5), universe-{(0, 0)},
           universe-{(2, 0)}, frozenset()]
background_sites = [(2, 0), (-2, 0), (5, 0), (0, 5), (0, 2)]
dependence = [[0, 1, 4], [0], [4], [2, 3], [0, 1, 4]]
filled = [box(1), box(1, (4, 0)), box(1, (2, 0)), box(4), box(1)]
assert all(background_sites[j] in enlargements[i]-filled[i]
           for i in range(5) for j in dependence[i])
domain_checks, coefficient_checks, tails = 0, 0, 0
example = None
for state in itertools.product((0, 1), repeat=len(background_sites)):
    weights = [F(1+sum(state[j] for j in dependence[i]), 1+len(dependence[i])) / 32**sizes[i]
               for i in range(5)]
    # A finite-catalog version of the tilted root criterion. e^n <= 3^n.
    for i in range(5):
        assert sum(F(3, 16)**sizes[j] for j in range(5) if incompatible[i][j]) <= sizes[i]
    grouped = defaultdict(lambda: [F(0)]*(order+1))
    for n, labels, phi, divisor, support in multisets:
        grouped[support][n] += F(phi, divisor)*math.prod(weights[i] for i in labels)
    for domain in domains:
        domain_mask = sum(bits[p] for p in domain if p in bits)
        catalog = tuple(i for i in range(5) if enlargements[i] <= domain)
        poly = subset_polynomial(catalog, weights)
        deletion = deletion_polynomial(catalog, weights)
        assert poly == deletion + [F(0)]*(len(poly)-len(deletion))
        logarithm = log_coefficients(poly)
        grouped_inside = [sum(values[n] for support, values in grouped.items()
                              if support & domain_mask == support) for n in range(order+1)]
        assert grouped_inside == logarithm
        coefficient_checks += order
        domain_checks += 1
    # A rational remainder test for the actual logarithm, using its independent
    # alternating series in u = Xi(1)-1 rather than its activity-degree series.
    poly = subset_polynomial(tuple(range(5)), weights)
    u = sum(poly)-1
    assert 0 < u < 1
    log_lower = sum((-1)**(j+1)*u**j/j for j in range(1, 9))
    log_upper = log_lower + u**9/9
    degree6 = sum(sum(values) for values in grouped.values())
    # Tilted activities <= (1/16)^n. Rooted bound <= sum (3/16)^n.
    tail_bound = F(1, 2)**(min(sizes)*(order+1))*sum(F(3, 16)**n for n in sizes)
    assert max(abs(degree6-log_lower), abs(degree6-log_upper)) <= tail_bound
    tails += 1
    if state == (0,)*5:
        example = dict(overlapping_collar_sites=5, min_contour_size=min(sizes),
                       log_interval_width=str(log_upper-log_lower),
                       proven_cluster_tail_bound=str(tail_bound))

# Omitting repeated contour occurrences fails already at degree two.
w = F(1, 32)
single = log_coefficients([F(1), w])
assert single[1:] == [(-1)**(n+1)*w**n/n for n in range(1, order+1)]
assert single[2] == -w*w/2 != 0
# False incompatibility of overlapping collars wrongly discards a valid pair.
w0, w1 = F(1, 7), F(1, 11)
correct_pair = 1+w0+w1+w0*w1
wrong_pair = 1+w0+w1
assert correct_pair-wrong_pair == F(1, 77)
# A cutoff alone cannot give domain-independent U: already for one contour,
# changing its weight with the surrounding domain changes the linear log term.
small_domain_weight, large_domain_weight = F(1, 128), F(1, 256)
domain_dependent_gap = log_coefficients([F(1), small_domain_weight])[1] - \
                       log_coefficients([F(1), large_domain_weight])[1]
assert domain_dependent_gap == F(1, 256)

# Exact threshold arithmetic at tau=4 log H: r=e B/H^3 < 3B/H^3.
thresholds = []
for d in (2, 3):
    for m in (1, 2):
        qd, degree, labels = 3**d, 3**d-1, 3**(m**d)
        base = degree**2*labels
        h = 3*base*(qd+1)
        upper_r = F(3*base, h**3)
        assert upper_r <= F(1, qd+1)
        assert qd*upper_r/(1-upper_r) <= 1
        # The same root condition after cubing, independently of logarithms.
        assert h**3 >= 3*base*(qd+1)
        thresholds.append(dict(d=d, m=m, q=qd, B=base, H=h, r_upper=str(upper_r)))

output = dict(graph_cases=graph_cases, backgrounds=32, domains_per_background=len(domains),
              domain_checks=domain_checks, exact_log_coefficients=coefficient_checks,
              rational_log_tail_checks=tails, expansion_order=order,
              negative_checks=dict(repetition_degree2=str(single[2]),
                                   false_collar_incompatibility_gap='1/77',
                                   domain_dependent_activity_gap=str(domain_dependent_gap)),
              example=example, threshold_checks=thresholds,
              effective_nice=os.getpriority(os.PRIO_PROCESS, 0),
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              elapsed_seconds=time.monotonic()-start)
assert output['peak_rss_bytes'] < 1024**3
Path('cluster_checks.json').write_text(json.dumps(output, indent=2)+'\n')
print('All simple incompatibility graphs through five occurrences:', graph_cases)
print('Connected-edge sums = Penrose intervals; tree bound and sign passed.')
print('Exact fixed-background domain checks:', domain_checks)
print('Logarithm coefficients through degree six:', coefficient_checks)
print('Independent rational logarithm tail checks:', tails)
print('Nested supports, overlapping collars, repeated contours and same-support codes included.')
print('Negative tests: omitting repeats loses -w^2/2; false collar conflict loses 1/77.')
print('Domain-dependent activities change the linear logarithm coefficient by 1/256.')
print('Exact threshold checks:', len(thresholds))
print('Effective nice:', output['effective_nice'])
print('Peak RSS bytes:', output['peak_rss_bytes'])
print('Elapsed seconds:', output['elapsed_seconds'])
print('All checks passed.')
