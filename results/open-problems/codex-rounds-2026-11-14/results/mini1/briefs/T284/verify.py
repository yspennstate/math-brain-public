#!/usr/bin/env python3
"""Small checks for PROOF.md; no graph-search performance experiment."""
import os
import sys
import math
import json
import time
import resource
from fractions import Fraction as F
from itertools import combinations, product
from decimal import Decimal, getcontext

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
# The inputs are tiny; try an additional cap where the platform permits it.
cap = 768 * 1024 * 1024
old_soft, old_hard = resource.getrlimit(resource.RLIMIT_AS)
try:
    resource.setrlimit(resource.RLIMIT_AS, (cap if old_soft < 0 else min(cap, old_soft), old_hard))
    cap_status = '768 MiB address-space cap requested successfully'
except (ValueError, OSError) as exc:
    cap_status = 'Address-space cap unsupported: ' + str(exc)


def mass(x, m, p):
    return p ** x.bit_count() * (1-p) ** (m-x.bit_count())


def kernel(x, y, m, p, delta):
    ans = F(1)
    for i in range(m):
        theta = (1-delta) * ((x >> i) & 1) + delta*p
        ans *= theta if ((y >> i) & 1) else 1-theta
    return ans


# Bayes' formula from the forward joint law, independently of the repair proof.
n = 4
edges = list(combinations(range(n), 2))
m = len(edges)
p, delta = F(1, 5), F(1, 3)
weights = [mass(x, m, p) for x in range(1 << m)]
transition = [[kernel(x, y, m, p, delta) for y in range(1 << m)]
              for x in range(1 << m)]
bayes_checks = 0
for h in range(1 << m):
    assert sum(weights[g]*transition[g][h] for g in range(1 << m)) == weights[h]
    for g in range(1 << m):
        posterior = weights[g]*transition[g][h]/weights[h]
        assert posterior == transition[h][g]
        bayes_checks += 1

posterior_checks = 0
by_size = {}
for k in (2, 3, 4):
    by_size[str(k)] = 0
    for h in range(1 << m):
        for subset in combinations(range(n), k):
            pair_mask = sum(1 << i for i, (u, v) in enumerate(edges)
                            if u in subset and v in subset)
            if h & pair_mask:
                continue
            counts = [F(0) for _ in range(math.comb(k, 2)+1)]
            for g in range(1 << m):
                posterior = weights[g]*transition[g][h]/weights[h]
                counts[(g & pair_mask).bit_count()] += posterior
            theta = delta*p
            for j, actual in enumerate(counts):
                expected = (math.comb(math.comb(k, 2), j) * theta**j
                            * (1-theta)**(math.comb(k, 2)-j))
                assert actual == expected
            posterior_checks += 1
            by_size[str(k)] += 1

# All nonempty Boolean events on three coordinates for several very biased laws.
moment_checks = 0
moment_results = []
for p, delta in product((F(1, 100), F(1, 5), F(1, 2), F(9, 10)),
                        (F(1, 8), F(1, 3), F(1, 2))):
    dim = 3
    states = 1 << dim
    w = [mass(x, dim, p) for x in range(states)]
    K = [[kernel(x, y, dim, p, delta) for y in range(states)] for x in range(states)]
    r = float(delta/2)
    max_nonfull = 0.0
    for event in range(1, 1 << states):
        members = [y for y in range(states) if (event >> y) & 1]
        v = sum(w[y] for y in members)
        q = [sum(K[x][y] for y in members) for x in range(states)]
        ratio = float(v) * sum(float(w[x])*float(q[x])**(-r) for x in range(states))
        assert ratio <= 1+1e-12, (p, delta, event, ratio)
        if event != (1 << states)-1:
            max_nonfull = max(max_nonfull, ratio)
        moment_checks += 1
    moment_results.append({'edge_bias': str(p), 'refresh': str(delta),
                           'max_v_times_negative_moment_nonfull': max_nonfull})

