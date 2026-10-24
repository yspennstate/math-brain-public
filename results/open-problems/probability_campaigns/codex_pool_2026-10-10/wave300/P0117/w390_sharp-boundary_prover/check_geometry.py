"""Small exact graph checks of the saved proof; not a formal infinite-volume proof."""
from __future__ import annotations

import argparse
import datetime as dt
from fractions import Fraction
import heapq
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def requirements(A: int, w: int, m: int):
    expensive = {edge((x, y), (x + 1, y)) for x in range(A, A + m) for y in range(-w, w + 1)}
    cheap = {edge((x, w + 1), (x + 1, w + 1)) for x in range(A, A + m)}
    cheap |= {edge((x, y), (x, y + 1)) for x in (A, A + m) for y in range(-w, w + 1)}
    return expensive, cheap


def shortest_from(source, w, m, low, high, *, outside_row):
    ymax = w + int(outside_row)
    dist = {source: 0}
    queue = [(0, source)]
    while queue:
        cost, u = heapq.heappop(queue)
        if cost != dist[u]:
            continue
        x, y = u
        for v in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if not (0 <= v[0] <= m and -w <= v[1] <= ymax):
                continue
            # Independent graph oracle: interior horizontal edges are high;
            # vertical and bypass-row edges are low.
            weight = high if v[1] == y and -w <= y <= w else low
            candidate = cost + weight
            if candidate < dist.get(v, math.inf):
                dist[v] = candidate
                heapq.heappush(queue, (candidate, v))
    return dist


def run_checks():
    started = time.perf_counter()
    cpu_started = time.process_time()
    endpoint_pairs = 0
    geometry_patterns = 0
    probability_coefficient_checks = 0
    overlap_negative_controls = 0
    samples = []
    for low, high in ((0, 1), (1, 2), (5, 7)):
        K = Fraction(1) + Fraction(4 * low, high - low)
        for w in range(65):
            m = ((4 * w + 2) * low) // (high - low) + 1
            assert m * (high - low) > (4 * w + 2) * low
            assert m <= K * (w + 1)
            assert m * (2 * w + 1) <= 2 * K * (w + 1) ** 2
            assert m + 4 * w + 2 <= (K + 4) * (w + 1) ** 2
            probability_coefficient_checks += 1
        for w in range(4):
            m = ((4 * w + 2) * low) // (high - low) + 1
            expensive, cheap = requirements(0, w, m)
            assert len(expensive) == m * (2 * w + 1)
            assert len(cheap) == m + 4 * w + 2
            assert not expensive & cheap
            later_high, later_low = requirements(m + 1, w, m)
            assert not (expensive | cheap) & (later_high | later_low)
            bad_high, bad_low = requirements(m, w, m)
            assert (expensive | cheap) & (bad_high | bad_low)
            overlap_negative_controls += 1
            geometry_patterns += 1
            for y in range(-w, w + 1):
                inside = shortest_from((0, y), w, m, low, high, outside_row=False)
                outside = shortest_from((0, y), w, m, low, high, outside_row=True)
                for z in range(-w, w + 1):
                    cost_inside = inside[(m, z)]
                    cost_outside = outside[(m, z)]
                    bypass_bound = (m + 2 * (w + 1) - y - z) * low
                    assert cost_inside >= m * high
                    assert cost_outside <= bypass_bound
                    assert cost_outside < cost_inside
                    endpoint_pairs += 1
            samples.append({'low': low, 'high': high, 'w': w, 'm': m,
                            'expensive_edges': len(expensive), 'cheap_edges': len(cheap),
                            'minimum_certified_cost_gain': m * (high - low) - (4 * w + 2) * low})
            if time.process_time() - cpu_started > 3:
                raise RuntimeError('Three-second CPU budget exceeded; no broader computation is authorized.')
    # Constant-law negative control: the ambient graph retains horizontal geodesics.
    for w in range(4):
        d = shortest_from((0, 0), w, 7, 1, 1, outside_row=True)
        assert d[(7, 0)] == 7
    C_uniform = 37 * math.log(4)
    return {'status': 'PASS', 'endpoint_pair_checks': endpoint_pairs,
            'geometry_patterns': geometry_patterns,
            'probability_coefficient_checks': probability_coefficient_checks,
            'overlap_negative_controls': overlap_negative_controls,
            'constant_law_negative_controls': 4,
            'uniform_1_2_example': {'l': 1.25, 'h': 1.75, 'p_l': .25, 'p_h': .25,
                                  'K': 11, 'C': C_uniform, 'sufficient_tube_coefficient': 1 / math.sqrt(C_uniform)},
            'wall_seconds_internal': time.perf_counter() - started,
            'cpu_seconds': time.process_time() - cpu_started, 'samples': samples,
            'formal_proof': False,
            'limits': 'Finite deterministic checks complement the written proof and do not establish the infinite-volume theorem by themselves.'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--gate-receipt', type=Path, required=True)
    a = p.parse_args()
    gate = json.loads(a.gate_receipt.read_text(encoding='utf-8'))
    if gate.get('permit') is not True:
        p.error('The fresh resource gate did not permit these checks.')
    stamp = dt.datetime.fromisoformat(gate['at_utc'])
    if (dt.datetime.now(dt.timezone.utc) - stamp).total_seconds() > 60:
        p.error('Gate receipt is older than 60 seconds; obtain a fresh one.')
    result = run_checks()
    result['gate_receipt'] = str(a.gate_receipt)
    result['at_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    output = ROOT / 'reports' / 'geometry_checks.json'
    output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'samples'}, indent=2))


if __name__ == '__main__':
    main()
