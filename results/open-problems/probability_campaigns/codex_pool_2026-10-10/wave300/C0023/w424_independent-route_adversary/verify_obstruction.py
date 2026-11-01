"""Bounded deterministic checks; the analytic proof is INDEPENDENT_DERIVATION.md."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
START = time.perf_counter()
GATE = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
checks = []


def check(name, condition):
    if time.perf_counter() - START > GATE['max_runtime_seconds_inside_script']:
        raise RuntimeError('Fresh compute gate exceeded')
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def b(k):
    return 8 if k > 0 and k & (k - 1) == 0 else 2


def multiply(a, c):
    out = [F(0)] * (len(a) + len(c) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(c):
            out[i + j] += x * y
    return out


def finite_distribution(depth, p):
    # Full offspring generating polynomial, built from the last generation back.
    g = [F(0), F(1)]
    for k in range(depth, 0, -1):
        one_child = [p * x for x in g]
        one_child[0] += 1 - p
        g = [F(1)]
        for _ in range(b(k)):
            g = multiply(g, one_child)
    return g


def moments(depth, p):
    first = second = F(1)
    for k in range(1, depth + 1):
        mean = b(k) * p
        variance = b(k) * p * (1 - p)
        second = mean * mean * second + variance * first
        first *= mean
    return first, second


distribution_rows = []
for p in (F(1, 4), F(1, 2), F(3, 4)):
    for depth in (0, 1, 2):
        dist = finite_distribution(depth, p)
        first = sum(F(i) * prob for i, prob in enumerate(dist))
        second = sum(F(i * i) * prob for i, prob in enumerate(dist))
        expected = moments(depth, p)
        check(f'full-pgf-depth-{depth}-p-{p}', sum(dist) == 1 and (first, second) == expected)
        distribution_rows.append({'depth': depth, 'p': str(p), 'mean': str(first),
                                  'second_moment': str(second), 'survival': str(1 - dist[0])})

dist = finite_distribution(3, F(1, 2))
check('full-pgf-depth-3-p-1/2', sum(dist) == 1 and
      sum(F(i) * v for i, v in enumerate(dist)) == 16 and
      sum(F(i * i) * v for i, v in enumerate(dist)) == 304)

mean = F(1)
qratio = F(1)
moment_rows = []
for k in range(1, GATE['max_tree_moment_depth'] + 1):
    qratio += F(1, b(k) * mean)
    mean *= F(b(k), 2)
    if k & (k + 1) == 0:  # complete dyadic blocks
        j = (k + 1).bit_length() - 1
        closed_form = F(1) + F(1, 4) * (1 - F(1, 2 ** j))
        check(f'exact-dyadic-sum-depth-{k}', qratio == closed_form and qratio <= F(5, 4))
        check(f'exact-generation-mean-depth-{k}', mean == 4 ** k.bit_length() and mean <= 4 * k * k)
        moment_rows.append({'depth': k, 'mean': str(mean), 'normalized_second_moment': str(qratio),
                            'survival_lower_bound': str(1 / qratio)})


def survival_and_derivative(depth, p):
    # Exact finite-model recursion, evaluated with floating point only in this section.
    q, derivative = 1.0, 0.0
    for k in range(depth, 0, -1):
        failure_one = 1.0 - p * q
        new_derivative = b(k) * failure_one ** (b(k) - 1) * (q + p * derivative)
        q = -math.expm1(b(k) * math.log1p(-p * q))
        derivative = new_derivative
    return q, derivative


numeric_rows = []
for depth in (64, 256, 1024, 4096):
    critical, derivative = survival_and_derivative(depth, 0.5)
    delta = 1.0 / depth ** 2
    near_p = 0.5 - delta
    near, _ = survival_and_derivative(depth, near_p)
    fixed, _ = survival_and_derivative(depth, 0.49)
    continuity_error = delta * depth / near_p
    check(f'numerical-critical-bound-depth-{depth}', critical >= 0.8 - 1e-12)
    check(f'numerical-narrow-window-depth-{depth}', near >= 0.8 - continuity_error - 1e-12)
    check(f'numerical-fixed-subcritical-depth-{depth}', fixed <= min(1.0, 4 * depth ** 2 * 0.98 ** depth) + 1e-12)
    numeric_rows.append({'depth': depth, 'critical_survival': critical,
                         'p_half_minus_n_inverse_squared': near_p, 'near_survival': near,
                         'narrow_window_rigorous_lower_bound': 0.8 - continuity_error,
                         'survival_at_p_0_49': fixed,
                         'conditional_open_pivotal_mean_at_half': 0.5 * derivative / critical})

result = {
    'command': 'python -X utf8 verify_obstruction.py',
    'gate_id': GATE['gate_id'], 'checks_passed': len(checks), 'failed': 0,
    'exact_checks_passed': sum(not x.startswith('numerical-') for x in checks),
    'numeric_checks_passed': sum(x.startswith('numerical-') for x in checks),
    'checks': checks, 'full_distribution_rows': distribution_rows,
    'exact_dyadic_rows': moment_rows, 'numeric_rows': numeric_rows,
    'interpretation': 'Finite algebra checks and illustrative recursion values; no deployed brain recall or agent accuracy was measured.',
    'runtime_seconds': round(time.perf_counter() - START, 6),
    'C0023_proved': False, 'independently_refereed': False,
}
(ROOT / 'MEASUREMENTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
summary = {'checks_passed': len(checks), 'failed': 0, 'runtime_seconds': result['runtime_seconds'],
           'max_critical_normalized_second_moment': str(qratio), 'numeric_rows': numeric_rows,
           'C0023_proved': False}
(ROOT / 'RUN_RESULT.txt').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, indent=2))
