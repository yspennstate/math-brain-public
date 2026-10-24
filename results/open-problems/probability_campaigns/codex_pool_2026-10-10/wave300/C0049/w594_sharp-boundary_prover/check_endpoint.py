"""Bounded, standard-library controls for the C0049 endpoint packet.

The analytic proof is in ATTEMPT.md. Floating-point controls are not certificates.
The FK enumeration below uses a synthetic bounded winding function, explicitly
not an FK exploration winding; it checks the change-of-measure/error inequality.
"""
from __future__ import annotations

import argparse
import cmath
import itertools
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def cluster_count(mask, edges, vertex_count, wired):
    parents = list(range(vertex_count))

    def find(a):
        while parents[a] != a:
            a = parents[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parents[b] = a

    for a in wired[1:]:
        union(wired[0], a)
    for j, (a, b) in enumerate(edges):
        if mask & (1 << j):
            union(a, b)
    return len({find(a) for a in range(vertex_count)})


def controls():
    result = {}
    # Gaussian-integer direction ratios: no trigonometric roundoff here.
    valid = invalid = 0
    for parity in (1, -1):
        phases = [parity, -parity, -parity * 1j, parity * 1j]
        for mask in itertools.product((0, 1), repeat=4):
            f = [x * y for x, y in zip(phases, mask)]
            residual = f[0] - f[1] - 1j * (f[2] - f[3])
            balanced = mask[0] + mask[1] == mask[2] + mask[3]
            if balanced:
                assert residual == 0
                valid += 1
            else:
                assert residual != 0  # malformed-path negative control
                invalid += 1
    result['flux'] = {'balanced_cases': valid, 'negative_controls': invalid,
                      'exact_residual_on_balanced_cases': 0}

    path_rows = []
    for n in (8, 16, 32, 64):
        points = [(j / n, (j % 2) / n) for j in range(-n, n + 1)]
        assert points[0] == (-1, 0) and points[-1] == (1, 0)
        worst = max(abs(y) for _, y in points)
        assert worst == 1 / n
        occupied = set(zip(points, points[1:]))
        assert len(occupied) == 2 * n
        # Independently assemble global occupation counts.
        flow = {}
        for a, b in occupied:
            flow[a] = flow.get(a, 0) - 1
            flow[b] = flow.get(b, 0) + 1
        assert all(flow.get(p, 0) == 0 for p in points[1:-1])
        path_rows.append({'n': n, 'edges': 2*n, 'uniform_distance_to_diameter': worst})
    result['deterministic_paths'] = path_rows

    # A 2x3 square-lattice graph; boundary wiring fixed across q.
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
    v, m = 6, len(edges)
    wired = (0, 1, 2)
    configurations = []
    for mask in range(1 << m):
        o = mask.bit_count()
        k = cluster_count(mask, edges, v, wired)
        # Synthetic W; proof of (E) applies to all bounded real functions.
        winding = (o - 3) * math.pi / 2
        indicator = bool(mask & 1)
        configurations.append((o, k, winding, indicator))
    n_bound = m + 2*v
    l_bound = max(abs(w) for _, _, w, _ in configurations)

    def expectation(h, f):
        # Direct p^o(1-p)^(m-o)q^k, rather than relative cosine weights.
        q = 4 * math.cos(math.pi*h/2)**2
        p = math.sqrt(q)/(1+math.sqrt(q))
        numerator = 0j
        denominator = 0.0
        for o, k, w, indicator in configurations:
            weight = p**o * (1-p)**(m-o) * q**k
            denominator += weight
            numerator += weight * f(w, indicator)
        return numerator/denominator

    g0 = expectation(0, lambda w, indicator: w*cmath.exp(1j*w)*indicator)
    rows = []
    for h in (1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/256):
        f_spin = expectation(h, lambda w, indicator: cmath.exp(1j*(1-h)*w)*indicator)
        f_one = expectation(h, lambda w, indicator: cmath.exp(1j*w)*indicator)
        d = (f_spin-f_one)/(-1j*h)
        error = abs(d-g0)
        bound = h*l_bound*l_bound/2 + l_bound*math.expm1(math.pi**2*n_bound*h*h/4)
        assert error <= bound + 1e-11
        rows.append({'h': h, 'actual_error': error, 'proved_bound': bound})
    result['finite_fk_measure'] = {
        'configurations': len(configurations), 'primal_edges': m, 'primal_vertices': v,
        'wiring': list(wired), 'N': n_bound, 'L': l_bound,
        'winding_kind': 'synthetic bounded function, not an exploration winding',
        'rows': rows,
        'before_error': rows[0]['actual_error'], 'after_error': rows[-1]['actual_error'],
        'error_reduction_factor': rows[0]['actual_error']/rows[-1]['actual_error']}

    ratio = math.sqrt(1+4/math.pi**2)
    winding_rows = []
    for n in (1, 2, 8, 32, 128):
        h, w = 1/(2*n), 2*math.pi*n
        d = (cmath.exp(-1j*h*w)-1)/(-1j*h)
        relative = abs(d-w)/abs(w)
        assert math.isclose(relative, ratio, abs_tol=1e-12)
        winding_rows.append({'n': n, 'h': h, 'relative_error': relative})
    result['nonuniform_winding'] = {'kind': 'abstract Dirac-law variables, not an FK family',
                                     'exact_relative_error': 'sqrt(1+4/pi^2)',
                                     'relative_error': ratio, 'rows': winding_rows}
    result['status'] = 'PASS'
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gate-receipt', type=Path, required=True)
    args = parser.parse_args()
    receipt = json.loads(args.gate_receipt.read_text(encoding='utf-8-sig'))
    age = time.time() - receipt['checked_at_epoch']
    if not receipt.get('allowed') or not (0 <= age <= 120):
        held = {'status': 'HELD', 'gate_age_seconds': age, 'gate_receipt': str(args.gate_receipt)}
        (ROOT/'measurements.json').write_text(json.dumps(held, indent=2), encoding='utf-8')
        print(json.dumps(held))
        return 2
    start = time.perf_counter()
    result = controls()
    result['seconds'] = time.perf_counter()-start
    result['command'] = f'python -X utf8 {__file__} --gate-receipt {args.gate_receipt}'
    result['gate_receipt'] = str(args.gate_receipt)
    result['gate_age_seconds'] = age
    (ROOT/'measurements.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
