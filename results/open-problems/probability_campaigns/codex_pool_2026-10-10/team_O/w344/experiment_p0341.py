import json
import math
import pathlib
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
exact_checks = 0
for n in range(2, 21):
    harmonic = sum((Fraction(1, j) for j in range(1, n)), Fraction())
    assert sum((1 / (Fraction(n-j) * harmonic) for j in range(1, n)), Fraction()) == 1
    exact_checks += 1
harmonics = [0.0]
for j in range(1, 2**18 + 65):
    harmonics.append(harmonics[-1] + 1/j)
records = []
for trim in (0, 1, 8, 64):
    for k in (8, 12, 16, 18):
        target = 2**k
        n = target + trim + 1
        assert target == n - trim - 1 and n < 2 * target
        comparison = sum(6 * 2**r * harmonics[2**r-1] / (math.pi**2 * (2**r-1)) for r in range(1, k+1))
        first_jump = 1 / ((trim+1) * harmonics[n-1])
        lower_ratio = target * first_jump / comparison
        records.append({'trim': trim, 'K': k, 'n': n, 'first_jump_probability': first_jump, 'comparison_sum': comparison, 'actual_sum_lower_bound': target * first_jump, 'ratio_lower_bound': lower_ratio})
actual = []
for k in (4, 6, 8):
    trim = 1
    target = 2**k
    n = target + trim + 1
    visits = [0.0] * (n+1)
    visits[n] = 1.0
    for state in range(n, 1, -1):
        for j in range(1, state):
            visits[j] += visits[state] / ((state-j) * harmonics[state-1])
    assert abs(visits[1] - 1) < 1e-12
    assert max(visits) <= 1 + 1e-12
    first_jump = 1 / ((trim+1) * harmonics[n-1])
    assert visits[target] >= first_jump - 1e-12
    weighted = sum(2**r * visits[2**r] for r in range(1, k+1))
    comparison = sum(6 * 2**r * harmonics[2**r-1] / (math.pi**2 * (2**r-1)) for r in range(1, k+1))
    actual.append({'K': k, 'n': n, 'trim': trim, 'weighted_sum': weighted, 'comparison_sum': comparison, 'ratio': weighted/comparison})
report = {'exact_transition_normalization_checks': exact_checks, 'lower_bound_cases': records, 'full_descent_cases': actual, 'label': 'finite numerical checks of a proved lower-bound mechanism; not a substitute for the asymptotic proof'}
(HERE / 'p0341_measurements.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({'exact_checks': exact_checks, 'full_descent_cases': actual, 'K18_lower_bounds': [r for r in records if r['K']==18]}))
