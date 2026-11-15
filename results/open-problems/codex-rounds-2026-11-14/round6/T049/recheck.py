"""Independent tree-route integration of the earlier finite certificates."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(600)
START = time.monotonic()
HERE = Path(__file__).resolve().parent
BASE = Path('~')
R1 = BASE/'codex_op_1114/briefs/T049'
R3 = BASE/'codex_op_1114r3/briefs/T049'
R4 = BASE/'codex_op_1114r4/briefs/T049'
R5 = BASE/'codex_op_1114r5/briefs/T049'


def tree_integral(edges, tree_ids):
    """Exponential cycle inequalities; sum all order simplices by suffix DP."""
    count = len(tree_ids)
    adj = [[] for _ in range(count+1)]
    for bit, i in enumerate(tree_ids):
        a, b, _ = edges[i]
        adj[a].append((b, bit))
        adj[b].append((a, bit))

    def route(a, b):
        stack = [(a, -1, 0)]
        while stack:
            x, parent, mask = stack.pop()
            if x == b:
                return mask
            stack.extend((y, x, mask | (1 << bit)) for y, bit in adj[x]
                         if y != parent)
        raise AssertionError('not a spanning tree')

    constraints = [(route(a, b), rate) for i, (a, b, rate) in enumerate(edges)
                   if i not in tree_ids]
    rates = [edges[i][2] for i in tree_ids]
    density = 1
    for rate in rates:
        density *= rate
    dp = [F(1)]+[F(0)]*((1 << count)-1)
    for mask in range(1, 1 << count):
        denominator = sum(rates[i] for i in range(count) if mask >> i & 1)
        denominator += sum(rate for bits, rate in constraints if bits & mask)
        dp[mask] = sum((dp[mask ^ (1 << i)] for i in range(count)
                        if mask >> i & 1), F(0))/denominator
    return density*dp[-1]


def path_probability(n, internal, d):
    degrees = Counter(v for e in internal for v in e)
    edges = [(i, i+1, 1) for i in range(n-1)]
    edges += [(a, b, 1) for a, b in internal if b != a+1]
    value = F(0)
    for r in range(n):
        rate = 2*d-degrees[r]
        if not rate:
            continue
        graph = edges+[(r, n, rate)]
        graph += [(v, n, 2*d-degrees[v]) for v in range(n)
                  if v != r and 2*d-degrees[v]]
        value += tree_integral(graph, tuple(range(n-1))+(len(edges),))
    return value


def pendant_probability(m, k):
    root = 4+k
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)]
    edges += [(0, v, 1) for v in range(4, root)]
    spokes = [m-k, m, m, m]+[m+1]*k
    edges += [(v, root, rate) for v, rate in enumerate(spokes) if rate]
    lookup = {(a, b): i for i, (a, b, _) in enumerate(edges)}
    result = F(0)
    trees = 0
    for r in range(4):
        if not spokes[r]:
            continue
        for bits in product((0, 1), repeat=k):
            ids = (0, 1, 2, lookup[r, root])+tuple(
                lookup[v, root] if bits[v-4] else lookup[0, v]
                for v in range(4, root))
            result += tree_integral(edges, ids)
            trees += 1
    for bridge in range(4, root):
        others = [v for v in range(4, root) if v != bridge]
        for bits in product((0, 1), repeat=k-1):
            ids = (0, 1, 2, lookup[0, bridge], lookup[bridge, root])+tuple(
                lookup[v, root] if bit else lookup[0, v]
                for v, bit in zip(others, bits))
            result += tree_integral(edges, ids)
            trees += 1
    return result, trees


def usage():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    return dict(seconds=time.monotonic()-START, peak_rss_bytes=rss,
                nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, deadline=600)


def main():
    old_square = json.loads((R1/'data.json').read_text())['rows']
    old_five = json.loads((R3/'extension.json').read_text())['rows']
    old_seven = json.loads((R4/'extension.json').read_text())['rows']
    old_enlarged = json.loads((R5/'extension.json').read_text())['rows']
    graphs = json.loads((R4/'graphs.json').read_text())['graphs']
    square = [(0, 1), (1, 2), (2, 3), (0, 3)]
    cycle6 = [(i, i+1) for i in range(5)]+[(0, 5)]
    comparisons = 0
    for a, b, c, e in zip(old_square, old_five, old_seven, old_enlarged):
        d = a['d']
        q = path_probability(4, square, d)
        assert q == F(a['plaquette_probability']) == F(e['old_square_probability'])
        baseline = F(1, d)+2*(d-1)*q
        assert baseline == F(a['connectivity_lower_bound'])
        comparisons += 1
        counts = dict(C=4*(d-1)*(d-2), A=2*(d-1)*(2*d-3), B=4*(d-1)*(2*d-3))
        for name, chords in [('C', []), ('A', [(1, 4)]), ('B', [(0, 3)])]:
            p = path_probability(6, cycle6+chords, d)
            assert p == F(b['probabilities'][name])
            comparisons += 1
            baseline += counts[name]*p
        assert baseline == F(b['bound'])
        for item in c['graphs']:
            g = next(g for g in graphs if g['id'] == item['id'])
            p = path_probability(8, list(map(tuple, g['internal'])), d)
            assert p == F(item['probability'])
            baseline += item['count']*p
            comparisons += 1
        assert baseline == F(c['bound']) == F(e['previous_bound'])
        assert baseline+2*(d-1)*(F(e['enlarged_square_probability'])-q) == F(e['bound'])
        print('d', d, 'all earlier path probabilities and sums PASS', flush=True)
    checks = []
    for row in old_enlarged[:2]:
        for k, expected in enumerate(row['probabilities_by_k']):
            probability, trees = pendant_probability(row['m'], k)
            assert probability == F(expected)
            checks.append(dict(d=row['d'], k=k, trees=trees, probability=str(probability)))
            print('enlarged full graph d', row['d'], 'k', k, 'trees', trees,
                  probability, 'PASS', flush=True)
    assert comparisons == 202
    out = dict(status='PASS', earlier_path_comparisons=comparisons,
               enlarged_full_graph_checks=checks, usage=usage())
    (HERE/'recheck.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', json.dumps(out['usage']))


if __name__ == '__main__':
    main()
