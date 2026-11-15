"""Independent sector-tensor audit of the earlier exact-barrier claim."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import ctypes
import itertools as it
import json
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (100, 100))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15
import numpy as np
np.seterr(all='raise')
start = time.monotonic()
root = Path(__file__).resolve().parent
I = np.eye(2)
X = np.array([[0., 1.], [1., 0.]])
Z = np.diag([1., -1.])

def mul(a, b):
    return np.einsum('ij,jk->ik', a, b, optimize=False)

def tensor(factors):
    out = np.ones((1, 1))
    for a in factors:
        out = np.kron(out, a)
    return out

def onsite(a, i, n):
    return tensor([a if j == i else I for j in range(n)])

def runs(mask):
    return [tuple(g) for val, group in it.groupby(range(len(mask)), key=lambda i: mask[i])
            if val for g in [list(group)]]

def ham(h, g, J):
    n = len(h)
    if n == 0:
        return np.zeros((1, 1))
    out = sum(h[i]*onsite(Z, i, n)+g[i]*onsite(X, i, n) for i in range(n))
    for i, j in enumerate(J):
        out += j*tensor([Z if k in (i, i+1) else I for k in range(n)])
    return out

rng = np.random.default_rng(981115)
largest = 0.
matrix_cases = 0
for n in range(1, 6):
    configs = list(it.product((1, -1), repeat=n))
    for mask in it.product((0, 1), repeat=n):
        blocks = runs(mask)
        frozen = [i for i in range(n) if not mask[i]]
        h = rng.uniform(-3, 3, n)
        g = rng.uniform(-.6, .6, n)*mask
        J = rng.uniform(-1, 1, n-1)
        H = ham(h, g, J)
        U = np.zeros_like(H)
        # Assemble U separately in each frozen sector, by tensoring the
        # conditional block eigenvectors; no product of embedded gates.
        for signs in it.product((1, -1), repeat=len(frozen)):
            eta = dict(zip(frozen, signs))
            factors = []
            for block in blocks:
                hh = h[list(block)].copy()
                a, b = block[0], block[-1]
                if a > 0:
                    hh[0] += J[a-1]*eta[a-1]
                if b+1 < n:
                    hh[-1] += J[b]*eta[b+1]
                _, v = np.linalg.eigh(ham(hh, g[list(block)], J[a:b]))
                factors.append(v)
            active_u = tensor(factors)
            indices = [k for k, s in enumerate(configs)
                       if all(s[i] == eta[i] for i in frozen)]
            U[np.ix_(indices, indices)] = active_u
        D = mul(mul(U.T, H), U)
        residuals = [np.linalg.norm(mul(U.T, U)-np.eye(2**n), 'fro'),
                     np.linalg.norm(D-np.diag(np.diag(D)), 'fro')]
        for i in range(n):
            tau = mul(mul(U, onsite(Z, i, n)), U.T)
            residuals.append(np.linalg.norm(mul(H, tau)-mul(tau, H), 'fro'))
            if not mask[i]:
                residuals.append(np.linalg.norm(tau-onsite(Z, i, n), 'fro'))
        err = max(residuals)/max(1., np.linalg.norm(H, 'fro'))
        assert np.isfinite(err) and err < 1e-11
        largest = max(largest, float(err))
        matrix_cases += 1

# Count supports from padded block sets, then compare to a formula that uses
# only the availability of the two physical boundaries.
probability_checks = 0
for n in range(1, 9):
    for p in (Q(1, 5), Q(1, 2), Q(4, 5)):
        actual = {(i, r): Q(0) for i in range(n) for r in range(1, n+1)}
        for mask in it.product((0, 1), repeat=n):
            weight = p**sum(mask)*(1-p)**(n-sum(mask))
            padded = [set(range(max(0, b[0]-1), min(n, b[-1]+2))) for b in runs(mask)]
            for i in range(n):
                support = {i}.union(*(b for b in padded if i in b))
                radius = max(abs(j-i) for j in support)
                for r in range(1, radius):
                    actual[i, r] += weight
        for (i, r), prob in actual.items():
            sides = int(i > r) + int(n-1-i > r)
            assert prob == 1-(1-p**r)**sides
            assert prob <= 2*p**r-p**(2*r)
            probability_checks += 1

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
result = dict(status='PASS', matrix_cases=matrix_cases,
              largest_normalized_residual=largest,
              exact_probability_checks=probability_checks,
              exact_probability_error='0', nice_value=priority,
              peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-start)
(root/'earlier_audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
