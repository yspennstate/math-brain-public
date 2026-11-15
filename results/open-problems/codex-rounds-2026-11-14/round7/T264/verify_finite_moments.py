"""Small independent audits of the interpolation and moment bounds.

No optimizers or numerical libraries. Compression uses exact rational
arithmetic on the floating-point sample-response columns.
"""
from fractions import Fraction as F
import json
import math
import os
from pathlib import Path
import random
import resource
import signal
import sys
import time

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
signal.alarm(120)
started = time.monotonic()
root = Path(__file__).resolve().parent
assert root == Path.cwd().resolve()
rng = random.Random(264072)
pi = math.pi


def dot(x, y):
    return math.fsum(a*b for a, b in zip(x, y))


def norm(x):
    return math.sqrt(dot(x, x))


def unit(x):
    length = norm(x)
    return tuple(t/length for t in x)


def random_unit(d):
    return unit([rng.gauss(0, 1) for _ in range(d)])


def value(atoms, x):
    return math.fsum(c*max(0., dot(w, x)) for c, w in atoms)


def sine(x, y):
    # Exterior-product norm: independent of 1-dot(x,y)^2 cancellation.
    return math.sqrt(math.fsum((x[i]*y[j]-x[j]*y[i])**2
                    for i in range(len(x)) for j in range(i)))


