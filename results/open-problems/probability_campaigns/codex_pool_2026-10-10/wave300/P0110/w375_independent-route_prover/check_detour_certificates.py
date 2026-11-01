"""Small exact certificates; refuse numerical work unless the live compute gate is clear."""
from __future__ import annotations

import heapq
import itertools
import json
import math
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE = Path('~/.claude/compute/compute_state.json')


def fresh_gate():
    now = time.time()
    receipt = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
               'state_path': str(STATE), 'workload': 'single-thread exact finite graph checks; no models, GPU, random sampling or network',
               'allowed': False, 'checks_started': False}
    try:
        d = json.loads(STATE.read_text(encoding='utf-8-sig'))
        stamp = datetime.fromisoformat(d['ts'])
        age = now - stamp.timestamp()
        for key in ('ts', 'status', 'mode', 'reasons', 'cpu_pct', 'mem_load_pct',
                    'mem_avail_mb', 'commit_used_pct', 'commit_eff_used_pct',
                    'commit_avail_mb', 'commit_eff_avail_mb', 'disk_free_gb', 'hung_windows'):
            if key in d:
                receipt[key] = d[key]
        receipt['age_s'] = age
        issues = []
        if not 0 <= age <= 60:
            issues.append('telemetry stale or future')
        if d.get('status') not in ('ok', 'warn') or d.get('mode') == 'throttle':
            issues.append('live governor holds new numerical work')
        for key, ceiling in (('cpu_pct', 85), ('mem_load_pct', 85), ('commit_used_pct', 85), ('commit_eff_used_pct', 85)):
            v = d.get(key)
            if not isinstance(v, (int, float)) or not math.isfinite(v) or v >= ceiling:
                issues.append(f'{key} unavailable or pressured')
        for key, floor in (('mem_avail_mb', 8192), ('commit_avail_mb', 16384), ('commit_eff_avail_mb', 16384), ('disk_free_gb', 5)):
            v = d.get(key)
            if not isinstance(v, (int, float)) or not math.isfinite(v) or v <= floor:
                issues.append(f'{key} unavailable or insufficient')
        if d.get('hung_windows'):
            issues.append('hung windows present')
        receipt['issues'] = issues
        receipt['allowed'] = not issues
    except Exception as exc:
        receipt['issues'] = [f'gate unavailable: {type(exc).__name__}']
    (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    return receipt


def edge(u, v):
    return tuple(sorted((u, v)))


def path_edges(vertices):
    return [edge(u, v) for u, v in zip(vertices, vertices[1:])]


def axial_paths(k, start=0):
    axis = [(start + i, 0) for i in range(k + 1)]
    detour = [(start, 0)] + [(start + i, 1) for i in range(k + 1)] + [(start + k, 0)]
    return axis, detour


def dijkstra(weights, start, end):
    graph = {}
    for (u, v), w in weights.items():
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
    distance = {start: F(0)}
    previous = {}
    heap = [(F(0), start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if cost != distance[u]:
            continue
        if u == end:
            route = [end]
            while route[-1] != start:
                route.append(previous[route[-1]])
            return cost, list(reversed(route))
        for v, w in graph[u]:
            new = cost + w
            if v not in distance or new < distance[v]:
                distance[v] = new
                previous[v] = u
                heapq.heappush(heap, (new, v))
    raise AssertionError('no path')


def monotone_dp(weights, n):
    dp = {(0, 0): F(0)}
    for y in range(n + 1):
        for x in range(n + 1):
            if x == y == 0:
                continue
            terms = []
            if x:
                terms.append(dp[(x - 1, y)] + weights[edge((x - 1, y), (x, y))])
            if y:
                terms.append(dp[(x, y - 1)] + weights[edge((x, y - 1), (x, y))])
            dp[(x, y)] = min(terms)
    return dp[(n, n)]


def exact_cycle_enumeration(k, high):
    axis, detour = axial_paths(k)
    aa, bb = path_edges(axis), path_edges(detour)
    assert set(aa).isdisjoint(bb)
    savings = F(0)
    strict = 0
    count = 0
    for config in itertools.product((1, high), repeat=2 * k + 2):
        weights = dict(zip(aa + bb, map(F, config)))
        unrestricted, route = dijkstra(weights, axis[0], axis[-1])
        axial = sum(weights[e] for e in aa)
        detoured = sum(weights[e] for e in bb)
        assert unrestricted == min(axial, detoured)
        assert len(route) == len(set(route))
        difference = axial - unrestricted
        assert difference >= 0
        savings += difference
        strict += int(difference > 0)
        count += 1
    # A separate binomial aggregation verifies the exhaustive graph computation.
    total = F(0)
    for i in range(k + 1):
        for j in range(k + 3):
            s = k + (high - 1) * i
            h = k + 2 + (high - 1) * j
            total += math.comb(k, i) * math.comb(k + 2, j) * max(0, s - h)
    assert savings == total
    return {'k': k, 'law': [1, high], 'configurations': count,
            'strict_detour_configurations': strict, 'mean_saving': str(savings / count)}


def run_checks():
    results = []
    for k, high, expected_strict, expected_saving in ((1, 2, 0, F(0)), (2, 2, 0, F(0)), (3, 2, 1, F(1, 256)), (2, 3, 1, F(1, 32))):
        row = exact_cycle_enumeration(k, high)
        assert row['strict_detour_configurations'] == expected_strict
        assert F(row['mean_saving']) == expected_saving
        results.append(row)
    axis, detour = axial_paths(2)
    aa, bb = path_edges(axis), path_edges(detour)
    weights = {e: F(3) for e in aa} | {e: F(1) for e in bb}
    shortest, route = dijkstra(weights, (0, 0), (2, 0))
    assert shortest == 4 and sum(weights[e] for e in aa) == 6
    results.append({'certificate': 'axial', 'directed_cost': '6', 'unrestricted_subgraph_cost': str(shortest), 'route': route})
    all_low = {e: F(1) for e in aa + bb}
    assert dijkstra(all_low, (0, 0), (2, 0))[0] == 2
    results.append({'control': 'constant weights', 'directed_cost': '2', 'unrestricted_cost': '2'})
    # The weak-disorder threshold is checked with exact fractions, not fitted exponents.
    for epsilon in map(F, ('1', '1/2', '1/10', '1/100')):
        n = int(2 / epsilon) + 1
        margin = n * epsilon - 2
        eta = margin / (4 * n + 4)
        low, high = 1 + eta, 1 + epsilon - eta
        axis, detour = axial_paths(n)
        aa, bb = path_edges(axis), path_edges(detour)
        weights = {e: high for e in aa} | {e: low for e in bb}
        before = n * high
        after, _ = dijkstra(weights, (0, 0), (n, 0))
        assert before - after == margin / 2 > 0
        assert (n - 1) * epsilon <= 2
        results.append({'epsilon': str(epsilon), 'first_possible_integer_n': n,
                        'directed_cost': str(before), 'detour_cost': str(after), 'strict_gap': str(before - after)})
    n, low, high = 11, F(5, 4), F(7, 4)
    weights = {}
    high_edges = set()
    low_edges = set()
    for x in range(n):
        for y in range(n + 1):
            high_edges.add(edge((x, y), (x + 1, y)))
    for x in range(n):
        for y in range(n):
            high_edges.add(edge((x, y), (x, y + 1)))
    for y in range(n):
        low_edges.add(edge((n, y), (n, y + 1)))
    for x in range(n):
        low_edges.add(edge((x, -1), (x + 1, -1)))
    low_edges |= {edge((0, 0), (0, -1)), edge((n, -1), (n, 0))}
    assert high_edges.isdisjoint(low_edges)
    assert len(high_edges) == 253 and len(low_edges) == 24
    weights.update({e: high for e in high_edges})
    weights.update({e: low for e in low_edges})
    before = monotone_dp(weights, n)
    after, route = dijkstra(weights, (0, 0), (n, n))
    assert before == 33 and after == 30
    assert len(route) == len(set(route)) and (0, -1) in route
    robust_directed_lower = n * high + n * F(1)
    assert robust_directed_lower - (2 * n + 2) * low == F(1, 4)
    results.append({'certificate': 'diagonal', 'directed_cost': str(before), 'unrestricted_subgraph_cost': str(after),
                    'robust_interval_gap': '1/4', 'high_edge_count': 253, 'low_edge_count': 24})
    all_used_edges = set()
    for j in range(5):
        axis, detour = axial_paths(2, 3 * j)
        block = set(path_edges(axis) + path_edges(detour)) | {edge((3 * j + 2, 0), (3 * j + 3, 0))}
        assert all_used_edges.isdisjoint(block)
        all_used_edges.update(block)
    results.append({'certificate': 'five independent block geometries', 'blocks': 5,
                    'mean_block_cost_with_connector': '191/32', 'axial_time_constant_upper_bound': '191/96',
                    'mean_directed_edge_cost': '2', 'strict_per_edge_gap': '1/96'})
    return results


def main():
    receipt = fresh_gate()
    if not receipt['allowed']:
        result = {'status': 'BLOCKED_BY_FRESH_GATE', 'checks_started': False,
                  'passed': False, 'issues': receipt['issues']}
        (ROOT / 'CERTIFICATE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(result))
        return 3
    started = time.perf_counter()
    try:
        rows = run_checks()
        result = {'status': 'PASS', 'checks_started': True, 'passed': True,
                  'finite_scope_only': True, 'elapsed_s': time.perf_counter() - started, 'rows': rows}
    except Exception as exc:
        result = {'status': 'FAIL', 'checks_started': True, 'passed': False,
                  'failure': f'{type(exc).__name__}: {exc}'}
    (ROOT / 'CERTIFICATE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
