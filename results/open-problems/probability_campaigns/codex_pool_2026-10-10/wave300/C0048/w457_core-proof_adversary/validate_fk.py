"""Small, bounded, exact FK check. Independently derive conditionals by enumeration."""
from fractions import Fraction
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
GATE = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))


def check_gate():
    if time.monotonic() - START > GATE['max_elapsed_seconds']:
        raise RuntimeError('Fresh compute gate expired; do not enlarge it automatically')


def classes(n, edges, mask, groups):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def join(x, y):
        parent[find(x)] = find(y)

    for group in groups:
        for v in group[1:]:
            join(group[0], v)
    for j, (u, v) in enumerate(edges):
        if mask & (1 << j):
            join(u, v)
    return [find(v) for v in range(n)]


def exact_case(name, n, edges, groups, p, q):
    m = len(edges)
    assert m <= GATE['max_graph_edges']
    assert 2**m <= GATE['max_configurations_per_case']
    a = p / (p + q * (1 - p))
    weights = []
    for mask in range(2**m):
        if mask % 256 == 0:
            check_gate()
        k = len(set(classes(n, edges, mask, groups)))
        opened = mask.bit_count()
        # Common denominator p.denominator**m cancels in all probabilities.
        weights.append(p.numerator**opened * (p.denominator-p.numerator)**(m-opened) * q**k)
    z = sum(weights)
    mismatches = []
    checked = 0
    extrema = set()
    for j, (u, v) in enumerate(edges):
        for mask in range(2**m):
            if mask & (1 << j):
                continue
            prob = Fraction(weights[mask | (1 << j)], weights[mask] + weights[mask | (1 << j)])
            cls = classes(n, edges, mask, groups)
            expected = p if cls[u] == cls[v] else a
            checked += 1
            extrema.add(prob)
            if prob != expected or not a <= prob <= p:
                mismatches.append({'edge': j, 'mask': mask, 'prob': str(prob), 'expected': str(expected)})
        check_gate()
    marginals = [Fraction(sum(w for mask, w in enumerate(weights) if mask & (1 << j)), z) for j in range(m)]
    joint = Fraction(weights[-1], z)
    product = Fraction(1)
    for marginal in marginals:
        product *= marginal
    result = {
        'case': name, 'vertices': n, 'edges': m, 'p': str(p), 'q': q,
        'wired_groups': groups, 'configurations': 2**m, 'conditionals_checked': checked,
        'conditional_values': sorted(map(str, extrema)), 'conditional_mismatches': mismatches,
        'partition_numerator': z, 'edge_marginals': list(map(str, marginals)),
        'all_open': str(joint), 'product_of_marginals': str(product),
        'joint_to_product_ratio': str(joint/product),
        'joint_to_product_ratio_decimal': float(joint/product),
    }
    if name == 'cycle4-free-half-q3':
        assert z == 258 and joint == Fraction(1, 86)
        assert set(marginals) == {Fraction(11, 43)}
        assert joint > product
    if q == 1:
        assert joint == product
    assert not mismatches
    return result


def main():
    cycle = [(0, 1), (1, 2), (2, 3), (3, 0)]
    cube = [(v, v ^ (1 << bit)) for v in range(8) for bit in range(3) if v < (v ^ (1 << bit))]
    cases = [
        ('cycle4-free-half-q3', 4, cycle, [], Fraction(1, 2), 3),
        ('cycle4-wired-half-q3', 4, cycle, [[0, 2]], Fraction(1, 2), 3),
        ('cycle4-free-half-q1', 4, cycle, [], Fraction(1, 2), 1),
        ('cycle4-free-half-q2', 4, cycle, [], Fraction(1, 2), 2),
        ('cube-free-tenth-q3', 8, cube, [], Fraction(1, 10), 3),
        ('cube-free-half-q3', 8, cube, [], Fraction(1, 2), 3),
        ('cube-wired-two-fifths-q3', 8, cube, [[1, 2, 4]], Fraction(2, 5), 3),
    ]
    assert len(cases) <= GATE['max_cases']
    results = [exact_case(*case) for case in cases]
    # Record exact arithmetic in the self-contained infinite-volume obstruction.
    d, q, p = 3, 3, Fraction(1, 10)
    a = p / (p + q*(1-p))
    assert a == Fraction(1, 28)
    one_arm_bounds = {
        str(N): str(2*d*p*((2*d-1)*p)**(N-1)) for N in [1, 4, 8, 16, 32]
    }
    check_gate()
    report = {
        'command': 'python -X utf8 validate_fk.py', 'gate': GATE,
        'cases': results, 'configurations_total': sum(r['configurations'] for r in results),
        'conditionals_checked_total': sum(r['conditionals_checked'] for r in results),
        'mismatches_total': sum(len(r['conditional_mismatches']) for r in results),
        'local_positive_nonpercolation_example': {
            'd': d, 'q': q, 'p': str(p), 'conditional_lower': str(a),
            'one_arm_upper_bounds': one_arm_bounds,
            'infinite_volume_limit_from_analytic_bound': 0,
            'at_criticality': False,
        },
        'elapsed_seconds': time.monotonic()-START,
        'proof_scope': 'Exact finite-graph sanity check; analytic infinite-volume proof is ATTEMPT.md I1',
    }
    encoded = json.dumps(report, indent=2)
    assert len(encoded.encode()) < GATE['max_output_bytes']
    (ROOT / 'measurements.json').write_text(encoded+'\n', encoding='utf-8')
    print(json.dumps({
        'cases': len(results), 'configurations': report['configurations_total'],
        'conditionals': report['conditionals_checked_total'], 'mismatches': report['mismatches_total'],
        'cycle_joint': results[0]['all_open'], 'cycle_product': results[0]['product_of_marginals'],
        'cycle_ratio': results[0]['joint_to_product_ratio_decimal'],
        'elapsed_seconds': report['elapsed_seconds'], 'saved': str(ROOT/'measurements.json'),
    }))


if __name__ == '__main__':
    main()
