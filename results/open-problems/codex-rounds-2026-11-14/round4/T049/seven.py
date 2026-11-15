#!/usr/bin/env python3
"""Exact wired-path certificates. Standard library; no earlier code imported."""
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from math import comb
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
OLD = Path('~/codex_op_1114/briefs/T049')
ROUND3 = Path('~/codex_op_1114r3/briefs/T049')


def usage():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    return dict(peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-START,
                nice=os.getpriority(os.PRIO_PROCESS, 0), OMP_NUM_THREADS='1',
                alarm_seconds=600)


def save(name, data):
    (HERE/name).write_text(json.dumps(data, indent=2)+'\n')


def event_probability(n, edges, d):
    """Condition on the next accepted edge, tracking only successful partitions."""
    degree = Counter(v for edge in edges for v in edge)
    spokes = [2*d-degree[v] for v in range(n)]
    assert min(spokes) >= 0

    def join(p, a, b):
        x, y = p[a], p[b]
        names = {}
        return tuple(names.setdefault(x if z == y else z, len(names)) for z in p)

    @lru_cache(None)
    def visit(p):
        if len(set(p[:n])) == 1:
            return F(1)
        total = sum(p[a] != p[b] for a, b in edges)
        total += sum(spokes[v] for v in range(n) if p[v] != p[n])
        numerator = sum((visit(join(p, i, i+1)) for i in range(n-1)
                         if p[i] != p[i+1]), F(0))
        if all(p[v] != p[n] for v in range(n)):
            numerator += sum((spokes[v]*visit(join(p, v, n))
                              for v in range(n) if spokes[v]), F(0))
        return numerator/total

    result = visit(tuple(range(n+1)))
    return result, visit.cache_info().currsize


def fixed_tree_probability(n, edges, d):
    """Sum probabilities for each possible final tree over accepted-edge subsets."""
    degree = Counter(v for edge in edges for v in edge)
    spokes = [2*d-degree[v] for v in range(n)]
    answer = F(0)
    for root_at in range(n):
        if not spokes[root_at]:
            continue
        tree = [(i, i+1) for i in range(n-1)] + [(root_at, n)]
        dp = [F(0)]*(1 << n)
        dp[-1] = F(1)
        for mask in range((1 << n)-2, -1, -1):
            parent = list(range(n+1))

            def find(a):
                while parent[a] != a:
                    a = parent[a]
                return a

            for i, (a, b) in enumerate(tree):
                if mask & (1 << i):
                    parent[find(a)] = find(b)
            labels = [find(a) for a in range(n+1)]
            denominator = sum(labels[a] != labels[b] for a, b in edges)
            denominator += sum(spokes[v] for v in range(n)
                               if labels[v] != labels[n])
            dp[mask] = sum((dp[mask | (1 << i)] for i in range(n)
                            if not mask & (1 << i)), F(0))/denominator
        answer += spokes[root_at]*dp[0]
    return answer


def recheck():
    square = ((0, 1), (1, 2), (2, 3), (0, 3))
    comparisons = 0
    for row in json.loads((OLD/'data.json').read_text())['rows']:
        d = row['d']
        p, _ = event_probability(4, square, d)
        assert p == F(row['plaquette_probability'])
        assert F(1, d)+2*(d-1)*p == F(row['connectivity_lower_bound'])
        comparisons += 1
    cycle = tuple([(i, i+1) for i in range(5)] + [(0, 5)])
    graphs = dict(C=cycle, A=cycle+((1, 4),), B=cycle+((0, 3),))
    rows = []
    for row in json.loads((ROUND3/'extension.json').read_text())['rows']:
        d = row['d']
        p4, _ = event_probability(4, square, d)
        probs = {}
        for name, graph in graphs.items():
            p, states = event_probability(6, graph, d)
            assert p == F(row['probabilities'][name])
            assert p == fixed_tree_probability(6, graph, d)
            probs[name] = p
            comparisons += 1
        bound = F(1, d)+2*(d-1)*p4
        bound += 4*(d-1)*(d-2)*probs['C']
        bound += 2*(d-1)*(2*d-3)*probs['A']
        bound += 4*(d-1)*(2*d-3)*probs['B']
        assert bound == F(row['bound'])
        rows.append(dict(d=d, bound=str(bound)))
        print('recheck d', d, 'bound', bound, flush=True)
    out = dict(status='PASS', probability_comparisons=comparisons,
               rows=rows, usage=usage())
    save('recheck.json', out)
    print('PASS: 11 square and 33 six-vertex probabilities; all 11 bounds')
    print(json.dumps(out['usage']))


