"""Generate whole CTCS trees, and measure every cyclic pair in each tree.

No author code, potential, pair-chain, or approximate harmonic numbers used.
Harmonic-mixture inverse CDF is the finite split law, not an asymptotic sampler.
Separate trees, rather than leaves, are the independent Monte Carlo units.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import bisect
import math
import random
import time
import resource
import numpy as np

START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
NMAX = 4096
H = [0.]
for k in range(1, NMAX+1):
    H.append(H[-1]+1/k)
mu, variance = np.zeros(NMAX+1), np.zeros(NMAX+1)
for m in range(2, NMAX+1):
    k = np.arange(1, m)
    rates = 1/(m-k)
    mu[m] = (1+np.sum(rates*mu[k]))/H[m-1]
    variance[m] = np.sum(rates*(variance[k]+(mu[m]-mu[k])**2))/H[m-1]

SIG = 2*1.2020569031595942854/(math.pi**2/6)**3
rng = random.Random(202611140109)
def tree(n):
    """Independent clocks for BOTH children; returns all n leaf heights."""
    heights = np.empty(n)
    stack = [(0, n, 0.)]
    while stack:
        lo, m, birth = stack.pop()
        if m == 1:
            heights[lo] = birth
            continue
        death = birth + rng.expovariate(H[m-1])
        # q ~ 1/(q H[m-1]), then cut=q or m-q equiprobably.
        q = bisect.bisect_right(H, rng.random()*H[m-1], 0, m)
        cut = q if rng.getrandbits(1) else m-q
        assert 1 <= cut < m
        stack.append((lo+cut, m-cut, death))
        stack.append((lo, cut, death))
    return heights

print('WHOLE TREE exact finite-law Monte Carlo; seed=202611140109', flush=True)
print('Covariance uses all n cyclic pairs, centered at the independently recursed exact mean.', flush=True)
print('SE uses independent trees; no independence of leaves is assumed.', flush=True)
print('n trees r Var SE_V Cov SE_C Var-theory Cov-theory normalized_V normalized_C rho target', flush=True)
for n, repeats in ((32, 12000), (256, 8000), (4096, 2500)):
    rs = sorted(set([1, 2, round(math.sqrt(n)), n//4, n//2-1, n//2, n-1]))
    records = np.empty((repeats, 2+len(rs)))
    for t in range(repeats):
        x = tree(n)-mu[n]
        records[t, 0] = float(np.mean(x*x))
        records[t, 1] = float(x.mean())
        for a, r in enumerate(rs, 2):
            records[t, a] = float(np.sum(x*np.roll(x, -r))/n)
        if t % 32 == 0 and time.monotonic()-START > 220:
            raise RuntimeError('wall deadline reached')
    means = records.mean(axis=0)
    se = records.std(axis=0, ddof=1)/math.sqrt(repeats)
    assert abs(means[1]) <= 6*se[1]
    assert abs(means[0]-variance[n]) <= 6*se[0]
    # Cyclic offset n-1 has exactly the same averaged product as offset 1.
    assert np.max(np.abs(records[:, 2]-records[:, -1])) < 1e-12
    for a, r in enumerate(rs, 2):
        short = min(r, n-r)
        dv = means[0]-SIG*math.log(n)
        dc = means[a]-SIG*math.log(n/short)
        rho = means[a]/means[0]
        infl = (records[:, a]-rho*records[:, 0])/means[0]
        rho_se = infl.std(ddof=1)/math.sqrt(repeats)
        print('%d %d %d %.6f %.6f %.6f %.6f %+.6f %+.6f %+.6f %+.6f %.6f %.6f' % (
            n, repeats, r, means[0], se[0], means[a], se[a], dv, dc,
            dv/math.sqrt(math.log(n)), dc/math.sqrt(math.log(n)), rho, 1-math.log(short)/math.log(n)), flush=True)
        print('  correlation SE %.6f' % rho_se, flush=True)
    print('  exact-recursion variance %.9f; sampled mean error %+.6f +/- %.6f SE' % (variance[n], means[1], se[1]), flush=True)
print('PASS mean/variance calibration and offset reflection; wall_seconds=%.3f peak_RSS_MiB=%.2f' % (
    time.monotonic()-START, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2), flush=True)
