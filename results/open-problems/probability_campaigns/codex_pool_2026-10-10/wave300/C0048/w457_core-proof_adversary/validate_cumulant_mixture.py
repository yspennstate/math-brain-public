"""Check FK mixing cumulants against a direct, independent Potts spin sum."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys
import time

sys.dont_write_bytecode = True
from validate_fk import classes

ROOT = Path(__file__).resolve().parent
GATE = json.loads((ROOT / 'CUMULANT_GATE.json').read_text(encoding='utf-8'))
START = time.monotonic()


def guard():
    if time.monotonic()-START > GATE['max_elapsed_seconds']:
        raise RuntimeError('Compute gate expired')


def case(name, n, edges):
    q, p = 3, F(1, 2)
    assert n <= GATE['max_vertices']
    assert q**n <= GATE['max_spin_assignments_per_case']
    assert 2**len(edges) <= GATE['max_fk_configurations_per_case']
    # Spin ground truth: at exp(beta)=2 each equal-color edge multiplies weight by 2.
    spin_z = 0
    spin_moment_sums = [F(0) for _ in range(5)]
    for sigma in product(range(q), repeat=n):
        weight = 2**sum(sigma[u] == sigma[v] for u, v in edges)
        centered = F(sum(color == 0 for color in sigma)) - F(n, q)
        spin_z += weight
        for j in range(1, 5):
            spin_moment_sums[j] += weight*centered**j
    moments = [value/spin_z for value in spin_moment_sums]
    assert moments[1] == 0
    actual = {2: moments[2], 3: moments[3], 4: moments[4]-3*moments[2]**2}

    # FK oracle: an independent sum over all edge configurations.
    fk_z = 0
    sums = {2: F(0), 3: F(0), 4: F(0), '2sq': F(0)}
    for mask in range(2**len(edges)):
        cls = classes(n, edges, mask, [])
        sizes = [cls.count(c) for c in set(cls)]
        weight = q**len(sizes)
        fk_z += weight
        h = {j: sum(size**j for size in sizes) for j in [2, 3, 4]}
        for j in [2, 3, 4]:
            sums[j] += weight*h[j]
        sums['2sq'] += weight*h[2]**2
    assert spin_z == fk_z
    averages = {j: value/fk_z for j, value in sums.items()}
    variance = averages['2sq']-averages[2]**2
    c2, c3, c4 = F(2, 9), F(2, 27), F(-2, 27)
    omitted = c4*averages[4]
    corrected = omitted+3*c2*c2*variance
    predicted = {2: c2*averages[2], 3: c3*averages[3], 4: corrected}
    assert actual == predicted
    assert omitted != actual[4]
    guard()
    return {
        'case': name, 'vertices': n, 'edges': edges,
        'spin_assignments': q**n, 'fk_configurations': 2**len(edges),
        'partition_numerator': spin_z,
        'direct_spin_cumulants': {str(j): str(x) for j, x in actual.items()},
        'fk_cluster_cumulants': {str(j): str(x) for j, x in predicted.items()},
        'variance_h2': str(variance),
        'baseline_omitted_variance_kappa4': str(omitted),
        'corrected_kappa4': str(corrected),
        'baseline_absolute_error': str(abs(omitted-actual[4])),
        'corrected_absolute_error': str(abs(corrected-actual[4])),
        'pressure_kappa4': str(corrected/n),
        'baseline_pressure_absolute_error': str(abs(omitted-actual[4])/n),
    }


def main():
    results = [case('one-edge-q3-half', 2, [(0,1)]),
               case('cycle4-q3-half', 4, [(0,1),(1,2),(2,3),(3,0)])]
    assert len(results) <= GATE['max_cases']
    report = {
        'command': GATE['command'], 'gate': GATE, 'cases': results,
        'equalities_checked': 3*len(results),
        'baseline_wrong_fourth_cumulants': len(results),
        'corrected_wrong_fourth_cumulants': 0,
        'elapsed_seconds': time.monotonic()-START,
        'scope': 'Tests the omitted-variance shortcut, which w456 correctly did not use',
    }
    output = json.dumps(report,indent=2)
    assert len(output.encode()) < GATE['max_output_bytes']
    (ROOT/'cumulant_measurements.json').write_text(output+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
