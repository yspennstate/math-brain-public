"""Exact finite audits of the first-discarded-block estimates.

The marking model is an upper majorant, not a numerical model of full MBL.
All generated files stay beside this script. No dense matrices are needed.
"""
import os
THREAD_KEYS = ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
               'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
for key in THREAD_KEYS:
    os.environ[key] = '1'
import ctypes
from fractions import Fraction as Q
from itertools import product
import json
from math import log, exp, e, prod
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(600)
resource.setrlimit(resource.RLIMIT_CPU, (500, 500))
libc = ctypes.CDLL(None, use_errno=True)
ctypes.set_errno(0)
priority = libc.getpriority(0, 0)
assert ctypes.get_errno() == 0 and priority >= 15
ROOT = Path(__file__).resolve().parent
started = time.monotonic()
counts = {}


def count(key, amount=1):
    counts[key] = counts.get(key, 0)+amount


def pieces(sites):
    """Nearest-neighbor components from physical sites."""
    out = []
    for x in sorted(sites):
        if not out or x != out[-1][-1]+1:
            out.append([x])
        else:
            out[-1].append(x)
    return out


def cells(mask):
    n = len(mask)
    result = {}
    for f in range(n):
        if mask[f]:
            continue
        lo = hi = f
        while lo and mask[lo-1]:
            lo -= 1
        while hi+1 < n and mask[hi+1]:
            hi += 1
        core = set(range(lo, hi+1))
        full = set(range(max(0, lo-1), min(n, hi+2)))
        m = hi-lo
        c = int(lo > 0)+int(hi+1 < n)
        assert max(full)-min(full) == m+c
        result[f] = (core, full, m, c)
    return result


def unions(mask, cc, discarded):
    B = set().union(*(cc[f][0] for f in discarded))
    E = set().union(*(cc[f][1] for f in discarded))
    return B, E


def inflate(sites, n):
    return {y for x in sites for y in (x-1, x, x+1) if 0 <= y < n}


def subsets(items):
    for bits in product((0, 1), repeat=len(items)):
        yield {f for f, bit in zip(items, bits) if bit}


# Exhaustive ternary configurations, independently checking core components
# through occupied sites, rather than assembling cores a second time.
for n in range(1, 10):
    for mask in product((0, 1), repeat=n):
        cc = cells(mask)
        active = {x for x in range(n) if mask[x]}
        frozen = sorted(cc)
        for discarded in subsets(frozen):
            B, E = unions(mask, cc, discarded)
            selected = set().union(*(set(C) for C in pieces(active | discarded)
                                     if discarded.intersection(C)))
            assert B == selected
            assert E == inflate(B, n)
            for j in range(n-4):
                if all(not mask[y] for y in range(j, j+5)):
                    middle = {j+1, j+2, j+3}
                    if not (middle & discarded):
                        assert j+2 not in E
                        count('separator_geometry_checks')
            count('ternary_geometry_cases')

# Collars really can merge: core sizes alone are insufficient for full cells.
mask = (0,)*5
B, E = unions(mask, cells(mask), {1, 3})
assert [len(C) for C in pieces(B)] == [1, 1]
assert [len(C) for C in pieces(E)] == [5]
count('shared_control_merger_fixture')

# Independent indicator-incidence audit, including external active runs.
# The sharp bulk multiplicity two is attained, so replacing 16^s by 4^s
# would not be justified by this argument.
attained_two = False
for n in range(1, 9):
    for mask in product((0, 1), repeat=n):
        cc = cells(mask)
        for lo in range(n):
            for hi in range(lo, n):
                frozen = [f for f in cc if lo <= f <= hi]
                actual = sum(cc[f][2] for f in frozen)
                active_inside = sum(mask[lo:hi+1])
                left = lo-1
                while left >= 0 and mask[left]:
                    left -= 1
                right = hi+1
                while right < n and mask[right]:
                    right += 1
                external = lo-1-left+right-hi-1
                assert actual <= 2*active_inside+external
                for x in range(n):
                    if mask[x]:
                        multiplicity = sum(x in cc[f][0] for f in frozen)
                        assert multiplicity <= (2 if lo <= x <= hi else 1)
                        attained_two |= multiplicity == 2
                count('incidence_interval_checks')
assert attained_two


def capped(p, t):
    if t >= 1:
        return Q(1)
    k = 0
    while t*4**(k+1) <= 1:
        k += 1
    return ((1-p)**2*t*sum((j+1)*(4*p)**j for j in range(k+1))
            + p**(k+1)*(k+2-(k+1)*p))


