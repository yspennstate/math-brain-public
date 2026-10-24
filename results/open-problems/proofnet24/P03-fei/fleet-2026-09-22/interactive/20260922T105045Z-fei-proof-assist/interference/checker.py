#!/usr/bin/env python3
"""Actual Boolean-source sanity checks; analytic proof is in REPORT.md.

Integer Walsh transforms are exact. Entropies are floating evaluations, not
interval or formal certificates. No repository/network writes are performed.
"""
import itertools
import json
import math
import random

LN2 = math.log(2)
A = 2 / (3 * LN2)
B = 1 / (6 * LN2)
TOL = 2e-10


def h(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1-x) * math.log2(1-x)


def j(x):
    if x <= 0 or x >= 1:
        return 0.0
    return 1-h(min(1.0, 0.5+math.sqrt(x*(1-x))))


def entropy(weights):
    return -sum(x*math.log2(x) for x in weights if x > 0)


def walsh(values):
    raw = list(values)
    length = len(raw)
    width = 1
    while width < length:
        for base in range(0, length, 2*width):
            for t in range(width):
                a, b = raw[base+t], raw[base+t+width]
                raw[base+t], raw[base+t+width] = a+b, a-b
        width *= 2
    return [x/length for x in raw]


def data(values):
    coeffs = walsh(values)
    mass = [x*x for x in coeffs]
    n = len(values).bit_length()-1
    influence = [sum(p for s, p in enumerate(mass) if s & (1 << i))
                 for i in range(n)]
    return {
        'coeffs': coeffs, 'mass': mass, 'influences': influence,
        'H': entropy(mass), 'P': sum(j(x) for x in influence),
        'J': sum(min(x, 1-x) for x in influence), 'I': sum(influence),
        'W': sum(x*(1-x) for x in influence),
    }


