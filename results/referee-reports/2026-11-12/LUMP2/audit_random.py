"""Exact adversarial checks of Sections 1--4 and 6, independent of author code."""
import os
import random
import resource
import signal
import time
from itertools import combinations
from audit_core import Q, chain, dot, energy, inverse, killed, mul, potentials, quotient, solve

signal.alarm(240)
started = time.monotonic()
rng = random.Random(831727019)
counts = dict(networks=0, merges=0, entries=0, minimum_checks=0, set_tests=0, roots=0)
largest = Q(0)


def psd(a):
    a = [row[:] for row in a]
    while a:
        assert a[0][0] >= 0
        if a[0][0] == 0:
            assert all(v == 0 for v in a[0])
            a = [row[1:] for row in a[1:]]
        else:
            a = [[a[i][j] - a[i][0] * a[0][j] / a[0][0]
                  for j in range(1, len(a))] for i in range(1, len(a))]


def base_checks(c):
    n, pi, f, kap = c['n'], c['pi'], c['F'], c['kappa']
    assert c['T'] > 0
    tau0 = dot(pi, c['H'][0])
    assert all(dot(pi, row) == tau0 for row in c['H'])
    z = inverse([[int(i == j) - c['P'][i][j] + pi[j] for j in range(n)] for i in range(n)])
    assert sum(z[i][i] for i in range(n)) - 1 == tau0
    assert c['T'] <= tau0 <= (n - 1) * c['T']
    # Exact spectral inequality T >= tau2: T*L >= D - dd^T/W.
    psd([[c['T'] * c['L'][i][j] - int(i == j) * c['d'][i]
          + c['d'][i] * c['d'][j] / c['W'] for j in range(n-1)] for i in range(n-1)])
    for i in range(n):
        assert min(c['phi'][i]) == 0 and dot(pi, c['phi'][i]) == kap[i]
        assert dot(pi, f[i]) == 0
        x = [pi[j] * c['phi'][i][j] for j in range(n)]
        # Expected pre-stopping departures x, terminal mass pi; optimality certificate.
        assert sum(x) == kap[i]
        assert all(x[j] - sum(x[k] * c['P'][k][j] for k in range(n))
                   == int(i == j) - pi[j] for j in range(n))
        for j in range(n):
            assert f[i][j] == f[j][i]
            assert energy(c, c['phi'][i], c['phi'][j]) == -c['W'] * f[i][j]
    for root in range(n):
        gamma = potentials(c, root)
        zeta = mul(gamma, c['d'])
        mean = dot(pi, zeta)
        for i in range(n):
            assert zeta[i] == c['H'][i][root]
            for j in range(n):
                assert c['H'][i][j] == zeta[i] - zeta[j] - c['W'] * (gamma[i][j] - gamma[j][j])
                assert f[i][j] == zeta[i] + zeta[j] - mean - c['W'] * gamma[i][j]
                assert mul(c['L'], [f[k][j] for k in range(n)])[i] == c['d'][i] - c['W'] * int(i == j)
        counts['roots'] += 1


def test_merges(c):
    global largest
    n, f, pi, kap = c['n'], c['F'], c['pi'], c['kappa']
    for u, v in combinations(range(n), 2):
        blocks = [[u, v]] + [[i] for i in range(n) if i not in (u, v)]
        idx = {x: i for i, block in enumerate(blocks) for x in block}
        d = chain(quotient(c['w'], blocks))
        assert d['W'] == c['W']
        assert d['pi'] == [sum(pi[x] for x in block) for block in blocks]
        # Direct Dirichlet solve for the harmonic measure, including loops in P.
        keep = [i for i in range(n) if i not in (u, v)]
        h = [Q(int(i == u)) for i in range(n)]
        hs = solve([[int(i == j) - c['P'][i][j] for j in keep] for i in keep],
                   [c['P'][i][u] for i in keep])
        for i, val in zip(keep, hs):
            h[i] = val
        resistance = 1 / energy(c, h, h)
        hb = dot(pi, h)
        beta = [f[i][v] - f[i][u] for i in range(n)]
        assert beta == [c['W'] * resistance * (h[i] - hb) for i in range(n)]
        gamma = potentials(c, v)
        for i in range(n):
            assert gamma[i][u] == resistance * h[i]
            for j in range(n):
                lifted = d['F'][idx[i]][idx[j]]
                assert lifted == f[i][j] + beta[i] * beta[j] / (c['W'] * resistance)
                assert lifted <= kap[i] + kap[j]
                if beta[i] * beta[j] > 0:
                    sign = 1 if beta[i] > 0 else -1
                    bi, bj = sign * beta[i], sign * beta[j]
                    uu, vv = (u, v) if sign == 1 else (v, u)
                    gi = [value / bi for value in c['phi'][i]]
                    gj = [value / bj for value in c['phi'][j]]
                    eta = list(map(min, gi, gj))
                    xi = [a - b for a, b in zip(gi, eta)]
                    xj = [a - b for a, b in zip(gj, eta)]
                    em = dot(pi, eta)
                    assert eta[uu] - eta[vv] == 1 and eta[uu] >= 1
                    assert em >= pi[uu] > 0
                    assert energy(c, eta, eta) >= 1 / resistance
                    assert energy(c, xi, xj) <= 0
                    lhs = energy(c, gi, eta) + energy(c, gj, eta) - energy(c, gi, gj)
                    assert lhs == energy(c, eta, eta) - energy(c, xi, xj)
                    assert lhs == c['W'] * ((eta[i]-em)/bi + (eta[j]-em)/bj + f[i][j]/(bi*bj))
                    assert lifted <= kap[i] + kap[j] - (bi+bj)*em < kap[i]+kap[j]
                    counts['minimum_checks'] += 1
                else:
                    assert lifted <= f[i][j] <= kap[i]
                counts['entries'] += 1
        assert d['T'] < 2*c['T']
        assert d['T'] <= (n-2)*c['T'] if n > 2 else d['T'] == 0
        largest = max(largest, d['T']/c['T'])
        counts['merges'] += 1


