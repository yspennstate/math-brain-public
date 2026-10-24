"""Focused, reproducible audit of the root QSO certificate and worker 026 copy.

The certificate verifier below uses its own rational operator parser/evaluator.
It does not import either solver's validation, evaluation, or certification code.
Run this script directly; only computations/026_qso_audit_results.json is written.
"""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CAP = F(2, 5)


def require(test, message):
    if not test:
        raise ValueError(message)


def rational_string(value, label):
    require(type(value) is str, label + ' must be a rational string')
    try:
        return F(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(label + ' must be finite and rational') from exc


def read_operator(data):
    require(type(data) is dict and type(data.get('pairs')) is list,
            'An operator with a pairs list is required')
    require(len(data['pairs']) == 10, 'Exactly ten pairs are required')
    P = [[[F(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    seen = set()
    for row in data['pairs']:
        require(type(row) is dict, 'Pair must be an object')
        i, j = row.get('i'), row.get('j')
        require(type(i) is int and type(j) is int and 0 <= i <= j < 4,
                'Invalid pair indices')
        require((i, j) not in seen, 'Repeated parent pair')
        seen.add((i, j))
        raw = row.get('p')
        require(type(raw) is list and len(raw) == 4, 'Invalid probability row')
        p = []
        for value in raw:
            require(type(value) in (int, str), 'Coefficient must be exact')
            p.append(F(value))
        require(all(v >= 0 for v in p) and sum(p) == 1,
                'Probability row is not exactly stochastic')
        require(p[i] == p[j] == 0, 'Forbidden parental offspring')
        P[i][j], P[j][i] = p[:], p[:]
    require(len(seen) == 10, 'Incomplete operator')
    return P


def evaluate(P, x):
    result = [F(0) for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            weight = x[i] * x[j] * (1 if i == j else 2)
            for k in range(4):
                result[k] += weight * P[i][j][k]
    return result


def verify_certificate(certificate, external_operator=None):
    """Return exact values or raise; supports root records with external input.

    For the self-contained worker 026 schema, the operator and cap are mandatory.
    With both embedded and external inputs, they must denote the same operator.
    This is a finite arithmetic verifier, conditional on the analytic theorem.
    """
    require(type(certificate) is dict, 'Certificate must be an object')
    if 'operator' in certificate:
        require(certificate.get('certificate_schema') ==
                'four-type-qso-residual-v1', 'Unrecognized certificate schema')
        require(rational_string(certificate.get('cap'), 'Cap') == CAP,
                'Certificate cap must be exactly 2/5')
        P = read_operator(certificate['operator'])
        if external_operator is not None:
            require(P == read_operator(external_operator),
                    'Embedded operator differs from the supplied input')
    else:
        require(external_operator is not None,
                'Root record needs its external coefficient input')
        P = read_operator(external_operator)
    raw = certificate.get('candidate')
    require(type(raw) is list and len(raw) == 4, 'Candidate needs four coordinates')
    x = [rational_string(v, 'Candidate coordinate') for v in raw]
    require(min(x) >= 0 and sum(x) == 1 and max(x) <= CAP,
            'Serialized candidate is not in the exact capped simplex')
    vx = evaluate(P, x)
    require(min(vx) >= 0 and sum(vx) == 1,
            'Exact stochastic evaluation invariant failed')
    residual = sum(abs(a - b) for a, b in zip(vx, x))
    require(rational_string(certificate.get('exact_residual_l1'), 'Residual') ==
            residual, 'Residual differs from exact recomputation')
    radius = min(F(2), 5 * residual)
    require(rational_string(certificate.get('certified_error_l1_upper'), 'Error') ==
            radius, 'Error differs from the stated factor-five bound')
    intervals = certificate.get('coordinate_intervals')
    require(type(intervals) is list and len(intervals) == 4,
            'Exactly four coordinate intervals are required')
    for pair, xi in zip(intervals, x):
        require(type(pair) is list and len(pair) == 2, 'Invalid coordinate interval')
        lo, hi = [rational_string(v, 'Interval endpoint') for v in pair]
        require([lo, hi] == [max(F(0), xi - radius / 2),
                             min(CAP, xi + radius / 2)],
                'Coordinate interval differs from the zero-sum bound')
    if 'requested_tolerance' in certificate or 'tolerance_met' in certificate:
        tolerance = rational_string(certificate.get('requested_tolerance'), 'Tolerance')
        require(tolerance > 0, 'Tolerance must be positive')
        flag = certificate.get('tolerance_met')
        require(type(flag) is bool and flag == (radius <= tolerance),
                'Tolerance flag differs from the exact comparison')
    if 'search_step' in certificate:
        step = certificate['search_step']
        require(type(step) is int and 0 <= step <= 100000, 'Invalid search step')
    return {'candidate': x, 'residual': residual, 'radius': radius}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejection(call):
    try:
        call()
    except (ValueError, TypeError, KeyError, ArithmeticError) as exc:
        return type(exc).__name__ + ': ' + str(exc)
    raise AssertionError('Expected rejection, but the call succeeded')


def boundary_input():
    rows = []
    for i in range(4):
        for j in range(i, 4):
            allowed = [k for k in range(3) if k not in (i, j)]
            rows.append({'i': i, 'j': j,
                         'p': [str(F(1, len(allowed))) if k in allowed else '0'
                               for k in range(4)]})
    return {'pairs': rows}


def run_audit():
    # The original bug remains reproducible after the parent hardens the root.
    root_path = HERE / '026_original_qso_certified_solver.py'
    patched_path = HERE / '026_qso_certified_solver.py'
    root = load_module('qso_root_026_audit', root_path)
    hardened = load_module('qso_hardened_026_audit', patched_path)
    report = {'root_sha256': hashlib.sha256(root_path.read_bytes()).hexdigest(),
              'hardened_sha256': hashlib.sha256(patched_path.read_bytes()).hexdigest(),
              'passed': {}, 'confirmed_root_api_failures': {}}

    # Existing exact oracles are checked without running the shared writer script.
    oracle_cases = []
    for name, data, fixed in [
        ('equiprobable interior', root.equiprobable_input(), [F(1, 4)] * 4),
        ('invariant triple boundary', boundary_input(), [F(1, 3)] * 3 + [F(0)]),
    ]:
        assert evaluate(read_operator(data), fixed) == fixed
        original = root.solve(root.validate_pairs(data))
        hardened_result = hardened.solve(hardened.validate_pairs(data))
        for key, value in original.items():
            assert hardened_result[key] == value
        checked = verify_certificate(json.loads(json.dumps(original)), data)
        self_contained = verify_certificate(json.loads(json.dumps(hardened_result)))
        assert checked == self_contained and original['tolerance_met']
        actual = sum(abs(a - b) for a, b in zip(checked['candidate'], fixed))
        assert actual <= checked['radius']
        assert max(abs(a - b) for a, b in zip(checked['candidate'], fixed)) <= actual / 2
        for (lo, hi), value in zip(original['coordinate_intervals'], fixed):
            assert F(lo) <= value <= F(hi)
        oracle_cases.append({'name': name, 'actual_error_l1': str(actual),
                             'root_result': original})
    report['passed']['exact_oracles_and_json_roundtrip'] = oracle_cases

    # Tiny exact changes expose inexact arithmetic without any unknown fixed point.
    delta = F(1, 10**20)
    tiny = root.equiprobable_input()
    tiny['pairs'][0]['p'] = ['0', str(F(1, 3) + delta),
                            str(F(1, 3) - delta), '1/3']
    P = root.validate_pairs(tiny)
    false_zero = root.certify(P, [.25] * 4)
    exact_residual = sum(abs(v - F(1, 4)) for v in evaluate(read_operator(tiny), [F(1, 4)] * 4))
    assert exact_residual == delta / 8 and F(false_zero['exact_residual_l1']) == 0
    report['confirmed_root_api_failures']['false_zero_certificate'] = {
        'operator': tiny, 'record': false_zero,
        'actual_exact_residual': str(exact_residual),
        'independent_verifier_rejection': rejection(lambda: verify_certificate(false_zero, tiny)),
        'hardened_rejection': rejection(lambda: hardened.certify(P, [.25] * 4))}
    correct = root.certify(P, [F(1, 4)] * 4)
    assert verify_certificate(correct, tiny)['residual'] == exact_residual
    report['passed']['same_tiny_perturbation_exact_api'] = correct

    bad_normalization = root.certify(root.validate_pairs(boundary_input()),
                                      [1 / 3, 1 / 3, 1 / 3, 0.0])
    report['confirmed_root_api_failures']['serialized_float_normalization'] = {
        'serialized_sum': str(sum(F(v) for v in bad_normalization['candidate'])),
        'independent_verifier_rejection': rejection(
            lambda: verify_certificate(bad_normalization, boundary_input()))}

    # This is a real underflow: a scientific decimal string remains exact in R.
    underflow = root.equiprobable_input()
    small = F(1, 10**400)
    underflow['pairs'][0]['p'] = ['-0', '1e-400', '1/3', str(F(2, 3) - small)]
    Pu = root.validate_pairs(underflow)
    assert Pu[0][0][1] == small and float(Pu[0][0][1]) == 0.0
    underflow_cert = root.certify(Pu, [F(1, 4)] * 4)
    assert verify_certificate(underflow_cert, underflow)['residual'] == F(1, 24) - small / 8
    underflow_solve = root.solve(Pu)
    verify_certificate(underflow_solve, underflow)
    assert underflow_solve['tolerance_met']
    report['passed']['exact_scientific_string_and_float_underflow'] = {
        'tiny_coefficient': str(small), 'search_float': float(Pu[0][0][1]),
        'initial_exact_residual': underflow_cert['exact_residual_l1'],
        'certified_search_result': underflow_solve}

    # Invalid cases distinguish type errors, nonfiniteness, and exact constraints.
    invalid_inputs = {}
    mutations = [
        ('boolean probability', lambda d: d['pairs'][0]['p'].__setitem__(0, False)),
        ('boolean index', lambda d: d['pairs'][0].__setitem__('i', False)),
        ('JSON scientific number', lambda d: d['pairs'][0]['p'].__setitem__(0, 0e0)),
        ('nonfinite JSON number', lambda d: d['pairs'][0]['p'].__setitem__(0, float('nan'))),
        ('nonfinite exact string', lambda d: d['pairs'][0]['p'].__setitem__(0, 'Infinity')),
        ('negative coefficient with unit sum', lambda d: d['pairs'][0].__setitem__('p', ['0', '-1/4', '1/4', '1'])),
        ('unit sum off by 10^-30', lambda d: d['pairs'][0]['p'].__setitem__(1, str(F(1, 3) + F(1, 10**30)))),
        ('duplicate pair', lambda d: d['pairs'].__setitem__(9, copy.deepcopy(d['pairs'][0]))),
    ]
    for name, mutate in mutations:
        data = root.equiprobable_input()
        mutate(data)
        invalid_inputs[name] = rejection(lambda: root.validate_pairs(data))
        rejection(lambda: hardened.validate_pairs(data))
    scientific = root.equiprobable_input()
    scientific['pairs'][0]['p'] = ['-0', '2.5e-1', '2.5E-1', '+5e-1']
    assert root.validate_pairs(scientific)[0][0] == [F(0), F(1, 4), F(1, 4), F(1, 2)]
    report['passed']['invalid_exact_inputs_rejected'] = invalid_inputs

    valid_P = root.validate_pairs(root.equiprobable_input())
    parameter_failures = {}
    for label, tolerance in [('bool', True), ('positive infinity', float('inf')),
                             ('NaN', float('nan')), ('ordinary float', 1e-8)]:
        result = root.solve(valid_P, tolerance, max_steps=0)
        parameter_failures[label] = {'root_requested_tolerance': result['requested_tolerance'],
                                     'root_tolerance_met': result['tolerance_met'],
                                     'hardened_rejection': rejection(
                                         lambda: hardened.solve(valid_P, tolerance, max_steps=0))}
    parameter_failures['boolean digits'] = {
        'root_accepted': bool(root.solve(valid_P, digits=True, max_steps=0)),
        'hardened_rejection': rejection(lambda: hardened.solve(valid_P, digits=True, max_steps=0))}
    parameter_failures['boolean max_steps'] = {
        'root_accepted': bool(root.solve(valid_P, max_steps=True)),
        'hardened_rejection': rejection(lambda: hardened.solve(valid_P, max_steps=True))}
    report['confirmed_root_api_failures']['invalid_settings_accepted'] = parameter_failures

    # The positive l1 error bound is compared with epsilon exactly, including equality.
    base = root.solve(valid_P, F(2), digits=1, max_steps=0)
    radius = F(base['certified_error_l1_upper'])
    assert radius == F(5, 3)
    exact_threshold = root.solve(valid_P, radius, digits=1, max_steps=0)
    below_threshold = root.solve(valid_P, radius - F(1, 10**100), digits=1, max_steps=0)
    finite_failure = root.solve(valid_P, F(1, 10), digits=1, max_steps=7)
    for result in (exact_threshold, below_threshold, finite_failure):
        verify_certificate(result, root.equiprobable_input())
    assert exact_threshold['tolerance_met'] and not below_threshold['tolerance_met']
    assert not finite_failure['tolerance_met'] and finite_failure['search_step'] == 0
    report['passed']['exact_stopping_and_best_candidate'] = {
        'at_threshold': exact_threshold, 'just_below_threshold': below_threshold,
        'grid_resolution_failure': finite_failure}

    edge = [CAP, CAP, F(1, 5), F(0)]
    edge_cert = root.certify(valid_P, edge)
    verify_certificate(edge_cert, root.equiprobable_input())
    outside = [CAP + F(1, 10**30), CAP - F(1, 10**30), F(1, 5), F(0)]
    cap_rejection = rejection(lambda: root.certify(valid_P, outside))
    grid_cases = []
    for x, digits in [([.25] * 4, 1), ([.25] * 4, 30),
                      ([.4, .2, .2, .2], 12), ([5e-324] * 4, 12),
                      ([1e308] * 4, 12)]:
        rounded = root.rational_simplex_candidate(x, digits)
        assert rounded == hardened.rational_simplex_candidate(x, digits)
        assert sum(rounded) == 1 and min(rounded) >= 0
        assert all((v * 10**digits).denominator == 1 for v in rounded)
        grid_cases.append({'digits': digits, 'input_float_repr': repr(x),
                           'candidate': [str(v) for v in rounded]})
    report['passed']['exact_cap_and_largest_remainders'] = {
        'on_cap': edge_cert, 'outside_cap_rejection': cap_rejection,
        'normalization_cases': grid_cases}

    # A valid certificate must be bound to the supplied coefficient array.
    standalone = hardened.certify(valid_P, edge)
    corruption = {}
    for name, mutate in [
        ('residual changed', lambda r: r.__setitem__('exact_residual_l1', '0')),
        ('error changed', lambda r: r.__setitem__('certified_error_l1_upper', '0')),
        ('interval narrowed', lambda r: r['coordinate_intervals'][0].__setitem__(1, '1/10')),
        ('cap changed', lambda r: r.__setitem__('cap', '1/2')),
        ('forbidden offspring', lambda r: r['operator']['pairs'][0].__setitem__('p', ['1', '0', '0', '0'])),
    ]:
        damaged = copy.deepcopy(standalone)
        mutate(damaged)
        corruption[name] = rejection(lambda: verify_certificate(damaged))
    corruption['operator substitution with external input'] = rejection(
        lambda: verify_certificate(standalone, tiny))
    corruption['root record without coefficient input'] = rejection(lambda: verify_certificate(edge_cert))
    report['passed']['independent_verifier_detects_tampering_or_missing_binding'] = corruption

    invalid_array = copy.deepcopy(valid_P)
    invalid_array[0][1][2] = F(1)
    invalid_array[0][1][3] = F(0)
    array_validation = {'asymmetric array': rejection(lambda: hardened.certify(invalid_array, edge))}
    float_array = [[[float(v) for v in row] for row in plane] for plane in valid_P]
    array_validation['float coefficient array'] = rejection(lambda: hardened.certify(float_array, edge))
    report['passed']['hardened_array_preconditions_enforced'] = array_validation

    # Meaningful end-to-end status and JSON checks, without shared file writes.
    cli = []
    for path in (root_path, patched_path):
        for options, expected in [([], 0), (['--digits', '1', '--max-steps', '0', '--tolerance', '1e-8'], 2)]:
            completed = subprocess.run([sys.executable, str(path), *options],
                                       text=True, capture_output=True, check=False)
            assert completed.returncode == expected and not completed.stderr
            output = json.loads(completed.stdout)
            verify_certificate(output, root.equiprobable_input())
            cli.append({'module': path.name, 'options': options,
                        'exit_status': completed.returncode,
                        'tolerance_met': output['tolerance_met']})
    report['passed']['command_line_statuses'] = cli
    report['status'] = 'All audit assertions passed; listed root public-API failures were reproduced.'
    report['scope'] = ('Exact finite certificate arithmetic and focused interface cases. '
                       'The global error guarantee uses the analytic four-type theorem; '
                       'there is no formal proof or universal numerical-convergence claim.')
    return report


if __name__ == '__main__':
    report = run_audit()
    output = HERE / '026_qso_audit_results.json'
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': report['status'],
                      'passed_groups': len(report['passed']),
                      'confirmed_failure_groups': len(report['confirmed_root_api_failures']),
                      'output': str(output)}))
