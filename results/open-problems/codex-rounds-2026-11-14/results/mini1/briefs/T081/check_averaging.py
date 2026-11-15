#!/usr/bin/env python3
"""Exact integration over shifted-grid cells; standard library only."""
import itertools
import json
import math
import os
import resource
import signal
from fractions import Fraction as Q
from pathlib import Path


def timeout(signum, frame):
    raise TimeoutError('60 second checker limit')


signal.signal(signal.SIGALRM, timeout)
signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def tent(z):
    return math.prod(max(Q(0), 1 - abs(v)) for v in z)


def kernel(r, side):
    z = tuple(v / side for v in r)
    same = tent(z)
    adjacent = Q(0)
    for axis in range(len(r)):
        for sign in (-1, 1):
            delta = list(z)
            delta[axis] -= sign
            adjacent += tent(delta)
    return same, adjacent


def integrate(points, side=Q(1), core=Q(1, 10)):
    """Integrate exactly on all rectangular intervals between shift breakpoints.

    The weight is recorded as a polynomial in q=exp(beta*j), with j=1.
    Forbidden shifts have weight zero and are recorded separately.
    """
    dim = len(points[0])
    axes = []
    for axis in range(dim):
        cuts = sorted({Q(0), side} | {p[axis] % side for p in points})
        axes.append([(left, right) for left, right in zip(cuts, cuts[1:])])
    moments = {'same': Q(0), 'adjacent': Q(0)}
    poly = {}
    forbidden = Q(0)
    for rect in itertools.product(*axes):
        shift = tuple((lo + hi) / 2 for lo, hi in rect)
        mass = math.prod((hi - lo) / side for lo, hi in rect)
        boxes = [tuple((v - t) // side for v, t in zip(p, shift)) for p in points]
        exponent = 0
        bad = False
        for i in range(len(points)):
            for k in range(i):
                distance = sum(abs(a - b) for a, b in zip(boxes[i], boxes[k]))
                same = distance == 0
                adjacent = distance == 1
                moments['same'] += mass * same
                moments['adjacent'] += mass * adjacent
                if same:
                    sqdist = sum((a - b) ** 2 for a, b in zip(points[i], points[k]))
                    bad |= sqdist < core ** 2
                exponent += same or adjacent
        if bad:
            forbidden += mass
        else:
            poly[exponent] = poly.get(exponent, Q(0)) + mass
    assert sum(poly.values(), forbidden) == 1
    return poly, moments, forbidden


def multiply(p, r):
    out = {}
    for i, a in p.items():
        for k, b in r.items():
            out[i + k] = out.get(i + k, Q(0)) + a * b
    return out


def evaluate(p, q):
    return sum(coefficient * q ** degree for degree, coefficient in p.items())


def serial_poly(p):
    return {str(k): str(v) for k, v in sorted(p.items())}


def zero(dim):
    return (Q(0),) * dim


data = {'kernel_checks': [], 'configurations': [], 'n_pair_checks': []}
kernel_count = 0
for dim in (2, 3):
    for side in (Q(1), Q(2)):
        values = [Q(-5, 2), Q(-3, 2), Q(-1, 2), Q(0), Q(1, 2), Q(3, 2), Q(5, 2)]
        for z in itertools.product(values, repeat=dim):
            r = tuple(side * v for v in z)
            _, moments, _ = integrate([zero(dim), r], side)
            same, adjacent = kernel(r, side)
            assert moments['same'] == same
            assert moments['adjacent'] == adjacent
            data['kernel_checks'].append({'d': dim, 'L': str(side), 'r': list(map(str, r)),
                                          'same': str(same), 'adjacent': str(adjacent)})
            kernel_count += 1

for dim in (2, 3):
    for side in (Q(1), Q(2)):
        a0 = zero(dim)
        a1 = (3 * side / 2,) + (Q(0),) * (dim - 1)
        pair, _, bad = integrate([a0, a1], side)
        assert bad == 0 and pair == {0: Q(1, 2), 1: Q(1, 2)}
        product = multiply(pair, pair)
        assert product == {0: Q(1, 4), 1: Q(1, 2), 2: Q(1, 4)}
        for separation in (3, 7, 100):
            for offset in (Q(0), side / 2):
                delta = (offset, separation * side) + (Q(0),) * (dim - 2)
                b0 = tuple(v + t for v, t in zip(a0, delta))
                b1 = tuple(v + t for v, t in zip(a1, delta))
                joint, _, bad = integrate([a0, a1, b0, b1], side)
                assert bad == 0
                expected = {0: Q(1, 2), 2: Q(1, 2)} if offset == 0 else {1: Q(1)}
                assert joint == expected
                for x in (a0, a1):
                    for y in (b0, b1):
                        cross, _, forbidden = integrate([x, y], side)
                        assert cross == {0: Q(1)} and forbidden == 0
                # An independent Bernoulli-variance calculation at q=2,3,5.
                for q in (Q(2), Q(3), Q(5)):
                    excess = evaluate(joint, q) - evaluate(product, q)
                    expected_excess = (q - 1) ** 2 / 4
                    if offset != 0:
                        expected_excess *= -1
                    assert excess == expected_excess
                data['configurations'].append({'d': dim, 'L': str(side),
                    'M': separation, 'offset': str(offset), 'pair': serial_poly(pair),
                    'product': serial_poly(product), 'joint': serial_poly(joint)})

for n in range(1, 9):
    points = []
    for k in range(n):
        points.extend([(Q(0), Q(3 * k)), (Q(3, 2), Q(3 * k))])
    poly, _, bad = integrate(points)
    assert bad == 0 and poly == {0: Q(1, 2), n: Q(1, 2)}
    assert sum(Q(exponent) * probability for exponent, probability in poly.items()) == Q(n, 2)
    data['n_pair_checks'].append({'n': n, 'weight': serial_poly(poly),
                                 'mean_energy': str(-Q(n, 2))})

# A sub-core pair is forbidden for some shifts, not all shifts.
poly, _, bad = integrate([(Q(0), Q(0)), (Q(1, 20), Q(0))])
assert bad == Q(19, 20) and poly == {1: Q(1, 20)}
data['sub_core_pair'] = {'distance': '1/20', 'core': '1/10',
                        'forbidden_shift_mass': str(bad), 'weight': serial_poly(poly)}

# Floating-point numbers are supplementary; all decisive comparisons above are exact.
q = Q(2)
pair_weight = Q(3, 2)
aligned_weight = Q(5, 2)
ratio = aligned_weight / pair_weight ** 2
assert ratio == Q(10, 9)
beta = math.log(2)
gap = -math.log(float(ratio)) / beta
gap_independent = (-math.log(float(aligned_weight)) + 2 * math.log(float(pair_weight))) / beta
assert abs(gap - gap_independent) < 1e-14
data['q2_example'] = {'beta': 'log(2)', 'j': 1, 'ratio': str(ratio),
                      'gap': gap, 'independent_gap': gap_independent}

output_path = Path(__file__).with_name('averaging_checks.json')
output_path.write_text(json.dumps(data, indent=2) + '\n')
print('effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Exact tent-kernel checks:', kernel_count)
print('Exact four-particle checks:', len(data['configurations']))
print('Separations in cube sides: 3, 7, 100; dimensions: 2, 3; cube sides: 1, 2')
print('Two-particle weight: (1 + q)/2')
print('Aligned four-particle weight: (1 + q^2)/2')
print('Staggered four-particle weight: q')
print('Product of isolated weights: (1 + 2q + q^2)/4')
print('Exact variance/excess checks at q=2,3,5: passed')
print('Exact n-pair weight checks n=1,...,8: passed')
print('Sub-core pair: forbidden shift mass 19/20; weight q/20')
print('At q=2: joint/product =', ratio)
print('At beta=log(2), j=1: effective group interaction =', format(gap, '.15f'))
print('Independent logarithm evaluation agrees within 1e-14')
print('Data:', output_path.name)
print('Peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('All checks passed.')
signal.alarm(0)
