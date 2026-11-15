"""Independent full-Hamiltonian check of the frozen-field cancellation.

No old script is imported. Dimensions are at most 128, all writes local.
"""
import os
KEYS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
        'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for key in KEYS:
    os.environ[key] = '1'
import ctypes
from itertools import product
from pathlib import Path
import json
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
counts, maxima = {}, {}


def count(key):
    counts[key] = counts.get(key, 0)+1


def record(key, err):
    err = abs(float(err))
    assert np.isfinite(err) and err < 2e-10, (key, err)
    maxima[key] = max(maxima.get(key, 0.), err)


def mm(a, b):
    return np.einsum('ij,jk->ik', a, b, optimize=False)


def signs(k, n):
    return tuple(1-2*((k >> (n-1-i)) & 1) for i in range(n))


def ham(h, g, J):
    n = len(h)
    H = np.zeros((2**n, 2**n))
    for k in range(2**n):
        s = signs(k, n)
        H[k, k] = sum(h[i]*s[i] for i in range(n))
        H[k, k] += sum(J[i]*s[i]*s[i+1] for i in range(n-1))
        for i in range(n):
            H[k ^ (1 << (n-1-i)), k] = g[i]
    return H


def blocks(mask):
    ans = []
    for i, active in enumerate(mask):
        if active:
            if i and mask[i-1]:
                ans[-1].append(i)
            else:
                ans.append([i])
    return ans


def sector_energies(h, g, J, mask):
    """Direct full-H sector expectation in tensor-product block eigenvectors."""
    H = ham(h, g, J)
    n = len(mask)
    frozen = [f for f in range(n) if not mask[f]]
    bb = blocks(mask)
    out = {}
    for ss in product((1, -1), repeat=len(frozen)):
        eta = dict(zip(frozen, ss))
        U = np.ones((1, 1))
        for B in bb:
            lo, hi = B[0], B[-1]
            hh = h[lo:hi+1].copy()
            if lo:
                hh[0] += J[lo-1]*eta[lo-1]
            if hi+1 < n:
                hh[-1] += J[hi]*eta[hi+1]
            _, v = np.linalg.eigh(ham(hh, g[lo:hi+1], J[lo:hi]))
            U = np.kron(U, v)
        indices = [k for k in range(2**n)
                   if all(signs(k, n)[f] == eta[f] for f in frozen)]
        K = H[np.ix_(indices, indices)]
        D = mm(mm(U.T, K), U)
        record('sector_offdiagonal', np.linalg.norm(D-np.diag(np.diag(D)), 'fro'))
        record('sector_full_spectrum', np.max(np.abs(
            np.sort(np.diag(D))-np.linalg.eigvalsh(K))))
        labels = list(product(*(range(2**len(B)) for B in bb)))
        out[ss] = dict(zip(labels, np.diag(D)))
        count('full_H_sectors')
    return out


def local_spectra(h, g, J, mask, f, eta):
    lo = hi = f
    while lo and mask[lo-1]:
        lo -= 1
    while hi+1 < len(mask) and mask[hi+1]:
        hi += 1
    hh = h[lo:hi+1].copy()
    hh[f-lo] = 0
    if lo:
        hh[0] += J[lo-1]*eta[lo-1]
    if hi+1 < len(mask):
        hh[-1] += J[hi]*eta[hi+1]
    H = ham(hh, g[lo:hi+1], J[lo:hi])
    out = []
    for sf in (1, -1):
        idx = [k for k in range(len(H)) if signs(k, hi-lo+1)[f-lo] == sf]
        out.append(np.linalg.eigvalsh(H[np.ix_(idx, idx)]))
    return out


rng = np.random.default_rng(981106)
masks = ((0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0),
         (1, 0, 1, 0, 1, 0, 1), (0, 0, 0))
for mask in masks:
    n = len(mask)
    h = rng.uniform(-2, 2, n)
    g = rng.uniform(.1, .6, n)*mask
    J = rng.uniform(-.7, .7, n-1)
    frozen = [f for f in range(n) if not mask[f]]
    bb = blocks(mask)
    base = sector_energies(h, g, J, mask)
    # A completely new frozen-field sample must shift every energy by only
    # its frozen scalar. Active eigenvectors and all offset sets stay fixed.
    hp = h.copy()
    hp[frozen] += rng.uniform(-4, 4, len(frozen))
    shifted = sector_energies(hp, g, J, mask)
    for ss in base:
        shift = sum((hp[f]-h[f])*s for f, s in zip(frozen, ss))
        for labels in base[ss]:
            record('frozen_scalar_shift', shifted[ss][labels]-base[ss][labels]-shift)
            count('frozen_scalar_checks')
    for f in frozen:
        adjacent = [j for j, B in enumerate(bb)
                    if B[-1] == f-1 or B[0] == f+1]
        spectators = [j for j in range(len(bb)) if j not in adjacent]
        rest = [z for z in frozen if z != f]
        for outer_signs in product((1, -1), repeat=len(rest)):
            eta = dict(zip(rest, outer_signs))
            sp = tuple(1 if z == f else eta[z] for z in frozen)
            sm = tuple(-1 if z == f else eta[z] for z in frozen)
            ep, em = local_spectra(h, g, J, mask, f, eta)
            predicted = np.sort((2*h[f]+ep[:, None]-em[None, :]).ravel())
            ep2, em2 = local_spectra(hp, g, J, mask, f, eta)
            record('local_offsets_ignore_frozen_fields', np.max(np.abs(ep-ep2)))
            record('local_offsets_ignore_frozen_fields', np.max(np.abs(em-em2)))
            for spec in product(*(range(2**len(bb[j])) for j in spectators)):
                specdict = dict(zip(spectators, spec))
                labs = [lab for lab in base[sp]
                        if all(lab[j] == val for j, val in specdict.items())]
                direct = np.sort([base[sp][a]-base[sm][b]
                                  for a, b in product(labs, repeat=2)])
                direct2 = np.sort([shifted[sp][a]-shifted[sm][b]
                                   for a, b in product(labs, repeat=2)])
                record('local_vs_full_transition_offsets', np.max(np.abs(direct-predicted)))
                record('other_frozen_fields_cancel', np.max(np.abs(
                    direct2-direct-2*(hp[f]-h[f]))))
                count('full_transition_multisets')
    count('physical_masks')

rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss_raw if sys.platform == 'darwin' else 1024*rss_raw
assert rss < 1_000_000_000
result = dict(status='PASS', counts=counts, residual_maxima=maxima,
              largest_matrix_dimension=max(2**len(mask) for mask in masks),
              nice_value=priority, thread_environment={k: os.environ[k] for k in KEYS},
              peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-started)
(ROOT/'conditioning_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
