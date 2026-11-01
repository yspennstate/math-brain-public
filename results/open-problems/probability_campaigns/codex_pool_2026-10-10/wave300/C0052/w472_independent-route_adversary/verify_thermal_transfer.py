"""Finite controls, not a proof of C0052. Run: python -X utf8 verify_thermal_transfer.py."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
GATE = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
START = time.monotonic()
VISITED = 0


def deadline():
    if time.monotonic() - START > GATE['max_wall_seconds']:
        raise RuntimeError('compute gate exceeded; no result certified')


def enumerate_cycle(n, a):
    # a=exp(2 beta), weights rescaled by a^(n/2), hence integral.
    global VISITED
    assert 4 <= n <= GATE['max_spins'] and n % 2 == 0
    totals = Counter()
    for spins in product((-1, 1), repeat=n):
        VISITED += 1
        if VISITED > GATE['max_enumerated_configurations']:
            raise RuntimeError('enumeration gate exceeded')
        if VISITED % 256 == 0:
            deadline()
        energy = sum(spins[i] * spins[(i + 1) % n] for i in range(n))
        totals[sum(spins)] += a ** ((energy + n) // 2)
    z = sum(totals.values())
    m2 = Q(sum(m*m*w for m, w in totals.items()), z)
    m4 = Q(sum(m**4*w for m, w in totals.items()), z)
    return m2, m4 - 3*m2*m2


def transfer_cycle(n, a):
    # Derived independently by differentiating log(lambda_+^n + lambda_-^n).
    v = Q(a-1, a+1)
    q = v**n
    bulk2 = Q(a)
    bulk4 = bulk2 - 3*bulk2**3
    ratio = (1-q)/(1+q)
    k2 = n*bulk2*ratio
    k4 = n*bulk4*ratio + 12*n*n*bulk2**2*q/(1+q)**2
    return k2, k4


def run():
    assert GATE['allowed'] is True
    exact = []
    for a in (2, 3, 4):
        for n in (4, 8, 12):
            actual2, actual4 = enumerate_cycle(n, a)
            expected2, expected4 = transfer_cycle(n, a)
            assert actual2 == expected2 and actual4 == expected4
            row = {'a':a, 'n':n, 'k2_exact':str(actual2), 'k4_exact':str(actual4),
                   'k2_difference':str(actual2-expected2), 'k4_difference':str(actual4-expected4),
                   'status':'PASS'}
            exact.append(row)
            with (ROOT/'FINITE_CONTROLS.jsonl').open('a', encoding='utf-8') as output:
                output.write(json.dumps(row)+'\n')

    a = 2
    xi = -1/math.log((a-1)/(a+1))
    bulk_g = (3*a-1/a)/xi
    scaling = []
    for n in (16, 64, 256, 1024):
        deadline()
        k2, k4 = transfer_cycle(n, a)
        deficit = float(-k4/k2**2)
        finite_g = deficit*n/xi
        scaling.append({'n':n, 'binder_deficit':deficit,
                        'correct_volume_factor':n/xi, 'rescaled_coupling':finite_g,
                        'bulk_coupling':bulk_g, 'absolute_coupling_error':abs(finite_g-bulk_g)})
    assert scaling[-1]['binder_deficit'] < 0.006
    assert abs(scaling[-1]['rescaled_coupling']-bulk_g) < 1e-12
    assert bulk_g > 6
    critical = []
    for a in (2, 4, 16, 256):
        xi = -1/math.log((a-1)/(a+1))
        critical.append({'a':a,'xi':xi,'thermal_coupling':(3*a-1/a)/xi})
    receipt = {'command':'python -X utf8 verify_thermal_transfer.py',
               'completed_at':datetime.now(timezone.utc).isoformat(),
               'scope':'1D periodic ferromagnetic Ising; validation of a limit/normalization obstruction',
               'exact_cases':len(exact), 'exact_discrepancies':0,
               'configurations_enumerated':VISITED, 'elapsed_seconds':time.monotonic()-START,
               'normalization_controls':scaling, 'low_temperature_controls':critical,
               'three_dimensional_proof':False, 'independent_math_review':'pending w473'}
    (ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print(json.dumps(receipt,indent=2))


if __name__ == '__main__':
    run()
