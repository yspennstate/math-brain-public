"""Serial independent checks of the earlier bound and the first rotation.

All output stays beside this script. Matrices have dimension at most 128.
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import ctypes
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15
import numpy as np
np.seterr(all='raise')
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
C = np.sqrt(8/3)
rng = np.random.default_rng(98110450)
counts = {}
maxima = {}


def mm(a, b):
    out = np.einsum('ij,jk->ik', a, b, optimize=False)
    assert np.all(np.isfinite(out))
    return out


def comm(a, b):
    return mm(a, b)-mm(b, a)


def norm(a):
    return float(np.linalg.norm(a, 2))


def record(name, value, tolerance=2e-10):
    value = float(value)
    assert np.isfinite(value) and value <= tolerance, (name, value, tolerance)
    maxima[name] = max(maxima.get(name, 0.), value)


def count(name, amount=1):
    counts[name] = counts.get(name, 0)+amount


def signs(k, n):
    return [1-2*((k >> (n-1-j)) & 1) for j in range(n)]


def ham(h, g, bonds):
    n = len(h)
    out = np.zeros((2**n, 2**n))
    for k in range(2**n):
        s = signs(k, n)
        out[k, k] = sum(h[j]*s[j] for j in range(n))
        out[k, k] += sum(bonds[j]*s[j]*s[j+1] for j in range(n-1))
        for j in range(n):
            out[k ^ (1 << (n-1-j)), k] += g[j]
    return out


def pauli(n, j, kind):
    if kind == 'Z':
        return np.diag([signs(k, n)[j] for k in range(2**n)])
    out = np.zeros((2**n, 2**n))
    for k in range(2**n):
        out[k ^ (1 << (n-1-j)), k] = 1
    return out


def embed(local, support, n):
    """Embed by explicit basis indices, independent of Kronecker products."""
    support = list(support)
    outside = [j for j in range(n) if j not in support]
    out = np.zeros((2**n, 2**n), dtype=local.dtype)
    for row, col in product(range(2**n), repeat=2):
        rs, cs = signs(row, n), signs(col, n)
        if all(rs[j] == cs[j] for j in outside):
            r = sum(int(rs[j] == -1) << (len(support)-1-i)
                    for i, j in enumerate(support))
            c = sum(int(cs[j] == -1) << (len(support)-1-i)
                    for i, j in enumerate(support))
            out[row, col] = local[r, c]
    return out


def exp_skew(A):
    vals, vecs = np.linalg.eigh(1j*A)
    return mm(vecs*np.exp(-1j*vals)[None, :], vecs.conj().T)


def rotation(h, g, bonds, mask, f):
    """Construct the local inverse by eigenvectors; audit by a linear solve."""
    n = len(h)
    lo, hi = f, f
    while lo > 0 and mask[lo-1]:
        lo -= 1
    while hi+1 < n and mask[hi+1]:
        hi += 1
    outer = ([lo-1] if lo else [])+([hi+1] if hi+1 < n else [])
    left, right = max(0, lo-1), min(n-1, hi+1)
    support = list(range(left, right+1))
    hh = h[left:right+1].copy()
    gg = g[left:right+1].copy()
    for j in outer:
        hh[j-left] = 0.
    Hc = ham(hh, gg, bonds[left:right])
    local_n, ff = len(support), f-left
    local = np.zeros_like(Hc)
    entries = []
    gap = float('inf')
    for eta in product((1, -1), repeat=len(outer)):
        idx = []
        for s in (1, -1):
            idx.append([k for k in range(2**local_n)
                        if signs(k, local_n)[ff] == s and
                        all(signs(k, local_n)[j-left] == val
                            for j, val in zip(outer, eta))])
        Kp, Km = [Hc[np.ix_(i, i)] for i in idx]
        ep, up = np.linalg.eigh(Kp)
        em, um = np.linalg.eigh(Km)
        diffs = ep[:, None]-em[None, :]
        gap = min(gap, float(np.min(np.abs(diffs))))
        assert np.min(np.abs(diffs)) > 1e-7
        B = mm(mm(up, mm(up.T, um)/diffs), um.T)
        # Row-major vectorization of Kp B - B Km = I.
        d = len(Kp)
        sylvester = np.kron(Kp, np.eye(d))-np.kron(np.eye(d), Km.T)
        direct = np.linalg.solve(sylvester, np.eye(d).ravel()).reshape(d, d)
        record('sylvester_vs_spectral', norm(B-direct)/max(1., norm(B)))
        record('local_inverse_equation', norm(mm(Kp, B)-mm(B, Km)-np.eye(d)))
        local[np.ix_(idx[0], idx[1])] = B
        local[np.ix_(idx[1], idx[0])] = -B.T
        # The independent field shifts each sector by +/- eta_h exactly.
        shifted = Hc.copy()
        shifted += .371*pauli(local_n, ff, 'Z')
        for s, ii, ev in zip((1, -1), idx, (ep, em)):
            check = np.linalg.eigvalsh(shifted[np.ix_(ii, ii)])
            record('earlier_affine_field_slope', np.max(np.abs(check-ev-s*.371)))
        count('local_control_sectors')
        entries.extend(diffs.ravel().tolist())
    assert len(entries) == 2**len(outer)*4**(hi-lo)
    delta = gap/2
    return embed(local, support, n), support, delta, entries


def capped(p, t):
    if t >= 1:
        return F(1)
    k = 0
    while t*4**(k+1) <= 1:
        k += 1
    return ((1-p)**2*t*sum((j+1)*(4*p)**j for j in range(k+1))
            +p**(k+1)*((k+2)-(k+1)*p))


# Independent rational audit: enumerate pairs of clipped geometric lengths.
for p in (F(1, 10), F(1, 4), F(1, 2), F(9, 10)):
    for k in range(7):
        for c in (F(999, 1000), F(1), F(1001, 1000)):
            t = c/F(4**k)
            N = 0
            while t*4**N < 1:
                N += 1
            weights = [(1-p)*p**j for j in range(N)]+[p**N]
            actual = sum(weights[a]*weights[b]*min(F(1), t*4**(a+b))
                         for a, b in product(range(N+1), repeat=2))
            assert actual == capped(p, t)
            count('earlier_exact_capped_sums')

# Finite-volume truncations, enumerated without geometric-run formulas.
for n in range(1, 7):
    for f in range(n):
        for p in (F(1, 4), F(1, 2), F(3, 4)):
            t = F(1, 64)
            total = F(0)
            for rest in product((0, 1), repeat=n-1):
                mask = rest[:f]+(0,)+rest[f:]
                a = b = 0
                while f-a > 0 and mask[f-a-1]:
                    a += 1
                while f+b+1 < n and mask[f+b+1]:
                    b += 1
                total += p**sum(rest)*(1-p)**(n-1-sum(rest))*min(F(1), t*4**(a+b))
            assert total <= capped(p, t)
            count('earlier_exact_finite_volumes')

# The two Sobolev integrals entering C_* are exact rational numbers.
assert 2*(F(1, 3)+1) == 2*(1+F(1, 3)) == F(8, 3)

# All masks through five sites. Different sites' generators share controls.
for n in range(1, 6):
    for mask in product((0, 1), repeat=n):
        h = rng.uniform(-2, 2, n)
        g = rng.uniform(-.6, .6, n)*mask
        bonds = rng.uniform(-.7, .7, n-1)
        H = ham(h, g, bonds)
        frozen = [f for f in range(n) if not mask[f]]
        generators, perturbations = {}, {}
        for f in frozen:
            Aunit, support, delta, gaps = rotation(h, g, bonds, mask, f)
            eps = min(.03, .1*delta/C)
            A, V = eps*Aunit, eps*pauli(n, f, 'X')
            bound = C*eps/delta
            assert norm(A) <= bound+1e-12
            record('antihermiticity', norm(A+A.T))
            record('global_homological_equation', norm(comm(H, A)-V))
            Z = pauli(n, f, 'Z')
            record('frozen_parity', norm(mm(A, Z)+mm(Z, A)))
            U = exp_skew(A)
            record('rotation_unitarity', norm(mm(U, U.conj().T)-np.eye(2**n)))
            rotated = mm(mm(U, H+V), U.conj().T)
            R = rotated-H
            Q = comm(A, V)/2
            T = R-Q
            actual_a = norm(A)
            assert norm(R) <= actual_a*eps+2e-11
            assert norm(T) <= 4/3*actual_a**2*eps+2e-11
            record('same_barrier_even_parity', norm(comm(Q, Z)))
            dressed = mm(mm(U.conj().T, Z), U)
            assert norm(dressed-Z) <= min(2., 2*actual_a)+2e-11
            assert norm(comm(H+V, dressed)) <= 8/3*actual_a**2*eps+2e-11
            record('dressed_spin_involution', norm(mm(dressed, dressed)-np.eye(2**n)))
            generators[f], perturbations[f] = A, V
            count('physical_barrier_cases')
        for f, gsite in product(frozen, repeat=2):
            if f >= gsite:
                continue
            Af, Ag = generators[f], generators[gsite]
            Vf, Vg = perturbations[f], perturbations[gsite]
            Qfg = (comm(Af, Vg)+comm(Ag, Vf))/2
            assert norm(Qfg) <= norm(Af)*norm(Vg)+norm(Ag)*norm(Vf)+1e-12
            if any(f < j < gsite for j in frozen):
                record('nonconsecutive_pair_zero', norm(Qfg))
                count('nonconsecutive_pair_checks')
            else:
                count('consecutive_pair_checks')
            for j in frozen:
                Zj = pauli(n, j, 'Z')
                parity = mm(Qfg, Zj)+mm(Zj, Qfg) if j in (f, gsite) else comm(Qfg, Zj)
                record('two_barrier_parity', norm(parity))

# Generic interlaced spectra and degeneracies within a sector. This also
# checks the dimension-free inequality independently of Ising coefficients.
for d in (1, 2, 4, 8, 16):
    for kind in ('interlaced', 'degenerate', 'random'):
        up, _ = np.linalg.qr(rng.normal(size=(d, d)))
        um, _ = np.linalg.qr(rng.normal(size=(d, d)))
        if kind == 'interlaced':
            ep, em = 2*np.arange(d, dtype=float), 2*np.arange(d, dtype=float)+1
        elif kind == 'degenerate':
            ep, em = np.full(d, 3.), np.full(d, -3.)
        else:
            ep, em = rng.uniform(-3, 3, d), rng.uniform(-3, 3, d)
        gap = np.min(np.abs(ep[:, None]-em[None, :]))
        B = mm(mm(up, mm(up.T, um)/(ep[:, None]-em[None, :])), um.T)
        assert norm(B) <= C/gap+1e-10
        count('interlacing_and_degeneracy_cases')

# An explicit spectator test: A_f must ignore active spins beyond its controls.
n, f = 7, 3
mask = (1, 0, 1, 0, 1, 0, 1)
h = np.array([.3, -.8, 1.1, 2.2, -.9, .7, -.6])
g = np.array([.24, 0., -.31, 0., .18, 0., -.27])
bonds = np.array([.41, -.53, .62, -.29, .37, -.46])
Aunit, support, delta, _ = rotation(h, g, bonds, mask, f)
assert support == [1, 2, 3, 4, 5]
H = ham(h, g, bonds)
record('spectator_homological_equation', norm(comm(H, Aunit)-pauli(n, f, 'X')))
for j in (0, 1, 5, 6):
    record('spectator_or_control_Z_commutator', norm(comm(Aunit, pauli(n, j, 'Z'))))
for j in (0, 6):
    record('spectator_X_commutator', norm(comm(Aunit, pauli(n, j, 'X'))))
    count('spectator_sites')

# One shared active block: audit the spectral path formula and finite Taylor
# coefficient, without deriving that coefficient from the same commutator.
n, mask = 3, (0, 1, 0)
h = np.array([2.3, .71, -1.6])
g = np.array([0., .37, 0.])
bonds = np.array([.41, -.29])
H = ham(h, g, bonds)
As, Vs = [], []
for f in (0, 2):
    Au, _, _, _ = rotation(h, g, bonds, mask, f)
    As.append(.05*Au)
    Vs.append(.05*pauli(n, f, 'X'))
A, V = sum(As), sum(Vs)
Q = comm(A, V)/2
ev, u = np.linalg.eigh(H)
Ve = mm(mm(u.T, V), u)
gaps = ev[:, None]-ev[None, :]
Ae = np.zeros_like(Ve)
np.divide(Ve, gaps, out=Ae, where=~np.eye(2**n, dtype=bool))
Qpaths = np.zeros_like(Ve)
for a, b, k in product(range(2**n), repeat=3):
    if k != a and k != b:
        Qpaths[a, b] += .5*Ve[a, k]*Ve[k, b]*(1/(ev[a]-ev[k])+1/(ev[b]-ev[k]))
record('spectral_path_formula', norm(Qpaths-mm(mm(u.T, Q), u)))
record('spectral_generator_formula', norm(Ae-mm(mm(u.T, A), u)))
errors = []
for t in (.04, .02):
    Uplus, Uminus = exp_skew(t*A), exp_skew(-t*A)
    P = mm(mm(Uplus, H+t*V), Uplus.conj().T)
    M = mm(mm(Uminus, H-t*V), Uminus.conj().T)
    estimate = (P+M-2*H)/(2*t*t)
    errors.append(norm(estimate-Q))
assert errors[1] < .4*errors[0], errors
count('symmetric_taylor_checks', 2)

# Check the bad-site term in (14) with only one of the two generators retained.
Ag, Vg, Vb = As[0], Vs[0], Vs[1]
Qbad = comm(Ag, Vg)/2+comm(Ag, Vb)
t = .02
Up, Um = exp_skew(t*Ag), exp_skew(-t*Ag)
P = mm(mm(Up, H+t*(Vg+Vb)), Up.conj().T)
M = mm(mm(Um, H-t*(Vg+Vb)), Um.conj().T)
record('bad_site_taylor_coefficient', norm((P+M-2*H)/(2*t*t)-Qbad), 1e-7)

# A twice-at-f path can be off diagonal on the active labels.
n, mask = 3, (1, 0, 1)
h = np.array([1.1, 3., -.7])
g = np.array([.3, 0., .2])
bonds = np.array([.6, -.4])
H = ham(h, g, bonds)
Au, _, delta, _ = rotation(h, g, bonds, mask, 1)
V = .04*pauli(n, 1, 'X')
Q = comm(.04*Au, V)/2
u = np.zeros_like(H)
for s in (1, -1):
    ix = [k for k in range(8) if signs(k, 3)[1] == s]
    _, block_u = np.linalg.eigh(H[np.ix_(ix, ix)])
    u[np.ix_(ix, ix)] = block_u
Qe = mm(mm(u.T, Q), u)
same_barrier_offdiagonal = norm(Qe-np.diag(np.diag(Qe)))
assert same_barrier_offdiagonal > 1e-7

# Larger rotations and an exactly degenerate active sector. Bounds (4) use
# unitarity rather than a small-norm exponential estimate.
for eps in (.01, .8, 3.):
    H = np.diag([1., -1.])
    V = eps*np.array([[0., 1.], [1., 0.]])
    A = eps/2*np.array([[0., 1.], [-1., 0.]])
    U = exp_skew(A)
    R = mm(mm(U, H+V), U.conj().T)-H
    Q = comm(A, V)/2
    assert norm(R) <= norm(A)*eps+1e-12
    assert norm(R-Q) <= 4/3*norm(A)**2*eps+1e-12
    record('one_spin_diagonal_correction', norm(Q-eps**2/2*H))
    count('large_and_small_rotation_cases')

# A second, trigonometric derivation audits the signs and the factors 4/3
# and 8/3. The limiting ratios show these factors are attained to leading order
# when expressed in terms of the actual generator norm.
scalar_ratios = []
for a in (.01, .005):
    eps = 2*a
    Z, X = np.diag([1., -1.]), np.array([[0., 1.], [1., 0.]])
    A = a*np.array([[0., 1.], [-1., 0.]])
    U = exp_skew(A)
    R = mm(mm(U, Z+eps*X), U.conj().T)-Z
    rz = np.cos(2*a)-1+2*a*np.sin(2*a)
    rx = 2*a*np.cos(2*a)-np.sin(2*a)
    record('one_spin_trigonometric_remainder', norm(R-rz*Z-rx*X))
    T = R-2*a*a*Z
    dressed = mm(mm(U.conj().T, Z), U)
    ratio_T = norm(T)/(a*a*eps)
    ratio_comm = norm(comm(Z+eps*X, dressed))/(a*a*eps)
    assert abs(ratio_T-4/3) < .001
    assert abs(ratio_comm-8/3) < .001
    scalar_ratios.append(dict(a=a, cubic_remainder_ratio=ratio_T,
                              dressed_commutator_ratio=ratio_comm))
    count('trigonometric_constant_checks')
mask = (1, 0, 1)
h = np.array([0., 3., 0.])
g = np.zeros(3)
bonds = np.zeros(2)
Au, _, _, _ = rotation(h, g, bonds, mask, 1)
record('degenerate_active_inverse', norm(Au-np.kron(np.eye(2), np.kron(np.array([[0., 1/6], [-1/6, 0.]]), np.eye(2)))))

rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss_raw if sys.platform == 'darwin' else rss_raw*1024
assert rss < 1_000_000_000
result = dict(status='PASS', counts=counts, residual_maxima=maxima,
              C_star=float(C), C_star_squared_exact='8/3',
              symmetric_taylor_errors=errors,
              same_barrier_active_offdiagonal_norm=same_barrier_offdiagonal,
              scalar_constant_ratios=scalar_ratios,
              nice_value=priority, peak_rss_bytes=rss,
              elapsed_seconds=time.monotonic()-started,
              thread_environment={key: os.environ[key] for key in (
                  'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                  'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')})
(ROOT/'rotation_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
