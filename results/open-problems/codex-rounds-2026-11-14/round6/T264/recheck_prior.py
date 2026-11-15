"""Independent checks of the round-5 hemisphere mechanism; standard library."""
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

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(45)
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert ROOT == Path.cwd().resolve()
rng = random.Random(26406)


def dot(x, y):
    return math.fsum(a*b for a, b in zip(x, y))


def unit(x):
    size = math.sqrt(dot(x, x))
    return tuple(a/size for a in x)


def relu(t):
    return max(t, 0.)


def value(atoms, x):
    return math.fsum(c*relu(dot(u, x)) for c, u in atoms)


signed_count = 0
for d in (2, 3, 7):
    for theta in (.001, .05, .4):
        a, b = math.cos(theta/2), math.sin(theta/2)
        for _ in range(700):
            u = unit(tuple(rng.gauss(0, 1) for _ in range(d)))
            delta = relu(a*u[0]+b*u[1])-relu(a*u[0]-b*u[1])
            for t in (-1, 1):
                dist = dot(u, u)+1-2*t*u[1]
                # An independent stronger inequality uses unnormalized delta.
                assert dist <= 4*(1-t*delta/(2*b))+1e-11
                signed_count += 1
print(f'PASS prior localization: {signed_count} signed ambient directions')

# Four observations with two extra points in the positive separation hemisphere.
# Select fixed negative-first-coordinate directions, and solve 2x2 by Cramer.
z = [unit((-1., 1.)), unit((1., 1.))]
directions = [unit((-1., 0.)), unit((-1., 2.))]
matrix = [[relu(dot(u, x)) for u in directions] for x in z]
det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
assert abs(det) > .1
rows = []
for theta in (.01, .001, .0001):
    a, b = math.cos(theta/2), math.sin(theta/2)
    rhs = [y-relu(x[0])/a for x, y in zip(z, (2., -1.))]
    c0 = (rhs[0]*matrix[1][1]-matrix[0][1]*rhs[1])/det
    c1 = (matrix[0][0]*rhs[1]-rhs[0]*matrix[1][0])/det
    atoms = [(1/a, (1., 0.)), (-1/(a*b), (b, -a)),
             (c0, directions[0]), (c1, directions[1])]
    err = max(abs(value(atoms, x)-y) for x, y in
              [((a, b), 1.), ((a, -b), -1.)]+list(zip(z, (2., -1.))))
    assert err < 1e-12
    # Actual function values integrated by midpoint rule, not a kernel identity.
    count = 16384
    scaled = math.fsum((theta*value(atoms,
        (math.cos(2*math.pi*(j+.5)/count),
         math.sin(2*math.pi*(j+.5)/count))))**2 for j in range(count))/count
    uniform = max(abs(theta*value(atoms,
        (math.cos(2*math.pi*j/count), math.sin(2*math.pi*j/count)))
        +2*relu(-math.sin(2*math.pi*j/count))) for j in range(count))
    cost = math.fsum(abs(c) for c, _ in atoms)
    # The explicitly solved coefficients have total bounded cost below 18;
    # this is a competitor constant, not an optimal-cost assertion.
    assert cost-2/math.sin(theta) < 18
    assert uniform < 20*theta
    assert abs(scaled-1.) < 50*theta
    rows.append({'theta': theta, 'interpolation_error': err,
                 'cost_above_2_over_s': cost-2/math.sin(theta),
                 'theta_squared_risk_d2': scaled, 'uniform_error': uniform})
print('PASS prior correction: fresh 2x2 solve, all four constraints and scaled profile')
print('Smallest-angle record:', rows[-1])

# Enumerate labels and hemisphere signs together, without inserting either factor.
for n in range(3, 10):
    outcomes = list(itertools.product((-1, 1), repeat=n))
    good = sum(o[0] != o[1] and len(set(o[2:])) == 1 for o in outcomes)
    probability = good/len(outcomes)
    assert probability == 2.**(2-n)
    for d in range(2, 8):
        alpha = (d-1)/2
        # At the endpoint the angular integral and the tail integral are log-divergent.
        assert d-2-2*alpha == -1
        assert alpha-1-alpha == -1
        cd = math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d-1)/2))
        tail = probability*cd/(d-1)*(2/d)**alpha
        if d == 2:
            assert abs(tail-probability/math.pi) < 1e-16
        if d == 3:
            assert abs(tail-probability/6) < 1e-16
print('PASS prior probability: joint enumeration and both endpoint exponents')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == 'darwin' else 1024*rss
assert rss < 1_000_000_000
stats = {'seconds': time.monotonic()-started, 'peak_rss_bytes': rss,
         'nice': os.getpriority(os.PRIO_PROCESS, 0), 'threads': 1}
(ROOT/'prior_data.json').write_text(json.dumps({'records': rows, 'resources': stats}, indent=2)+'\n')
print('All assertions passed.')
print('Resources:', stats)
