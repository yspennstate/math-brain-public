from fractions import Fraction as Q
from itertools import combinations_with_replacement
import json
from pathlib import Path
import time
import mpmath as mp

started = time.perf_counter()
ROOT = Path(__file__).resolve().parent


def workload(ages):
    return max([Q(0)] + [Q(i + 1) - age for i, age in enumerate(sorted(ages))])


def parallel_workload(ages):
    return sum((max(Q(0), 1-a) for a in ages), Q(0))


grid = [Q(k, 4) for k in range(9)]
configurations = additions = 0
for n in range(5):
    for ages in combinations_with_replacement(grid, n):
        configurations += 1
        v, t = workload(ages), parallel_workload(ages)
        assert v >= t
        for a in grid:
            additions += 1
            new = ages + (a,)
            assert workload(new) - parallel_workload(new) >= v-t

mp.mp.dps = 55
delta = mp.tan(mp.pi / 1024)


def closed(c):
    z = (delta-mp.j)*c
    return mp.re((z-1+mp.exp(-z))/(z*z))


errors = []
for c in [mp.mpf('0.0001'), mp.mpf('0.1'), mp.mpf(1), mp.pi, 2*mp.pi, 3*mp.pi, mp.mpf('6.294'), mp.mpf('8.979'), mp.mpf(40)]:
    quadrature = mp.quad(lambda u: (1-u)*mp.exp(-delta*c*u)*mp.cos(c*u), [0, 1])
    error = abs(closed(c)-quadrature)
    errors.append(error)
    assert error < mp.mpf('1e-45')
    j0 = (1-mp.cos(c))/(c*c)
    assert abs(closed(c)-j0) <= delta*c/6

coarse_margin = Q(137, 46080)-Q(1, 700)
exact_margin = Q(137, 46080)-Q(27, 19994)
assert coarse_margin == Q(2491, 1612800) > 0
assert exact_margin > coarse_margin
actual_coefficient = (closed(3*mp.pi)-closed(2*mp.pi))/2
assert actual_coefficient > mp.mpf(137)/46080

receipt = {
    'command': 'python -X utf8 verify_p0289.py',
    'label': 'finite exact checks and numerical evidence; written proof is audited separately',
    'configuration_checks': configurations,
    'single_addition_checks': additions,
    'configuration_violations': 0,
    'quadrature_checks': len(errors),
    'maximum_quadrature_difference': str(max(errors)),
    'rational_margin_lower_bound': str(coarse_margin),
    'workload_difference_lower_bound_eps_1e_minus4': str(coarse_margin * Q(1, 10000**2)),
    'computed_second_order_rise': str(actual_coefficient),
    'seconds': round(time.perf_counter()-started, 3),
}
(ROOT/'p0289_measurements.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
