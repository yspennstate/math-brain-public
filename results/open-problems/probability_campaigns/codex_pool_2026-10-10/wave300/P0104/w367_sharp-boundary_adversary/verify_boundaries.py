"""Small exact checks for w367's proof and the deterministic paths in w366-C1.

This is an arithmetic/finite-graph receipt, not a formal theorem certificate.
No imports from live code, no network, no store writes, no child processes.
"""
from datetime import datetime, timezone
from fractions import Fraction
from heapq import heappop, heappush
from itertools import combinations
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
MAX_CONFIGURATIONS = 2500
WALL_LIMIT_SECONDS = 10


def rectangle_edges(n):
    return ([((x, 0), (x + 1, 0)) for x in range(n)]
            + [((x, 1), (x + 1, 1)) for x in range(n)]
            + [((x, 0), (x, 1)) for x in range(n + 1)])


def shortest_cost(n, edges, weights):
    adj = {v: [] for e in edges for v in e}
    for (u, v), w in zip(edges, weights):
        adj[u].append((v, w))
        adj[v].append((u, w))
    distances = {(0, 0): 0}
    heap = [(0, (0, 0))]
    while heap:
        cost, u = heappop(heap)
        if cost != distances[u]:
            continue
        if u == (n, 0):
            return cost
        for v, w in adj[u]:
            new_cost = cost + w
            if new_cost < distances.get(v, float('inf')):
                distances[v] = new_cost
                heappush(heap, (new_cost, v))
    raise AssertionError('Disconnected rectangle')


def path_edges(turns):
    result = []
    for u, v in zip(turns, turns[1:]):
        assert (u[0] == v[0]) != (u[1] == v[1])
        step = ((v[0] > u[0]) - (v[0] < u[0]),
                (v[1] > u[1]) - (v[1] < u[1]))
        while u != v:
            w = (u[0] + step[0], u[1] + step[1])
            result.append(tuple(sorted((u, w))))
            u = w
    return result


def main():
    started = time.perf_counter()
    cpu_started = time.process_time()
    cases = [(1, Fraction(2)), (1, Fraction(5, 2)),
             (2, Fraction(1)), (2, Fraction(3, 2)),
             (3, Fraction(2, 3)), (3, Fraction(3, 4))]
    expected_total = sum(2 ** len(rectangle_edges(n)) for n, _ in cases)
    assert expected_total <= MAX_CONFIGURATIONS
    gate = {'created_utc': datetime.now(timezone.utc).isoformat(),
            'kind': 'bounded exact arithmetic, not a heavy compute run',
            'planned_configurations': expected_total,
            'configuration_cap': MAX_CONFIGURATIONS,
            'wall_limit_seconds': WALL_LIMIT_SECONDS,
            'local_gpu': False, 'training': False, 'child_processes': False,
            'gate_scope': 'Fresh local bounds for this exact diagnostic; not a shared-governor receipt.'}
    (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
    graph_results = []
    total = 0
    for n, epsilon in cases:
        edges = rectangle_edges(n)
        m = len(edges)
        count = 2 ** m
        direct_failures = 0
        sum_cost = 0
        sum_square = 0
        witness = None
        denominator = epsilon.denominator
        for mask in range(count):
            assert total < MAX_CONFIGURATIONS
            assert time.perf_counter() - started < WALL_LIMIT_SECONDS
            weights = [denominator + epsilon.numerator * ((mask >> i) & 1)
                       for i in range(m)]
            direct = sum(weights[:n])
            shortest = shortest_cost(n, edges, weights)
            assert shortest <= direct
            if shortest < direct:
                direct_failures += 1
                if witness is None:
                    witness = {'mask': mask, 'weights_scaled': weights,
                               'scale': denominator,
                               'straight_cost': str(Fraction(direct, denominator)),
                               'shortest_cost': str(Fraction(shortest, denominator))}
            sum_cost += shortest
            sum_square += shortest ** 2
            total += 1
        variance = (Fraction(sum_square, count * denominator ** 2)
                    - Fraction(sum_cost, count * denominator) ** 2)
        threshold_holds = n * epsilon <= 2
        if threshold_holds:
            assert direct_failures == 0
            assert variance == n * epsilon ** 2 / 4  # Bernoulli endpoint law
        else:
            assert direct_failures > 0
        graph_results.append({'n': n, 'epsilon': str(epsilon), 'states': count,
                              'threshold_holds': threshold_holds,
                              'straight_path_failures': direct_failures,
                              'exact_bernoulli_passage_variance': str(variance),
                              'first_counterexample': witness})

    # Independent integration of continuous one-edge first and second moments.
    uniform_results = []
    for n in (1, 2, 8, 27, 1000, 1000000):
        epsilon = Fraction(1, n)
        first = 1 + epsilon / 2
        second = 1 + epsilon + epsilon ** 2 / 3
        sum_second = n * second + n * (n - 1) * first ** 2
        variance = sum_second - (n * first) ** 2
        assert variance == n * epsilon ** 2 / 12
        edge_variance = epsilon ** 2 / 12
        normalized = variance / edge_variance
        assert normalized == n
        uniform_results.append({'n': n, 'epsilon': str(epsilon),
                                'exact_passage_variance': str(variance),
                                'variance_divided_by_edge_variance': str(normalized),
                                'ratio_to_normalized_n_two_thirds': n ** (1 / 3)})

    peer_paths = []
    for n in (1, 2, 3, 17):
        turns = [[(0, 0), (n, 0)],
                 [(0, 0), (0, 1), (n, 1), (n, 0)],
                 [(0, 0), (0, -1), (n, -1), (n, 0)],
                 [(0, 0), (-1, 0), (-1, 2), (n + 1, 2), (n + 1, 0), (n, 0)]]
        paths = [path_edges(t) for t in turns]
        assert [len(p) for p in paths] == [n, n + 2, n + 2, n + 8]
        for left, right in combinations(paths, 2):
            assert set(left).isdisjoint(right)
        peer_paths.append({'n': n, 'lengths': [len(p) for p in paths],
                           'pairwise_edge_intersections': [0] * 6})

    receipt = {'result': 'PASS', 'command': 'python -X utf8 verify_boundaries.py',
               'configurations_checked': total, 'graph_cases': graph_results,
               'continuous_uniform_moment_checks': uniform_results,
               'w366_fixed_path_checks': peer_paths,
               'wall_seconds': time.perf_counter() - started,
               'cpu_seconds': time.process_time() - cpu_started,
               'limits': ['Finite rectangles supply checks and counterexample witnesses only.',
                          'The full-lattice theorem uses the separate length/parity proof.',
                          'No formal checker, no KPZ exponent, no fixed-law asymptotic claim.']}
    (ROOT / 'VERIFICATION.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps({'result': receipt['result'], 'configurations': total,
                      'cpu_seconds': receipt['cpu_seconds'],
                      'wall_seconds': receipt['wall_seconds'],
                      'straight_path_failures': [r['straight_path_failures'] for r in graph_results]}))


if __name__ == '__main__':
    main()
