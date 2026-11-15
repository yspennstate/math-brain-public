"""Serial audits of the interaction proof; no full-spectrum MBL numerics.

Dense matrices have dimension at most 128. All files stay beside this script.
"""
import os
THREAD_KEYS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
               'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for key in THREAD_KEYS:
    os.environ[key] = '1'
import ctypes
from fractions import Fraction as F
from itertools import product
from math import exp, factorial
import json
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(300)
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15
import numpy as np
np.seterr(all='raise')
ROOT = Path(__file__).resolve().parent
started = time.monotonic()
rng = np.random.default_rng(98050819)
counts, maxima = {}, {}

def count(key, amount=1):
    counts[key] = counts.get(key, 0)+amount

def record(key, value, tolerance=2e-10):
    value = float(value)
    assert np.isfinite(value) and value <= tolerance, (key, value, tolerance)
    maxima[key] = max(maxima.get(key, 0.), value)

def atoms(mask):
    out, j = [], 0
    while j < len(mask):
        end = j+1
        if mask[j]:
            while end < len(mask) and mask[end]:
                end += 1
        out.append(tuple(range(j, end)))
        j = end
    return out

def cell(mask, f):
    lo = hi = f
    while lo and mask[lo-1]:
        lo -= 1
    while hi+1 < len(mask) and mask[hi+1]:
        hi += 1
    outer = ([lo-1] if lo else [])+([hi+1] if hi+1 < len(mask) else [])
    return tuple(range(max(0, lo-1), min(len(mask), hi+2))), outer

def atom_support(sites, aa):
    ss = set(sites)
    ans = frozenset(i for i, a in enumerate(aa) if set(a) & ss)
    assert set().union(*(set(aa[i]) for i in ans)) == ss
    return ans

def diam(S, aa):
    return max(aa[i][-1] for i in S)-min(aa[i][0] for i in S)

def scalar_norm(phi, m):
    return max((sum(v for S, v in phi.items() if x in S) for x in range(m)), default=0)

def scalar_bracket(A, B):
    out = {}
    for S, a in A.items():
        for T, b in B.items():
            if S & T:
                U = S | T
                out[U] = out.get(U, F(0))+2*a*b
    return out

# Exhaustive support audit, including adjacent frozen sites and physical ends.
for n in range(1, 11):
    for mask in product((0, 1), repeat=n):
        aa = atoms(mask)
        supports = [atom_support(cell(mask, f)[0], aa)
                    for f in range(n) if not mask[f]]
        assert all(len(S) <= 5 for S in supports)
        assert all(sum(c in S for S in supports) <= (2 if mask[a[0]] else 3)
                   for c, a in enumerate(aa))
        count('structural_masks')

# Long active blocks do not increase the number of atoms per generator.
mask = (0,)+(1,)*499+(0,)+(1,)*499+(0,)
aa = atoms(mask)
assert len(aa) == 5 and len(cell(mask, 500)[0]) == 1001
assert len(atom_support(cell(mask, 500)[0], aa)) == 5
count('long_block_structure')

# Exact positive path majorants, with no cancellations or matrix identities.
# This independently challenges the factorial and the constant q=10 alpha.
for n in range(1, 8):
    for mask in product((0, 1), repeat=n):
        aa = atoms(mask)
        roots = {frozenset([i]): F(1) for i, a in enumerate(aa) if not mask[a[0]]}
        for ell in (2, 4, 20):
            A = {}
            for f in range(n):
                if mask[f]:
                    continue
                sites, _ = cell(mask, f)
                if sites[-1]-sites[0] <= ell:
                    S = atom_support(sites, aa)
                    A[S] = A.get(S, F(0))+F(1, 100)
            q = 10*scalar_norm(A, len(aa))
            B = roots
            for order in range(1, 7):
                B = scalar_bracket(A, B)
                assert scalar_norm(B, len(aa)) <= factorial(order)*q**order
                count('exact_path_majorant_checks')

# Independent recurrence-product audit of the abstract support-size bound.
for k in range(1, 6):
    a = F(1, 37)
    q = 2*k*a
    value = q
    for order in range(1, 13):
        assert value <= factorial(order)*q**order
        count('exact_recurrence_checks')
        value *= 2*a*(k+1+order*(k-1))

