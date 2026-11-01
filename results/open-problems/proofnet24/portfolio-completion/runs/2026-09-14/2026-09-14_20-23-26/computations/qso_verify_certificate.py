"""Independently recompute the finite arithmetic in a QSO residual certificate.

The mathematical error guarantee depends on FOUR_TYPE_UNIQUENESS.md.
This evaluator does not import the solver. Adapted from the independent026 audit.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
CAP=F(2,5)

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


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--operator', type=Path, help='Optional original operator to compare with the embedded array')
    args=parser.parse_args()
    try:
        record=json.loads(args.certificate.read_text())
        original=json.loads(args.operator.read_text()) if args.operator else None
        result=verify_certificate(record, original)
    except (ValueError,TypeError,KeyError,ArithmeticError,OSError) as exc:
        parser.error(str(exc))
    print(json.dumps({'status':'exact certificate verified',
                      'exact_residual_l1':str(result['residual']),
                      'certified_error_l1_upper':str(result['radius'])},indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
