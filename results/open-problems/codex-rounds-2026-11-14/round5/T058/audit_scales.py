"""Independent log-space diagnostic for the pair scale; no huge graph is built."""

import json
import math
import os
import resource
import time
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()
ell = math.log(2)


def at_phase(exponent, phase):
    # Newton in log_2(n), rather than Decimal Newton in log(n).
    def f(u):
        return 2*u-2*math.log2(u)+2/ell-1
    target = math.floor(f(exponent))+float(phase)
    u = float(exponent)
    for _ in range(8):
        u -= (f(u)-target)/(2-2/(u*ell))
    return u, math.floor(target)


def diagnostic(exponent, phase):
    u, k = at_phase(exponent, phase)
    L = u*ell
    # For these inputs, ignoring the finite-population correction changes
    # log binom(n-k,r) by at most 2*k^2/n. The largest bound is <1e-8.
    log_correction_bound = math.log(2*k*k)-L
    log_mu = k*L-math.lgamma(k+1)-k*(k-1)/2*ell
    conditional_logs = []
    for j in range(1, k):
        r = k-j
        log_binom_kj = math.lgamma(k+1)-math.lgamma(j+1)-math.lgamma(r+1)
        conditional_logs.append(log_binom_kj+r*L-math.lgamma(r+1)
                                -(k*(k-1)-j*(j-1))/2*ell)
    maximum = max(conditional_logs)
    log_sum = maximum+math.log(math.fsum(math.exp(v-maximum) for v in conditional_logs))
    log_normalized_EY = .5*log_mu+log_sum-ell
    # Independently calculate the leading term using its product of powers.
    log_normalized_leading = 1.5*log_mu+2*math.log(k)-L-ell
    return {'log2_n': u, 'target_phase': phase, 'k': k,
            'log10_EY_over_sqrt_mean': log_normalized_EY/math.log(10),
            'log10_leading_over_sqrt_mean': log_normalized_leading/math.log(10),
            'log10_of_finite_population_log_correction_bound': log_correction_bound/math.log(10)}


exact = json.loads(Path('packing_verification.json').read_text())
comparisons = []
for row in exact['asymptotic_diagnostics']:
    exponent = round(row['log2_n'])
    floating = diagnostic(exponent, row['target_phase'])
    error = abs(floating['log10_EY_over_sqrt_mean']-math.log10(row['EY_over_sqrt_mean']))
    assert error < 3e-7
    assert floating['log10_of_finite_population_log_correction_bound'] < -8
    comparisons.append({'exponent': exponent, 'phase': row['target_phase'],
                        'absolute_log10_error': error})

extended = [diagnostic(exponent, phase)
            for phase in ('.5', '.625', '.75')
            for exponent in (320, 640, 1280, 2560)]
result = {'status': 'independent log-scale diagnostics passed',
          'nice': os.getpriority(os.PRIO_PROCESS, 0),
          'comparisons_with_exact_arithmetic': comparisons,
          'extended_diagnostics': extended,
          'elapsed_seconds': time.monotonic()-started,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('scale_audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