def walks(d, length):
    """Reachability-pruned lattice DFS, with exact length and no repeated vertices."""
    origin = (0,)*d
    target = (1,)+(0,)*(d-1)
    current = [origin]
    seen = {origin}

    def visit(left):
        v = current[-1]
        distance = sum(abs(x-y) for x, y in zip(v, target))
        if distance > left or (left-distance) % 2:
            return
        if left == 0:
            if v == target:
                yield tuple(current)
            return
        for axis in range(d):
            for sign in (-1, 1):
                w = tuple(x+(sign if j == axis else 0) for j, x in enumerate(v))
                if w in seen or (w == target and left != 1):
                    continue
                if v == origin and w == target:
                    continue
                seen.add(w)
                current.append(w)
                yield from visit(left-1)
                current.pop()
                seen.remove(w)
    yield from visit(length)


def induced(path):
    return tuple((a, b) for a, b in combinations(range(len(path)), 2)
                 if sum(abs(x-y) for x, y in zip(path[a], path[b])) == 1)


def signature(edges, n):
    forward = tuple(sorted(edges))
    backward = tuple(sorted((n-1-b, n-1-a) for a, b in edges))
    return min(forward, backward)


def transverse_support(path):
    return sum(any(v[j] for v in path) for j in range(1, len(path[0])))


def enumerate_graphs():
    tables = {}
    representatives = {}
    for k in (1, 2, 3):
        counter = Counter()
        total = 0
        for path in walks(k+1, 7):
            total += 1
            if transverse_support(path) != k:
                continue
            graph = signature(induced(path), 8)
            counter[graph] += 1
            representatives.setdefault(graph, path)
        tables[k] = counter
        print('enumeration ambient d', k+1, 'all paths', total,
              'using all transverse axes', sum(counter.values()), flush=True)
    graphs = sorted(set().union(*(set(c) for c in tables.values())))
    rows = []
    for i, graph in enumerate(graphs):
        rows.append(dict(id='G%02d' % (i+1), internal=graph,
                         support_counts=[tables[k][graph] for k in (1, 2, 3)],
                         representative=representatives[graph]))
    save('graphs.json', dict(status='PASS', graphs=rows,
                            support_totals=[sum(tables[k].values()) for k in (1, 2, 3)],
                            usage=usage()))
    print('induced graphs up to path reversal:', len(rows))
    print(json.dumps(usage()))


def extend():
    data = json.loads((HERE/'graphs.json').read_text())
    previous = json.loads((ROUND3/'extension.json').read_text())['rows']
    rows = []
    for old in previous:
        d = old['d']
        by_graph = []
        for graph in data['graphs']:
            counts = graph['support_counts']
            count = sum(comb(d-1, k)*counts[k-1] for k in (1, 2, 3) if k <= d-1)
            if count == 0:
                continue
            edges = [tuple(e) for e in graph['internal']]
            p, states = event_probability(8, edges, d)
            alternate = fixed_tree_probability(8, edges, d)
            assert p == alternate
            assert p > F(1, comb(16*d-len(edges), 7))
            by_graph.append(dict(id=graph['id'], count=count, probability=str(p),
                                 contribution=str(count*p), states=states))
        gain = sum((F(g['contribution']) for g in by_graph), F(0))
        bound = F(old['bound'])+gain
        assert F(old['bound']) < bound < 1
        row = dict(d=d, path_count=sum(g['count'] for g in by_graph),
                   previous_bound=old['bound'], gain=str(gain), bound=str(bound),
                   decimal=float(bound), graphs=by_graph)
        rows.append(row)
        # Checkpoint after every completed dimension.
        save('extension.json', dict(status='RUNNING', rows=rows, usage=usage()))
        print('d', d, 'paths', row['path_count'], 'types', len(by_graph), flush=True)
        print('gain', gain, 'bound', bound, format(float(bound), '.15f'), flush=True)
    save('extension.json', dict(status='PASS', rows=rows, usage=usage()))
    print('PASS: every seven-edge detour; both exact probability calculations agree')
    print(json.dumps(usage()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['recheck', 'enumerate', 'extend'])
    args = parser.parse_args()
    dict(recheck=recheck, enumerate=enumerate_graphs, extend=extend)[args.mode]()
