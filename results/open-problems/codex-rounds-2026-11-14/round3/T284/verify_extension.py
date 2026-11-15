#!/usr/bin/env python3
"""Finite checks for the vanishing-loss theorem; no solver experiment."""
import json
import math
import os
import resource
import time
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from itertools import product
from pathlib import Path

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
getcontext().prec = 100


def decimal(q):
    q = F(q)
    return D(q.numerator) / D(q.denominator)


def ceil(q):
    return -((-q.numerator) // q.denominator)


def integer_log2_ceiling(n):
    return (n-1).bit_length()


# Enumerate elementary latent variables (original, refresh, replacement).
# This computes the posterior without invoking reversibility of the graph kernel.
latent_checks = 0
for bias, delta in product((F(1, 100), F(1, 5), F(1, 2)),
                           (F(1, 2), F(1, 4), F(1, 16))):
    for pairs in range(4):
        joint = [F(0)] * (pairs+1)
        for triples in product(tuple(product((0, 1), repeat=3)), repeat=pairs):
            weight = F(1)
            originals = 0
            allowed = True
            for original, refresh, replacement in triples:
                weight *= bias if original else 1-bias
                weight *= delta if refresh else 1-delta
                weight *= bias if replacement else 1-bias
                observed = replacement if refresh else original
                allowed = allowed and not observed
                originals += original
            if allowed:
                joint[originals] += weight
        denominator = sum(joint)
        assert denominator == (1-bias)**pairs
        for count in range(pairs+1):
            actual = joint[count]/denominator
            expected = (F(math.comb(pairs, count)) * (delta*bias)**count
                        * (1-delta*bias)**(pairs-count))
            assert actual == expected
            latent_checks += 1

# A distinct count-based enumeration allows more internal pairs.
count_checks = 0
for pairs, bias, delta in product(range(11), (F(1, 37), F(2, 7)),
                                  (F(1, 2), F(1, 8), F(1, 128))):
    for count in range(pairs+1):
        zero_refresh_sum = sum(
            (F(math.comb(pairs-count, z))*delta**z
             *(1-delta)**(pairs-count-z)*(1-bias)**z
             for z in range(pairs-count+1)), F(0))
        joint = (F(math.comb(pairs, count))*bias**count
                 *(1-bias)**(pairs-count)*delta**count
                 *(1-bias)**count*zero_refresh_sum)
        posterior = joint/(1-bias)**pairs
        direct = (F(math.comb(pairs, count))*(delta*bias)**count
                  *(1-delta*bias)**(pairs-count))
        assert posterior == direct
        count_checks += 1

# Numeric sanity checks of the imported moment inequality, at dyadic scales.
# Exact rationals are used for f, its mean, and all transition probabilities.
moment_checks = 0
worst_moment_ratio = 0.0
for bias, j in product((F(1, 100), F(1, 7), F(1, 2)), range(1, 9)):
    delta = F(1, 2**j)
    dim = 3
    states = range(1 << dim)
    masses = [bias**x.bit_count()*(1-bias)**(dim-x.bit_count()) for x in states]
    transition = []
    for x in states:
        row = []
        for y in states:
            weight = F(1)
            for i in range(dim):
                theta = (1-delta)*((x >> i) & 1)+delta*bias
                weight *= theta if ((y >> i) & 1) else 1-theta
            row.append(weight)
        assert sum(row) == 1
        transition.append(row)
    for mask in range(1, 1 << (1 << dim)):
        values = [F((mask >> y) & 1) for y in states]
        mean = sum(masses[y]*values[y] for y in states)
        refreshed = [sum(transition[x][y]*values[y] for y in states) for x in states]
        ratio = float(mean)*sum(float(masses[x])*float(refreshed[x])**(-float(delta/2))
                                for x in states)
        assert ratio <= 1+2e-12, (bias, delta, mask, ratio)
        worst_moment_ratio = max(worst_moment_ratio, ratio)
        moment_checks += 1

# Check the Chernoff bound against exact tails, including zero internal pairs.
gamma = D(2).ln()-D(1)/2
exact_tail_checks = 0
for pairs, theta in product(range(37), (F(1, 1000), F(1, 17), F(1, 4))):
    lam = 2*pairs*theta
    repair_budget = ceil(lam)
    tail = sum((F(math.comb(pairs, x))*theta**x*(1-theta)**(pairs-x)
                for x in range(repair_budget+1, pairs+1)), F(0))
    bound = (-gamma*decimal(lam)).exp()
    assert decimal(tail) <= bound + D('1e-95')
    exact_tail_checks += 1

# Independent optimized Poisson exponent at mean=lambda/2, threshold=lambda.
optimized_gamma = (D(1)/(D(1)/2)).ln()-1+D(1)/2
assert gamma == optimized_gamma
# Also compute log(2) by a rational atanh series, not Decimal.ln.
series = 2*sum((F(1, 3)**(2*i+1)/F(2*i+1) for i in range(110)), F(0))
remainder = 2*F(1, 3)**221/(221*(1-F(1, 9)))
assert abs(D(2).ln()-decimal(series)) < decimal(remainder)+D('1e-98')
assert remainder < F(1, 10**106)

# Uniform dyadic choice and exact ceiling inequalities for small and huge n.
# No graph or array of size n is allocated.
scale_checks = 0
sampler_checks = 0
excluded_small_scale_cases = 0
ns = (3, 8, 64, 1000, 10**6, 2**64, 2**512, 2**8192)
for n in ns:
    m = integer_log2_ceiling(n)
    assert 2**(m-1) < n <= 2**m
    assert m <= n
    # Exact probability-budget bound for all scales and trials.
    assert F(m*n**4, 2**(10*m)) <= F(1, n**5)
    sampler_checks += 1
    ln_n = D(n).ln()
    ln_ln_n = ln_n.ln()
    for s, kval in product((D(0), D(10).ln(), ln_n.sqrt(), ln_n/D(1000)),
                            (D(1)/4, D(1), D(3), D(10))):
        beta_decimal = 2*(s+kval*ln_ln_n)/ln_n
        if not (D(0) < beta_decimal <= D(1)/4):
            continue
        beta = F(beta_decimal)
        if beta <= F(1, 2**m):
            excluded_small_scale_cases += 1
            continue
        # Choose by rational comparisons, independently of the log-floor formula.
        eligible = [j for j in range(1, m+1) if F(1, 2**j) >= beta]
        j = max(eligible)
        delta = F(1, 2**j)
        assert beta <= delta < 2*beta
        assert s-decimal(delta)*ln_n/2 <= -kval*ln_ln_n+D('1e-94')
        for density, degree in product((F(1, 7), F(1, 2), F(1)),
                                        (F(1, 2), F(3), F(20))):
            k = ceil(density*n)
            lam = delta*degree*k*(k-1)/n
            bound = 2*beta*degree*k*(k-1)/n
            assert ceil(lam) <= ceil(bound)
            assert ceil(lam) <= lam+1
            scale_checks += 1

# Rounding identities over finite n, including the small k=1 case.
rounding_checks = 0
for n in range(3, 301):
    for density, degree in product((F(1, 9), F(1, 2), F(1)),
                                   (F(1, 2), F(3), F(20))):
        if n <= degree:
            continue
        k = ceil(density*n)
        for j in range(1, integer_log2_ceiling(n)+1):
            delta = F(1, 2**j)
            mean = F(math.comb(k, 2))*delta*degree/n
            lam = delta*degree*k*(k-1)/n
            assert lam == 2*mean
            assert ceil(lam) <= lam+1
            assert k*(k-1) <= n*n
            rounding_checks += 1

report = {
    'status': 'PASS',
    'latent_refresh_posterior_checks': latent_checks,
    'count_based_posterior_checks': count_checks,
    'dyadic_negative_moment_checks': moment_checks,
    'worst_moment_ratio': worst_moment_ratio,
    'exact_binomial_tail_checks': exact_tail_checks,
    'scale_and_loss_checks': scale_checks,
    'all_scale_sampler_budget_checks': sampler_checks,
    'excluded_small_scale_cases': excluded_small_scale_cases,
    'rounding_checks': rounding_checks,
    'largest_test_n': '2^8192 (symbolic integers only; no n-sized allocation)',
    'gamma_decimal': str(gamma),
    'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'omp_num_threads': os.environ['OMP_NUM_THREADS'],
    'elapsed_seconds': round(time.monotonic()-started, 4),
    'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'limitations': 'Finite checks supplement the proof and do not prove reverse hypercontractivity or solve T284.'
}
assert report['max_rss_bytes_macos'] < 1024**3
Path('extension_verification.json').write_text(json.dumps(report, indent=2)+'\n')
for key, value in report.items():
    print(f'{key}: {value}')
