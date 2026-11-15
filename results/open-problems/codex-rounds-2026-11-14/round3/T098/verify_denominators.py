"""Serial small-matrix and exact-rational checks for PROOF.md.

No sampling of the full MBL problem. All generated files stay beside this script.
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import ctypes
from fractions import Fraction as Q
import itertools as it
import json
from pathlib import Path
import resource
import signal
import time
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
    out = np.einsum('ij,jk->ik', a, b, optimize=False)
    assert np.all(np.isfinite(out))
    return out

def tensor(factors):
    out = np.ones((1, 1))
    for a in factors:
        out = np.kron(out, a)
    return out

def ham(h, g, J):
    n = len(h)
    if n == 0:
        return np.zeros((1, 1))
    out = np.zeros((2**n, 2**n))
    for i in range(n):
        out += tensor([h[i]*Z+g[i]*X if j == i else I for j in range(n)])
    for i, j in enumerate(J):
        out += j*tensor([Z if k in (i, i+1) else I for k in range(n)])
    return out

def bit_ham(h, g, J):
    n = len(h)
    out = np.zeros((2**n, 2**n))
    for k in range(2**n):
        s = [1-2*((k >> (n-1-i)) & 1) for i in range(n)]
        out[k, k] = sum(x*y for x, y in zip(h, s))
        out[k, k] += sum(J[i]*s[i]*s[i+1] for i in range(n-1))
        for i, v in enumerate(g):
            out[k, k ^ (1 << (n-1-i))] += v
    return out

def union_length(intervals, lo, hi):
    clipped = sorted((max(lo, a), min(hi, b)) for a, b in intervals
                     if max(lo, a) < min(hi, b))
    total = 0
    end = lo
    for a, b in clipped:
        total += max(0, b-max(a, end))
        end = max(end, b)
    return total

rng = np.random.default_rng(981116)
matrix_cases = 0
interval_checks = 0
max_spectrum_error = 0.
max_slope_error = 0.
max_difference_error = 0.
max_overlap_error = 0.
largest_dimension = 0
for a in range(4):
    for b in range(4):
        if a+b > 5:
            continue
        n, m, f = a+b+1, a+b, a
        for ends in it.product((False, True), repeat=2):
            h = rng.uniform(-2, 2, n)
            h[f] = 0
            g = rng.uniform(-.5, .5, n)
            g[f] = 0
            J = rng.uniform(-1, 1, n-1)
            outer_J = rng.uniform(-1, 1, 2)
            offsets = []
            for eta in it.product((1, -1), repeat=sum(ends)):
                hh = h.copy()
                ctr = iter(eta)
                if ends[0]:
                    hh[0] += outer_J[0]*next(ctr)
                if ends[1]:
                    hh[-1] += outer_J[1]*next(ctr)
                H = ham(hh, g, J)
                assert np.max(np.abs(H-bit_ham(hh, g, J))) < 1e-12
                vals, vecs, sectors = [], [], []
                for sign in (1, -1):
                    idx = [k for k in range(2**n)
                           if 1-2*((k >> b) & 1) == sign]
                    sectors.append(idx)
                    K = H[np.ix_(idx, idx)]
                    e, v = np.linalg.eigh(K)
                    vals.append(e)
                    vecs.append(v)
                    # Independent construction as a Kronecker sum of left
                    # and right block Hamiltonians plus the central scalar.
                    hl, hr = hh[:f].copy(), hh[f+1:].copy()
                    if a:
                        hl[-1] += J[f-1]*sign
                    if b:
                        hr[0] += J[f]*sign
                    el = np.linalg.eigvalsh(bit_ham(hl, g[:f], J[:max(0, f-1)]))
                    er = np.linalg.eigvalsh(bit_ham(hr, g[f+1:], J[f+1:]))
                    pred = np.sort((el[:, None]+er[None, :]+sign*hh[f]).ravel())
                    err = float(np.max(np.abs(e-pred)))
                    max_spectrum_error = max(max_spectrum_error, err)
                    assert err < 2e-11
                    for hf in (-.37, .71):
                        shifted = hh.copy()
                        shifted[f] += hf
                        Hshift = bit_ham(shifted, g, J)
                        es = np.linalg.eigvalsh(Hshift[np.ix_(idx, idx)])
                        err = float(np.max(np.abs(es-e-sign*hf)))
                        max_slope_error = max(max_slope_error, err)
                        assert err < 2e-11
                diff = (vals[0][:, None]-vals[1][None, :]).ravel()
                offsets.extend(diff.tolist())
                # Difference operator gives an independent list of all pairs.
                if m <= 3:
                    kp = H[np.ix_(sectors[0], sectors[0])]
                    km = H[np.ix_(sectors[1], sectors[1])]
                    T = np.kron(kp, np.eye(2**m))-np.kron(np.eye(2**m), km.T)
                    err = float(np.max(np.abs(np.linalg.eigvalsh(T)-np.sort(diff))))
                    max_difference_error = max(max_difference_error, err)
                    assert err < 2e-11
                overlap = mul(vecs[0].T, vecs[1])
                err = float(np.linalg.norm(mul(overlap.T, overlap)-np.eye(2**m), 'fro'))
                max_overlap_error = max(max_overlap_error, err)
                assert err < 2e-11
                largest_dimension = max(largest_dimension, 2**n)
                matrix_cases += 1
            assert len(offsets) == 2**sum(ends)*4**m
            for delta in (.0001, .01, .25, 4.):
                # Exact integration of the numerically computed interval union
                # for a uniform field; no Monte Carlo error.
                W = 4.
                prob = union_length([((-c-delta)/2, (-c+delta)/2) for c in offsets], -W, W)/(2*W)
                sharper = min(1., 2**sum(ends)*4**m*delta/(2*W))
                assert prob <= sharper+1e-12
                interval_checks += 1

# Empty adjacent blocks saturate the factor four for four distinct controls.
# h uniform on [-8,8], J_left=1, J_right=3, delta=1/4.
delta = Q(1, 4)
centers = [-Q(l)-3*Q(r) for l, r in it.product((1, -1), repeat=2)]
sat_prob = union_length([(c-delta/2, c+delta/2) for c in centers], Q(-8), Q(8))/16
assert sat_prob == 4*Q(1, 16)*delta == Q(1, 16)
# Full degeneracy: all offsets zero, one interval, not d^2 independent events.
degenerate_prob = union_length([(-delta/2, delta/2)]*64, Q(-8), Q(8))/16
assert degenerate_prob == Q(1, 64)

def capped_formula(p, t):
    if t >= 1:
        return Q(1)
    K = 0
    while t*4**(K+1) <= 1:
        K += 1
    return ((1-p)**2*t*sum((k+1)*(4*p)**k for k in range(K+1))
            +p**(K+1)*((K+2)-(K+1)*p))

def double_geometric(p, t):
    # Collapse each geometric tail at N. Whenever a tail is selected the
    # capped integrand is already one, so the result is exact.
    N = 0
    while t*4**N < 1:
        N += 1
    w = [(1-p)*p**j for j in range(N)]+[p**N]
    assert sum(w) == 1
    return sum(w[a]*w[b]*min(Q(1), t*4**(a+b))
               for a in range(N+1) for b in range(N+1))

rational_checks = 0
fractional_checks = 0
selected = []
ps = (Q(1, 10), Q(1, 4), Q(1, 2), Q(9, 10))
ts = [Q(2), Q(1), Q(1, 2)]
for k in range(1, 9):
    ts += [Q(1, 4**k), Q(999, 1000*4**k), Q(1001, 1000*4**k)]
for p in ps:
    for t in ts:
        F = capped_formula(p, t)
        assert F == double_geometric(p, t)
        if p < Q(1, 4):
            assert F <= t*((1-p)/(1-4*p))**2
        # q=1/32 is admissible for all p tested, including p=.9.
        q = 1/32
        assert float(p)*4**q < 1
        assert float(F) <= float(t)**q*((1-float(p))/(1-float(p)*4**q))**2+1e-12
        rational_checks += 1
        fractional_checks += 1
        if t == Q(1, 4**8):
            selected.append(dict(p=str(p), t=str(t), F=str(F), decimal=float(F)))

# Enumerate finite-chain masks to verify truncation domination independently.
finite_checks = 0
for L in range(1, 7):
    for f in range(L):
        for p in (Q(1, 4), Q(1, 2), Q(3, 4)):
            for t in (Q(1, 16), Q(1, 64)):
                total = Q(0)
                for rest in it.product((0, 1), repeat=L-1):
                    mask = rest[:f]+(0,)+rest[f:]
                    a = 0
                    while f-a-1 >= 0 and mask[f-a-1]:
                        a += 1
                    b = 0
                    while f+b+1 < L and mask[f+b+1]:
                        b += 1
                    weight = p**sum(rest)*(1-p)**(L-1-sum(rest))
                    total += weight*min(Q(1), t*4**(a+b))
                assert total <= capped_formula(p, t)
                finite_checks += 1

# Seven sites: active spectator spins at both ends share frozen controls
# with the two active neighbors of f=3. Build the complete diagonalizer by
# analytic one-spin rotations. X_f in that basis must be identity on both
# spectators, even though their energies depend on the outer controls.
n, f = 7, 3
largest_dimension = max(largest_dimension, 2**n)
h = np.array([.3, -.8, 1.1, -.2, -.9, .7, -.6])
g = np.array([.24, 0., -.31, 0., .18, 0., -.27])
J = np.array([.41, -.53, .62, -.29, .37, -.46])
H = ham(h, g, J)
U = np.eye(2**n)
for i in (0, 2, 4, 6):
    gate = np.zeros_like(U)
    for col in range(2**n):
        signs = [1-2*((col >> (n-1-j)) & 1) for j in range(n)]
        z = h[i]
        if i:
            z += J[i-1]*signs[i-1]
        if i+1 < n:
            z += J[i]*signs[i+1]
        theta = np.arctan2(g[i], z)
        c, s = np.cos(theta/2), np.sin(theta/2)
        v = np.array([[c, -s], [s, c]])
        colbit = (col >> (n-1-i)) & 1
        for rowbit in (0, 1):
            row = col ^ ((rowbit ^ colbit) << (n-1-i))
            gate[row, col] = v[rowbit, colbit]
    U = mul(U, gate)
D = mul(mul(U.T, H), U)
assert np.linalg.norm(D-np.diag(np.diag(D)), 'fro') < 1e-11
xf = tensor([X if i == f else I for i in range(n)])
T = mul(mul(U.T, xf), U)
# Partial trace over sites 0 and 6, followed by tensoring back identities.
reduced = np.zeros((32, 32))
for l, r in it.product((0, 1), repeat=2):
    idx = [(l << 6)+(k << 1)+r for k in range(32)]
    reduced += T[np.ix_(idx, idx)]/4
spectator_error = float(np.linalg.norm(T-tensor([I, reduced, I]), 'fro'))
assert spectator_error < 1e-11
spectator_checks = 0
for eta in it.product((0, 1), repeat=2):
    # Compare all 16 local transition differences, for all 4 spectator labels.
    matrices = []
    for s in (0, 1):
        indices = [(eta[0] << 4)+(l << 3)+(s << 2)+(r << 1)+eta[1]
                   for l, r in it.product((0, 1), repeat=2)]
        matrices.append(indices)
    for lp, lm in it.product(range(4), repeat=2):
        local_plus = matrices[0][lp]
        local_minus = matrices[1][lm]
        gaps = []
        for l, r in it.product((0, 1), repeat=2):
            ip = (l << 6)+(local_plus << 1)+r
            im = (l << 6)+(local_minus << 1)+r
            gaps.append(float(D[ip, ip]-D[im, im]))
        assert max(gaps)-min(gaps) < 1e-11
        spectator_checks += 1

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
result = dict(status='PASS', matrix_cases=matrix_cases,
              largest_physical_matrix_dimension=largest_dimension,
              max_block_spectrum_error=max_spectrum_error,
              max_field_shift_error=max_slope_error,
              max_difference_operator_error=max_difference_error,
              max_overlap_unitarity_error=max_overlap_error,
              uniform_field_interval_union_checks=interval_checks,
              factor_four_saturation_probability=str(sat_prob),
              degenerate_interval_probability=str(degenerate_prob),
              exact_capped_sum_checks=rational_checks,
              fractional_power_checks=fractional_checks,
              finite_volume_domination_checks=finite_checks,
              spectator_support_error=spectator_error,
              spectator_energy_cancellation_checks=spectator_checks,
              selected_capped_bounds=selected,
              nice_value=priority, peak_rss_bytes=rss,
              elapsed_seconds=time.monotonic()-start)
(root/'denominator_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
