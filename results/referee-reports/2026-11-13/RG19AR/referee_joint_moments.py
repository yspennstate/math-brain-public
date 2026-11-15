"""Original-cut first-step recursion for every pair of leaf heights.

This checks the joint law without the paper's common-clade kernel, potential,
martingales, or separation argument. Exact fractions through n=9, floats to 160.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import math
import time
import resource
from fractions import Fraction as F
import numpy as np

START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
u = {1: [F(0)]}
v = {1: [[F(0)]]}
print('Exact original-cut joint-height moments; zero based ranks in this program', flush=True)
for m in range(2, 10):
    h = sum((F(1, q) for q in range(1, m)), F(0))
    u[m] = []
    for j in range(m):
        expected = F(1)
        for cut in range(1, m):
            rate = F(m, 2*cut*(m-cut))
            child, rank = (cut, j) if j < cut else (m-cut, j-cut)
            expected += rate*u[child][rank]
        u[m].append(expected/h)
    v[m] = [[F(0) for k in range(m)] for j in range(m)]
    for j in range(m):
        for k in range(m):
            expected = u[m][j]+u[m][k]
            for cut in range(1, m):
                rate = F(m, 2*cut*(m-cut))
                if j < cut and k < cut:
                    prod = v[cut][j][k]
                elif j >= cut and k >= cut:
                    prod = v[m-cut][j-cut][k-cut]
                elif j < cut:
                    prod = u[cut][j]*u[m-cut][k-cut]
                else:
                    prod = u[m-cut][j-cut]*u[cut][k]
                expected += rate*prod
            v[m][j][k] = expected/h
    mu = sum(u[m])/m
    var = sum(v[m][j][j] for j in range(m))/m-mu**2
    covs = [sum(v[m][j][(j+r)%m] for j in range(m))/m-mu**2 for r in range(1, m//2+1)]
    print('n=%d mean=%s variance=%s cyclic_covariances=%s' % (m, mu, var, ','.join(map(str, covs))), flush=True)

N = 160
U = [None, np.zeros(1)]
V = [None, np.zeros((1, 1))]
sigma = 2*1.2020569031595942854/(math.pi**2/6)**3
max_discrepancy = 0.
for m in range(2, N+1):
    h = sum(1/q for q in range(1, m))
    means = np.ones(m)
    for cut in range(1, m):
        rate = m/(2*cut*(m-cut))
        means[:cut] += rate*U[cut]
        means[cut:] += rate*U[m-cut]
    means /= h
    products = means[:, None]+means[None, :]
    for cut in range(1, m):
        rate = m/(2*cut*(m-cut))
        products[:cut, :cut] += rate*V[cut]
        products[cut:, cut:] += rate*V[m-cut]
        independent = rate*np.outer(U[cut], U[m-cut])
        products[:cut, cut:] += independent
        products[cut:, :cut] += independent.T
    products /= h
    U.append(means)
    V.append(products)
    assert np.max(np.abs(means-means[::-1])) < 1e-12
    assert np.max(np.abs(products-products[::-1, ::-1])) < 1e-12
    if m <= 9:
        exact = np.array([[float(x) for x in row] for row in v[m]])
        max_discrepancy = max(max_discrepancy, float(np.max(np.abs(products-exact))))
    if m in (32, 128, 160):
        mean = means.mean()
        variance = np.diag(products).mean()-mean**2
        print('n=%d original-cut joint recursion: mean=%.9f variance=%.9f residual=%+.9f' % (m, mean, variance, variance-sigma*math.log(m)), flush=True)
        for r in sorted(set([1, 2, round(math.sqrt(m)), m//4, m//2-1, m//2])):
            covariance = products[np.arange(m), (np.arange(m)+r)%m].mean()-mean**2
            residual = covariance-sigma*math.log(m/r)
            print('  r=%d covariance=%.9f residual=%+.9f residual/sqrt(log n)=%+.9f' % (r, covariance, residual, residual/math.sqrt(math.log(m))), flush=True)
    if time.monotonic()-START > 220:
        raise RuntimeError('wall deadline reached')
print('Fraction/float maximum joint-moment discrepancy %.3g; reflection PASS' % max_discrepancy, flush=True)
print('wall_seconds=%.3f peak_RSS_MiB=%.2f' % (time.monotonic()-START, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2), flush=True)