def null_vector(columns):
    """Exact kernel vector for n+1 rational columns in n dimensions."""
    n, m = len(columns[0]), len(columns)
    a = [[columns[j][i] for j in range(m)] for i in range(n)]
    pivots = []
    row = 0
    for col in range(m):
        p = next((j for j in range(row, n) if a[j][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        denominator = a[row][col]
        a[row] = [v/denominator for v in a[row]]
        for j in range(n):
            if j != row:
                coefficient = a[j][col]
                a[j] = [v-coefficient*w for v, w in zip(a[j], a[row])]
        pivots.append(col)
        row += 1
        if row == n:
            break
    free = next(j for j in range(m) if j not in pivots)
    t = [F(0)]*m
    t[free] = F(1)
    for j, pivot in enumerate(pivots):
        t[pivot] = -a[j][free]
    assert all(sum(t[j]*columns[j][i] for j in range(m)) == 0
               for i in range(n))
    return t


def compress(atoms, samples):
    entries = []
    for c, w in atoms:
        if c == 0:
            continue
        sign = 1 if c > 0 else -1
        col = tuple(F(sign*max(0., dot(w, x))) for x in samples)
        entries.append([F(abs(c)), sign, w, col])
    initial_cost = sum(e[0] for e in entries)
    initial_response = [sum(e[0]*e[3][i] for e in entries)
                        for i in range(len(samples))]
    while len(entries) > len(samples):
        m = len(samples)+1
        t = null_vector([e[3] for e in entries[:m]])
        if sum(t) < 0:
            t = [-v for v in t]
        assert sum(t) >= 0 and any(v > 0 for v in t)
        step = min(entries[j][0]/v for j, v in enumerate(t) if v > 0)
        for j, v in enumerate(t):
            entries[j][0] -= step*v
            assert entries[j][0] >= 0
        entries = [e for e in entries if e[0]]
    assert sum(e[0] for e in entries) <= initial_cost
    for i in range(len(samples)):
        assert sum(e[0]*e[3][i] for e in entries) == initial_response[i]
    return [(float(beta)*sign, w) for beta, sign, w, col in entries]


def configuration(d, n, kind, eps=0.01):
    if kind == 'random':
        return [random_unit(d) for _ in range(n)]
    if kind == 'planar':
        return [tuple([math.cos(pi*(i+.17)/n), math.sin(pi*(i+.17)/n)]
                      +[0.]*(d-2)) for i in range(n)]
    center, tangent = random_unit(d), random_unit(d)
    tangent = unit([x-dot(tangent, center)*y for x, y in zip(tangent, center)])
    if kind in ('near_pair', 'near_antipode'):
        second = tuple(math.cos(eps)*x+math.sin(eps)*y
                       for x, y in zip(center, tangent))
        if kind == 'near_antipode':
            second = tuple(-v for v in second)
        return [center, second]+[random_unit(d) for _ in range(n-2)]
    assert kind == 'cluster'
    return [unit([x+eps*y for x, y in zip(center, random_unit(d))])
            for _ in range(n)]


def audit_configuration(samples, name, do_compress=False):
    n, d = len(samples), len(samples[0])
    C = 8*(n-1)*math.sqrt(d-1)
    K = n*(2+4*C)
    delta = min(sine(x, y) for i, x in enumerate(samples) for y in samples[:i])
    assert delta > 0
    labels = [(-1., 0., 1.)[i % 3] for i in range(n)]
    atoms, tents, attempts = [], [], []
    max_sine_error = 0.
    for i, e in enumerate(samples):
        other = [(j, x, sine(e, x)) for j, x in enumerate(samples) if i != j]
        for j, x, s in other:
            projection = tuple(v-dot(e, x)*u for v, u in zip(x, e))
            max_sine_error = max(max_sine_error, abs(norm(projection)-s))
            assert abs(norm(projection)-s) < 2e-14
        delta_i = min(s for j, x, s in other)
        for attempt in range(1, 513):
            if d == 2:
                z = (-e[1], e[0])
            else:
                g = [rng.gauss(0, 1) for _ in range(d)]
                z = unit([v-dot(g, e)*u for v, u in zip(g, e)])
            if all(abs(dot(z, x)) >= s/C for j, x, s in other):
                break
        else:
            raise AssertionError('No tangent direction found in 512 trials')
        attempts.append(attempt)
        assert abs(dot(z, e)) < 2e-14
        L = C/delta_i
        wplus = tuple(L*v+u for v, u in zip(z, e))
        wminus = tuple(L*v-u for v, u in zip(z, e))
        wzero = tuple(L*v for v in z)
        raw = [(1., wplus), (1., wminus), (-2., wzero)]
        tents.append((e, z, L, raw))
        for c, w in raw:
            length = norm(w)
            atoms.append((labels[i]*c*length, tuple(v/length for v in w)))
        actual_cost = math.fsum(abs(c)*norm(w) for c, w in raw)
        independent_cost = 2*math.hypot(1, L)+2*L
        assert abs(actual_cost-independent_cost) < 1e-12*independent_cost
        assert actual_cost <= (2+4*C)/delta_i*(1+1e-12)
    cost = math.fsum(abs(c) for c, w in atoms)
    assert cost <= K/delta*(1+1e-12)
    error = max(abs(value(atoms, x)-y) for x, y in zip(samples, labels))
    assert error < 1e-8, (name, error, cost)
    identity_error = 0.
    for x in samples+[random_unit(d) for _ in range(20)]:
        for e, z, L, raw in tents:
            direct = max(0., abs(dot(e, x))-L*abs(dot(z, x)))
            identity_error = max(identity_error, abs(value(raw, x)-direct))
        direct_sum = math.fsum(y*max(0., abs(dot(e, x))-L*abs(dot(z, x)))
                             for y, (e, z, L, raw) in zip(labels, tents))
        assert abs(value(atoms, x)-direct_sum) < 2e-10*max(1., cost)
    after = None
    compressed_error = None
    if do_compress:
        compressed = compress(atoms, samples)
        assert len(compressed) <= n
        after = math.fsum(abs(c) for c, w in compressed)
        assert after <= cost*(1+1e-12)
        compressed_error = max(abs(value(compressed, x)-y)
                               for x, y in zip(samples, labels))
        assert compressed_error < 1e-8
    return dict(name=name, d=d, n=n, delta=delta, cost=cost,
                proved_cost_bound=K/delta, interpolation_error=error,
                tent_identity_error=identity_error, max_trials=max(attempts),
                independent_sine_error=max_sine_error,
                compressed_cost=after, compressed_interpolation_error=compressed_error)


rows = []
for d in (2, 3, 4, 5, 8, 12):
    for n in (2, 3, 4, 6, 10):
        rows.append(audit_configuration(configuration(d, n, 'random'),
                    f'random_d{d}_n{n}', do_compress=(d == 4)))
for d in (2, 4, 8):
    for kind in ('near_pair', 'near_antipode', 'cluster'):
        for eps in (.01, .0001):
            rows.append(audit_configuration(configuration(d, 6, kind, eps),
                f'{kind}_d{d}_eps{eps}', do_compress=(eps == .01 and d == 4)))
    rows.append(audit_configuration(configuration(d, 6, 'planar'),
                f'planar_d{d}', do_compress=True))
print(f'PASS construction: {len(rows)} configurations, d=2,3,4,5,8,12, n=2,3,4,6,10')
print('PASS near-coincident pairs, near-antipodes, whole clusters, planar rank deficiency')
print('Maximum interpolation error:', max(r['interpolation_error'] for r in rows))
print('Maximum tangent-selection trials:', max(r['max_trials'] for r in rows))
print('PASS exact rational compression:', sum(r['compressed_cost'] is not None for r in rows),
      'networks reduced to at most n units, exact response preservation and cost decrease')


def simpson(fun, lo, hi, count=4096):
    h = (hi-lo)/count
    return h/3*(fun(lo)+fun(hi)+math.fsum(
        (4 if j % 2 else 2)*fun(lo+j*h) for j in range(1, count)))


moments = []
for d in range(4, 13):
    # Integrate the unnormalized sine powers directly, without a beta function.
    numerator = simpson(lambda t: math.sin(t)**(d-4), 0., pi)
    denominator = simpson(lambda t: math.sin(t)**(d-2), 0., pi)
    quadrature = numerator/denominator
    gamma_ratio = (math.gamma((d-3)/2)*math.gamma(d/2)
                   /(math.gamma((d-2)/2)*math.gamma((d-1)/2)))
    elementary = (d-2)/(d-3)
    assert abs(quadrature-elementary) < 1e-11
    assert abs(gamma_ratio-elementary) < 1e-13
    moments.append(dict(d=d, direct_integral=quadrature,
                        gamma_ratio=gamma_ratio, rational_value=elementary))
print('PASS mean pair factor: direct sine integrals, gamma ratios, and (d-2)/(d-3), d=4..12')
print('Pair factors:', [(m['d'], m['direct_integral']) for m in moments])

# The second tangent-selection proof uses spherical coordinate densities.
# Check its constant independently, including the exceptional k=1,2 cases.
for k in range(2, 21):
    ck = math.gamma(k/2)/(math.sqrt(pi)*math.gamma((k-1)/2))
    for N in (1, 2, 5, 9, 20):
        eta = 1/(8*N*math.sqrt(k))
        exact_forbidden = 2*ck*simpson(
            lambda t: (1-t*t)**((k-3)/2), 0., eta, 256)
        assert exact_forbidden <= 2*math.sqrt(k)*eta
        assert N*exact_forbidden < .25
print('PASS independent tangent constant: spherical small-ball integrals, k=2..20')

shells = []
for d in (2, 3, 4, 8):
    alpha = (d-1)/2
    for r in (alpha-.125, alpha, alpha+.125):
        def log_integrand(v):
            t = math.exp(v)
            return (math.sin(t)/t)**(d-2-2*r)*math.exp((d-1-2*r)*v)
        first = simpson(log_integrand, -12., -11.)
        second = simpson(log_integrand, -13., -12.)
        predicted = math.exp(-(d-1-2*r))
        assert abs(second/first-predicted) < 1e-9
        shells.append(dict(d=d, r=r, inward_shell_ratio=second/first,
                           predicted_ratio=predicted))
print('PASS threshold: decreasing, constant, increasing angular shells below/at/above (d-1)/2')

# Check the two projective caps independently, including the factor of two.
caps = []
for d in (2, 3, 4, 8):
    cd = math.gamma(d/2)/(math.sqrt(pi)*math.gamma((d-1)/2))
    eps = .0001
    cap = 2*cd*simpson(lambda t: math.sin(t)**(d-2), 0., math.asin(eps))
    leading = 2*cd/(d-1)*eps**(d-1)
    assert abs(cap/leading-1) < 2e-8
    caps.append(dict(d=d, sine_cutoff=eps, both_caps=cap, leading_value=leading))
print('PASS projective tail: both angular caps and exponent d-1')

# Exactly parallel opposite-label observations cannot be interpolated by tents.
x = (1., 0., 0., 0.)
assert sine(x, x) == 0 and sine(x, tuple(-v for v in x)) == 0
print('PASS excluded degeneracy: exact parallelism has delta=0; no positive-separation claim')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == 'darwin' else 1024*rss
assert rss < 1_000_000_000
stats = dict(seconds=time.monotonic()-started, peak_rss_bytes=rss,
             nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1)
data = dict(configurations=rows, pair_moments=moments, threshold_shells=shells,
            projective_caps=caps, resources=stats)
(root/'verification_data.json').write_text(json.dumps(data, indent=2)+'\n')
print('All assertions passed.')
print('Resources:', stats)
