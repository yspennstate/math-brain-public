"""Full-graph recursion, explicit cycle integrals and integer arithmetic audit."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, product
import json
from math import gcd, lcm, prod
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


def graph(m, k):
    n = 4+k
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)]
    edges += [(0, i, 1) for i in range(4, n)]
    edges += [(v, n, rate) for v, rate in enumerate([m-k]+[m]*3+[m+1]*k) if rate]
    return n, edges


def full_event(m, k):
    n, edges = graph(m, k)
    def join(p, x, y):
        old, new = p[y], p[x]
        return tuple(new if label == old else label for label in p)
    @lru_cache(None)
    def visit(p):
        if len(set(p[:4])) == 1:
            return Q(1)
        square_blocks = set(p[:4])
        denominator = 0
        numerator = Q(0)
        for edge_id, (a, b, rate) in enumerate(edges):
            if p[a] == p[b]:
                continue
            denominator += rate
            if edge_id < 3 or not (p[a] in square_blocks and p[b] in square_blocks):
                numerator += rate*visit(join(p, a, b))
        return numerator/denominator
    result = visit(tuple(range(n+1)))
    return result, visit.cache_info().currsize


def final_trees(m, k):
    n, edges = graph(m, k)
    edge_ids = {(a, b): i for i, (a, b, rate) in enumerate(edges)}
    leaf_a = [edge_ids[0, i] for i in range(4, n)]
    leaf_b = [edge_ids[i, n] for i in range(4, n)]
    # One direct core-root edge, each leaf attached on exactly one side.
    for v in range(4):
        if (v, n) not in edge_ids:
            continue
        for choices in product((0, 1), repeat=k):
            yield (0, 1, 2, edge_ids[v, n])+tuple(
                leaf_b[i] if bit else leaf_a[i] for i, bit in enumerate(choices))
    # One bridging leaf, every other leaf attached on exactly one side.
    for bridge in range(k):
        others = [i for i in range(k) if i != bridge]
        for choices in product((0, 1), repeat=k-1):
            yield (0, 1, 2, leaf_a[bridge], leaf_b[bridge])+tuple(
                leaf_b[i] if bit else leaf_a[i] for i, bit in zip(others, choices))


def cycle_integrals(m, k):
    """All tree shapes and all label-order simplices on the unreduced graph."""
    n, edges = graph(m, k)
    answer = Q(0)
    simplex_count = tree_count = 0
    seen = set()
    for ids in final_trees(m, k):
        assert len(ids) == n
        assert frozenset(ids) not in seen
        seen.add(frozenset(ids))
        tree_count += 1
        adjacency = [[] for _ in range(n+1)]
        for bit, i in enumerate(ids):
            a, b, rate = edges[i]
            adjacency[a].append((b, bit))
            adjacency[b].append((a, bit))
        def route(a, b):
            queue = [(a, -1, 0)]
            for v, parent, mask in queue:
                if v == b:
                    return mask
                queue.extend((w, v, mask | (1 << bit)) for w, bit in adjacency[v]
                             if w != parent)
            raise AssertionError('disconnected final tree')
        constraints = [(route(a, b), rate) for i, (a, b, rate) in enumerate(edges)
                       if i not in ids]
        denominators = [0]*(1 << n)
        rates = [edges[i][2] for i in ids]
        for mask in range(1, 1 << n):
            denominators[mask] = sum(rate for i, rate in enumerate(rates) if mask >> i & 1)
            denominators[mask] += sum(rate for path, rate in constraints if path & mask)
        products = Counter()
        for order in permutations(range(n)):
            mask = (1 << n)-1
            denominator = 1
            for i in order:
                denominator *= denominators[mask]
                mask ^= 1 << i
            products[denominator] += 1
            simplex_count += 1
        rate_product = prod(rates)
        answer += sum((Q(rate_product*count, denominator)
                       for denominator, count in products.items()), Q(0))
    return answer, tree_count, simplex_count


def add_integers(pairs):
    denominator = lcm(*(b for a, b in pairs))
    numerator = sum(a*(denominator//b) for a, b in pairs)
    divisor = gcd(numerator, denominator)
    return numerator//divisor, denominator//divisor


def rational_pair(value):
    parts = value.split('/')
    return int(parts[0]), int(parts[1]) if len(parts) > 1 else 1


def main():
    data = json.loads((HERE/'extension.json').read_text())
    assert data['status'] == 'PASS'
    generic_checks = []
    integral_checks = []
    for row in data['rows'][:2]:
        m = row['m']
        for k, expected in enumerate(row['probabilities_by_k']):
            actual, states = full_event(m, k)
            assert actual == Q(expected)
            generic_checks.append(dict(d=row['d'], k=k, states=states))
        actual, trees, simplices = cycle_integrals(m, m)
        assert actual == Q(row['enlarged_square_probability'])
        integral_checks.append(dict(d=row['d'], probability=str(actual), trees=trees,
                                    simplices=simplices))
        print('full graph d', row['d'], 'all k generic recursion PASS;', trees,
              'trees and', simplices, 'cycle integrals PASS', flush=True)

    integer_checks = []
    for row in data['rows']:
        m = row['m']
        a, b = rational_pair(row['enlarged_square_probability'])
        c, d = rational_pair(row['old_square_probability'])
        gain = add_integers([(m*a, b), (-m*c, d)])
        assert '%s/%s' % gain == row['gain']
        bound = add_integers([rational_pair(row['previous_bound']), gain])
        assert '%s/%s' % bound == row['bound']
        coefficients = {int(s): count for s, count in row['signed_coefficients'].items()}
        assert sum(coefficients.values()) == 1
        assert sum(s*count for s, count in coefficients.items()) == 0  # no direct spoke at 0
        # At q=1/2, check the survival polynomial with integers only.
        degree = max(coefficients)
        expanded = sum(c*(2**(degree-s)) for s, c in coefficients.items())
        # (q+q^(m+1)-q^(m+2))^m, with common denominator 2^degree.
        base_numerator = 2**(m+1)+1
        base_denominator_exponent = m+2
        assert degree == m*(m+2)
        assert expanded == base_numerator**m
        integer_checks.append(dict(d=row['d'], gain=list(gain), bound=list(bound)))
    print('integer LCM/GCD sums and signed-survival checks: 11/11 PASS', flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    out = dict(status='PASS', generic_checks=generic_checks, integral_checks=integral_checks,
               integer_checks=integer_checks,
               usage=dict(elapsed_seconds=time.monotonic()-START, peak_rss_bytes=rss,
                          nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, alarm_seconds=900))
    (HERE/'audit.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', json.dumps(out['usage']))


if __name__ == '__main__':
    main()
