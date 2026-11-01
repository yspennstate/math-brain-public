"""Small, exact proof controls; no simulations, model loads, GPU, or live writes."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import product
from math import comb, erf, exp, sqrt, factorial, pi
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    value = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            value = -value
        value *= a[i][i]
        for j in range(i + 1, len(a)):
            factor = a[j][i] / a[i][i]
            a[j][i] = 0
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return value


def gram(a):
    return [[Q(sum(r[k] * s[k] for k in range(len(r)))) for s in a] for r in a]


def event_by_sylvester(b, t):
    # lambda_min(B B^T)<=t^2 iff B B^T-t^2 I is not positive definite.
    g = gram(b)
    for i in range(len(g)):
        g[i][i] -= t * t
    return any(determinant([r[:k] for r in g[:k]]) <= 0
               for k in range(1, len(g) + 1))


def hadamard(n):
    h = [[1]]
    while len(h) < n:
        h = [r + r for r in h] + [r + [-x for x in r] for r in h]
    assert len(h) == n
    return h


def fresh_gate():
    p = Path('~/.claude/compute/compute_state.json')
    s = json.loads(p.read_text(encoding='utf-8-sig'))
    age = time.time() - p.stat().st_mtime
    gate = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
            'source': str(p), 'age_seconds': age, 'mode': s.get('mode'),
            'scope': 'one CPU, standard-library exact arithmetic, n<=8, <=256 sign vectors; no experiments or training'}
    gate['governor_status'] = s.get('status')
    gate['cpu_pct'] = s.get('cpu_pct')
    gate['hung_windows'] = s.get('hung_windows')
    gate['reason_for_polite_scope'] = 'COMPUTE_DOCTRINE.md lines 8-13 permits local testing; only the bounded scalar proof controls run in owner_present_polite mode.'
    if (age < -10 or age > 90
            or s.get('mode') not in ('normal', 'ok', 'healthy', 'warn', 'owner_present_polite')
            or s.get('status') in ('distress', 'throttle')
            or s.get('hung_windows', 0)
            or any('critical' in r for r in s.get('reasons', []))):
        gate['status'] = 'BLOCKED'
        (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
        raise SystemExit('Fresh resource gate does not permit even the bounded check; receipt saved.')
    gate['status'] = 'ALLOW_BOUNDED_PROOF_CHECK'
    (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
    return gate


def main():
    gate = fresh_gate()
    started = time.perf_counter()
    cpu_started = time.process_time()
    assert sum(a == b for a, b in product((-1, 1), repeat=2)) == 2
    hadamard_controls = []
    for n in (2, 4, 8):
        h = hadamard(n)
        assert gram(h) == [[Q(n if i == j else 0) for j in range(n)] for i in range(n)]
        hits = sum(sum(a * b for a, b in zip(x, h[-1])) == 0
                   for x in product((-1, 1), repeat=n))
        assert hits == comb(n, n // 2)
        assert Q(hits, 2 ** n) >= Q(1, n + 1)
        hadamard_controls.append({'n': n, 'zero_atom': str(Q(hits, 2 ** n)), 'count': hits})
    h = hadamard(4)
    a, v = h[:-1], h[-1]
    xs = list(product((-1, 1), repeat=4))
    z2 = [Q(sum(xx * vv for xx, vv in zip(x, v)), 2) ** 2 for x in xs]
    assert Counter(z2) == {Q(0): 6, Q(1): 8, Q(4): 2}
    threshold_controls = 0
    for t in (Q(0), Q(1, 2), Q(3, 4), Q(1), Q(3, 2), Q(2)):
        for x, y in zip(xs, z2):
            expected = y == 0 if t == 0 else (
                True if t >= 2 else y <= t * t * (1 + (4 - y) / (4 - t * t)))
            assert event_by_sylvester(a + [list(x)], t) == expected
            threshold_controls += 1
    # Exact equality boundary, plus the rank-deficient A branch.
    assert event_by_sylvester([[2, 0], [0, 1]], Q(1))
    assert not event_by_sylvester([[2, 0], [0, 1]], Q(1, 2))
    for x in product((-1, 1), repeat=3):
        assert event_by_sylvester([[1, 1, 1], [1, 1, 1], list(x)], Q(0))
    t = Q(3, 4)
    r2 = [t * t * (1 + (4 - y) / (4 - t * t)) for y in z2]
    true_probability = Q(sum(y <= r for y, r in zip(z2, r2)), 16)
    independent_probability = Q(sum(y <= r for y in z2 for r in r2), 256)
    assert true_probability == Q(7, 8)
    assert independent_probability == Q(13, 16)
    a6 = [[-1 if i == j else 1 for j in range(5)] + [1] for i in range(5)]
    assert gram(a6) == [[Q(6 if i == j else 2) for j in range(5)] for i in range(5)]
    joint6 = Counter()
    radius6 = Counter()
    y6 = Counter()
    true_hits6 = 0
    for x in product((-1, 1), repeat=6):
        s, eta = sum(x[:5]), x[5]
        y = Q((s - 3 * eta) ** 2, 14)
        b = Q((3 * s + 5 * eta) ** 2, 70)
        radius = Q(9, 64) + Q(9, 887) * b + Q(9, 247) * (6 - y - b)
        assert radius < Q(8, 7)
        assert event_by_sylvester(a6 + [list(x)], Q(3, 8)) == (y <= radius)
        threshold_controls += 1
        true_hits6 += y <= radius
        joint6[(y, b)] += 1
        radius6[radius] += 1
        y6[y] += 1
    assert joint6 == {(Q(2, 7), Q(40, 7)): 2, (Q(0), Q(14, 5)): 10,
                      (Q(2, 7), Q(32, 35)): 20, (Q(8, 7), Q(2, 35)): 20,
                      (Q(18, 7), Q(8, 35)): 10, (Q(32, 7), Q(10, 7)): 2}
    assert Q(2, 7) - (Q(9, 64) + Q(126, 4435) + Q(144, 1235)) == Q(39125, 490759360)
    true6 = Q(true_hits6, 64)
    independent6 = Q(sum(cy * cr for y, cy in y6.items() for r, cr in radius6.items() if y <= r), 4096)
    assert true6 == Q(15, 32)
    assert independent6 == Q(95, 256)
    # Independently integrate the normal density by its convergent Taylor series.
    series = sum(Q((-1) ** k, (2 ** k) * factorial(k) * (2 * k + 1)) for k in range(18))
    actual_gaussian_n1 = sqrt(2 / pi) * float(series)
    series_remainder_bound = sqrt(2 / pi) / ((2 ** 18) * factorial(18) * 37)
    incorrectly_exact_limit = 1 - exp(-Q(3, 2))
    assert abs(actual_gaussian_n1 - incorrectly_exact_limit) > 0.09
    corrected_gaussian_n1 = erf(1 / sqrt(2))
    assert abs(actual_gaussian_n1 - corrected_gaussian_n1) < 3e-15
    receipt = {
        'status': 'PASS', 'command': 'python -X utf8 ~/brain_workers/w565/verify_exact.py',
        'gate': gate, 'elapsed_seconds': time.perf_counter() - started,
        'cpu_seconds': time.process_time() - cpu_started,
        'hadamard_controls': hadamard_controls,
        'threshold_controls_exact': threshold_controls,
        'boundary_and_rank_controls_exact': 10,
        'dependent_radius_probability': str(true_probability),
        'independent_radius_probability': str(independent_probability),
        'underestimate': str(true_probability - independent_probability),
        'n6_nontrivial_scale': {
            'epsilon_squared': '27/32', 'true_probability': str(true6),
            'independent_radius_probability': str(independent6),
            'underestimate': str(true6 - independent6),
            'joint_classes': [{'y': str(y), 'b': str(b), 'count': c} for (y, b), c in joint6.items()]},
        'gaussian_n1_t1': {
            'true_cdf': actual_gaussian_n1, 'old_claim_value': incorrectly_exact_limit,
            'before_absolute_error': abs(actual_gaussian_n1 - incorrectly_exact_limit),
            'corrected_finite_n_expression': 'erf(t/sqrt(2)) at n=1; fixed-t limit as n->infinity in general',
            'after_absolute_error_at_control': abs(actual_gaussian_n1 - corrected_gaussian_n1)},
        'gaussian_series_truncation_bound': series_remainder_bound,
        'limits': 'Finite controls are not a proof of the parent conjecture or of all-n statements; proofs and external review are separate.'}
    (ROOT / 'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
