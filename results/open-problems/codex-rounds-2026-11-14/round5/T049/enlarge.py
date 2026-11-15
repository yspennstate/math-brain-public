"""Exact square certificates enlarged by pendant lattice neighbors."""
import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from functools import lru_cache
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
signal.alarm(900)
START = time.monotonic()
HERE = Path(__file__).resolve().parent
R4 = Path('~/codex_op_1114r4/briefs/T049')
PATH = ((0, 1), (1, 2), (2, 3))
CYCLE = PATH+((0, 3),)


def merge(partition, a, b):
    x, y = partition[a], partition[b]
    names = {}
    return tuple(names.setdefault(x if z == y else z, len(names)) for z in partition)


@lru_cache(None)
def weighted_square(m, s):
    """Probability for Exp(s),Exp(m),Exp(m),Exp(m) root labels.

    Sum the probabilities of four possible final trees. The integer masks
    track accepted edges of one fixed tree, with independent exponential
    clocks of the indicated rates.
    """
    rates = (s, m, m, m)
    graph = [(a, b, 1) for a, b in CYCLE]+[(v, 4, rates[v]) for v in range(4)]
    answer = Q(0)
    for r in range(4):
        tree = list(PATH)+[(r, 4)]
        values = [Q(0)]*16
        values[15] = Q(1)
        for mask in range(14, -1, -1):
            p = tuple(range(5))
            for i, (a, b) in enumerate(tree):
                if mask >> i & 1:
                    p = merge(p, a, b)
            denominator = sum(rate for a, b, rate in graph if p[a] != p[b])
            values[mask] = sum((values[mask | (1 << i)] for i in range(4)
                                if not (mask >> i & 1)), Q(0))/denominator
        answer += rates[r]*values[0]
    return answer


def coefficients(m, k):
    """Survival expansion for m-k ordinary spokes and k two-stage branches."""
    result = Counter()
    for b in range(k+1):
        for c in range(k-b+1):
            result[m+m*b+(m+1)*c] += comb(k, b)*comb(k-b, c)*(-1)**c
    return {s: count for s, count in sorted(result.items()) if count}


def reduced_probability(m, k):
    return sum((coefficient*weighted_square(m, s)
                for s, coefficient in coefficients(m, k).items()), Q(0))


def direct_probability(m, k):
    """Independent recursion on successful partitions and leaf counts.

    Each unattached leaf has one edge to 0 and m+1 to the root. Once it
    attaches at one end, its remaining crossing edges have rate m+1 or 1.
    No effective-edge reduction or signed summation is used here.
    """
    r = m+1
    @lru_cache(None)
    def visit(p, u, a, b):
        if len(set(p[:4])) == 1:
            return Q(1)
        if p[0] == p[4] and (u or a or b):
            # These branches cannot change the square partition any longer.
            return visit(p, 0, 0, 0)
        rates = [m-k+(a*r+b if p[0] != p[4] else 0), m, m, m]
        denominator = sum(p[x] != p[y] for x, y in CYCLE)
        denominator += sum(rates[v] for v in range(4) if p[v] != p[4])
        denominator += u*(r+1) if p[0] != p[4] else 0
        numerator = sum((visit(merge(p, x, y), u, a, b) for x, y in PATH
                         if p[x] != p[y]), Q(0))
        # Every accepted non-path edge must avoid merging two square blocks.
        if all(p[v] != p[4] for v in range(4)):
            numerator += sum((rates[v]*visit(merge(p, v, 4), u, a, b)
                              for v in range(4) if rates[v]), Q(0))
        if u and p[0] != p[4]:
            numerator += u*visit(p, u-1, a+1, b)
            numerator += u*r*visit(p, u-1, a, b+1)
        return numerator/denominator
    answer = visit(tuple(range(5)), k, 0, 0)
    return answer, visit.cache_info().currsize


def geometry(d):
    origin = (0,)*d
    e1 = (1,)+(0,)*(d-1)
    ej = (0, 1)+(0,)*(d-2)
    opposite = tuple(a+b for a, b in zip(e1, ej))
    square = [origin, ej, opposite, e1]
    leaves = []
    for axis in range(d):
        for sign in (-1, 1):
            v = [0]*d
            v[axis] = sign
            v = tuple(v)
            if v not in square:
                leaves.append(v)
    q = square+leaves
    where = {x: i for i, x in enumerate(q)}
    internal = set()
    outside = []
    for i, x in enumerate(q):
        boundary = 0
        for axis in range(d):
            for sign in (-1, 1):
                y = list(x)
                y[axis] += sign
                j = where.get(tuple(y))
                if j is None:
                    boundary += 1
                else:
                    internal.add(tuple(sorted((i, j))))
        outside.append(boundary)
    m = 2*d-2
    assert len(leaves) == m and len(q) == 2*d+2
    assert internal == set(CYCLE) | {(0, i) for i in range(4, 4+m)}
    assert outside == [0, m, m, m]+[m+1]*m
    assert len(internal)+sum(outside) == 4+m+3*m+m*(m+1)
    return dict(d=d, vertices=q, internal=sorted(internal), spokes=outside,
                total_edges=len(internal)+sum(outside))


def usage():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    return dict(elapsed_seconds=time.monotonic()-START, peak_rss_bytes=rss,
                nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, alarm_seconds=900)


def decimal(x):
    with localcontext() as ctx:
        ctx.prec = 55
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def extend(last):
    previous = json.loads((R4/'extension.json').read_text())['rows']
    rows = []
    for old in previous:
        d = old['d']
        if d > last:
            break
        m = 2*d-2
        shape = geometry(d)
        probabilities = []
        states = []
        for k in range(m+1):
            by_reduction = reduced_probability(m, k)
            by_direct, state_count = direct_probability(m, k)
            assert by_reduction == by_direct, (d, k)
            assert 0 < by_reduction < 1
            if probabilities:
                assert probabilities[-1] < by_reduction
            probabilities.append(by_reduction)
            states.append(state_count)
        assert probabilities[1] == (weighted_square(m, m)+weighted_square(m, 2*m)
                                    -weighted_square(m, 2*m+1))
        previous_bound = Q(old['bound'])
        gain = 2*(d-1)*(probabilities[-1]-probabilities[0])
        bound = previous_bound+gain
        assert previous_bound < bound < 1
        row = dict(d=d, m=m, old_square_probability=str(probabilities[0]),
                   enlarged_square_probability=str(probabilities[-1]),
                   enlarged_square_decimal=decimal(probabilities[-1]),
                   probabilities_by_k=[str(p) for p in probabilities],
                   direct_recursion_states=states, previous_bound=str(previous_bound),
                   gain=str(gain), gain_decimal=decimal(gain), bound=str(bound),
                   bound_decimal=decimal(bound), geometry=shape,
                   signed_coefficients=coefficients(m, m))
        rows.append(row)
        (HERE/'extension.json').write_text(json.dumps(dict(status='RUNNING', rows=rows,
                                                         usage=usage()), indent=2)+'\n')
        print('d', d, 'k = 0,...,', m, 'both methods agree; max states', max(states), flush=True)
        print('square', row['enlarged_square_probability'], flush=True)
        print('gain', row['gain'], row['gain_decimal'], flush=True)
        print('bound', row['bound'], row['bound_decimal'], flush=True)
        print('usage', json.dumps(usage()), flush=True)
    result = dict(status='PASS', rows=rows, weighted_square_evaluations=weighted_square.cache_info().currsize,
                  usage=usage())
    (HERE/'extension.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', json.dumps(result['usage']), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--last', type=int, default=12)
    extend(parser.parse_args().last)