def marking_probabilities(cc, ell, t):
    return {f: Q(1) if m+c > ell else min(Q(1), t*4**m)
            for f, (_, _, m, c) in cc.items()}


# Exact rational fractional-moment audit. Use a=4^s rational and t=4^-k,
# so t^s=a^-k, M and lambda are rational, even when s is irrational.
moment_params = ((Q(1, 5), Q(3, 2)), (Q(1, 2), Q(5, 4)),
                 (Q(9, 10), Q(21, 20)))
for p, a in moment_params:
    assert 1 < a <= 4 and p*a*a < 1
    M = (1-p)/(1-p*a)
    for ell in (2, 4, 8):
        for k in (2, 5):
            t = Q(1, 4**k)
            u = max(a**(-k), a**(-(ell-1)))
            lam = p*a*a+(1-p)*u
            for n in range(1, 8):
                actual = {(lo, hi): Q(0) for lo in range(n)
                          for hi in range(lo, n)}
                for mask in product((0, 1), repeat=n):
                    cc = cells(mask)
                    ds = marking_probabilities(cc, ell, t)
                    weight = p**sum(mask)*(1-p)**(n-sum(mask))
                    for f, (_, _, m, _) in cc.items():
                        assert ds[f] <= u*a**m
                        count('conditional_majorant_checks')
                    for lo, hi in actual:
                        prob = Q(1)
                        for f in cc:
                            if lo <= f <= hi:
                                prob *= ds[f]
                        actual[lo, hi] += weight*prob
                for (lo, hi), probability in actual.items():
                    assert probability <= M*M*lam**(hi-lo+1)
                    count('exact_core_interval_bounds')

