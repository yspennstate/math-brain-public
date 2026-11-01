"""Small foreground algebra checks; numerical checks are not proof receipts."""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import itertools
import json
import math
import time
from pathlib import Path
from fractions import Fraction
import numpy as np

ROOT = Path(__file__).resolve().parent
gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
started = time.perf_counter()
checks = {}

def cap():
    if time.perf_counter() - started > gate['max_wall_seconds_after_import']:
        raise RuntimeError('compute gate exceeded; do not broaden')

def exact_det(a):
    a = [[Fraction(int(v)) for v in row] for row in a]
    n = len(a)
    result = Fraction(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            result = -result
        pivot = a[j][j]
        result *= pivot
        for k in range(j + 1, n):
            ratio = a[k][j] / pivot
            for l in range(j + 1, n):
                a[k][l] -= ratio * a[j][l]
    assert result.denominator == 1
    return int(result)

rng = np.random.default_rng(29)
max_inverse_residual = 0.0
min_gap_ratio = float('inf')
inverse_count = 0
for i in range(gate['max_random_matrices']):
    cap()
    n = 2 + i % 5
    b = rng.choice([-1, 1], size=(n, n))
    dr = b[:, 0] * b[0, 0]
    dc = b[0, :]
    c = dr[:, None] * b * dc[None, :]
    assert np.all(c[0, :] == 1) and np.all(c[:, 0] == 1)
    h = (1 - c[1:, 1:]) // 2
    d_b, d_c, d_h = exact_det(b), exact_det(c), exact_det(h)
    assert d_c == (-2) ** (n - 1) * d_h
    assert d_b % (2 ** (n - 1)) == 0
    assert np.allclose(np.linalg.svd(b, compute_uv=False),
                       np.linalg.svd(c, compute_uv=False), atol=1e-12)
    if d_h:
        alpha = (2 * math.sqrt(n - 1) / n) ** (n - 1)
        ratio = np.linalg.svd(b, compute_uv=False)[-1] / alpha
        min_gap_ratio = min(min_gap_ratio, float(ratio))
        assert ratio >= 1 - 1e-12
        inv_h = np.linalg.inv(h.astype(float))
        e = np.ones(n - 1)
        k = np.empty((n, n))
        k[0, 0] = 1 - .5 * e @ inv_h @ e
        k[0, 1:] = .5 * e @ inv_h
        k[1:, 0] = .5 * inv_h @ e
        k[1:, 1:] = -.5 * inv_h
        residual = float(np.max(np.abs(c @ k - np.eye(n))))
        max_inverse_residual = max(max_inverse_residual, residual)
        assert residual < 1e-11
        inverse_count += 1
checks['random_algebra'] = {'matrices': gate['max_random_matrices'],
    'n_range': [2, 6], 'nonsingular_inverse_checks': inverse_count,
    'max_inverse_residual': max_inverse_residual,
    'min_smin_over_arithmetic_bound': min_gap_ratio}

# Full n=2 population verifies the gauge's multiplicities, not merely its marginals.
interiors = {-1: 0, 1: 0}
singular_count = 0
for signs in itertools.product([-1, 1], repeat=4):
    cap()
    b = np.array(signs).reshape(2, 2)
    c = (b[:, 0] * b[0, 0])[:, None] * b * b[0, :][None, :]
    interiors[int(c[1, 1])] += 1
    singular_count += exact_det(b) == 0
assert interiors == {-1: 8, 1: 8} and singular_count == 8
checks['exact_n2'] = {'population': 16, 'interior_counts': interiors,
                      'singular_count': singular_count}

# Exercise both sides of the Schur criterion, equality, t=0 and an excluded endpoint.
r = np.array([[2., 0., 0.], [0., 3., 0.]])
crossings = []
for t in [.25, 1., 1.9]:
    threshold = t * math.sqrt(1 + .25 / (4 - t*t) + 1 / (9 - t*t))
    for factor in [.8, 1., 1.2]:
        cap()
        a = factor * threshold
        matrix = np.vstack([r, [.5, 1., a]])
        smin = float(np.linalg.svd(matrix, compute_uv=False)[-1])
        if factor < 1:
            assert smin < t
        elif factor > 1:
            assert smin > t
        else:
            assert abs(smin - t) < 1e-12
        crossings.append({'t': t, 'factor': factor, 'smin': smin})
for a in [0., 1.]:
    assert (exact_det(np.vstack([r, [0., 0., a]])) == 0) == (a == 0)
checks['schur_crossings'] = crossings
checks['schur_endpoint'] = {'t': 2, 'admissible': False,
                           'reason': 'd_min-t^2 is zero'}

q = np.array([[1, 1], [1, -1]])
hadamard = []
for n in [2, 4, 8]:
    cap()
    if n > 2:
        q = np.block([[q, q], [q, -q]])
    assert np.array_equal(q @ q.T, n * np.eye(n, dtype=int))
    assert np.array_equal(q[1:] @ np.ones(n, dtype=int), np.zeros(n - 1))
    zero_count = math.comb(n, n // 2)
    assert zero_count * (n + 1) >= 2**n
    hadamard.append({'n': n, 'zero_count': zero_count,
                    'population': 2**n, 'conditional_atom': zero_count / 2**n})
checks['hadamard_obstruction'] = hadamard

t = .1
true_n1 = math.erf(t / math.sqrt(2))
limiting = 1 - math.exp(-t - t*t/2)
assert abs(true_n1 - limiting) > .01
checks['gaussian_correction'] = {'n': 1, 't': t, 'true_cdf': true_n1,
    'misstated_finite_cdf': limiting, 'absolute_error': abs(true_n1-limiting),
    'true_slope_at_zero': math.sqrt(2/math.pi), 'limiting_slope_at_zero': 1}
cap()
receipt = {'gate': 'COMPUTE_GATE.json', 'status': 'PASS',
           'elapsed_s_after_import': round(time.perf_counter()-started, 6),
           'checks': checks, 'formal_proof': False,
           'independent_review': 'PENDING w569'}
(ROOT / 'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