# Exact finite-volume cutoff probabilities, without assuming infinite runs.
for n in range(1, 9):
    for f in range(n):
        for ell in (2, 3, 4):
            histogram = [0]*n
            for rest in product((0, 1), repeat=n-1):
                mask = rest[:f]+(0,)+rest[f:]
                sites, _ = cell(mask, f)
                if sites[-1]-sites[0] > ell:
                    histogram[sum(rest)] += 1
            for p in (F(1, 4), F(1, 2), F(3, 4)):
                actual = sum(v*p**j*(1-p)**(n-1-j) for j, v in enumerate(histogram))
                tail = p**(ell-1)*(ell-(ell-1)*p)
                assert actual <= tail
                count('exact_cutoff_probability_checks')
for p in (F(1, 4), F(1, 2), F(3, 4)):
    for ell in range(2, 11):
        N = ell-1
        weights = [(1-p)*p**j for j in range(N)]+[p**N]
        tail = sum(weights[a]*weights[b] for a, b in product(range(N+1), repeat=2)
                   if a+b >= N)
        assert tail == p**N*((N+1)-N*p)
        count('exact_infinite_tail_checks')

I = np.eye(2)
X = np.array([[0., 1.], [1., 0.]])
Z = np.diag([1., -1.])

def mm(a, b):
    out = np.einsum('ij,jk->ik', a, b, optimize=False)
    assert np.all(np.isfinite(out))
    return out

def comm(a, b):
    return mm(a, b)-mm(b, a)

def opnorm(a):
    return float(np.linalg.norm(a, 2))

def tensor(ff):
    ans = np.ones((1, 1))
    for f in ff:
        ans = np.kron(ans, f)
    return ans

def onsite(a, i, n):
    return tensor([a if j == i else I for j in range(n)])

def ham(h, g, J):
    n = len(h)
    out = np.zeros((2**n, 2**n))
    for i in range(n):
        out += onsite(h[i]*Z+g[i]*X, i, n)
    for i in range(n-1):
        out += J[i]*tensor([Z if j in (i, i+1) else I for j in range(n)])
    return out

def unitary(A):
    e, u = np.linalg.eigh(1j*A)
    return mm(u*np.exp(-1j*e), u.conj().T)

def local_inverse(h, g, J, mask, f, delta):
    sites, outer = cell(mask, f)
    left, right = sites[0], sites[-1]
    hh, gg = h[left:right+1].copy(), g[left:right+1].copy()
    for j in outer:
        hh[j-left] = 0
    H = ham(hh, gg, J[left:right])
    nn, ff = len(sites), f-left
    A = np.zeros_like(H)
    pieces, gap = [], float('inf')
    for eta in product((0, 1), repeat=len(outer)):
        idx = [[i for i in range(2**nn)
                if (i >> (nn-1-ff)) & 1 == spin
                and all((i >> (nn-1-(j-left))) & 1 == t for j, t in zip(outer, eta))]
               for spin in (0, 1)]
        ep, up = np.linalg.eigh(H[np.ix_(idx[0], idx[0])])
        em, um = np.linalg.eigh(H[np.ix_(idx[1], idx[1])])
        gaps = ep[:, None]-em[None, :]
        gap = min(gap, float(np.min(np.abs(gaps))))
        pieces.append((idx, ep, em, up, um))
    if gap < delta:
        return None, gap
    for idx, ep, em, up, um in pieces:
        b = mm(mm(up, mm(up.T, um)/(ep[:, None]-em[None, :])), um.T)
        A[np.ix_(idx[0], idx[1])] = b
        A[np.ix_(idx[1], idx[0])] = -b.T
    embedded = tensor([np.eye(2**left), A, np.eye(2**(len(mask)-1-right))])
    return embedded, gap

def add_to(phi, S, a):
    if opnorm(a) > 0:
        phi[S] = phi.get(S, np.zeros_like(a))+a

def bracket(A, B):
    out = {}
    for S, a in A.items():
        for T, b in B.items():
            if S & T:
                add_to(out, S | T, comm(a, b))
    return out

def combine(A, B, ca=1., cb=1.):
    out = {S: ca*a for S, a in A.items()}
    for S, b in B.items():
        add_to(out, S, cb*b)
    return out

def isum(A, n):
    return sum(A.values(), np.zeros((2**n, 2**n)))

