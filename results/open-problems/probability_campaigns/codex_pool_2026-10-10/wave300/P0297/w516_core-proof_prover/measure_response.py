"""Bounded deterministic reproduction for ATTEMPT.md L1-L3. Python standard library only."""
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = time.perf_counter()
DEADLINE_SECONDS = 120


def deadline():
    if time.perf_counter() - START > DEADLINE_SECONDS:
        raise TimeoutError('compute gate exhausted')


def simpson(function, low, high, n):
    assert n % 2 == 0
    step = (high - low) / n
    total = 0.0
    for j in range(n + 1):
        coefficient = 1 if j in (0, n) else 4 if j % 2 else 2
        total += coefficient * function(low + j * step)
    return total * step / 3


def response(x, covariance, paths, xi, beta):
    path_logs, weights, path_derivatives = [], [], []
    for coefficients in paths:
        logs = [math.log(a) + xi * value if a else -math.inf
                for a, value in zip(coefficients, x)]
        maximum = max(logs)
        values = [math.exp(value - maximum) for value in logs]
        normalizer = sum(values)
        weight = [value / normalizer for value in values]
        path_logs.append(maximum + math.log(normalizer))
        weights.append(weight)
        path_derivatives.append(sum(w * value for w, value in zip(weight, x)))
    logits = [-beta * value for value in path_logs]
    maximum = max(logits)
    masses = [math.exp(value - maximum) for value in logits]
    total_mass = sum(masses)
    probabilities = [value / total_mass for value in masses]
    free_energy = -(maximum + math.log(total_mass)) / beta
    averaged_weight = [sum(p * w[i] for p, w in zip(probabilities, weights))
                       for i in range(len(x))]

    def quadratic(weight):
        return sum(weight[i] * covariance[i][j] * weight[j]
                   for i in range(len(x)) for j in range(len(x)))

    averaged_quadratic = sum(p * quadratic(w) for p, w in zip(probabilities, weights))
    within = sum(probabilities[p] * sum(covariance[i][i] * weights[p][i]
                                      for i in range(len(x)))
                 for p in range(len(paths))) - averaged_quadratic
    switching = beta * (averaged_quadratic - quadratic(averaged_weight))
    direct_derivative = sum(p * derivative for p, derivative
                            in zip(probabilities, path_derivatives))
    return free_energy, direct_derivative, xi * (within - switching), within, switching


def expectation_case(xi, beta, n=160):
    covariance = ((1.0, 0.0, 0.6), (0.0, 1.0, 0.4), (0.6, 0.4, 0.52))
    paths = ((1.0, 0.0, 0.7), (0.0, 1.0, 0.4), (1.0, 1.0, 0.0))
    cutoff = 8.0
    step = 2 * cutoff / n
    totals = [0.0] * 5
    finite_differences = 0.0
    delta = 1e-4
    for i in range(n + 1):
        deadline()
        z1 = -cutoff + i * step
        ci = 1 if i in (0, n) else 4 if i % 2 else 2
        for j in range(n + 1):
            z2 = -cutoff + j * step
            cj = 1 if j in (0, n) else 4 if j % 2 else 2
            x = (z1, z2, 0.6 * z1 + 0.4 * z2)
            integration_weight = ci * cj * math.exp(-(z1 * z1 + z2 * z2) / 2) / (2 * math.pi)
            values = response(x, covariance, paths, xi, beta)
            for k, value in enumerate(values):
                totals[k] += integration_weight * value
            upper = response(x, covariance, paths, xi + delta, beta)[0]
            lower = response(x, covariance, paths, xi - delta, beta)[0]
            finite_differences += integration_weight * (upper - lower) / (2 * delta)
    scale = step * step / 9
    totals = [value * scale for value in totals]
    finite_differences *= scale
    row = {'xi': xi, 'beta': beta, 'grid_points': (n + 1) ** 2,
           'expected_log_soft_min': totals[0], 'expected_direct_derivative': totals[1],
           'expected_corrected_response': totals[2], 'expected_within_term': totals[3],
           'expected_switch_term': totals[4], 'finite_difference': finite_differences,
           'ibp_absolute_error': abs(totals[1] - totals[2]),
           'finite_difference_error': abs(totals[1] - finite_differences)}
    assert row['ibp_absolute_error'] < 2e-6, row
    assert row['finite_difference_error'] < 2e-7, row
    assert totals[4] >= -1e-12, row
    return row


def logistic_density(u):
    value = math.exp(-abs(u))
    return value / ((1 + value) ** 2)


