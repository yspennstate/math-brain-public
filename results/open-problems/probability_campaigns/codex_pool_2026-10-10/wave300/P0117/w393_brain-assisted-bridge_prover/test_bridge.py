"""Small exact finite checks; these are not a proof of absence of bigeodesics."""
from fractions import Fraction
import heapq
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


def radius(v):
    return max(abs(v[0]), abs(v[1]))


def graph(n, weight):
    vertices = [(x, y) for x in range(-n, n + 1) for y in range(-n, n + 1)]
    adjacent = {v: [] for v in vertices}
    for u in vertices:
        for dx, dy in [(1, 0), (0, 1)]:
            v = (u[0] + dx, u[1] + dy)
            if v in adjacent:
                w = weight(u, v)
                assert w > 0
                adjacent[u].append((v, w))
                adjacent[v].append((u, w))
    return adjacent


def distances(adjacent, start):
    distance = {start: Fraction(0)}
    queue = [(Fraction(0), start)]
    while queue:
        d, u = heapq.heappop(queue)
        if d != distance[u]:
            continue
        for v, w in adjacent[u]:
            candidate = d + w
            if v not in distance or candidate < distance[v]:
                distance[v] = candidate
                heapq.heappush(queue, (candidate, v))
    return distance


def anchored_event(n, weight):
    adjacent = graph(n, weight)
    boundary = [v for v in adjacent if radius(v) == n]
    d0 = distances(adjacent, (0, 0))
    for i, x in enumerate(boundary):
        dx = distances(adjacent, x)
        for y in boundary[i + 1:]:
            # In positive weights, equality makes the concatenated minimizing
            # paths simple; a repeated vertex would yield a positive removable loop.
            if dx[y] == d0[x] + d0[y]:
                return True
    return False


def main():
    gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    if time.time() > gate['expires_unix']:
        raise RuntimeError('Compute gate expired; renew explicitly before this bounded run.')
    started = time.monotonic()
    cpu_started = time.process_time()
    rows = []
    for case in range(8):
        def weight(u, v):
            code = (u[0] + 5) * 71 + (u[1] + 5) * 29 + (v[0] + 5) * 13 + (v[1] + 5) * 7
            return Fraction(1 + (code * (case + 3) + case * 19) % 37)
        events = [anchored_event(n, weight) for n in (1, 2, 3)]
        assert not any(events[i + 1] and not events[i] for i in (0, 1))
        rows.append({'case': case, 'E1_E2_E3': events, 'nesting': 'pass'})
        if time.process_time() - cpu_started > gate['cpu_seconds']:
            raise RuntimeError('Compute gate CPU budget exceeded.')

    def ring_weight(u, v):
        return Fraction(1, 100) if radius(u) == radius(v) == 2 else Fraction(1)
    ring_events = [anchored_event(n, ring_weight) for n in (1, 2)]
    assert ring_events == [True, False]
    rows.append({'case': 'outer-cheap-ring', 'E1_E2': ring_events, 'kill': 'pass'})
    assert anchored_event(3, lambda u, v: Fraction(1))

    def expensive_origin(u, v):
        return Fraction(10) if (0, 0) in (u, v) else Fraction(1)
    negative_events = [anchored_event(n, expensive_origin) for n in (1, 2, 3)]
    assert negative_events == [False, False, False]
    rows.append({'case': 'expensive-origin', 'E1_E2_E3': negative_events})
    for M in (2, 3):
        def escaping_ring(u, v):
            return Fraction(1, 8 * M) if radius(u) == radius(v) == M else Fraction(1)
        actual = [anchored_event(n, escaping_ring) for n in (1, 2, 3)]
        expected = [n < M for n in (1, 2, 3)]
        assert actual == expected
        rows.append({'case': f'escaping-ring-M{M}', 'E1_E2_E3': actual,
                     'limit_interchange_counterexample': 'pass'})

    product = Fraction(1)
    for n in range(1, 101):
        product *= 1 - Fraction(1, (n + 1) ** 2)
        assert product == Fraction(n + 2, 2 * (n + 1))
    rows.append({'case': 'positive-hazard-counterexample', 'stages': 100,
                 'survival_exact': str(product), 'limiting_survival': '1/2'})
    # An unconditional product is invalid even for nested identical events.
    rows.append({'case': 'dependent-unconditional-product', 'P_intersection': '1/2',
                 'false_product_after_10': str(Fraction(1, 2 ** 10))})
    m = Fraction(1, 4)
    b1 = (m / 16) ** 16
    assert b1 == Fraction(1, 64 ** 16)
    rows.append({'case': 'uniform-ring-hazard', 'm': '1/4', 'first_hazard_exact': str(b1),
                 'first_hazard_float': float(b1), 'summability': 'eventually bounded by 2^(-8(n+1))'})
    result = {'status': 'pass', 'rows': rows, 'max_box_radius': 3,
              'max_vertices': 49, 'finite_nesting_implications_checked': 16,
              'elapsed_seconds': round(time.monotonic() - started, 6),
              'cpu_seconds': round(time.process_time() - cpu_started, 6),
              'scope': 'Finite exact checks and inference counterexamples, not an infinite FPP theorem.'}
    (ROOT / 'finite_checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