def children(values, coordinate):
    lowmask = (1 << coordinate)-1
    def lift(index, bit):
        return (index & lowmask) | ((index & ~lowmask) << 1) | (bit << coordinate)
    return tuple(tuple(values[lift(k, bit)] for k in range(len(values)//2))
                 for bit in (0, 1))


stats = {'source_coordinate_checks': 0, 'tree_checks': 0,
         'max_identity_error': 0.0, 'minimum_refund_margin': float('inf'),
         'minimum_folded_margin': float('inf')}


def equality(left, right):
    error = abs(left-right)
    stats['max_identity_error'] = max(stats['max_identity_error'], error)
    assert error <= TOL, (left, right, error)


def local(values, coordinate):
    parent = data(values)
    g0, g1 = children(values, coordinate)
    d0, d1 = data(g0), data(g1)
    u, v = d0['coeffs'], d1['coeffs']
    e = [(a*a+b*b)/2 for a, b in zip(u, v)]
    q = [(a-b)**2/(4*m) if m else 0 for a, b, m in zip(u, v, e)]
    query = parent['influences'][coordinate]
    equality(sum(m*t for m, t in zip(e, q)), query)
    js = entropy(e)-(d0['H']+d1['H'])/2
    ell = sum(m*h(t) for m, t in zip(e, q))
    equality(js, sum(m*j(t) for m, t in zip(e, q)))
    equality(parent['H']-(d0['H']+d1['H'])/2, js+ell)
    refund = parent['P']-(d0['P']+d1['P'])/2-js
    packet_var = sum(m*(t-query)**2 for m, t in zip(e, q))
    packet_bernoulli = sum(m*t*(1-t) for m, t in zip(e, q))
    influence_var = sum((a-b)**2 for a, b in zip(d0['influences'], d1['influences']))
    equality(parent['W']-(d0['W']+d1['W'])/2,
             packet_bernoulli+packet_var+influence_var/4)
    lower = A*packet_var+B*influence_var
    margin = refund-lower
    assert margin >= -TOL, (values, coordinate, refund, lower, margin)
    stats['minimum_refund_margin'] = min(stats['minimum_refund_margin'], margin)
    delta_spec = sum(m*min(t, 1-t) for m, t in zip(e, q))
    assert js <= j(delta_spec)+TOL
    assert j(delta_spec) <= j(query)+TOL
    assert js >= -TOL and ell >= -TOL
    equality(parent['I']-(d0['I']+d1['I'])/2, query)
    folded_margin = parent['J']-(d0['J']+d1['J'])/2-min(query, 1-query)
    assert folded_margin >= -TOL
    stats['minimum_folded_margin'] = min(stats['minimum_folded_margin'], folded_margin)
    stats['source_coordinate_checks'] += 1
    return {
        'children': (g0, g1), 'JS': js, 'L': ell, 'refund': refund,
        'packet_var': packet_var, 'influence_var': influence_var,
        'packet_bernoulli': packet_bernoulli,
        'query': query, 'folded': min(query, 1-query),
    }


def tree(values, selector, depth=0):
    if len(values) == 1 or min(values) == max(values):
        return {k: 0.0 for k in ['JS', 'L', 'refund', 'packet_var',
                                 'influence_var', 'packet_bernoulli', 'query', 'folded']}
    influence = data(values)['influences']
    coordinate = (0 if selector == 'ordered' else
                  max(range(len(influence)),
                      key=lambda k: (min(influence[k], 1-influence[k]),
                                     ((k+depth) % max(1, len(influence))))))
    node = local(values, coordinate)
    left = tree(node['children'][0], selector, depth+1)
    right = tree(node['children'][1], selector, depth+1)
    return {k: node[k]+(left[k]+right[k])/2 for k in left}


def check_tree(values, selector):
    root = data(values)
    totals = tree(values, selector)
    equality(root['H'], totals['JS']+totals['L'])
    equality(root['P'], totals['JS']+totals['refund'])
    equality(root['I'], totals['query'])
    equality(root['W'], totals['packet_bernoulli']+totals['packet_var']+totals['influence_var']/4)
    equality(root['H']-root['P'], totals['L']-totals['refund'])
    assert totals['folded'] <= root['J']+TOL
    assert totals['JS'] <= root['P']+TOL
    assert totals['JS'] <= (2/LN2)*totals['folded']+TOL
    assert totals['packet_var'] <= root['J']+TOL
    assert totals['influence_var'] <= 4*root['J']+TOL
    assert totals['refund'] >= A*totals['packet_var']+B*totals['influence_var']-TOL
    stats['tree_checks'] += 1
    return {k: round(v, 12) for k, v in dict(
        H=root['H'], I=root['I'], J=root['J'], P=root['P'], **totals).items()}


def source_majority9():
    values = []
    for word in range(512):
        bits = [1 if word & (1 << i) else -1 for i in range(9)]
        inner = [1 if sum(bits[k:k+3]) > 0 else -1 for k in (0, 3, 6)]
        values.append(1 if sum(inner) > 0 else -1)
    return tuple(values)


def main():
    exhaustive_count = 0
    for n in range(1, 4):
        for truth in itertools.product((-1, 1), repeat=1 << n):
            for coordinate in range(n):
                local(truth, coordinate)
            check_tree(truth, 'ordered')
            check_tree(truth, 'adaptive')
            exhaustive_count += 1
    rng = random.Random(20260922)
    random_count = 0
    for n, count in [(4, 512), (5, 128), (6, 32)]:
        for _ in range(count):
            truth = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
            for coordinate in range(n):
                local(truth, coordinate)
            check_tree(truth, 'adaptive')
            random_count += 1
    examples = {}
    for n in (3, 6, 9):
        truth = tuple(-1 if k == 0 else 1 for k in range(1 << n))
        examples['one_point_'+str(n)] = check_tree(truth, 'adaptive')
        parity = tuple(-1 if k.bit_count() % 2 else 1 for k in range(1 << n))
        examples['character_'+str(n)] = check_tree(parity, 'adaptive')
    examples['recursive_majority_9'] = check_tree(source_majority9(), 'adaptive')
    result = {
        'status': 'all_checks_passed',
        'scope': 'Exact integer Walsh transforms; floating entropy sanity checks only, not a universal computational proof.',
        'exhaustive_boolean_sources_n1_through_n3': exhaustive_count,
        'seeded_random_boolean_sources_n4_through_n6': random_count,
        'strong_concavity_modulus': 4/(3*LN2),
        'packet_variance_coefficient': A,
        'influence_difference_square_coefficient': B,
        'statistics': stats,
        'examples': examples,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