def main():
    gate = json.loads((ROOT / 'COMPUTE_GATE_004.json').read_text(encoding='utf-8'))
    assert gate['gate_id'] == 'w516-P0297-gaussian-response-004'
    assert gate['max_runtime_seconds'] == DEADLINE_SECONDS
    assert 81 ** 2 <= gate['max_grid_points_per_case']
    assert 6001 <= gate['max_grid_points_per_case']
    prior_path = ROOT / 'measurements.json'
    if prior_path.exists():
        prior = json.loads(prior_path.read_text(encoding='utf-8'))
        if prior.get('gate_id') == 'w516-P0297-gaussian-response-002':
            (ROOT / 'measurements_gate002_complete.json').write_text(json.dumps(prior, indent=2) + '\n', encoding='utf-8')
        if prior.get('gate_id') == 'w516-P0297-gaussian-response-003':
            (ROOT / 'measurements_gate003_grid_variance.json').write_text(json.dumps(prior, indent=2) + '\n', encoding='utf-8')
    data = {'gate_id': gate['gate_id'], 'command': 'python -X utf8 ./measure_response.py',
            'method': 'deterministic Simpson quadrature; no Monte Carlo or LQG extrapolation',
            'finite_beta_cases': [], 'two_edge_cases': [], 'controls': [],
            'prior_gate_receipts': ['measurements_gate001_partial.json', 'measurements_gate002_complete.json', 'measurements_gate003_grid_variance.json'],
            'gate_variance_receipt': 'GATE_VARIANCE.json',
            'mathematical_proof': 'ATTEMPT.md L1-L5; author-proved, independent review pending'}
    for xi, beta in ((0.2, 0.5), (0.2, 2.0), (0.2, 8.0), (0.8, 2.0)):
        row = expectation_case(xi, beta, n=80)
        data['finite_beta_cases'].append(row)
        print(json.dumps(row))
        (ROOT / 'measurements.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')

    # Change variables to resolve the narrowing near-tie window at large beta.
    xi = 0.7
    exact_derivative = -1 / math.sqrt(math.pi)
    for beta in (2.0, 10.0, 50.0, 250.0, 1250.0):
        deadline()
        ratio = simpson(lambda u: logistic_density(u) * math.exp(-u*u/(4*beta*beta*xi*xi)),
                        -40.0, 40.0, 6000)
        switching = ratio / (xi * math.sqrt(math.pi))
        corrected = -xi * switching
        row = {'xi': xi, 'beta': beta, 'beta_expected_B': switching,
               'finite_beta_derivative': corrected, 'zero_temperature_derivative': exact_derivative,
               'baseline_without_switch': 0.0, 'baseline_absolute_error': abs(exact_derivative),
               'corrected_absolute_error': abs(corrected - exact_derivative),
               'omitted_logistic_tail_bound': 2 * math.exp(-40) / (xi * math.sqrt(math.pi))}
        data['two_edge_cases'].append(row)
        print(json.dumps(row))
    assert data['two_edge_cases'][-1]['corrected_absolute_error'] < 1e-6

    covariance = ((1.0, 0.2), (0.2, 0.7))
    shifted = tuple(tuple(value + 3.5 for value in row) for row in covariance)
    paths = ((1.0, 0.4), (0.2, 1.0))
    original = response((0.3, -0.5), covariance, paths, 0.7, 5.0)
    common_mode = response((0.3, -0.5), shifted, paths, 0.7, 5.0)
    common_error = max(abs(original[i] - common_mode[i]) for i in (2, 3, 4))
    assert common_error < 1e-12
    data['controls'].append({'name': 'common Gaussian mode invariance', 'maximum_error': common_error})
    single = response((0.3, -0.5), covariance, (paths[0],), 0.7, 5.0)
    assert abs(single[4]) < 1e-12
    data['controls'].append({'name': 'single deterministic path has no switching term', 'switching': single[4]})
    data['comparison_bound'] = {'xi_critical_upper': 2 - math.sqrt(2.5),
                                'interpretation': 'author-derived comparison bound; no novelty claim'}
    data['elapsed_script_seconds'] = time.perf_counter() - START
    data['assertions_passed'] = True
    data['maximum_ibp_absolute_error'] = max(row['ibp_absolute_error'] for row in data['finite_beta_cases'])
    data['maximum_finite_difference_error'] = max(row['finite_difference_error'] for row in data['finite_beta_cases'])
    (ROOT / 'measurements.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'complete': True, 'elapsed_script_seconds': data['elapsed_script_seconds'],
                      'maximum_ibp_absolute_error': data['maximum_ibp_absolute_error'],
                      'baseline_error': abs(exact_derivative),
                      'corrected_error': data['two_edge_cases'][-1]['corrected_absolute_error']}))


if __name__ == '__main__':
    main()
