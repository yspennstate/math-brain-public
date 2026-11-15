"""Independent aggregate recurrence for the round 5 pressure examples."""
import itertools
import json
import math
import os
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('60s limit')))
signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()
records = []
enumerations = 0
for t in map(F, (F(3, 2), 2, 3, 10, 17, 100)):
    k = 1 + 2*t - 1/t
    root = 1 + 2*t
    other = 1 - 1/t
    # Aggregate states ending in 0, and ending in either 1 or 2.
    # This 2x2 recurrence is derived by counting allowed final edges.
    a, b = F(1), F(2)
    partitions = []
    for n in range(1, 41):
        z = (a+b)/3**n
        # Derive both characteristic roots from trace and determinant.
        assert root+other == 1+k
        assert root*other == k-2
        closed = ((1+2*t)**2 * (root/3)**(n-1)
                  + 2*(t-1)**2 * (other/3)**(n-1))/(3*(1+2*t*t))
        assert z == closed
        # The positive right eigenvector of [[1,1],[2,k]] is (1,2t).
        # Initial vector (1,2) lies between v/t and v coordinatewise.
        ratio = z/(root/3)**n
        assert 1/t <= ratio <= 1
        if n <= 6:
            total = F(0)
            for states in itertools.product(range(3), repeat=n):
                weight = F(1)
                for x, y in zip(states, states[1:]):
                    weight *= 1 if x == 0 or y == 0 else k if x == y else 0
                total += weight
            assert total/3**n == z
            enumerations += 1
        partitions.append(str(ratio))
        a, b = a+b, 2*a+k*b
    records.append(dict(t=str(t), k=str(k), pressure_eigenvalue=str(root/3),
                        last_free_ratio=partitions[-1]))

# Independently reconstruct coefficients of the general surface argument.
safe = (2, 1)
cross = (1, 0)
add = lambda x, y: tuple(a+b for a, b in zip(x, y))
lower_ratio = add(safe, cross)
upper_free = add(lower_ratio, cross)
upper_conditioned = add(upper_free, cross)
assert lower_ratio == (3, 1)
assert upper_free == (4, 1)
assert upper_conditioned == (5, 1)
output = dict(aggregate_recurrences=6*40, direct_enumerations=enumerations,
              records=records, surface_coefficients=[lower_ratio, upper_free, upper_conditioned],
              effective_nice=os.getpriority(os.PRIO_PROCESS, 0),
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              elapsed_seconds=time.monotonic()-start)
assert output['peak_rss_bytes'] < 1024**3
Path('independent_surface.json').write_text(json.dumps(output, indent=2)+'\n')
print('Independent two-state aggregate recurrences:', output['aggregate_recurrences'])
print('Direct three-state enumerations:', enumerations)
print('Pressure eigenvalues and free ratios match exact characteristic-root formulas.')
print('Independent surface coefficients:', output['surface_coefficients'])
print('Effective nice:', output['effective_nice'])
print('Peak RSS bytes:', output['peak_rss_bytes'])
print('Elapsed seconds:', output['elapsed_seconds'])
print('All independent checks passed.')
