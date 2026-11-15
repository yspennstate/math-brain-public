"""Independent bit-mask geometry and rational centering algebra."""
import itertools
import json
import os
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('60s limit')))
signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()

# Rebuild adjacency and flooding with integer masks; no earlier module imported.
points = list(itertools.product(range(3), repeat=2))
adjacency = [sum(1 << j for j, q in enumerate(points)
                 if max(abs(p[k]-q[k]) for k in range(2)) <= 1) for p in points]


def expand(bits):
    out = bits
    for i in range(9):
        if bits & (1 << i):
            out |= adjacency[i]
    return out


def connected(bits):
    seen = bits & -bits
    while True:
        new = expand(seen) & bits
        if new == seen:
            return seen == bits
        seen = new


supports = [m for m in range(1, 512) if connected(m)]
separated_pairs = sum(not (expand(a) & b) for a in supports for b in supports)
assert (len(supports), separated_pairs) == (388, 204)
prior = json.loads(Path('geometry_checks.json').read_text())
assert prior['connected_supports_3x3'] == len(supports)
assert prior['counts']['support_pairs'] == separated_pairs

# Finite normalized convolution: diagonal retained separately in particle sums.
# This tests the algebra, with arbitrary integer occupations, not hard-sphere geometry.
n = 6
kernel = [[Q(1, 2) if i == j else Q(1, 4) if (i-j) % n in (1, n-1)
           else Q(0) for j in range(n)] for i in range(n)]
assert all(sum(row) == 1 for row in kernel)


def pair(a, b):
    return sum(a[i]*kernel[i][j]*b[j] for i in range(n) for j in range(n))


centering_checks = 0
profiles = ([0]*n, [1]*n, [0, 2, 0, 2, 0, 2], [2, 1, 0, 1, 2, 0])
for mask, profile, c in itertools.product(range(1, 1 << n), profiles, map(Q, (0, 1, 2))):
    inside = [Q(bool(mask & (1 << i))) for i in range(n)]
    outside = [1-x for x in inside]
    na = [profile[i]*inside[i] for i in range(n)]
    nb = [profile[i]*outside[i] for i in range(n)]
    xa = [na[i]-c*inside[i] for i in range(n)]
    xb = [nb[i]-c*outside[i] for i in range(n)]
    mu = -Q(1, 3)
    h = mu+c-kernel[0][0]/2
    count = sum(na)
    volume = sum(inside)
    boundary = pair(inside, outside)
    free_physical = -mu*count-(pair(na, na)-kernel[0][0]*count)/2
    physical = free_physical-pair(na, nb)
    centered_free = -h*count-pair(xa, xa)/2
    centered = centered_free-pair(xa, xb)
    scalar = c*c*(volume+boundary)/2-c*pair(inside, nb)
    assert physical == centered+scalar
    free_scalar = c*c*volume/2+c*pair(na, outside)-c*c*boundary/2
    assert free_physical == centered_free+free_scalar
    centering_checks += 1
assert centering_checks == 756

# Independently audit all coefficients as vectors (coefficient of M, of kappa).
safe_probability = (2, 1)
crossing = (1, 0)
lower_ratio = tuple(a+b for a, b in zip(safe_probability, crossing))
density = tuple(a+b for a, b in zip(lower_ratio, crossing))
upper_free = tuple(a+b for a, b in zip(lower_ratio, crossing))
upper_conditioned = tuple(a+b for a, b in zip(upper_free, crossing))
assert lower_ratio == (3, 1)
assert density == upper_free == (4, 1)
assert upper_conditioned == (5, 1)

output = dict(connected_supports=len(supports), separated_pairs=separated_pairs,
              exact_centering_and_free_identities=centering_checks,
              coefficient_vectors=dict(lower_ratio=lower_ratio, density=density,
                   upper_free=upper_free, upper_conditioned=upper_conditioned),
              effective_nice=os.getpriority(os.PRIO_PROCESS, 0),
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              elapsed_seconds=time.monotonic()-started)
assert output['peak_rss_bytes'] < 1024**3
Path('calculation_audit.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
print('Independent geometry counts, both centering identities and coefficient audit passed.')
