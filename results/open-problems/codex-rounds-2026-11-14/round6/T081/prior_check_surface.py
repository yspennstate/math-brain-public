"""Exact safe-state surface checks; no previous code imported."""
import itertools
import json
import math
import os
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('120s limit')))
signal.alarm(120)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()
counts = dict(interval_free=0, interval_conditioned=0, density=0,
              irregular_free=0, irregular_conditioned=0, eigenpairs=0,
              entropy_sandwich=0)
records = []


def mul(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def edge(a, b, k):
    if not a or not b:
        return Q(1)
    return k if a == b else Q(0)


def shannon(probabilities):
    return -sum(float(x)*math.log(float(x)) for x in probabilities if x)


def enumerate_domain(domain, exterior, k):
    sites = sorted(domain)
    internal = [(i, sites.index((p[0]+1, p[1]))) for i, p in enumerate(sites)
                if (p[0]+1, p[1]) in domain]
    crossing = [(i, exterior[(p[0]+dx, p[1])]) for i, p in enumerate(sites)
                for dx in (-1, 1) if (p[0]+dx, p[1]) not in domain]
    free = Q(0)
    conditioned = Q(0)
    safe_mass = Q(0)
    max_cross = Q(0)
    boundary = {p for p in sites if any((p[0]+dx, p[1]+dy) not in domain
                for dx, dy in itertools.product((-1, 0, 1), repeat=2)
                if dx or dy)}
    for state in itertools.product(range(3), repeat=len(sites)):
        w = math.prod(edge(state[i], state[j], k) for i, j in internal)
        free += w
        if not w:
            continue
        factor = math.prod(edge(state[i], ext, k) for i, ext in crossing)
        conditioned += w*factor
        max_cross = max(max_cross, factor)
        if all(state[i] == 0 for i, p in enumerate(sites) if p in boundary):
            safe_mass += w
    norm = Q(3)**len(sites)
    return free/norm, conditioned/norm, safe_mass/free, max_cross, len(boundary)


def row_formula(domain, t):
    lam = (1+2*t)/3
    small = (1-1/t)/3
    c = (1+2*t)**2/(3*(1+2*t*t))
    product = Q(1)
    left = set(domain)
    while left:
        p = min(left)
        # Minimum in its horizontal component, not necessarily its whole row.
        while (p[0]-1, p[1]) in left:
            p = (p[0]-1, p[1])
        n = 0
        while p in left:
            left.remove(p)
            n += 1
            p = (p[0]+1, p[1])
        product *= c*lam**(n-1)+(1-c)*small**(n-1)
    return product


for t in map(Q, (2, 10, 100)):
    k = 1+2*t-1/t
    lam = (1+2*t)/3
    a = [[Q(1), Q(1), Q(1)], [Q(1), k, Q(0)], [Q(1), Q(0), k]]
    v = [Q(1), t, t]
    for vec, val in ((v, 1+2*t), ([Q(0), Q(1), Q(-1)], k),
                     ([-2*t, Q(1), Q(1)], 1-1/t)):
        assert mul(a, vec) == [val*x for x in vec]
        counts['eigenpairs'] += 1
    # Pressure is checked both by spectral projection and entropy-energy.
    pi = [x*x/(1+2*t*t) for x in v]
    transition = [[a[i][j]*v[j]/((1+2*t)*v[i]) for j in range(3)] for i in range(3)]
    assert sum(pi) == 1
    assert all(sum(row) == 1 for row in transition)
    assert all(sum(pi[i]*transition[i][j] for i in range(3)) == pi[j] for j in range(3))
    entropy = -sum(float(pi[i]*transition[i][j])*math.log(float(3*transition[i][j]))
                   for i in range(3) for j in range(3) if transition[i][j])
    energy = -float(pi[1]*transition[1][1]+pi[2]*transition[2][2])*math.log(float(k))
    assert abs(entropy-energy-math.log(float(lam))) < 1e-12
    records.append(dict(t=str(t), k=str(k), pressure_eigenvalue=str(lam),
                        entropy_minus_energy=entropy-energy,
                        correlation_eigenvalue_ratio=str(k/(1+2*t)),
                        correlation_length=-1/math.log(float(k/(1+2*t)))))
    for n in range(1, 7):
        h = sum(float(pi[i])*shannon(transition[i]) for i in range(3))
        entropy_rate = h-math.log(3)
        block_entropy = shannon(pi)+(n-1)*h-n*math.log(3)
        gap_transition = [[Q(int(i == j)) for j in range(3)] for i in range(3)]
        for _ in range(n+1):
            gap_transition = [[sum(gap_transition[i][m]*transition[m][j] for m in range(3))
                               for j in range(3)] for i in range(3)]
        gap_entropy = sum(float(pi[i])*shannon(gap_transition[i]) for i in range(3))
        conditioned_entropy = (n+1)*h-gap_entropy-n*math.log(3)
        assert conditioned_entropy <= n*entropy_rate+1e-12
        assert n*entropy_rate <= block_entropy+1e-12
        counts['entropy_sandwich'] += 1
        domain = {(i, 0) for i in range(n)}
        transfer = [Q(1)]*3
        for _ in range(n-1):
            transfer = mul(a, transfer)
        transfer_free = sum(transfer)/Q(3)**n
        assert transfer_free == row_formula(domain, t)
        if t == 2:
            assert transfer_free/lam**n == (5+4*Q(1, 10)**n)/9
        for left, right in itertools.product(range(3), repeat=2):
            exterior = {(-1, 0): left, (n, 0): right}
            zf, zw, safe, max_cross, boundary = enumerate_domain(domain, exterior, k)
            assert zf == transfer_free
            # Independent matrix evaluation with pinned neighboring states.
            row = [a[left][s] for s in range(3)]
            for _ in range(n-1):
                row = mul(a, row)
            transfer_pinned = sum(row[s]*a[s][right] for s in range(3))/Q(3)**n
            assert zw == transfer_pinned
            counts['interval_conditioned'] += 1
            ratio = zw/zf
            # M=2 log k, kappa=log 3. All decisive bounds are rational.
            assert (3*k**6)**(-boundary) <= ratio <= k**(2*boundary)
            assert max_cross/ratio <= (3*k**8)**boundary
            assert safe >= (3*k**4)**(-boundary)
            assert k**(-2*boundary) <= zf/lam**n <= (3*k**8)**boundary
            assert (3*k**8)**(-boundary) <= zw/lam**n <= (3*k**10)**boundary
            counts['density'] += 1
        counts['interval_free'] += 1

    window = [(i, j) for i in range(3) for j in range(2)]
    for mask in range(1, 1 << len(window)):
        domain = {p for i, p in enumerate(window) if mask & (1 << i)}
        neighbors = {(x+dx, y) for x, y in domain for dx in (-1, 1)}-domain
        for pattern in range(4):
            exterior = {p: (0 if pattern == 0 else 1 if pattern == 1 else
                            2 if pattern == 2 else 1+(p[0]+p[1]) % 2) for p in neighbors}
            zf, zw, safe, max_cross, boundary = enumerate_domain(domain, exterior, k)
            assert zf == row_formula(domain, t)
            assert (3*k**6)**(-boundary) <= zw/zf <= k**(2*boundary)
            assert safe >= (3*k**4)**(-boundary)
            assert (3*k**10)**(-boundary) <= zw/lam**len(domain) <= (3*k**10)**boundary
            counts['irregular_conditioned'] += 1
        counts['irregular_free'] += 1

# Negative test: equality-only hard constraint has no universal safe state.
negative = []
for n in range(1, 9):
    free_count = 0
    pinned_count = 0
    for state in itertools.product((1, 2), repeat=n):
        admissible = all(x == y for x, y in zip(state, state[1:]))
        free_count += admissible
        pinned_count += admissible and state[0] == 1 and state[-1] == 2
    assert Q(free_count, 2**n) == Q(2, 2**n)
    assert pinned_count == 0
    negative.append(dict(n=n, free=str(Q(free_count, 2**n)), incompatible_pinned=0))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1024**3
output = dict(counts=counts, spectral_checks=records, negative_without_safe_state=negative,
              effective_nice=os.getpriority(os.PRIO_PROCESS, 0), peak_rss_bytes=rss,
              elapsed_seconds=time.monotonic()-started)
Path('surface_checks.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
print('All exact partition, boundary, safe-mass and density checks passed.')
print('Pressure also agrees with the stationary entropy-energy identity.')
print('No-safe-state counterexample: opposite pinned boundaries give zero partition function.')
