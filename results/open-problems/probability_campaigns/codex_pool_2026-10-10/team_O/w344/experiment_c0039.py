"""Finite S3 DPP optimal Hamming couplings; evidence, not a general proof."""
import os
for option in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[option] = '1'
import itertools
import json
import pathlib
import time
import warnings
import numpy as np
from scipy import sparse
from scipy.optimize import linprog, OptimizeWarning

HERE = pathlib.Path(__file__).resolve().parent
started = time.perf_counter()
group = list(itertools.permutations(range(3)))
index = {g: i for i, g in enumerate(group)}
def mul(a, b):
    return tuple(a[b[j]] for j in range(3))
def inverse(a):
    return tuple(a.index(j) for j in range(3))
basis = []
left = []
for a in group:
    right_a = np.zeros((6, 6))
    left_a = np.zeros((6, 6))
    for i, g in enumerate(group):
        right_a[index[mul(g, a)], i] = 1
        left_a[index[mul(a, g)], i] = 1
    basis.append((right_a + right_a.T) / 2)
    left.append(left_a)
identity = np.eye(6)
cost = np.array([[(a ^ b).bit_count() / 6 for b in range(64)] for a in range(64)])
constraints = sparse.vstack([
    sparse.kron(sparse.eye(64), np.ones((1, 64))),
    sparse.kron(np.ones((1, 64)), sparse.eye(64)),
], format='csr')
def distribution(q):
    lkernel = np.linalg.solve(identity - q, q)
    normalizer = np.linalg.det(identity - q)
    out = []
    for mask in range(64):
        chosen = [i for i in range(6) if mask >> i & 1]
        out.append(normalizer * (np.linalg.det(lkernel[np.ix_(chosen, chosen)]) if chosen else 1.0))
    out = np.array(out)
    assert out.min() >= -1e-12 and abs(out.sum() - 1) < 1e-10
    for i in range(6):
        assert abs(sum(out[s] for s in range(64) if s >> i & 1) - q[i, i]) < 1e-10
    return out
def compare(q, r, name):
    p, pprime = distribution(q), distribution(r)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', OptimizeWarning)
        result = linprog(cost.ravel(), A_eq=constraints, b_eq=np.r_[p, pprime], bounds=(0, None), method='highs', options={'time_limit': 15, 'threads': 1})
    assert result.success, result.message
    trace_norm = np.abs(np.linalg.eigvalsh(q - r)).sum() / 6
    primal_residual = np.max(np.abs(constraints @ result.x - np.r_[p, pprime]))
    dual_value = float(np.r_[p, pprime] @ result.eqlin.marginals)
    dual_violation = max(0., float(np.max(constraints.T @ result.eqlin.marginals - cost.ravel())))
    assert primal_residual < 1e-8 and abs(result.fun - dual_value) < 1e-8 and dual_violation < 1e-8
    assert max(np.linalg.norm(a @ q - q @ a) for a in left) < 1e-10
    assert max(np.linalg.norm(a @ r - r @ a) for a in left) < 1e-10
    return {'name': name, 'dbar_lp': float(result.fun), 'normalized_trace_norm': float(trace_norm), 'ratio': float(result.fun / trace_norm), 'commutator_frobenius': float(np.linalg.norm(q @ r - r @ q)), 'primal_residual': float(primal_residual), 'dual_gap': float(abs(result.fun - dual_value)), 'dual_violation': dual_violation}

rng = np.random.default_rng(344)
def random_kernel():
    raw = sum(float(x) * a for x, a in zip(rng.normal(size=6), basis))
    raw /= np.max(np.abs(np.linalg.eigvalsh(raw)))
    return .5 * identity + .4 * raw
records = []
output = HERE / 'c0039_measurements.jsonl'
with output.open('w', encoding='utf-8') as file:
    for i in range(12):
        record = compare(random_kernel(), random_kernel(), f'noncommuting-{i:02d}')
        assert record['commutator_frobenius'] > 1e-8
        records.append(record)
        file.write(json.dumps(record) + '\n')
        file.flush()
    control = compare(.3 * identity, .7 * identity, 'commuting-equality-control')
    assert abs(control['ratio'] - 1) < 1e-8
    records.append(control)
    file.write(json.dumps(control) + '\n')
summary = {'seed': 344, 'noncommuting_pairs': 12, 'controls': 1, 'lp_variables': 4096, 'max_noncommuting_ratio': max(r['ratio'] for r in records[:-1]), 'counterexamples_found': sum(r['dbar_lp'] > r['normalized_trace_norm'] + 1e-8 for r in records), 'max_primal_residual': max(r['primal_residual'] for r in records), 'max_dual_gap': max(r['dual_gap'] for r in records), 'seconds': time.perf_counter() - started, 'scope': 'finite real symmetric S3-equivariant kernels, spectra in [0.1,0.9]; numerical evidence only'}
(HERE / 'c0039_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(json.dumps(summary))