def partition_checks(c):
    n = c['n']
    # A random arbitrary partition, plus the identity and the one-state partition.
    q = rng.randrange(1, n+1)
    labels = list(range(q)) + [rng.randrange(q) for _ in range(n-q)]
    rng.shuffle(labels)
    for blocks in ([[i for i in range(n) if labels[i] == b] for b in range(q)],
                   [[i] for i in range(n)], [list(range(n))]):
        d = chain(quotient(c['w'], blocks))
        assert d['T'] <= dot(c['pi'], c['H'][0])
        assert d['T'] <= c['T'] * min(2**(n-len(blocks)), max(0,len(blocks)-1))
        if len(blocks) > 1:
            assert dot(d['pi'], d['H'][0]) <= dot(c['pi'], c['H'][0])
        for mask in range(1, 2**len(blocks)-1):
            at = {i for i in range(len(blocks)) if mask >> i & 1}
            target = {i for b in at for i in blocks[b]}
            ht, hq = killed(c, target), killed(d, at)
            assert max(hq) <= sum(ht) <= (n-len(target))*max(ht)
            counts['set_tests'] += 1


def random_weights(n):
    w = [[Q(0)]*n for _ in range(n)]
    for i in range(n):
        # Loops at every state. Widely differing mass scales.
        w[i][i] = Q(rng.randrange(1,10), rng.choice([1,3,101])) * Q(10)**rng.randrange(-2,4)
        if i:
            j = rng.randrange(i)
            w[i][j] = w[j][i] = Q(rng.randrange(1,8),rng.randrange(1,8))*Q(10)**rng.randrange(-2,4)
    for i,j in combinations(range(n),2):
        if rng.random() < .35:
            w[i][j] = w[j][i] = Q(rng.randrange(1,15),rng.randrange(1,11))
    return w


for n in range(2,9):
    for trial in range(5):
        c = chain(random_weights(n))
        base_checks(c)
        test_merges(c)
        partition_checks(c)
        counts['networks'] += 1
    print('finished size', n, counts, flush=True)

# Periodic chains and symmetric negative-eigenvalue examples.
for n in (2,3,4,6):
    weights = [[Q(int(abs(i-j)==1)) for j in range(n)] for i in range(n)]
    c = chain(weights)
    base_checks(c)
    test_merges(c)
    partition_checks(c)
    counts['networks'] += 1
for n in range(2,9):
    c = chain([[int(i != j) for j in range(n)] for i in range(n)])
    assert c['T'] == Q(n-1,n)
    base_checks(c)
    counts['networks'] += 1

elapsed = time.monotonic()-started
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('ALL EXACT RANDOM CHECKS PASSED', counts)
print('largest tested one-merge ratio', largest, float(largest))
print('elapsed_seconds', elapsed, 'peak_rss_bytes', rss)
with open('LOG.md','a') as log:
    log.write('\n## Independent exact random audit\n\n')
    log.write(f'- `audit_random.py`: all checks passed, {counts}; elapsed {elapsed:.3f} s, peak RSS {rss} bytes.\n')
    log.write(f'- Largest tested one-merge ratio: {float(largest):.9f}. Every entry checked against direct quotient hitting solves, with exact rank-one and strict minimum-potential inequalities. Grounded identities tested at every root; stopping occupation equations, exact spectral PSD inequality, arbitrary partitions, hitting sets, periodic chains and complete graphs also passed.\n')
