#!/usr/bin/env python3
"""Independent small audit of the earlier affine obstruction."""
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
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

# In dimension one all affine classifiers are thresholds in either direction.
# Compare every posterior-weighted label vector to the common noise tail.
n = 9
posterior = [Q(i, 10) for i in [1, 8, 2, 7, 5, 3, 9, 4, 6]]
patterns = set()
for cut in range(n + 1):
    mask = (1 << cut) - 1
    patterns.add(mask)
    patterns.add(mask ^ ((1 << n) - 1))
assert len(patterns) == 2 * n
actual = [Q(0)] * (n + 1)
comparison = [Q(0)] * (n + 1)
for bits in itertools.product([0, 1], repeat=n):
    mask = sum(bit << i for i, bit in enumerate(bits))
    prob = math.prod(p if bit else 1 - p for bit, p in zip(bits, posterior))
    actual[min((mask ^ a).bit_count() for a in patterns)] += prob
    comparison[sum(bits)] += math.prod(
        min(p, 1-p) if bit else max(p, 1-p)
        for bit, p in zip(bits, posterior))
assert sum(actual) == sum(comparison) == 1
for k in range(n + 1):
    assert sum(actual[:k+1]) <= min(1, len(patterns)*sum(comparison[:k+1]))

# Gaussian tail by direct quadrature rather than importing the earlier script.
steps = 20000
left, right = 2.0, 12.0
dx = (right-left)/steps
quad = dx/3 * math.fsum(
    (1 if j in (0, steps) else 4 if j % 2 else 2)
    * math.exp(-(left+j*dx)**2/2)/math.sqrt(2*math.pi)
    for j in range(steps+1))
tail = math.erfc(math.sqrt(2))/2
assert abs(quad-tail) < 1e-12
n, d = 10000, 20
alpha = .1 + .8 * quad
log_terms = [math.lgamma(n)-math.lgamma(j+1)-math.lgamma(n-j)
             for j in range(d+1)]
peak = max(log_terms)
log_m = math.log(2)+peak+math.log(math.fsum(math.exp(t-peak) for t in log_terms))
exact_log_m = math.log(2*sum(math.comb(n-1, j) for j in range(d+1)))
assert abs(log_m-exact_log_m) < 1e-10
exponent = log_m+n*math.log1p(-alpha)
lower = alpha-math.sqrt((log_m+math.log(100))/(2*n))
assert abs(exponent-(-1115.3559280520121)) < 1e-8
assert abs(lower-.03242408915612051) < 1e-12
result = dict(earlier_result_holds=True, exact_posterior_label_vectors=512,
              exact_tail_checks=10, gaussian_tail_quadrature=quad,
              gaussian_tail_erfc=tail, alpha=alpha, log_M=log_m,
              log_interpolation_bound=exponent, lower_error_99_percent=lower,
              niceness=priority,
              max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('recheck_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
