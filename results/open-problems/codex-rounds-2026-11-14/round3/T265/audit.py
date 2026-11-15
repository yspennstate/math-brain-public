#!/usr/bin/env python3
"""Exact algebra and independent quadrature for the localized interpolator."""
import itertools
import json
import math
import os
import resource
import signal
from fractions import Fraction as Q
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
signal.alarm(60)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def rho(x):
    return max(Q(0), x)


def hat(u, v, t, h):
    return (abs(v-(t-h)*u)-2*abs(v-t*u)+abs(v-(t+h)*u))/(2*h)


def triangular(u, v, t, h):
    return Q(0) if u == 0 else abs(u)*max(Q(0), 1-abs(v/u-t)/h)


def six_neurons(d, t, h, amplitude):
    out = []
    for location, coefficient in [(t-h, 1), (t, -2), (t+h, 1)]:
        w = [-location, Q(1)]+[Q(0)]*(d-2)
        for orientation in [-1, 1]:
            out.append((amplitude*coefficient/(2*h),
                        [orientation*x for x in w]))
    return out


def evaluate(neurons, x):
    return sum(a*rho(dot(w, x)) for a, w in neurons)


algebra_cases = 0
for t, h, u, v in itertools.product(
        [Q(-3), Q(-1, 2), Q(0), Q(2)],
        [Q(1, 7), Q(1), Q(3)],
        [Q(-2), Q(-1, 3), Q(0), Q(1, 5), Q(3)],
        [Q(-10), Q(-1), Q(0), Q(1, 3), Q(2), Q(10)]):
    result = hat(u, v, t, h)
    assert result == triangular(u, v, t, h)
    assert result == evaluate(six_neurons(2, t, h, Q(1)), [u, v])
    assert result == hat(-u, -v, t, h)
    assert 3*result == hat(3*u, 3*v, t, h)
    algebra_cases += 1


def fit(xs, ys):
    n, d = len(xs), len(xs[0])
    if d < 2 or any(x[0] == 0 for x in xs):
        raise ValueError('exceptional input')
    ts = [x[1]/x[0] for x in xs]
    if len(set(ts)) != n:
        raise ValueError('projective collision')
    baseline = [sum(y*x[j] for x, y in zip(xs, ys))/n for j in range(d)]
    neurons = [(Q(1), baseline), (Q(-1), [-x for x in baseline])]
    specs = []
    for i, (x, y, t) in enumerate(zip(xs, ys, ts)):
        gap = min([abs(t-other) for j, other in enumerate(ts) if j != i],
                  default=Q(3))
        h = min(Q(1, n**3), gap/3)
        amplitude = (y-dot(baseline, x))/abs(x[0])
        specs.append((t, h, amplitude))
        neurons.extend(six_neurons(d, t, h, amplitude))
    return baseline, neurons, specs


datasets = [
    ([[Q(1), Q(0)]], [Q(-1)]),
    ([[Q(-2), Q(1)], [Q(1), Q(3)]], [Q(-1), Q(1)]),
    ([[Q(1), Q(-2), Q(3)], [Q(-2), Q(1), Q(4)],
      [Q(3), Q(2), Q(-1)], [Q(-1), Q(-4), Q(0)]],
     [Q(1), Q(-1), Q(-1), Q(1)]),
    ([[Q(1, 10**12), Q(1)], [Q(1), Q(1)],
      [Q(-1), Q(-1)-Q(1, 10**9)], [Q(2), Q(-3)]],
     [Q(-1), Q(-1), Q(1), Q(-1)]),
    ([[Q(1), Q(0)], [Q(-1), Q(1, 1000)], [Q(1), Q(1, 1000)]],
     [Q(1), Q(1), Q(1)]),
]

