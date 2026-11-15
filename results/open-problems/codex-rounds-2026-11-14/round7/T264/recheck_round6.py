"""Fresh scalar check of round 6; writes only beside this script."""
import itertools
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
resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
signal.alarm(60)
started = time.monotonic()
root = Path(__file__).resolve().parent
assert root == Path.cwd().resolve()
rng = random.Random(264071)
pi = math.pi


def dot(x, y):
    return math.fsum(a*b for a, b in zip(x, y))


def simpson(fun, lo, hi, count=256):
    h = (hi-lo)/count
    return h/3*(fun(lo)+fun(hi)+math.fsum(
        (4 if j % 2 else 2)*fun(lo+j*h) for j in range(1, count)))


def check(theta, A, B):
    a, b, s = math.cos(theta/2), math.sin(theta/2), math.sin(theta)
    directions = ((b, a), (-b, a), (b, -a), (-b, -a))
    coefficients = (1/s, A/a-1/s, -1/s, B/a+1/s)
    assert coefficients[1] <= 0 and coefficients[3] >= 0
    def value(phi):
        x = (math.cos(phi), math.sin(phi))
        return math.fsum(c*max(0., dot(w, x))
                         for c, w in zip(coefficients, directions))
    labels = (1., -1., A, B)
    samples = ((a, b), (a, -b), (0., 1.), (0., -1.))
    error = max(abs(math.fsum(c*max(0., dot(w, x))
                    for c, w in zip(coefficients, directions))-y)
                for x, y in zip(samples, labels))
    assert error < 2e-9, error
    lam = (1/(a*b), -1/(a*b), -1/a, 1/a)
    cost = math.fsum(abs(c) for c in coefficients)
    assert abs(cost-dot(lam, labels)) < 1e-10*cost
    # Integrate the four actual ReLUs on their activation arcs.
    cuts = {0., 2*pi}
    for w in directions:
        ph = math.atan2(w[1], w[0])
        cuts.update(((ph-pi/2) % (2*pi), (ph+pi/2) % (2*pi)))
    cuts = sorted(cuts)
    circle = math.fsum(simpson(lambda t: value(t)**2, lo, hi)
                       for lo, hi in zip(cuts, cuts[1:]))/(2*pi)
    # Independently integrate the clipping identity over four quadrants.
    def clipped(phi):
        t, z = math.cos(phi), math.sin(phi)
        base = math.copysign(min(abs(t)/a, abs(z)/b), t*z)
        return base+A/a*max(0., -b*t+a*z)+B/a*max(0., -b*t-a*z)
    separate = math.fsum(simpson(lambda t: clipped(t)**2, lo, hi)
                         for lo, hi in zip(cuts, cuts[1:]))/(2*pi)
    discrepancy = abs(circle-separate)
    assert discrepancy < 2e-9*max(1., circle)
    # Direct moment of the limit on the circle: E[X1^2]=1/2.
    limit = (1+(A*A+B*B)/2)/2
    if theta == 1e-6:
        assert abs(circle-limit) < 5e-6
        assert abs(theta*cost-4) < 12e-6
    return dict(theta=theta, A=A, B=B, cost=cost, circle_risk=circle,
                independent_risk=separate, discrepancy=discrepancy,
                limiting_risk=limit, interpolation_error=error)


rows = [check(theta, A, B)
        for theta in (.3, .01, 1e-4, 1e-6)
        for A, B in [(0., 0.)]+list(itertools.product((-1., 1.), repeat=2))]
count = 0
for d in (2, 3, 8):
    for theta in (.001, .2, 1.2):
        a, b = math.cos(theta/2), math.sin(theta/2)
        for _ in range(200):
            w = [rng.gauss(0, 1) for _ in range(d)]
            norm = math.sqrt(dot(w, w))
            p, q = w[0]/norm, w[1]/norm
            numerator = max(0., a*p+b*q)-max(0., a*p-b*q)-b*q
            price = abs(numerator)/(a*b)
            independent = min(abs(p)/b, abs(q)/a)
            assert abs(price-independent) < 1e-12
            assert price <= 1+1e-12
            count += 1
print('PASS round 6: 20 interpolation/cost cases, two independent circle integrands')
print('PASS ambient dual identity:', count, 'directions')
print('Maximum circle-risk discrepancy:', max(r['discrepancy'] for r in rows))
print('Smallest-angle circle risks:',
      [(r['A'], r['B'], r['circle_risk']) for r in rows if r['theta'] == 1e-6])
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == 'darwin' else 1024*rss
assert rss < 1_000_000_000
stats = dict(seconds=time.monotonic()-started, peak_rss_bytes=rss,
             nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1)
(root/'prior_data.json').write_text(json.dumps(dict(cases=rows,
    ambient_directions=count, resources=stats), indent=2)+'\n')
print('All assertions passed.')
print('Resources:', stats)
