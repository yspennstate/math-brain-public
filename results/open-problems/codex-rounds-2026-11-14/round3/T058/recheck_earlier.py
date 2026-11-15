"""Independent finite checks of the previous worker's deterministic result."""
import json
import math
import os
import resource
import time
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()
ell = math.log(2)

# Use natural logs throughout, unlike the earlier direct enumeration.
def phase(n):
    y = math.log(n)
    return (2 / ell * (y - math.log(y) + math.log(ell) + 1) - 1) % 1

count = 0
counts = []
expected = {1000: 454, 10000: 4976, 100000: 49829, 200000: 106225}
for n in range(16, 200001):
    count += .25 <= phase(n) <= .75
    if n in expected:
        assert count == expected[n]
        counts.append([n, count])

# Iterate the entry/exit recurrence, without inverse endpoints or geometric sums.
r = math.sqrt(2)
s = math.sqrt(r)
entry = 0.0
for _ in range(1000):
    exit_fraction = (entry + s - 1) / s
    entry = exit_fraction / s
assert abs(entry - 1/(1+s)) < 1e-14

theta = []
for exponent in (10, 20, 40, 80, 160):
    n = 2**exponent
    f = 2/ell*(math.log(n)-math.log(math.log(n))+math.log(ell)+1)-1
    k = math.floor(f)
    # Integer binomial coefficient: independent of the earlier log-product method.
    log_mu = math.log(math.comb(n,k)) - ell*k*(k-1)/2
    theta.append([exponent, f-k, log_mu/math.log(n)])

result = dict(status='all checks passed', nice=os.getpriority(os.PRIO_PROCESS,0),
              integer_counts=counts, entry_density=entry, exit_density=exit_fraction,
              theta_checks=theta, elapsed_seconds=time.monotonic()-start,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('earlier_recheck.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