network_points = 0
support_points = 0
norm_checks = 0
sample_records = []
for xs, ys in datasets:
    n, d = len(xs), len(xs[0])
    baseline, neurons, specs = fit(xs, ys)
    assert len(neurons) == 6*n+2
    assert all(evaluate(neurons, x) == y for x, y in zip(xs, ys))
    for i, x in enumerate(xs):
        t, h, amp = specs[i]
        endpoint = x.copy()
        endpoint[1] += h*x[0]
        assert evaluate(neurons, endpoint) == dot(baseline, endpoint)
        assert abs(evaluate(neurons, x)-dot(baseline, x)) == abs(amp)*abs(x[0])
        norm_checks += 1
    points = xs + [[Q(u), Q(v)]+[Q(0)]*(d-2)
                   for u in [-3, -1, 0, 1, 2] for v in [-4, -1, 0, 2, 5]]
    for x in points:
        f = evaluate(neurons, x)
        odd = evaluate(neurons, [-z for z in x])
        assert f-odd == 2*dot(baseline, x)
        assert evaluate(neurons, [3*z for z in x]) == 3*f
        expected = dot(baseline, x)+sum(amp*triangular(x[0], x[1], t, h)
                                        for t, h, amp in specs)
        assert f == expected
        if x[0] == 0 or not any(abs(x[1]/x[0]-t) < h for t, h, _ in specs):
            assert f == dot(baseline, x)
            support_points += 1
        network_points += 1
    # Path formula (21), independently summed neuron by neuron.
    path_direct = math.fsum(abs(float(a))*math.sqrt(float(dot(w, w)))
                            for a, w in neurons)
    path_formula = 2*math.sqrt(float(dot(baseline, baseline)))+math.fsum(
        abs(float(amp/h))*(math.sqrt(1+float(t-h)**2)
                          +2*math.sqrt(1+float(t)**2)
                          +math.sqrt(1+float(t+h)**2))
        for t, h, amp in specs)
    assert math.isclose(path_direct, path_formula, rel_tol=2e-15)
    sample_records.append(dict(n=n, d=d, width=len(neurons),
                               min_halfwidth=str(min(row[1] for row in specs)),
                               path_norm=path_direct))

rejected_cases = 0
for xs, ys in [([[Q(0), Q(1)]], [Q(1)]),
               ([[Q(1), Q(2)], [Q(-2), Q(-4)]], [Q(1), Q(1)]),
               ([[Q(1)]], [Q(1)])]:
    try:
        fit(xs, ys)
    except ValueError:
        rejected_cases += 1
    else:
        raise AssertionError('degenerate sample was accepted')


def simpson(func, lo, hi, steps=6000):
    dx = (hi-lo)/steps
    return dx/3*math.fsum((1 if j in [0, steps] else 4 if j % 2 else 2)
                          * func(lo+j*dx) for j in range(steps+1))


def slope_closed(t, b, c):
    L = 1+t*t
    k = (b+c*t)/math.sqrt(L)
    perpendicular2 = (b*t-c)**2/L
    return math.exp(-perpendicular2/2)/(2*math.pi*L)*(
        2*math.exp(-k*k/2)+k*math.sqrt(2*math.pi)*math.erf(k/math.sqrt(2)))


def angle_density(theta, b, c):
    k = b*math.cos(theta)+c*math.sin(theta)
    perpendicular2 = max(0, b*b+c*c-k*k)
    return math.exp(-perpendicular2/2)/(2*math.pi)*(
        2*math.exp(-k*k/2)+k*math.sqrt(2*math.pi)*math.erf(k/math.sqrt(2)))


mean_cases = [(0., 0.), (2., 0.), (0., 3.), (3., 4.), (-1.5, 2.), (7., 0.)]
density_checks = 0
max_density_relative_error = 0.
for b, c in mean_cases:
    C = 1/math.pi+math.hypot(b, c)/math.sqrt(2*math.pi)
    for t in [-10., -2., -.25, 0., .5, 3., 10.]:
        # Direct Cartesian density integral, split at zero; no completed square.
        end = (math.hypot(b, c)+12)/math.sqrt(1+t*t)
        integral = simpson(lambda u: u/(2*math.pi)*(
            math.exp(-((u-b)**2+(t*u-c)**2)/2)
            +math.exp(-((-u-b)**2+(-t*u-c)**2)/2)), 0., end)
        closed = slope_closed(t, b, c)
        error = abs(integral-closed)/closed
        max_density_relative_error = max(max_density_relative_error, error)
        assert error < 5e-8, (b, c, t, error)
        assert closed <= C/(1+t*t)+1e-15
        if b == c == 0:
            assert math.isclose(closed, 1/(math.pi*(1+t*t)), rel_tol=1e-15)
        density_checks += 1
    # Independent polar-coordinate normalization over a projective half circle.
    total = simpson(lambda theta: angle_density(theta, b, c),
                    -math.pi/2, math.pi/2, steps=12000)
    assert abs(total-1) < 2e-11, (b, c, total)

mass_checks = 0
for b, c in mean_cases:
    C = 1/math.pi+math.hypot(b, c)/math.sqrt(2*math.pi)
    for xs, ys in [datasets[1], datasets[2], datasets[4]]:
        _, _, specs = fit(xs, ys)
        mass_cartesian = math.fsum(simpson(lambda t: slope_closed(t, b, c),
                                           float(t-h), float(t+h), steps=400)
                                   for t, h, _ in specs)
        mass_polar = math.fsum(simpson(lambda angle: angle_density(angle, b, c),
                                       math.atan(float(t-h)), math.atan(float(t+h)), steps=400)
                              for t, h, _ in specs)
        assert math.isclose(mass_cartesian, mass_polar, abs_tol=1e-12, rel_tol=2e-9)
        width_bound = 2*C*sum(float(h) for _, h, _ in specs)
        assert mass_cartesian <= width_bound+1e-13
        assert width_bound <= 2*C/len(xs)**2+1e-13
        if b == c == 0:
            exact_cauchy = math.fsum((math.atan(float(t+h))-math.atan(float(t-h)))/math.pi
                                     for t, h, _ in specs)
            assert abs(mass_cartesian-exact_cauchy) < 1e-12
        mass_checks += 1

