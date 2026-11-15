"""Independent final-tree enumeration and exact cycle-inequality integration."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
import json
from math import factorial, gcd, lcm
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(900)
HERE = Path(__file__).resolve().parent
START = time.monotonic()


def usage():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 768*1024**2
    return dict(seconds=time.monotonic()-START, peak_rss_bytes=rss,
                nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, deadline=900)


def local_patterns():
    # Contract the desired core path to C=0; R=1, x=2, y=3.
    graph = [(0, 2), (2, 3), (3, 0), (2, 1), (3, 1)]
    def roots(ids):
        parent = list(range(4))
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for i in ids:
            a, b = map(find, graph[i])
            if a == b:
                return None
            parent[a] = b
        return tuple(find(v) for v in range(4))
    forests, trees = [], []
    for ids in combinations(range(5), 2):
        p = roots(ids)
        if p is not None and p[0] != p[1] and all(x in p[:2] for x in p[2:]):
            forests.append(ids)
    for ids in combinations(range(5), 3):
        p = roots(ids)
        if p is not None and len(set(p)) == 1:
            trees.append(ids)
    assert len(forests) == len(trees) == 8
    return forests, trees


def module_graph(d):
    """Build the graph independently from its branch decomposition."""
    m = 2*d-2
    pairs = m-1
    root = 6+2*pairs
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1),
             (1, root, m), (2, root, m)]
    singles = []
    for endpoint, leaf in ((0, 4), (3, 5)):
        singles.append((len(edges), len(edges)+1))
        edges.extend([(endpoint, leaf, 1), (leaf, root, m+1)])
    modules = []
    for j in range(pairs):
        x, y = 6+2*j, 7+2*j
        modules.append(tuple(range(len(edges), len(edges)+5)))
        edges.extend([(0, x, 1), (x, y, 1), (y, 3, 1),
                      (x, root, m), (y, root, m)])
    return edges, singles, modules, root


def multisets(patterns, count):
    for ids in combinations_with_replacement(range(len(patterns)), count):
        multiplicity = factorial(count)
        for repetitions in Counter(ids).values():
            multiplicity //= factorial(repetitions)
        yield tuple(patterns[i] for i in ids), multiplicity


def all_tree_groups(d):
    forests, bridges = local_patterns()
    edges, singles, modules, root = module_graph(d)
    L = len(modules)
    grouped = {}
    reflected_local = (2, 1, 0, 4, 3)

    def emit(direct, tails, patterns, multiplicity):
        key = (direct, tuple(tails), tuple(sorted(patterns)))
        reflected = (3-direct if direct >= 0 else -1, tuple(reversed(tails)),
                     tuple(sorted(tuple(sorted(reflected_local[i] for i in p))
                                  for p in patterns)))
        key = min(key, reflected)
        if key in grouped:
            grouped[key][1] += multiplicity
            return
        ids = [0, 1, 2]
        if direct >= 0:
            ids.append(3+direct)  # direct=1 or 2 -> edge 4 or 5
        for tail, options in zip(tails, singles):
            ids.extend(options[i] for i in tail)
        for pattern, options in zip(patterns, modules):
            ids.extend(options[i] for i in pattern)
        assert len(ids) == root and len(set(ids)) == root
        # Every enumerated edge set is a spanning tree, independently checked.
        parent = list(range(root+1))
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for i in ids:
            a, b = map(find, edges[i][:2])
            assert a != b
            parent[a] = b
        assert len({find(v) for v in range(root+1)}) == 1
        grouped[key] = [tuple(ids), multiplicity]

    # A direct core-root edge is the unique bridge between the two terminals.
    for patterns, multiplicity in multisets(forests, L):
        for direct in (1, 2):
            for left, right in product((0, 1), repeat=2):
                emit(direct, ((left,), (right,)), patterns, multiplicity)
        # Or one unmatched leaf is the unique bridge.
        for which in (0, 1):
            for other in (0, 1):
                tails = ((0, 1), (other,)) if which == 0 else ((other,), (0, 1))
                emit(-1, tails, patterns, multiplicity)
    # Or one matched pair supplies the unique bridge.
    for remaining, multiplicity in multisets(forests, L-1):
        for bridge in bridges:
            for left, right in product((0, 1), repeat=2):
                emit(-1, ((left,), (right,)), (bridge,)+remaining, L*multiplicity)
    count = sum(x[1] for x in grouped.values())
    assert count == (12+4*L)*8**L
    return edges, list(grouped.values()), count


def integral(edges, tree):
    """Independent exponential density integral using route masks and zeta sums."""
    n = len(tree)
    adj = [[] for _ in range(n+1)]
    rates = []
    for bit, i in enumerate(tree):
        a, b, rate = edges[i]
        rates.append(rate)
        adj[a].append((b, bit))
        adj[b].append((a, bit))
    size = 1 << n
    route_sums = [0]*size
    total = 0
    tree_set = set(tree)
    for i, (a, b, rate) in enumerate(edges):
        if i in tree_set:
            continue
        queue = [(a, -1, 0)]
        for v, parent, mask in queue:
            if v == b:
                route_sums[mask] += rate
                total += rate
                break
            queue.extend((w, v, mask | (1 << bit)) for w, bit in adj[v] if w != parent)
        else:
            raise AssertionError('missing tree route')
    # route_sums[M] becomes the total rate of constraints with route inside M.
    for bit in range(n):
        step = 1 << bit
        for low in range(0, size, 2*step):
            for mask in range(low+step, low+2*step):
                route_sums[mask] += route_sums[mask-step]
    rate_sum = [0]*size
    values = [F(1)]+[F(0)]*(size-1)
    full = size-1
    for mask in range(1, size):
        least = mask & -mask
        rate_sum[mask] = rate_sum[mask ^ least]+rates[least.bit_length()-1]
        denominator = rate_sum[mask]+total-route_sums[full ^ mask]
        subtotal = F(0)
        bits = mask
        while bits:
            least = bits & -bits
            subtotal += values[mask ^ least]
            bits ^= least
        values[mask] = subtotal/denominator
    density = 1
    for rate in rates:
        density *= rate
    return density*values[-1]


def add_integer_fractions(terms):
    denominator = lcm(*(x.denominator for x in terms))
    numerator = sum(x.numerator*(denominator//x.denominator) for x in terms)
    g = gcd(numerator, denominator)
    return F(numerator//g, denominator//g)


def geometry_check(row):
    shape = row['geometry']
    points = list(map(tuple, shape['vertices']))
    where = {p: i for i, p in enumerate(points)}
    edges, spokes = set(), []
    d = row['d']
    for i, p in enumerate(points):
        outside = 0
        for axis in range(d):
            for sign in (-1, 1):
                q = list(p)
                q[axis] += sign
                j = where.get(tuple(q))
                if j is None:
                    outside += 1
                else:
                    edges.add(tuple(sorted((i, j))))
        spokes.append(outside)
    assert edges == set(map(tuple, shape['internal']))
    assert spokes == shape['spokes']
    assert len(edges)+sum(spokes) == shape['total_original_edges']
    # Degree and edge counts after grouping parallel root edges match the
    # separately constructed module graph, including both unmatched leaves.
    module_edges, _, _, root = module_graph(d)
    assert len(points) == root
    assert Counter(rate for a, b, rate in module_edges if b == root) == Counter(x for x in spokes if x)
    assert len(edges) == sum(b != root for a, b, rate in module_edges)


def main():
    data = json.loads((HERE/'extension.json').read_text())
    results = []
    for row in data['rows']:
        d = row['d']
        geometry_check(row)
        edges, groups, tree_count = all_tree_groups(d)
        print('d', d, 'labelled tree shapes', tree_count, 'integral groups', len(groups), flush=True)
        total = F(0)
        group_results = []
        for j, (tree, multiplicity) in enumerate(groups, 1):
            p = integral(edges, tree)
            assert p > 0
            total += multiplicity*p
            group_results.append(dict(tree=tree, multiplicity=multiplicity, probability=str(p)))
            if j % 100 == 0 or j == len(groups):
                progress = dict(d=d, completed=j, groups=len(groups), usage=usage())
                (HERE/'audit_progress.json').write_text(json.dumps(progress, indent=2)+'\n')
                print('integrated', j, '/', len(groups), json.dumps(usage()), flush=True)
        assert total == F(row['square_probability']), (d, total, row['square_probability'])
        gain = add_integer_fractions([(2*d-2)*total, -(2*d-2)*F(row['previous_square'])])
        bound = add_integer_fractions([gain, F(row['previous_bound'])])
        assert str(gain) == row['gain'] and str(bound) == row['bound']
        with localcontext() as context:
            context.prec = 80
            dec = str(Decimal(bound.numerator)/Decimal(bound.denominator))
        assert dec[:60] == row['bound_decimal'][:60]
        results.append(dict(d=d, tree_count=tree_count, integral_groups=len(groups),
                            probability=str(total), gain=str(gain), bound=str(bound),
                            groups=group_results))
        (HERE/'audit.json').write_text(json.dumps(dict(status='RUNNING', rows=results,
                                                       usage=usage()), indent=2)+'\n')
        print('d', d, 'exact integral, integer sums and geometry PASS', flush=True)
    out = dict(status='PASS', rows=results, usage=usage())
    (HERE/'audit.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', json.dumps(out['usage']))


if __name__ == '__main__':
    main()