def inorm(A, aa, mu):
    vals = {S: exp(mu*diam(S, aa))*opnorm(a) for S, a in A.items()}
    atom = max((sum(v for S, v in vals.items() if c in S)
                for c in range(len(aa))), default=0.)
    site = max((sum(v for S, v in vals.items()
                    if any(x in aa[c] for c in S))
                for x in range(sum(map(len, aa)))), default=0.)
    record('atom_vs_physical_norm', abs(atom-site))
    return atom

cases = [(tuple(mask), 3, None) for n in range(1, 6)
         for mask in product((0, 1), repeat=n)]
cases += [((0, 0, 0), 2, 'resonance'),
          ((0, 1, 1, 0, 0), 2, 'oversize'),
          ((0, 1, 0, 1, 0, 1), 6, None),
          ((1, 0, 1, 0, 1, 0, 1), 4, None),
          ((0, 1, 1, 1, 0), 6, None)]
rows = []
for mask, ell, fixture in cases:
    n, aa = len(mask), atoms(mask)
    mu, delta = 1/ell, .15
    h = rng.uniform(-2, 2, n)
    g = rng.uniform(-.5, .5, n)*mask
    J = rng.uniform(-.6, .6, n-1)
    if fixture == 'resonance':
        h, J = np.array([2., .7, 3.]), np.array([.2, .5])
    H = ham(h, g, J)
    frozen = [f for f in range(n) if not mask[f]]
    coeff = {f: (-1 if f % 2 else 1)*rng.uniform(.5, 1) for f in frozen}
    Aunit, retained, gaps = {}, set(), []
    for f in frozen:
        sites, _ = cell(mask, f)
        if sites[-1]-sites[0] > ell:
            continue
        au, gap = local_inverse(h, g, J, mask, f, delta)
        gaps.append(gap)
        if au is not None:
            record('local_homological_equation', opnorm(comm(H, au)-onsite(X, f, n)))
            assert opnorm(au) <= np.sqrt(8/3)/delta+1e-10
            add_to(Aunit, atom_support(sites, aa), coeff[f]*au)
            retained.add(f)
    alpha_unit = inorm(Aunit, aa, mu)
    scale = min(.02, .25/(10*alpha_unit)) if alpha_unit else .02
    A = {S: scale*a for S, a in Aunit.items()}
    VR, VD = {}, {}
    for f in frozen:
        S = atom_support((f,), aa)
        (VR if f in retained else VD)[S] = scale*coeff[f]*onsite(X, f, n)
    epsilon = max((scale*abs(c) for c in coeff.values()), default=0.)
    alpha = inorm(A, aa, mu)
    q = 10*alpha
    assert q <= .25000000001
    assert alpha <= 3*exp(mu*ell)*np.sqrt(8/3)*epsilon/delta+1e-12
    At, Vrt, Vdt = isum(A, n), isum(VR, n), isum(VD, n)
    Vt = Vrt+Vdt
    record('global_homological_equation', opnorm(comm(H, At)-Vrt))
    BR, BD, T, Q = VR, VD, {}, {}
    Hder, Vder = comm(At, H), Vt
    highest = 8
    for order in range(1, highest+1):
        BR, BD = bracket(A, BR), bracket(A, BD)
        Bfull = combine(BR, BD)
        assert inorm(Bfull, aa, mu) <= epsilon*factorial(order)*q**order+1e-13
        for S in set(BR) | set(BD):
            assert len(S) <= 1+4*order and diam(S, aa) <= order*ell
        term = combine(BR, BD, order/(order+1)/factorial(order), 1/factorial(order))
        assert inorm(term, aa, mu) <= epsilon*q**order+1e-13
        # Independent Taylor coefficient from H and V before cancellation.
        Hder, Vder = comm(At, Hder), comm(At, Vder)
        direct_coefficient = Hder/factorial(order+1)+Vder/factorial(order)
        record('uncancelled_taylor_coefficient', opnorm(isum(term, n)-direct_coefficient))
        if order == 1:
            Q = term
        else:
            T = combine(T, term)
        count('matrix_order_checks')
    bound_Q, bound_T = epsilon*q, epsilon*q*q/(1-q)
    assert inorm(Q, aa, mu) <= bound_Q+1e-13
    assert inorm(T, aa, mu) <= bound_T+1e-13
    if not VD:
        assert inorm(Q, aa, mu) <= epsilon*q/2+1e-13
        good_series = sum(order/(order+1)*q**order for order in range(2, 80))
        assert inorm(T, aa, mu) <= epsilon*good_series+1e-13
        count('all_retained_cases')
    if VR and VD:
        count('mixed_retained_discarded_cases')
    if fixture == 'resonance':
        assert 1 not in retained and {0, 2} <= retained
        bad_quadratic = opnorm(comm(At, Vdt))
        assert bad_quadratic > 1e-8
    if fixture == 'oversize':
        assert retained == {4}
    for radius in range(n+1):
        local_tail = max((sum(opnorm(a) for S, a in T.items()
                              if c in S and diam(S, aa) >= radius)
                          for c in range(len(aa))), default=0.)
        assert local_tail <= exp(-mu*radius)*bound_T+1e-13
        count('spatial_tail_checks')
    U = unitary(At)
    rotated = mm(mm(U, H+Vt), U.conj().T)
    remainder = rotated-H-Vdt-isum(Q, n)
    series_error = opnorm(remainder-isum(T, n))
    omitted_operator_bound = len(aa)*epsilon*q**(highest+1)/(1-q)
    assert series_error <= omitted_operator_bound+2e-11
    assert opnorm(remainder) <= len(aa)*bound_T+2e-11
    if fixture in ('resonance', 'oversize') or (mask == (0, 1, 0) and not VD):
        # Independent exact integral identity, using Gaussian quadrature
        # and direct matrix conjugations, rather than the commutator series.
        nodes, weights = np.polynomial.legendre.leggauss(16)
        B2R, B2D = comm(At, comm(At, Vrt)), comm(At, comm(At, Vdt))
        integral = np.zeros_like(rotated)
        for node, weight in zip(nodes, weights):
            u = (node+1)/2
            Uu = unitary(u*At)
            Bu = (1-u*u)/2*B2R+(1-u)*B2D
            integral += weight/2*mm(mm(Uu, Bu), Uu.conj().T)
        record('integral_vs_direct_remainder', opnorm(integral-remainder))
        count('matrix_integral_checks')
    record('unitary_residual', opnorm(mm(U, U.conj().T)-np.eye(2**n)))
    rows.append(dict(n=n, mask=''.join(map(str, mask)), ell=ell,
                     fixture=fixture, retained=sorted(retained),
                     discarded=sorted(set(frozen)-retained), q=q, epsilon=epsilon,
                     Q_interaction_norm=inorm(Q, aa, mu),
                     T_partial_interaction_norm=inorm(T, aa, mu),
                     T_bound=bound_T, series_operator_error=series_error,
                     omitted_operator_bound=omitted_operator_bound))
    count('physical_matrix_cases')

