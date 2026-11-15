"""Independent exact Bernstein replay of the proposed q=3 derivative covers."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

import sympy as sp


ROOT = Path('~/brain_workers')
REPORT = ROOT / 'w682/checks/softmax_derivative_v1/report.json'
HERE = ROOT / 'w683'
u, v, t = sp.symbols('u v t')
variables = (u, v, t)


def exact(x):
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def bernstein_coeffs(expr, degrees):
    power = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    terms = {tuple(k): exact(a) for k, a in power.terms()}
    assert all(e <= n for k in terms for e, n in zip(k, degrees))
    result = {}
    for k in product(*(range(n + 1) for n in degrees)):
        result[k] = sum(
            (a * Fraction(
                comb(k[0], e[0]) * comb(k[1], e[1]) * comb(k[2], e[2]),
                comb(degrees[0], e[0]) * comb(degrees[1], e[1]) * comb(degrees[2], e[2]),
            ) for e, a in terms.items() if all(e[j] <= k[j] for j in range(3))),
            Fraction(0),
        )
    return result, terms


def split_half(coeffs, degrees, axis, bit):
    n = degrees[axis]
    output = {}
    other = [j for j in range(3) if j != axis]
    for a in range(degrees[other[0]] + 1):
        for b in range(degrees[other[1]] + 1):
            keys = []
            for i in range(n + 1):
                k = [0, 0, 0]
                k[axis], k[other[0]], k[other[1]] = i, a, b
                keys.append(tuple(k))
            row = [coeffs[k] for k in keys]
            left = [row[0]]
            right = [row[-1]]
            while len(row) > 1:
                row = [(row[i] + row[i + 1]) / 2 for i in range(len(row) - 1)]
                left.append(row[0])
                right.append(row[-1])
            selected = left if bit == '0' else right[::-1]
            for k, val in zip(keys, selected):
                output[k] = val
    return output


def polynomials(direction):
    p = [u, (1 - u) * v, (1 - u) * (1 - v)]
    h = [0, t, 1] if direction == 'endpoint' else [t, 0, 1]
    mean = sum(p[i] * h[i] for i in range(3))
    centered = [h[i] - mean for i in range(3)]
    moments = [None] + [sum(p[i] * centered[i] ** order for i in range(3))
                        for order in range(1, 5)]
    d2 = p[0] * (centered[0] ** 2 - moments[2])
    d3 = p[0] * (centered[0] ** 3 - 3 * centered[0] * moments[2] - moments[3])
    d4 = p[0] * (centered[0] ** 4 - 6 * centered[0] ** 2 * moments[2]
                 - 4 * centered[0] * moments[3] + 6 * moments[2] ** 2 - moments[4])
    norm = sp.Rational(2, 3) * (1 - t + t * t)
    return {
        'D2_-1': norm / 5 - d2,
        'D2_+1': norm / 5 + d2,
        'D4_-1': 3 * norm ** 2 / 5 - d4,
        'D4_+1': 3 * norm ** 2 / 5 + d4,
        'D3_squared': 4 * norm ** 3 / 25 - d3 ** 2,
    }


def main():
    report = json.loads(REPORT.read_text(encoding='utf-8'))
    polys = {name: polynomials(name) for name in ('endpoint', 'middle')}
    results = []
    for job in report['jobs']:
        name = job['name']
        family, suffix = name.split('_', 1)
        degrees = tuple(int(n) - 1 for n in job['shape'])
        root, power = bernstein_coeffs(polys[family][suffix], degrees)
        stored = {tuple(e): Fraction(a) for e, a in job['root_power_terms']}
        assert power == stored, name
        paths = [leaf['path'] for leaf in job['leaves']]
        assert all(not b.startswith(a) for i, a in enumerate(paths)
                   for j, b in enumerate(paths) if i != j)
        assert sum((Fraction(1, 2 ** len(path)) for path in paths), Fraction(0)) == 1
        low = None
        zero = 0
        count = 0
        for path in paths:
            coeffs = root
            for depth, bit in enumerate(path):
                coeffs = split_half(coeffs, degrees, depth % 3, bit)
            minimum = min(coeffs.values())
            if minimum < 0:
                raise AssertionError((name, path, minimum))
            low = minimum if low is None else min(low, minimum)
            zero += sum(a == 0 for a in coeffs.values())
            count += len(coeffs)
        results.append({'job': name, 'leaves': len(paths), 'coefficients': count,
                        'minimum': str(low), 'zeros': zero})
    receipt = {'report_sha256': hashlib.sha256(REPORT.read_bytes()).hexdigest(),
               'jobs': results, 'total_leaves': sum(r['leaves'] for r in results),
               'all_exact_nonnegative': True,
               'method': 'Own Sympy centered moments, direct Fraction power-to-Bernstein and midpoint subdivisions'}
    destination = HERE / 'checks/t067_softmax_own.json'
    destination.write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps({'receipt': str(destination), 'jobs': len(results),
                      'leaves': receipt['total_leaves'],
                      'minima': [r['minimum'] for r in results]}))


if __name__ == '__main__':
    main()