# Exact moments, with a discrete isotropic G: (14) uses only these moments.
mu = [Q(1), Q(-2), Q(1, 2)]
sigma = Q(3, 2)
eta = Q(1, 5)
a = 1-2*eta
atoms = []
for S, F, G in itertools.product([-1, 1], [-1, 1], itertools.product([-1, 1], repeat=3)):
    Y = S*F
    X = [S*m+sigma*g for m, g in zip(mu, G)]
    prob = Q(1, 16)*(eta if F == -1 else 1-eta)
    atoms.append(([Y*x for x in X], prob))
assert sum(p for _, p in atoms) == 1
assert [sum(p*z[j] for z, p in atoms) for j in range(3)] == [a*m for m in mu]
covariance = [[sum(p*(z[j]-a*mu[j])*(z[k]-a*mu[k]) for z, p in atoms)
               for k in range(3)] for j in range(3)]
assert covariance == [[(sigma*sigma if j == k else 0)+4*eta*(1-eta)*mu[j]*mu[k]
                       for k in range(3)] for j in range(3)]
trace = 3*sigma*sigma+4*eta*(1-eta)*dot(mu, mu)
average_error = sum(p*q*sum(((z[j]+w[j])/2-a*mu[j])**2 for j in range(3))
                    for z, p in atoms for w, q in atoms)
assert average_error == trace/2

# Normal risk and the uniform plug-in bound, including reversed and zero directions.
baseline_risk_checks = 0
for mu in [[0., 0.], [2., 0.], [.25, -1.], [3., 4.]]:
    s = math.hypot(*mu)
    for eta in [0., .1, .49]:
        a = 1-2*eta
        alpha = eta+a*math.erfc(s/math.sqrt(2))/2
        for v in [[0., 0.], [1., 0.], [-1., 0.], [0., 1.], [3., -2.], [a*m for m in mu]]:
            nv = math.hypot(*v)
            if nv == 0:
                risk = .5
            else:
                projection = dot(v, mu)/nv
                risk = eta+a*math.erfc(projection/math.sqrt(2))/2
            rhs = math.sqrt(2/math.pi)*math.hypot(*[x-a*m for x, m in zip(v, mu)])
            assert -2e-16 <= risk-alpha <= rhs+2e-15
            if s > 0:
                error2 = sum((x-a*m)**2 for x, m in zip(v, mu))
                quadratic_rhs = math.sqrt(2/math.pi)*error2/(a*s)
                assert risk-alpha <= quadratic_rhs+2e-15
            baseline_risk_checks += 1

n, d, s, eta = 10000, 20, 2., .1
C = 1/math.pi+s/math.sqrt(2*math.pi)
example = dict(n=n, d=d, s=s, eta=eta, width=6*n+2,
               bayes_risk=eta+(1-2*eta)*math.erfc(s/math.sqrt(2))/2,
               localization_mass_bound=2*C/n**2,
               square_root_excess_bound=math.sqrt(2/math.pi)*math.sqrt((d+4*eta*(1-eta)*s*s)/n)+2*C/n**2,
               expected_excess_bound=math.sqrt(2/math.pi)*(d+4*eta*(1-eta)*s*s)/(n*(1-2*eta)*s)+2*C/n**2)
# Independent exact arithmetic for this example's quadratic variance factor.
variance_factor = (Q(d)+4*Q(1, 10)*Q(9, 10)*4)/(n*Q(4, 5)*2)
assert variance_factor == Q(67, 50000)
assert abs(example['expected_excess_bound']-(float(variance_factor)*2/math.sqrt(2*math.pi)+2*C/n**2)) < 1e-17
result = dict(algebra_cases=algebra_cases, exact_network_points=network_points,
              exact_support_checks=support_points, endpoint_norm_checks=norm_checks,
              rejected_degeneracies=rejected_cases, density_checks=density_checks,
              density_normalizations=len(mean_cases), cone_mass_checks=mass_checks,
              max_density_relative_error=max_density_relative_error,
              exact_moment_atoms=len(atoms), exact_sample_mean_pairs=len(atoms)**2,
              baseline_risk_checks=baseline_risk_checks,
              rational_sample_records=sample_records, example=example,
              niceness=priority, max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('audit_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
