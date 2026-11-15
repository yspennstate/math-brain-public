#!/usr/bin/env python3
"""Independent verification of the previous interpolation and risk bounds."""
import itertools
import json
import math
import os
import random
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


def three_hinges(x, t, h):
    # A different representation: the linear second difference is zero.
    return sum(c*max(Q(0), x[1]-r*x[0])
               for r, c in [(t-h, 1), (t, -2), (t+h, 1)])/h


rng = random.Random(26504)
samples = identities = interpolations = support_checks = 0
for n in range(2, 10):
    for d in [2, 3, 5]:
        for repeat in range(4):
            slopes = rng.sample(range(-30, 31), n)
            xs = []
            for t in slopes:
                u = Q(rng.choice([-3, -2, 1, 2, 4]), 3)
                xs.append([u, u*Q(t, 5)]+[Q(rng.randrange(-5, 6), 3)
                                          for _ in range(d-2)])
            ys = [Q(rng.choice([-1, 1])) for _ in xs]
            v = [sum(y*x[j] for x, y in zip(xs, ys))/n for j in range(d)]
            specs = []
            for i, x in enumerate(xs):
                t = x[1]/x[0]
                gap = min(abs(t-z[1]/z[0]) for j, z in enumerate(xs) if j != i)
                h = min(Q(1, n**3), gap/3)
                specs.append((t, h, (ys[i]-dot(v, x))/abs(x[0])))
            for x, y in zip(xs, ys):
                assert dot(v, x)+sum(a*three_hinges(x, t, h)
                                      for t, h, a in specs) == y
                interpolations += 1
            for t, h, a in specs:
                for u, shift in itertools.product([Q(-2), Q(0), Q(3)],
                                                   [Q(-2), Q(-1), Q(-1, 3), Q(0), Q(1), Q(2)]):
                    x = [u, u*(t+shift*h)]
                    expected = abs(u)*max(Q(0), 1-abs(shift))
                    assert three_hinges(x, t, h) == expected
                    identities += 1
                # Endpoints have no contribution from any cone.
                endpoint = [Q(1), t+h]
                assert sum(a0*three_hinges(endpoint, t0, h0)
                           for t0, h0, a0 in specs) == 0
                support_checks += 1
            samples += 1

# Independent integral of the ratio density, without completing its square.
def simpson(fun, lo, hi, steps=10000):
    dx = (hi-lo)/steps
    return dx/3*math.fsum((1 if i in [0, steps] else 4 if i % 2 else 2)
                          *fun(lo+i*dx) for i in range(steps+1))


density_checks = 0
for b, c in [(0, 0), (2, 0), (-1, 3), (3, 4)]:
    cs = 1/math.pi+math.hypot(b, c)/math.sqrt(2*math.pi)
    for t in [-3, -.25, 0, 2]:
        end = (math.hypot(b, c)+12)/math.sqrt(1+t*t)
        val = simpson(lambda u: u/(2*math.pi)*(
            math.exp(-((u-b)**2+(t*u-c)**2)/2)
            +math.exp(-((-u-b)**2+(-t*u-c)**2)/2)), 0, end)
        assert val <= cs/(1+t*t)+1e-12
        if b == c == 0:
            assert abs(val-1/(math.pi*(1+t*t))) < 1e-11
        density_checks += 1

# Re-evaluate the load-bearing numerical example with independent quadrature.
tail = simpson(lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi), 2, 12)
assert abs(tail-math.erfc(math.sqrt(2))/2) < 1e-13
n, d, s, eta = 10000, 20, Q(2), Q(1, 10)
a = 1-2*eta
variance_factor = (Q(d)+4*eta*(1-eta)*s*s)/(n*a*s)
assert variance_factor == Q(67, 50000)
cs = 1/math.pi+float(s)/math.sqrt(2*math.pi)
excess = 2/math.sqrt(2*math.pi)*float(variance_factor)+2*cs/n**2
alpha = float(eta)+float(a)*tail
assert abs(alpha-.11820010555854338) < 1e-13
assert abs(excess-.0010691876353647793) < 1e-16

# Re-derive the original affine example by exact integer arrangement count.
log_m = math.log(2*sum(math.comb(n-1, j) for j in range(d+1)))
log_prob = log_m+n*math.log1p(-alpha)
assert abs(log_prob+1115.3559280520121) < 1e-8

result = dict(earlier_result_holds=True, samples=samples,
              exact_interpolations=interpolations, three_hinge_identities=identities,
              exact_support_checks=support_checks, density_integrals=density_checks,
              bayes_risk=alpha, localization_bound=2*cs/n**2,
              expected_excess_bound=excess, affine_log_probability=log_prob,
              niceness=priority,
              max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('recheck_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