# Enumerate the independent-discard upper majorant, including all oversized
# cells with discard probability one. Given the indicators, its probabilities
# dominate the actual conditional discard probabilities for every active field.
samples = []
for p in (Q(1, 5), Q(1, 2), Q(9, 10)):
    for ell in (2, 3, 5):
        for k in (2, 4):
            t = Q(1, 4**k)
            sigma = (1-p)**5*(1-t)**3
            kappa = 1-sigma
            b = min(Q(1), capped(p, t)+p**(ell-1)*(ell-(ell-1)*p))
            for n in range(1, 8):
                density = [Q(0)]*n
                core_density = [Q(0)]*n
                tail = [[Q(0)]*(n+1) for _ in range(n)]
                intervals = {(lo, hi): Q(0) for lo in range(n)
                             for hi in range(lo, n)}
                no_sep = Q(0)
                total = Q(0)
                for mask in product((0, 1), repeat=n):
                    cc = cells(mask)
                    ds = marking_probabilities(cc, ell, t)
                    frozen = sorted(cc)
                    forced = {f for f in frozen if ds[f] == 1}
                    optional = [f for f in frozen if f not in forced]
                    iw = p**sum(mask)*(1-p)**(n-sum(mask))
                    for chosen in subsets(optional):
                        discarded = forced | chosen
                        weight = iw
                        for f in optional:
                            weight *= ds[f] if f in chosen else 1-ds[f]
                        assert weight > 0
                        total += weight
                        B, E = unions(mask, cc, discarded)
                        for x in B:
                            core_density[x] += weight
                        comps = pieces(E)
                        for C in comps:
                            lo, hi = C[0], C[-1]
                            for x in C:
                                density[x] += weight
                                tail[x][len(C)] += weight
                            for a in range(lo, hi+1):
                                for z in range(a, hi+1):
                                    intervals[a, z] += weight
                        separator_present = any(
                            all(not mask[y] for y in range(j, j+5))
                            and not ({j+1, j+2, j+3} & discarded)
                            for j in range(0, n-4, 5))
                        if not separator_present:
                            no_sep += weight
                        count('marking_configurations')
                assert total == 1
                assert no_sep <= kappa**(n//5)
                count('exact_no_separator_bounds')
                for (lo, hi), probability in intervals.items():
                    assert probability <= kappa**((hi-lo+1)//5)
                    count('exact_full_cell_interval_bounds')
                for x in range(n):
                    for r in (1, 2, 4, 8):
                        eta = min(Q(1), (2*r+1)*(1-p)*b+2*p**r)
                        assert core_density[x] <= eta
                        assert density[x] <= 3*eta
                        count('exact_rarity_bounds', 2)
                    for size in range(1, n+1):
                        probability = sum(tail[x][size:])
                        assert probability <= size*kappa**(size//5)
                        count('exact_full_cell_cluster_bounds')
                if n == 7 and ell == 5 and k == 4:
                    samples.append(dict(p=str(p), ell=ell, t=str(t),
                                        site=3, exceptional_probability=str(density[3]),
                                        full_chain_probability=str(intervals[0, 6]),
                                        kappa=str(kappa)))


def merge(intervals):
    out = []
    for a, b in sorted(intervals):
        if not out or a > out[-1][1]:
            out.append([a, b])
        else:
            out[-1][1] = max(out[-1][1], b)
    return out


def resonance_intervals(Jleft, Jright, delta, W):
    # Empty active blocks, all outer spin assignments; exact uniform h law.
    intervals = []
    for l, r in product((-1, 1), repeat=2):
        center = -Jleft*l-Jright*r
        lo, hi = max(-W, center-delta/2), min(W, center+delta/2)
        if lo < hi:
            intervals.append((lo, hi))
    return merge(intervals)


# A second derivation of the separator probability: exact integration of
# actual field resonance unions, with shared bonds and three distinct fields.
# Then sum a Cartesian partition into boxes; no product of bad-event bounds
# is used in the integration.
delta, W = Q(1, 8), Q(8)
rho = 1/(2*W)
t = 4*rho*delta
for bonds in ((Q(1), Q(3), Q(2), Q(4)), (Q(0),)*4,
              (Q(1), Q(1), Q(-1), Q(-1))):
    bad = [resonance_intervals(bonds[j], bonds[j+1], delta, W)
           for j in range(3)]
    intervals = []
    for bb in bad:
        endpoints = sorted({-W, W} | {v for pair in bb for v in pair})
        partition = []
        for lo, hi in zip(endpoints, endpoints[1:]):
            mid = (lo+hi)/2
            good = not any(a < mid < b for a, b in bb)
            partition.append((hi-lo, good))
        intervals.append(partition)
    direct = Q(0)
    for box in product(*intervals):
        if all(good for _, good in box):
            vol = Q(1)
            for length, _ in box:
                vol *= length/(2*W)
            direct += vol
        count('exact_field_boxes')
    product_probability = Q(1)
    for bb in bad:
        pf = sum(hi-lo for lo, hi in bb)/(2*W)
        assert pf <= t
        product_probability *= 1-pf
    assert direct == product_probability
    assert direct >= (1-t)**3
    count('exact_field_separator_integrations')

# Independent scalar maximization check for the exponential conversion.
for p in (0.2, 0.5, 0.9):
    for t in (0.01, 0.25, 0.5):
        kappa = 1-(1-p)**5*(1-t)**3
        rate = -log(kappa)/5
        for n in (1, 5, 20, 100, 1000):
            lhs = n*kappa**(n//5)
            rhs = 2/(rate*e*kappa)*exp(-rate*n/2)
            assert lhs <= rhs*(1+1e-12)
            count('exponential_conversion_checks')

# Exact two-window conditional separator computation, separate from the
# short-chain marking enumeration. This checks the floor(n/5) exponent.
for p in (Q(1, 5), Q(1, 2), Q(9, 10)):
    for t in (Q(1, 16), Q(1, 256)):
        sigma = (1-p)**5*(1-t)**3
        one = [sigma, 1-sigma]
        for windows in range(1, 9):
            no_success = sum(prod(one[bit] for bit in outcome)
                             for outcome in product((0, 1), repeat=windows)
                             if all(outcome))
            assert no_success == (1-sigma)**windows
            count('exact_disjoint_window_checks')

illustrations = []
for p, a, ell, k in ((Q(1, 2), Q(5, 4), 16, 16),
                     (Q(9, 10), Q(21, 20), 64, 64)):
    u = a**(-min(k, ell-1))
    lam = p*a*a+(1-p)*u
    assert lam < 1
    illustrations.append(dict(p=str(p), four_to_s=str(a), ell=ell,
                              t=f'4^-{k}', lambda_exact=str(lam),
                              lambda_decimal=float(lam),
                              M_exact=str((1-p)/(1-p*a))))

rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss_raw if sys.platform == 'darwin' else 1024*rss_raw
assert rss < 1_000_000_000
result = dict(status='PASS', counts=counts,
              exact_probability_arithmetic='fractions.Fraction',
              numerical_scope='majorants and geometry, not a simulation of MBL',
              selected_marking_probabilities=samples,
              nontrivial_core_parameters=illustrations,
              nice_value=priority, thread_environment={k: os.environ[k] for k in THREAD_KEYS},
              peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-started)
(ROOT/'cluster_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
