"""Exact wired square certificates using both endpoint neighborhoods."""
import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(900)
START = time.monotonic()
HERE = Path(__file__).resolve().parent
R5 = Path('~/codex_op_1114r5/briefs/T049')


def geometry(d, both=True):
    o = (0,)*d
    v = (1,)+(0,)*(d-1)
    a = (0, 1)+(0,)*(d-2)
    b = (1, 1)+(0,)*(d-2)
    vertices = [o, a, b, v]
    for endpoint in (o, v) if both else (o,):
        for axis in range(d):
            for sign in (-1, 1):
                x = list(endpoint)
                x[axis] += sign
                x = tuple(x)
                if x not in vertices:
                    vertices.append(x)
    internal = [(i, j) for i in range(len(vertices)) for j in range(i+1, len(vertices))
                if sum(abs(x-y) for x, y in zip(vertices[i], vertices[j])) == 1]
    degree = Counter(x for edge in internal for x in edge)
    spokes = [2*d-degree[i] for i in range(len(vertices))]
    path = [(0, 1), (1, 2), (2, 3)]
    edges = [(x, y, 1) for x, y in path]
    edges += [(x, y, 1) for x, y in internal if (x, y) not in path]
    edges += [(i, len(vertices), k) for i, k in enumerate(spokes) if k]
    m = 2*d-2
    if both:
        assert len(vertices) == 2*m+4 == 4*d
        assert len(internal) == 4+2*m+(m-1) == 3*m+3
        assert spokes[:4] == [0, m, m, 0]
        assert Counter(spokes[4:]) == {m: 2*(m-1), m+1: 2}
        assert len(internal)+sum(spokes) == 2*m*m+5*m+5
    else:
        assert spokes == [0, m, m, m]+[m+1]*m
    return dict(d=d, vertices=vertices, internal=internal, spokes=spokes,
                edges=edges, root=len(vertices), total_original_edges=len(internal)+sum(spokes))


def probability(shape, max_states=300000):
    """Kruskal recursion; fail on a non-path merge of two core blocks."""
    edges = shape['edges']
    calls = 0

    def merge(p, a, b):
        old, new = p[b], p[a]
        names = {}
        return tuple(names.setdefault(new if x == old else x, len(names)) for x in p)

    @lru_cache(None)
    def visit(p):
        nonlocal calls
        calls += 1
        if calls > max_states:
            raise RuntimeError('state cap reached')
        if len(set(p[:4])) == 1:
            return F(1)
        if calls % 1000 == 0:
            assert usage()['peak_rss_bytes'] < 768*1024**2
        terminals = set(p[:4])
        denominator = 0
        numerator = F(0)
        transitions = Counter()
        for i, (a, b, rate) in enumerate(edges):
            if p[a] == p[b]:
                continue
            denominator += rate
            if i < 3 or not (p[a] in terminals and p[b] in terminals):
                transitions[merge(p, a, b)] += rate
        for q, rate in transitions.items():
            numerator += rate*visit(q)
        return numerator/denominator

    result = visit(tuple(range(shape['root']+1)))
    return result, visit.cache_info().currsize


def usage():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    return dict(seconds=time.monotonic()-START, peak_rss_bytes=rss,
                nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, deadline=900)


def decimal(x):
    with localcontext() as c:
        c.prec = 65
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main(last):
    old_rows = json.loads((R5/'extension.json').read_text())['rows']
    rows = []
    for d in range(2, last+1):
        old = next(row for row in old_rows if row['d'] == d)
        previous, old_states = probability(geometry(d, False))
        assert previous == F(old['enlarged_square_probability'])
        shape = geometry(d)
        p, states = probability(shape)
        assert previous < p < F(1, 4)
        gain = (2*d-2)*(p-previous)
        bound = F(old['bound'])+gain
        assert F(old['bound']) < bound < 1
        row = dict(d=d, square_probability=str(p), square_decimal=decimal(p),
                   previous_square=str(previous), previous_bound=old['bound'],
                   gain=str(gain), gain_decimal=decimal(gain), bound=str(bound),
                   bound_decimal=decimal(bound), states=states,
                   previous_states=old_states, geometry=shape)
        rows.append(row)
        out = dict(status='RUNNING', rows=rows, usage=usage())
        (HERE/'extension.json').write_text(json.dumps(out, indent=2)+'\n')
        print('d', d, 'states', states, 'old states', old_states, flush=True)
        for name in ('square_probability', 'square_decimal', 'gain', 'gain_decimal', 'bound', 'bound_decimal'):
            print(name, row[name], flush=True)
        print('usage', json.dumps(usage()), flush=True)
    out['status'] = 'PASS'
    out['usage'] = usage()
    (HERE/'extension.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', json.dumps(out['usage']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--last', type=int, default=3)
    main(parser.parse_args().last)
