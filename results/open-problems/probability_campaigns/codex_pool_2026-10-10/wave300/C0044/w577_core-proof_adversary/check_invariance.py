"""Exact finite-stencil check; no simulation, network, or live-store writes."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import time

started = time.perf_counter()
d = 3
a, delta = Fraction(1, 2*d), Fraction(1, 4*d)
e1 = (1, 0, 0)
steps = [tuple(sign if j == i else 0 for j in range(d)) for i in range(d) for sign in (1, -1)]
origin = (0,)*d
minus_e1 = (-1, 0, 0)
stencil = sorted({origin, minus_e1} | {tuple(e[j]-e1[j] for j in range(d)) for e in steps})
total_f = total_Kf = Fraction(0)
minimum = Fraction(1)
row_count = 0
for signs in product((-1, 1), repeat=len(stencil)):
    sigma = dict(zip(stencil, signs))
    weights = [a + delta*sigma[origin] if e == e1 else a - delta*sigma[origin] if e == minus_e1 else a for e in steps]
    assert sum(weights) == 1
    assert min(weights) >= delta
    minimum = min(minimum, min(weights))
    total_f += sigma[minus_e1]
    total_Kf += sum(w*sigma[tuple(e[j]-e1[j] for j in range(d))] for e, w in zip(steps, weights))
    row_count += 1
mean_f, mean_Kf = total_f/row_count, total_Kf/row_count
assert mean_f == 0
assert mean_Kf == delta

# A doubly stochastic deterministic control has the invariance calculation expected by the invalid step.
control_Kf = Fraction(0)
for signs in product((-1, 1), repeat=len(stencil)):
    sigma = dict(zip(stencil, signs))
    control_Kf += sum(a*sigma[tuple(e[j]-e1[j] for j in range(d))] for e in steps)
control_Kf /= row_count
assert control_Kf == mean_f
result = {
    'command': 'python -X utf8 ~/brain_workers/w577/check_invariance.py',
    'method': 'Exhaustive exact Fraction arithmetic on a finite iid sign stencil, not a finite-time directional-transience simulation',
    'fresh_compute_gate': {'vertices': len(stencil), 'configurations': row_count, 'gpu': False, 'training': False, 'wall_limit_seconds': 60},
    'd': d, 'ellipticity_lower_bound': str(minimum), 'configurations_checked': row_count,
    'claimed_invariance_prediction': str(mean_f), 'actual_iid_mean_Kf': str(mean_Kf),
    'invariance_defect': str(mean_Kf-mean_f), 'deterministic_control_mean_Kf': str(control_Kf),
    'elapsed_seconds': time.perf_counter()-started,
    'target_solved': False,
}
assert result['elapsed_seconds'] < 60
Path(__file__).with_name('MEASUREMENT.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