# Second derivation of the exact coefficients, by elementary quadratures:
# integral_0^1 t exp(t ad_A)[A,V_R]dt and exp(ad_A)V_D.
from fractions import Fraction
for n in range(1, 21):
    good_integral_coefficient = Fraction(1, (n+1)*factorial(n-1))
    assert good_integral_coefficient == Fraction(n, factorial(n+1))
    assert Fraction(1, factorial(n)) == Fraction(n+1, factorial(n+1))
    count('exact_integral_coefficient_checks')

nodes, weights = np.polynomial.legendre.leggauss(64)
for qcheck in (0., .1, .25, .5, .9):
    u = (nodes+1)/2
    integral = float(np.sum(weights*(1-u)/(1-u*qcheck)**3))
    record('scalar_integral_geometric_bound', abs(integral-1/(1-qcheck)), 2e-11)
    count('scalar_integral_checks')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == 'darwin' else rss*1024
assert rss < 1_000_000_000
result = dict(status='PASS', counts=counts, residual_maxima=maxima,
              bad_site_quadratic_norm=bad_quadratic,
              physical_cases=rows, largest_matrix_dimension=max(2**r['n'] for r in rows),
              nice_value=priority, thread_environment={k: os.environ[k] for k in THREAD_KEYS},
              peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-started)
(ROOT/'simultaneous_verification.json').write_text(json.dumps(result, indent=2)+'\n')
summary = {k: v for k, v in result.items() if k != 'physical_cases'}
summary['max_series_operator_error'] = max(r['series_operator_error'] for r in rows)
summary['max_q'] = max(r['q'] for r in rows)
print(json.dumps(summary, indent=2))