# Explicit non-Boolean f to check that solver randomness needs no event reduction.
p, delta, dim = F(1, 7), F(1, 3), 2
states = 1 << dim
w = [mass(x, dim, p) for x in range(states)]
K = [[kernel(x, y, dim, p, delta) for y in range(states)] for x in range(states)]
randomized_checks = 0
for values in product((F(0), F(1, 2), F(1)), repeat=states):
    v = sum(w[y]*values[y] for y in range(states))
    if not v:
        continue
    q = [sum(K[x][y]*values[y] for y in range(states)) for x in range(states)]
    ratio = float(v) * sum(float(w[x])*float(q[x])**(-float(delta/2)) for x in range(states))
    assert ratio <= 1+1e-12
    randomized_checks += 1

# Ceilings and mean bound, including a=1 and very small slack.
rounding_checks = 0
for a in (F(1, 5), F(1, 2), F(4, 5), F(1)):
    for b in (a/2, 3*a/4, 99*a/100):
        eta = a-b
        for d in (F(2), F(10), F(100)):
            delta = min(F(1, 2), eta/(4*d*a*a))
            for n in range(1, 501):
                if n <= d or n < 1/a or n < 2/eta:
                    continue
                k = math.ceil(a*n)
                mu = F(math.comb(k, 2))*delta*d/n
                assert k <= n
                assert mu <= eta*n/4
                assert k-math.ceil(b*n) >= eta*n/2
                rounding_checks += 1

# Two independent evaluations of log(2): Decimal.log and its atanh series.
getcontext().prec = 60
ln2_direct = Decimal(2).ln()
x = F(1, 3)
series = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(65)), F(0))
ln2_series = Decimal(series.numerator)/Decimal(series.denominator)
series_remainder_bound = 2*x**131/(F(131)*(1-x*x))
assert abs(ln2_direct-ln2_series) < Decimal('1e-58')
assert series_remainder_bound < F(1, 10**60)
kappa_direct = (2*ln2_direct-1)/4
# Optimized Poisson-Chernoff exponent t log(t/mu)-t+mu, normalized eta*n=1.
kappa_chernoff = Decimal('0.5')*(Decimal('0.5')/Decimal('0.25')).ln()-Decimal('0.5')+Decimal('0.25')
assert kappa_direct == kappa_chernoff

# Repair formula, independent derivation from covariance and stationarity.
for p, delta in product((F(1, 100), F(1, 5), F(1, 2)), (F(1, 8), F(1, 3), F(1, 2))):
    # Cov(X,Y)=(1-delta)p(1-p); E[XY]=p^2+Cov(X,Y).
    exy = p*p+(1-delta)*p*(1-p)
    assert (p-exy)/(1-p) == delta*p

report = {
    'status': 'PASS',
    'exact_bayes_identities': bayes_checks,
    'exact_conditional_binomial_cases': posterior_checks,
    'conditional_cases_by_set_size': by_size,
    'boolean_negative_moment_checks': moment_checks,
    'randomized_negative_moment_checks': randomized_checks,
    'ceiling_and_mean_checks': rounding_checks,
    'kappa_decimal': str(kappa_direct),
    'ln2_independent_series_error_bound': str(series_remainder_bound),
    'moment_grid': moment_results,
    'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'omp_num_threads': os.environ['OMP_NUM_THREADS'],
    'elapsed_seconds': round(time.monotonic()-started, 4),
    'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'address_space_cap_status': cap_status,
    'limitations': 'Finite checks supplement the proof; no optimization algorithm or hardness conjecture is tested.'
}
with open('verification.json', 'w') as f:
    json.dump(report, f, indent=2)
    f.write('\n')
for key in ('status', 'exact_bayes_identities', 'exact_conditional_binomial_cases',
            'conditional_cases_by_set_size', 'boolean_negative_moment_checks',
            'randomized_negative_moment_checks', 'ceiling_and_mean_checks',
            'kappa_decimal', 'nice', 'omp_num_threads', 'elapsed_seconds', 'max_rss_bytes_macos'):
    print(f'{key}: {report[key]}')
