"""Independent small-matrix audit of the round-4 local inverse and remainder."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import ctypes
import json
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (100, 100))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15
import numpy as np
np.seterr(all='raise')
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(980515)

def mm(a, b):
    return np.einsum('ij,jk->ik', a, b, optimize=False)

def comm(a, b):
    return mm(a, b)-mm(b, a)

def norm(a):
    return float(np.linalg.norm(a, 2))

def unitary(a):
    e, u = np.linalg.eigh(1j*a)
    return mm(u*np.exp(-1j*e), u.conj().T)

rows = []
for d in (1, 2, 4, 8):
    for kind in ('interlaced', 'degenerate', 'separated'):
        up, _ = np.linalg.qr(rng.normal(size=(d, d)))
        um, _ = np.linalg.qr(rng.normal(size=(d, d)))
        if kind == 'interlaced':
            ep, em = 2*np.arange(d), 2*np.arange(d)+1
        elif kind == 'degenerate':
            ep, em = np.full(d, 3.), np.full(d, -2.)
        else:
            ep, em = rng.uniform(1, 4, d), rng.uniform(-4, -1, d)
        kp, km = mm(up*ep, up.T), mm(um*em, um.T)
        gap = float(np.min(np.abs(ep[:, None]-em[None, :])))
        eps = .02*gap
        # Primary construction: solve in the product basis, without eigenvectors.
        sylvester = np.kron(kp, np.eye(d))-np.kron(np.eye(d), km.T)
        b = np.linalg.solve(sylvester, (eps*np.eye(d)).ravel()).reshape(d, d)
        # Separate spectral construction checks the inverse and its sign.
        bs = mm(mm(up, eps*mm(up.T, um)/(ep[:, None]-em[None, :])), um.T)
        H = np.zeros((2*d, 2*d))
        H[:d, :d], H[d:, d:] = kp, km
        V = np.block([[np.zeros((d, d)), eps*np.eye(d)],
                      [eps*np.eye(d), np.zeros((d, d))]])
        A = np.block([[np.zeros((d, d)), b], [-b.T, np.zeros((d, d))]])
        u = unitary(A)
        R = mm(mm(u, H+V), u.conj().T)-H
        Q = comm(A, V)/2
        a = norm(A)
        residual = norm(comm(H, A)-V)
        spectral_error = norm(b-bs)
        remainder = norm(R-Q)
        assert residual < 1e-11 and spectral_error < 1e-11
        assert a <= np.sqrt(8/3)*eps/gap+1e-12
        assert norm(R) <= a*eps+1e-11
        assert remainder <= 4/3*a*a*eps+1e-11
        Z = np.diag([1.]*d+[-1.]*d)
        dressed = mm(mm(u.conj().T, Z), u)
        assert norm(comm(H+V, dressed)) <= 8/3*a*a*eps+1e-11
        rows.append(dict(d=d, kind=kind, inverse_residual=residual,
                         spectral_error=spectral_error,
                         cubic_ratio=remainder/(a*a*eps)))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == 'darwin' else rss*1024
assert rss < 1_000_000_000
result = dict(status='PASS', cases=rows, count=len(rows),
              max_inverse_residual=max(r['inverse_residual'] for r in rows),
              max_spectral_error=max(r['spectral_error'] for r in rows),
              nice_value=priority, peak_rss_bytes=rss,
              elapsed_seconds=time.monotonic()-started)
(ROOT/'previous_audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
