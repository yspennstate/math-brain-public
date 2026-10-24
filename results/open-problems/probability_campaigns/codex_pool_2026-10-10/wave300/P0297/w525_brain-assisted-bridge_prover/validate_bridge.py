"""Deterministic small validation; numerical agreement is not a mathematical audit."""
import json
import math
import time
from pathlib import Path
from lfpp_parameter_check import check_parameters


def simpson(function, lo, hi, count=1600):
    step = (hi - lo) / count
    return step / 3 * sum((1 if i in (0, count) else 4 if i % 2 else 2) * function(lo + i * step) for i in range(count + 1))


def switch_response(t):
    return simpson(lambda u: math.exp(-(u / t) ** 2) / math.cosh(u) ** 2, -16, 16) / (2 * math.sqrt(math.pi))


def two_path_mean(xi, beta):
    def integrand(difference):
        value = abs(beta * xi * difference / 2)
        log_two_cosh = value + math.log1p(math.exp(-2 * value))
        return -log_two_cosh / beta * math.exp(-difference * difference / 4) / (2 * math.sqrt(math.pi))
    return simpson(integrand, -12, 12)


def thermal_values(xi, x, beta, covariance):
    # Three competing routes. The two-vertex route can beat either singleton.
    path_weights = [(1.0, 0.0), (0.0, 1.3), (0.3, 0.4)]
    path_logs, gradients = [], []
    for weights in path_weights:
        terms = [weights[i] * math.exp(xi * x[i]) for i in range(2)]
        total = sum(terms)
        path_logs.append(math.log(total))
        gradients.append([term / total for term in terms])
    smallest = min(path_logs)
    terms = [math.exp(-beta * (f - smallest)) for f in path_logs]
    q = [term / sum(terms) for term in terms]
    bar = [sum(q[j] * gradients[j][i] for j in range(3)) for i in range(2)]
    def quadratic(vector):
        return sum(vector[i] * covariance[i][j] * vector[j] for i in range(2) for j in range(2))
    a = sum(q[j] * (sum(gradients[j][i] * covariance[i][i] for i in range(2)) - quadratic(gradients[j])) for j in range(3))
    b = sum(q[j] * quadratic(gradients[j]) for j in range(3)) - quadratic(bar)
    return smallest - math.log(sum(terms)) / beta, xi * (a - beta * b), a, b


def gaussian_comparison(correlation):
    xi, beta, h, count, bound = 0.65, 1.7, 1e-4, 96, 8.0
    step = 2 * bound / count
    totals = [0.0, 0.0, 0.0]
    for i in range(count + 1):
        z1 = -bound + i * step
        w1 = (1 if i in (0, count) else 4 if i % 2 else 2) * math.exp(-z1 * z1 / 2)
        for j in range(count + 1):
            z2 = -bound + j * step
            weight = w1 * (1 if j in (0, count) else 4 if j % 2 else 2) * math.exp(-z2 * z2 / 2) / (2 * math.pi)
            x = [z1, correlation * z1 + math.sqrt(1 - correlation ** 2) * z2]
            covariance = [[1, correlation], [correlation, 1]]
            totals[0] += weight * thermal_values(xi + h, x, beta, covariance)[0]
            totals[1] += weight * thermal_values(xi - h, x, beta, covariance)[0]
            totals[2] += weight * thermal_values(xi, x, beta, covariance)[1]
    totals = [v * (step / 3) ** 2 for v in totals]
    finite_difference = (totals[0] - totals[1]) / (2 * h)
    return {"correlation": correlation, "finite_difference": finite_difference, "interpolation": totals[2], "absolute_error": abs(finite_difference - totals[2])}


def main():
    # A fresh gate receipt must be present; no stochastic simulation, GPU, or training.
    gate_path = Path('measurements/compute_gate.json')
    gate = json.loads(gate_path.read_text(encoding='utf-8-sig'))
    if not gate.get('allowed') or time.time() - gate['checked_unix'] > 600:
        raise RuntimeError('No fresh admitted bounded compute gate.')
    started = time.perf_counter()
    gamma, xi, q = math.sqrt(8 / 3), 1 / math.sqrt(6), 5 / math.sqrt(6)
    bad_dimension = 2 * q / xi
    bad = check_parameters(gamma, bad_dimension, xi, q)
    good = check_parameters(gamma, gamma / xi, xi, q, 1 / 6)
    underdetermined = check_parameters(1.0, 3.0, 1 / 3, 2.5, 1 / 6)
    assert not bad['consistent'] and good['consistent'] and underdetermined['consistent']
    assert 'not proved' in underdetermined['proof_status']
    exact_response = 1 / math.sqrt(math.pi)
    table = [{"beta": beta, "retained_response": switch_response(beta), "exact_hard_response": exact_response, "absolute_error": abs(switch_response(beta) - exact_response)} for beta in [1, 4, 16, 64, 256]]
    assert table[-1]['absolute_error'] < 8e-6
    h = 1e-5
    derivative = (two_path_mean(1 + h, 4) - two_path_mean(1 - h, 4)) / (2 * h)
    assert abs(derivative + switch_response(4)) < 1e-8
    correlated = [gaussian_comparison(c) for c in [0.4, -0.4]]
    assert max(row['absolute_error'] for row in correlated) < 1e-7
    covariance = [[1, 0.4], [0.4, 1]]
    common_covariance = [[entry + 4 for entry in row] for row in covariance]
    point = thermal_values(0.65, [0.7, -0.2], 1.7, covariance)
    with_common_mode = thermal_values(0.65, [0.7, -0.2], 1.7, common_covariance)
    common_error = max(abs(point[i] - with_common_mode[i]) for i in [1, 2, 3])
    assert common_error < 1e-12
    report = {
        'command': 'python -X utf8 validate_bridge.py', 'compute_gate': str(gate_path),
        'elapsed_seconds': time.perf_counter() - started,
        'parameter_guard': {'prior_formula_dimension': bad_dimension, 'correct_anchor_dimension': gamma / xi, 'unchecked_bad_rows_rejected': 0, 'guard_bad_rows_rejected': 1, 'valid_control_rows_accepted': 2, 'bad_result': bad, 'good_result': good, 'underdetermined_control': underdetermined},
        'fixed_route_response_failure': {'predicted_derivative': 0.0, 'exact_derivative': -exact_response, 'absolute_error': exact_response},
        'retained_switch_response': table,
        'two_route_fixed_beta_derivative_error': abs(derivative + switch_response(4)),
        'correlated_gaussian_checks': correlated, 'common_mode_invariance_error': common_error,
        'two_route_variance_at_xi_1': 1 - 1 / math.pi,
        'poincare_upper_bound_at_xi_1': 1.0,
        'status': 'all bounded numerical controls passed; mathematical independent audit pending',
        'limitations': ['two-route model is not planar LFPP', 'parameter consistency is not a proof', 'quadrature errors are numerical evidence, not certified integration errors']
    }
    Path('measurements/bridge_validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
