"""Independent identities, constant audits, and high-precision finite probes.

Standard library only. No imports from earlier rounds and no worker processes.
"""

import json
import math
import os
import random
import resource
import signal
import sys
import time
from decimal import Decimal as R, getcontext
from fractions import Fraction as Q
from pathlib import Path

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
signal.alarm(150)
_, hard = resource.getrlimit(resource.RLIMIT_CPU)
cap = 100 if hard == resource.RLIM_INFINITY else min(100, hard)
resource.setrlimit(resource.RLIMIT_CPU, (cap, hard))
getcontext().prec = 120


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def matvec(a, v):
    return [dot(row, v) for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def gram(cols):
    return [[dot(x, y) for y in cols] for x in cols]


def determinant(a):
    a = [row[:] for row in a]
    answer = 1
    for j in range(len(a)):
        pivot = next((k for k in range(j, len(a)) if a[k][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        p = a[j][j]
        answer *= p
        for k in range(j+1, len(a)):
            f = a[k][j]/p
            for ell in range(j+1, len(a)):
                a[k][ell] -= f*a[j][ell]
            a[k][j] = 0
    return answer


def orthogonal_volume(cols):
    # Rational Gram-Schmidt, independent of elimination on the Gram matrix.
    orthogonal = []
    result = 1
    for col in cols:
        v = col[:]
        for w in orthogonal:
            scale = dot(col, w)/dot(w, w)
            v = [x-scale*y for x, y in zip(v, w)]
        normsq = dot(v, v)
        if not normsq:
            return 0
        orthogonal.append(v)
        result *= normsq
    return result


def values(cols, y):
    a, *u = cols
    q = dot(a, a)
    c = gram(u)
    v = [dot(a, col) for col in u]
    r = [vi-yi for vi, yi in zip(v, y)]
    return q, c, v, r


def update(cols, y):
    # Direct simultaneous parameter gradients; not a Gram/residual update.
    a, *u = cols
    r = [dot(a, col)-yi for col, yi in zip(u, y)]
    an = [ai-sum(col[i]*ri for col, ri in zip(u, r))
          for i, ai in enumerate(a)]
    un = [[ui-ai*ri for ui, ai in zip(col, a)]
          for col, ri in zip(u, r)]
    return [an]+un


def krylov_det(c, v):
    columns = []
    z = v[:]
    for _ in v:
        columns.append(z)
        z = matvec(c, z)
    return determinant(transpose(columns))


def decimal(q):
    if isinstance(q, Q):
        return R(q.numerator)/R(q.denominator)
    return R(q)


def eigenvalues(a):
    # Used only to construct starts and for diagnostic endpoint values.
    b = [[float(x) for x in row] for row in a]
    n = len(b)
    if n == 1:
        return [b[0][0]]
    for _ in range(100*n*n):
        i, j = max(((i, j) for i in range(n) for j in range(i+1, n)),
                   key=lambda ij: abs(b[ij[0]][ij[1]]))
        if abs(b[i][j]) < 1e-14:
            return sorted(b[k][k] for k in range(n))
        angle = .5*math.atan2(2*b[i][j], b[j][j]-b[i][i])
        cs, sn = math.cos(angle), math.sin(angle)
        ai, aj, off = b[i][i], b[j][j], b[i][j]
        for k in range(n):
            if k != i and k != j:
                x, z = b[k][i], b[k][j]
                b[k][i] = b[i][k] = cs*x-sn*z
                b[k][j] = b[j][k] = sn*x+cs*z
        b[i][i] = cs*cs*ai-2*cs*sn*off+sn*sn*aj
        b[j][j] = sn*sn*ai+2*cs*sn*off+cs*cs*aj
        b[i][j] = b[j][i] = 0.
    raise AssertionError('Jacobi cap')


def positive_definite(a):
    # Exact Sylvester criterion: used to certify every initial spectral margin.
    return all(determinant([row[:k] for row in a[:k]]) > 0
               for k in range(1, len(a)+1))


rng = random.Random(226202611151127)
identity_cases = 0
for d in (1, 2, 3, 4):
    m = d+2
    for case in range(10):
        cols = [[Q(rng.randint(-5, 5), 9) for _ in range(m)]
                for _ in range(d+1)]
        y = [Q(rng.randint(-3, 3), 17) for _ in range(d)]
        q, c, v, r = values(cols, y)
        nxt = update(cols, y)
        qn, cn, vn, rn = values(nxt, y)
        rr = dot(r, r)
        assert qn == q-2*rr+dot(r, matvec(c, r))-2*dot(y, r)
        assert cn == [[c[i][j]-(2-q)*r[i]*r[j]-r[i]*y[j]-y[i]*r[j]
                       for j in range(d)] for i in range(d)]
        assert rn == [ri-dot(row, r)-q*ri+dot(v, r)*ri
                      for row, ri in zip(c, r)]
        assert determinant(gram(nxt)) == determinant(gram(cols))*(1-rr)**2
        assert determinant(gram(cols)) == orthogonal_volume(cols)
        stepnorm = sum(dot([x-z for x, z in zip(a, b)],
                           [x-z for x, z in zip(a, b)])
                       for a, b in zip(cols, nxt))
        assert stepnorm == dot(r, matvec(c, r))+q*rr
        # Recheck round 5 using a separately implemented column representation.
        qn, cn, vn, rn = values(update(cols, [Q(0)]*d), [Q(0)]*d)
        h = dot(v, v)
        theta = (1-q)*(1-h)
        filt = [[(theta if i == j else 0)-cn[i][j]
                 for j in range(d)] for i in range(d)]
        assert krylov_det(cn, vn) == determinant(filt)*krylov_det(c, v)
        identity_cases += 1

# Independent scalar formula for a 2D projector, including a legitimate
# reduction of repeated scalar top and bottom blocks.
def top_weight(a, b, c, x, z):
    gap = math.hypot(a-c, 2*b)
    low = (a+c-gap)/2
    return ((a-low)*x*x+2*b*x*z+(c-low)*z*z)/gap

max_projector_error = 0.
for ht, hb, top, bottom in ((.09, .04, 3., 1.), (.13, .07, 4., .5)):
    x, z, alpha = math.sqrt(ht), math.sqrt(hb), 1.3
    def weight(s):
        return top_weight(top-s*alpha*ht, -s*alpha*x*z,
                          bottom-s*alpha*hb, x, z)
    eps = 1e-5
    observed = (weight(eps)-weight(-eps))/(2*eps)
    expected = -2*alpha*ht*hb/(top-bottom)
    error = abs(observed-expected)
    max_projector_error = max(max_projector_error, error)
    assert error < 1e-9
    gap = top-bottom-alpha*(ht+hb)
    assert weight(1) >= math.exp(-2*alpha*(ht+hb)/gap)*weight(0)

# Audit earlier exceptional endpoints without invoking a GD recurrence.
old = [[Q(4, 3), Q(1, 3), Q(0)],
       [Q(52, 51), Q(47, 51), Q(0)],
       [Q(0), Q(0), Q(1, 2)]]
qo, co, vo, _ = values(update(old, [Q(0)]*2), [Q(0)]*2)
assert qo+co[0][0] == Q(256, 81) and vo == [0, 0]
assert Q(113, 128)-2*Q(1, 16)/(2-Q(113, 128)) == Q(14111, 18304)
assert Q(14111, 18304)+Q(36, 25) == Q(1011719, 457600) > 2

# Constants: all rational factors checked before numerical exponentiation.
delta = Q(1, 16)
assert delta*(2-delta) == Q(31, 256)
assert 4/(delta*(2-delta)) == Q(1024, 31)
assert 2-Q(7, 2)*delta == Q(57, 32)
assert 8*(8+2)**8/delta**2 == 204800000000
for de in (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 64)):
    # Bootstrap corners, including the worst permitted mu=1/2.
    mu = Q(1, 2)
    k = de*mu
    be = de*k/8
    assert be <= k and be < de/2
    assert 2*be/k == de/4
    assert (2-4*de+de/4)/(1+de) < 2
    assert -1+2*de >= -1+k
    assert (1-Q(3, 2)*de)+be <= 1-de

m, d, n, p = 16, 8, 9, 3
tau2 = Q(1, 288)
denominator = math.prod((nu-2)*(nu-4)*(nu-6) for nu in range(8, 17))
moment_exact = Q(288**27, denominator)
log_moment = float(-n*p*math.log(2*float(tau2))+sum(
    math.lgamma(nu/2-p)-math.lgamma(nu/2) for nu in range(8, 17)))
assert abs(log_moment-math.log(float(moment_exact))) < 1e-12
gamma_direct = float(tau2)**(-n*p)*math.prod(
    2**(-p)*math.gamma(nu/2-p)/math.gamma(nu/2) for nu in range(8, 17))
assert abs(gamma_direct/float(moment_exact)-1) < 1e-13

dr = decimal(delta)
chi_r = (-R(4)/(dr*(2-dr))).exp()
K_r = R(8)*R(10)**8/(dr*dr*chi_r)
coefficient_r = decimal(moment_exact)*K_r**3
log10_coefficient = coefficient_r.log10()

def chernoff_log(u):
    return -R(m)/2*(u-1-u.ln()) if u > 1 else R(0)

eps_r = R(1)/32
threshold_r = 1-2*dr
u_q = threshold_r/(R(m)*decimal(tau2))
u_c = (1-eps_r)**2*u_q
tail_q = chernoff_log(u_q).exp()
tail_c = R(65)**8*chernoff_log(u_c).exp()
spectral_tail = tail_q+tail_c
for u in (u_q, u_c):
    # Re-evaluate the optimized MGF expression without the simplified exponent.
    t = (1-1/u)/2
    independent = -t*R(m)*u-R(m)/2*(1-2*t).ln()
    assert abs(independent-chernoff_log(u)) < R('1e-110')
bound_at_1e48 = spectral_tail+coefficient_r*R('1e-48')**3

# Certified rational intervals, independent of Decimal.exp/ln and lgamma.
# For positive x, terms after N have successive ratios <=x/(N+2).
def exp_interval(x):
    N = math.ceil(2*x)+120
    term = Q(1)
    partial = term
    for j in range(1, N+1):
        term *= x/j
        partial += term
    next_term = term*x/(N+1)
    remainder = next_term/(1-x/(N+2))
    return partial, partial+remainder

uq_exact = Q(63, 4)
uc_exact = uq_exact*Q(31, 32)**2
eq_lower, eq_upper = exp_interval(8*(uq_exact-1))
ec_lower, ec_upper = exp_interval(8*(uc_exact-1))
e_coefficient_lower, e_coefficient_upper = exp_interval(Q(3072, 31))
certified_tail_upper = uq_exact**8/eq_lower+65**8*uc_exact**8/ec_lower
certified_tail_lower = uq_exact**8/eq_upper+65**8*uc_exact**8/ec_upper
certified_coefficient_upper = moment_exact*204800000000**3*e_coefficient_upper
certified_coefficient_lower = moment_exact*204800000000**3*e_coefficient_lower
certified_full_upper = certified_tail_upper+certified_coefficient_upper*Q(1, 10**48)**3
assert certified_tail_upper < Q(9568, 10**28)  # 9.568e-25
assert certified_coefficient_upper < 1127*10**117  # 1.127e120
assert certified_full_upper < Q(21, 10**25)  # 2.1e-24
assert decimal(certified_tail_lower)*(1-R('1e-110')) <= spectral_tail
assert spectral_tail <= decimal(certified_tail_upper)*(1+R('1e-110'))
assert decimal(certified_coefficient_lower)*(1-R('1e-110')) <= coefficient_r
assert coefficient_r <= decimal(certified_coefficient_upper)*(1+R('1e-110'))
tail_interval_relative_width = decimal((certified_tail_upper-certified_tail_lower)/certified_tail_lower)
coefficient_interval_relative_width = decimal((certified_coefficient_upper-certified_coefficient_lower)/certified_coefficient_lower)

# An exact boundary start with a nonzero target lands at its minimum in one
# step. Both q and C increase, testing the monotonicity-error terms directly.
boundary_cols = [[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(-1, 2)]]
boundary_target = Q(1, 10**8)
bq, bc, bv, _ = values(boundary_cols, [boundary_target])
assert bq == bc[0][0] == Q(1, 2) and bv == [0]
assert determinant(gram(boundary_cols)) == Q(1, 4)
_, boundary_exp_upper = exp_interval(Q(64, 7))
boundary_threshold_lower = Q(1, 4)**2*Q(1, 4)/(8*3*boundary_exp_upper)
assert boundary_target < boundary_threshold_lower
boundary_next = update(boundary_cols, [boundary_target])
bqn, bcn, bvn, brn = values(boundary_next, [boundary_target])
assert brn == [0] and bvn == [boundary_target]
assert bqn == bq*(1+boundary_target**2) > bq
assert bcn[0][0] == bc[0][0]*(1+boundary_target**2) > bc[0][0]
assert bqn+bcn[0][0] < Q(9, 8)  # theorem endpoint at delta=1/4
assert update(boundary_next, [boundary_target]) == boundary_next
# Missing rank cannot be silently allowed for a nonzero target.
assert update([[Q(0)]*3, [Q(0)]*3], [Q(1)]) == [[0]*3, [0]*3]

# Nonzero-target finite probes use 120 digits: all target perturbations remain
# representable, including those far below binary64 roundoff.
initials = []
for m0, d0 in ((4, 2), (6, 3), (16, 8)):
    for case in range(2):
        cols = [[Q(rng.randint(-9, 9), 13) for _ in range(m0)]
                for _ in range(d0+1)]
        q, c, _, _ = values(cols, [Q(0)]*d0)
        sa = Q(round(10000*math.sqrt((.8, 1.15)[case]/float(q))), 10000)
        su = Q(round(10000*math.sqrt((.55, .45)[case]/max(eigenvalues(c)))), 10000)
        cols = [[x*sa for x in cols[0]]]+[[x*su for x in col] for col in cols[1:]]
        initials.append(('dense', cols))

example = [[Q(0)]*16 for _ in range(9)]
example[0][0] = Q(1)
example[1][0:2] = [Q(4, 5), Q(1, 10)]
for j in range(2, 9):
    example[j][j] = Q(1, 10)
initials.append(('initial_hessian_above_2', example))
assert (Q(9, 5)**2+2*Q(4, 5))/2 == Q(121, 50)
# Independent exact quartic symmetric differences recover the same quotient.
def line_loss(t):
    col = [v[:] for v in example]
    col[0][0] += t
    col[1][0] += t
    vv = [dot(col[0], v) for v in col[1:]]
    return dot(vv, vv)/2
s1 = line_loss(Q(1))+line_loss(Q(-1))-2*line_loss(Q(0))
sh = line_loss(Q(1, 2))+line_loss(Q(-1, 2))-2*line_loss(Q(0))
assert (16*sh-s1)/6 == Q(121, 50)

records = []
for case, (kind, initial) in enumerate(initials):
    d0, m0 = len(initial)-1, len(initial[0])
    q0, c0, v0, _ = values(initial, [Q(0)]*d0)
    for top in (2-4*delta-q0, 1-2*delta):
        matrix = [[(top if i == j else 0)-c0[i][j]
                   for j in range(d0)] for i in range(d0)]
        assert positive_definite(matrix), ('spectral certificate', case)
    det0 = determinant(gram(initial))
    assert det0 > 0 and det0 == orthogonal_volume(initial)
    M = R(d0+2)
    mu = chi_r*decimal(det0)/M**d0
    kappa = dr*mu
    allowed = dr*kappa/8
    for fraction in (R('.5'), R(1)):
        # Axis target has exactly the specified Euclidean norm.
        target_norm = allowed*fraction
        y = [target_norm]+[R(0)]*(d0-1)
        cols = [[decimal(x) for x in col] for col in initial]
        sum_r = R(0)
        sum_r2 = R(0)
        min_det_ratio = R(1)
        max_residual_ratio = R(0)
        rinitial = None
        updates = 0
        for iteration in range(3500):
            q, c, v, r = values(cols, y)
            r2 = dot(r, r)
            rn = r2.sqrt()
            if rinitial is None:
                rinitial = rn
            if rn <= target_norm*R('1e-28'):
                break
            assert r2 <= (1-dr)**2
            assert q <= decimal(q0)+2*target_norm*sum_r+R('1e-110')
            assert sum_r2 < 2
            assert 2*target_norm*sum_r <= dr/4
            nxt = update(cols, y)
            _, _, _, rnext = values(nxt, y)
            nextnorm = dot(rnext, rnext).sqrt()
            ratio = nextnorm/rn
            max_residual_ratio = max(max_residual_ratio, ratio)
            assert ratio <= 1-kappa+R('1e-25'), (case, iteration, ratio)
            if iteration % 20 == 0:
                det_ratio = determinant(gram(cols))/decimal(det0)
                min_det_ratio = min(min_det_ratio, det_ratio)
                assert det_ratio >= chi_r
            sum_r += rn
            sum_r2 += r2
            cols = nxt
            updates += 1
        q, c, v, r = values(cols, y)
        final_r = dot(r, r).sqrt()
        achieved = final_r <= target_norm*R('1e-28')
        assert achieved, (case, fraction, updates, str(final_r/target_norm))
        final_sharpness = float(q)+max(eigenvalues(c))
        assert final_sharpness < float(2-Q(7, 2)*delta)
        # With a nonzero target, final v is demonstrably not rounded to zero.
        assert abs(v[0]/target_norm-1) < R('1e-27')
        records.append({
            'case': case, 'kind': kind, 'm': m0, 'd': d0,
            'target_fraction_of_threshold': str(fraction),
            'target_norm': str(target_norm), 'initial_det': str(decimal(det0)),
            'proved_contraction_kappa': str(kappa), 'updates': updates,
            'residual_over_target': str(final_r/target_norm),
            'maximum_observed_residual_ratio': str(max_residual_ratio),
            'minimum_sampled_gram_det_ratio': str(min_det_ratio),
            'sum_squared_residuals': str(sum_r2),
            'cumulative_perturbation_bound': str(2*target_norm*sum_r),
            'final_output_sharpness': final_sharpness})

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    peak *= 1024
assert peak < 1024**3
summary = {
    'status': 'PASS', 'effective_nice': priority, 'cpu_cap_seconds': cap,
    'wall_alarm_seconds': 150, 'peak_rss_bytes': peak,
    'elapsed_seconds': time.monotonic()-started,
    'exact_rational_identity_cases': identity_cases,
    'projector_derivative_max_discrepancy': max_projector_error,
    'old_exceptional_endpoint': '256/81',
    'old_spectator_sharpness_lower_bound': '1011719/457600',
    'delta': '1/16', 'chi': str(chi_r), 'K_delta': str(K_r),
    'inverse_det_cubic_moment': str(decimal(moment_exact)),
    'cubic_probability_coefficient': str(coefficient_r),
    'log10_cubic_probability_coefficient': str(log10_coefficient),
    'gaussian_q_tail_bound': str(tail_q),
    'gaussian_C_tail_net_bound': str(tail_c),
    'spectral_complement_probability_bound': str(spectral_tail),
    'full_probability_bound_at_eta_b_1e_minus48': str(bound_at_1e48),
    'rationally_certified_spectral_tail_upper': '9.568e-25',
    'rationally_certified_cubic_coefficient_upper': '1.127e120',
    'rationally_certified_full_probability_upper_at_1e_minus48': '2.1e-24',
    'rational_tail_interval_relative_width': str(tail_interval_relative_width),
    'rational_coefficient_interval_relative_width': str(coefficient_interval_relative_width),
    'exact_boundary_nonzero_target_one_step_landing': True,
    'q_and_C_increase_in_boundary_example': True,
    'decimal_precision_digits': getcontext().prec,
    'high_precision_trajectory_cases': len(records),
    'largest_update_count': max(r['updates'] for r in records),
    'smallest_tested_nonzero_target': min(R(r['target_norm']) for r in records).to_eng_string(),
    'largest_final_output_sharpness': max(r['final_output_sharpness'] for r in records)}
Path('verification.json').write_text(json.dumps({'summary': summary, 'trajectories': records}, indent=2)+'\n')
print(json.dumps(summary, indent=2))
