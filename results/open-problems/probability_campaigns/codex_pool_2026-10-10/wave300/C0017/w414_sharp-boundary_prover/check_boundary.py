"""Small exact controls for the C0017 boundary counterexample; no simulation."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
MAX_CONFIGS = 50000
MAX_SECONDS = 45
TOTAL_CONFIGS = 0


def checkpoint():
    if time.monotonic() - START > MAX_SECONDS:
        raise RuntimeError('Small-check time budget exhausted; no larger run authorized.')


def fresh_gate():
    # This is a bounded CPU-only check, with a fresh resource snapshot and no
    # processes, workers, service changes, or accelerators. Fail closed if the
    # resource snapshot is unavailable. It grants no larger computation.
    import psutil
    cpu = psutil.cpu_percent(interval=1.0)
    memory = psutil.virtual_memory()
    gate = {
        'recorded_at': datetime.now(timezone.utc).isoformat(),
        'cpu_percent': cpu,
        'available_memory_bytes': memory.available,
        'limits': {'cpu_percent_max': 85, 'available_memory_min': 1073741824,
                   'enumerated_configurations_max': MAX_CONFIGS,
                   'wall_seconds_max': MAX_SECONDS, 'threads': 1},
        'purpose': 'Exact finite graph controls only, no simulation or training',
        'approved': cpu <= 85 and memory.available >= 1073741824,
    }
    (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2) + '\n', encoding='utf-8')
    if not gate['approved']:
        raise RuntimeError('Fresh resource gate declined the small computation.')
    return gate


def grid(n, a=None, b=None, m=None, extra=()):
    vertices = {(x, y) for x in range(n + 1) for y in range(n + 1)
                if a is None or x <= a or x >= b or y == m}
    vertices.update(extra)
    edges = []
    for x, y in sorted(vertices):
        for v in ((x + 1, y), (x, y + 1)):
            if v in vertices:
                edges.append(((x, y), v))
    return vertices, edges


def restricted(vertices, edges, predicate):
    subset = {v for v in vertices if predicate(v)}
    return subset, [e for e in edges if e[0] in subset and e[1] in subset]


def histogram(vertices, edges, sources, targets):
    global TOTAL_CONFIGS
    configurations = 1 << len(edges)
    if configurations > 32768 or TOTAL_CONFIGS + configurations > MAX_CONFIGS:
        raise RuntimeError('Exact-state gate exceeded; do not enlarge it.')
    TOTAL_CONFIGS += configurations
    adjacency = {v: [] for v in vertices}
    for i, (u, v) in enumerate(edges):
        adjacency[u].append((v, 1 << i))
        adjacency[v].append((u, 1 << i))
    successes = Counter()
    for mask in range(configurations):
        if mask % 256 == 0:
            checkpoint()
        seen = set(sources)
        stack = list(seen)
        hit = bool(seen & targets)
        while stack and not hit:
            u = stack.pop()
            for v, bit in adjacency[u]:
                if mask & bit and v not in seen:
                    if v in targets:
                        hit = True
                        break
                    seen.add(v)
                    stack.append(v)
        if hit:
            successes[mask.bit_count()] += 1
    return dict(successes), len(edges), configurations


def probability(hist, e, p):
    return sum((count * p**j * (1 - p)**(e - j) for j, count in hist.items()), Fraction(0))


def terminal_sets(vertices, n):
    return {v for v in vertices if v[0] == 0}, {v for v in vertices if v[0] == n}


def run():
    gate = fresh_gate()
    rows = []
    for n in (1, 2):
        vertices, edges = grid(n)
        sources, targets = terminal_sets(vertices, n)
        hist, e, configs = histogram(vertices, edges, sources, targets)
        q = probability(hist, e, Fraction(1, 2))
        if n == 1:
            assert q == Fraction(3, 4)
        rows.append({'case': f'canonical-square-{n}', 'edges': e,
                     'configurations': configs, 'probability_p_half': str(q),
                     'successful_configurations': sum(hist.values())})

    # Generic finite series graphs. These verify the exact factorization, not
    # the asymptotic theorem by extrapolation from small n.
    for n, a, b, m in ((2, 0, 2, 1), (3, 1, 3, 1)):
        vertices, edges = grid(n, a, b, m)
        sources, targets = terminal_sets(vertices, n)
        hist, e, configs = histogram(vertices, edges, sources, targets)
        lv, le = restricted(vertices, edges, lambda v: v[0] <= a)
        rv, re = restricted(vertices, edges, lambda v: v[0] >= b)
        lh, el, cl = histogram(lv, le, sources, {(a, m)})
        rh, er, cr = histogram(rv, re, {(b, m)}, targets)
        checks = []
        for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
            measured = probability(hist, e, p)
            factorized = p**(b - a) * probability(lh, el, p) * probability(rh, er, p)
            assert measured == factorized
            checks.append({'p': str(p), 'full_graph': str(measured),
                           'product': str(factorized), 'equal': True})
        rows.append({'case': f'series-neck-{n}-{a}-{b}-{m}',
                     'edges': e, 'corridor_edges': b - a, 'configurations': configs,
                     'successful_configurations_p_half': sum(hist.values()),
                     'probability_p_half': str(probability(hist, e, Fraction(1, 2))),
                     'chamber_configurations': cl + cr, 'checks': checks})

    # Bypass control: restoring one missing vertex creates a second row route.
    # It must invalidate the claim that the old two corridor edges are required.
    vertices, edges = grid(2, 0, 2, 1, extra=((1, 0),))
    sources, targets = terminal_sets(vertices, 2)
    hist, e, configs = histogram(vertices, edges, sources, targets)
    bypass_q = probability(hist, e, Fraction(1, 2))
    assert bypass_q > Fraction(1, 4)
    rows.append({'case': 'bypass-negative-control', 'edges': e,
                 'configurations': configs, 'probability_p_half': str(bypass_q),
                 'old_invalid_bound': '1/4', 'old_bound_fails': True})

    # Structural check on an actual member of the asymptotic family.
    n = 81
    t = math.isqrt(n)
    a, b, m = t, 2 * t + 1, n // 2
    vertices, edges = grid(n, a, b, m)
    assert (n + 1)**2 - len(vertices) == t * n
    for x in range(a, b):
        crosscut_edges = [edge for edge in edges
                         if edge[0][0] == x and edge[1][0] == x + 1]
        assert crosscut_edges == [((x, m), (x + 1, m))]
    rows.append({'case': 'actual-family-81-structure', 'vertices': len(vertices),
                 'edges': len(edges), 'removed_vertices': t * n,
                 'mandatory_single_edge_cuts': b - a, 'checks_passed': True})

    bounds = []
    for n in (81, 256, 10000, 1000000):
        t = math.isqrt(n)
        k = t + 1
        bounds.append({'n': n, 'corridor_edges': k,
                       'crossing_upper_bound': f'2^-{k}',
                       'crossing_upper_bound_float': math.ldexp(1.0, -k),
                       'closure_hausdorff_upper_bound': str(Fraction(k, 2 * n)),
                       'boundary_hausdorff_upper_bound': str(Fraction(2 * t + 1, n)),
                       'area_loss': str(Fraction(k * (n - 1), n * n)),
                       'marked_preimage_distance_upper_bound': str(Fraction(8, n)),
                       'type': 'computed analytic bound, not simulation'})
    result = {'recorded_at': datetime.now(timezone.utc).isoformat(),
              'command': "python -X utf8 ~/brain_workers/w414/check_boundary.py",
              'gate': gate, 'rows': rows, 'analytic_bounds': bounds,
              'enumerated_configurations': TOTAL_CONFIGS,
              'factorization_equalities_checked': 6,
              'elapsed_seconds': time.monotonic() - START,
              'scope': 'Exact finite controls and analytic bound evaluation; not a formal proof or a C0017 solution',
              'status': 'PASS'}
    (ROOT / 'MEASUREMENTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        result = {'status': 'DECLINED_OR_FAILED', 'error': str(exc),
                  'elapsed_seconds': time.monotonic() - START,
                  'enumerated_configurations': TOTAL_CONFIGS}
        (ROOT / 'CHECK_FAILURE.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        raise
