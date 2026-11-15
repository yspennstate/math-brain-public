"""Independent finite and moment checks; does not import the authors' code.

Run with one numerical thread. All arrays are small; wall deadline 220 seconds.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import math
import time
import resource
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
def deadline():
    if time.monotonic() - START > 220:
        raise RuntimeError('wall deadline reached')
mp.mp.dps = 45
c1, c2 = float(mp.zeta(2)), float(2 * mp.zeta(3))
sig = c2 / c1**3
print('Independent referee checks; numpy', np.__version__, 'mpmath', mp.__version__, flush=True)
print('c1=%.15f c2=%.15f sigma^2=%.15f' % (c1, c2, sig), flush=True)

# Recover beta=-1 weights from binomial(m,i) B(i,m-i), rather than the
# common-clade or potential formulas. Check all cut/tag outcomes rationally.
cases = 0
for m in range(2, 21):
    h = sum((Q(1, t) for t in range(1, m)), Q(0))
    rates = []
    uniform = {}
    for i in range(1, m):
        w = Q(math.comb(m, i) * math.factorial(i-1) * math.factorial(m-i-1), math.factorial(m-1))
        rate = w / 2
        assert rate == Q(m, 2*i*(m-i))
        rates.append(rate)
        for j in range(1, m+1):
            child = (i, j) if j <= i else (m-i, j-i)
            uniform[child] = uniform.get(child, Q(0)) + rate / m
    assert sum(rates) == h
    for k in range(1, m):
        assert all(uniform[k, j] == Q(1, k*(m-k)) for j in range(1, k+1))
    for r in range(1, m):
        s = m-r
        retained, separated = {}, {}
        for j in range(1, s+1):
            for i, rate in enumerate(rates, 1):
                mass = rate / s
                if j+r <= i:
                    child = (i, j)
                elif j > i:
                    child = (m-i, j-i)
                else:
                    separated[j, i-j+1] = mass
                    continue
                retained[child] = retained.get(child, Q(0)) + mass
        for k in range(r+1, m):
            ar = Q(m*(k-r), (m-r)*k*(m-k))
            assert Q(1, m-k)-ar == Q(r, (m-r)*k)
            assert all(retained[k, j] == ar/(k-r) for j in range(1, k-r+1))
        kill = sum(separated.values(), Q(0))
        expected = sum((Q(1, t) for t in range(m-r, m)), Q(0))
        expected += Q(r, m-r)*sum((Q(1, t) for t in range(r+1, m)), Q(0))
        assert kill == expected
        assert kill + sum(retained.values(), Q(0)) == h
        for (j, theta), mass in separated.items():
            i = j+theta-1
            assert mass == Q(m, 2*s*i*(m-i))
        cases += 1
print('Exact beta weights, uniform-tag kernel, pair kernel, killing and separating weights: PASS;', cases, 'pair states, m<=20', flush=True)

def direct_drifts(m, j):
    if m == 1:
        return 0., 0.
    cuts = np.arange(1, m, dtype=float)
    sizes = np.where(cuts >= j, cuts, m-cuts)
    ranks = np.where(cuts >= j, float(j), j-cuts)
    loss = math.log(j*(m+1-j)/m) - np.log(ranks*(sizes+1-ranks)/sizes)
    rates = m/(2*cuts*(m-cuts))
    assert loss.min() >= -2e-14
    return float(np.sum(rates*loss)), float(np.sum(rates*loss*loss))

worst = np.zeros(2)
minerr = np.full(2, np.inf)
states = [(m, j) for m in range(1, 161) for j in range(1, m+1)]
states += [(m, j) for m in (512, 2048, 8192, 65536) for j in (1, 2, 3, 8, m//4, m//2, m-1, m)]
for m, j in states:
    d = np.array(direct_drifts(m, j))
    e = np.array([c1, c2])-d
    assert e.min() > -2e-12
    k = min(j, m+1-j)
    worst = np.maximum(worst, e*k / np.array([1+math.log(k+1), 1+math.log(k+1)**2]))
    minerr = np.minimum(minerr, e)
deadline()
print('Direct original-cut drift/bracket:', len(states), 'states; max normalized errors', worst, 'min errors', minerr, flush=True)
for m in (512, 8192, 65536):
    d = direct_drifts(m, m//2)
    print('center m=%d: d1=%.10f d2=%.10f' % (m, *d), flush=True)

for p in (1, 2):
    val = mp.quad(lambda x: (-mp.log(x))**p/(1-x), [0, mp.mpf('.5'), 1])
    target = mp.factorial(p)*mp.zeta(p+1)
    assert abs(val-target) < mp.mpf('1e-40')
    print('Uniform-tag logarithmic jump moment p=%d: %s; quadrature error %s' % (p, mp.nstr(val, 30), mp.nstr(abs(val-target), 4)), flush=True)

# Direct original tagged-state reward recursions for the TOTAL accumulated
# drift/bracket error, including holding-time randomness, not just its mean.
N = 192
A = [None] + [np.zeros((2, m)) for m in range(1, N+1)]
B = [None] + [np.zeros((2, m)) for m in range(1, N+1)]
maxnorm = np.zeros(2)
for m in range(2, N+1):
    h = sum(1/t for t in range(1, m))
    for j in range(1, m+1):
        e = np.array([c1, c2])-np.array(direct_drifts(m, j))
        sa, sb = np.zeros(2), np.zeros(2)
        for i in range(1, m):
            k, z = (i, j) if j <= i else (m-i, j-i)
            rate = m/(2*i*(m-i))
            sa += rate*A[k][:, z-1]
            sb += rate*B[k][:, z-1]
        A[m][:, j-1] = (e+sa)/h
        B[m][:, j-1] = (2*e*A[m][:, j-1]+sb)/h
    maxnorm = np.maximum(maxnorm, np.sqrt(B[m].max(axis=1)))
    deadline()
print('Accumulated error reward recursion, all positions m<=192: max L2 norms', maxnorm, flush=True)

# Independent first-step recursion in the UNIFORM-tag size chain.
N = 16384
H = np.r_[0., np.cumsum(1/np.arange(1, N+1, dtype=float))]
mu, var = np.zeros(N+1), np.zeros(N+1)
for m in range(2, N+1):
    k = np.arange(1, m)
    rates = 1/(m-k)
    mu[m] = (1+np.sum(rates*mu[k]))/H[m-1]
    var[m] = np.sum(rates*(var[k]+(mu[m]-mu[k])**2))/H[m-1]
    if m % 512 == 0:
        deadline()
print('Single-leaf moment recursion: n mean variance Var-sigma^2*log(n) secant slope', flush=True)
for n in (32, 128, 512, 2048, 8192, 16384):
    slope = (var[n]-var[n//2])/math.log(2)
    print('%6d %.9f %.9f %+.9f %.9f' % (n, mu[n], var[n], var[n]-sig*math.log(n), slope), flush=True)

# Separation drift checked from original cuts and starts, without using a_r.
max_delta_err = 0.
for m in range(2, 65):
    for r in range(1, m):
        total = 0.
        for j in range(1, m-r+1):
            for i in range(1, m):
                gnew = math.log(i/r) if j+r <= i else (math.log((m-i)/r) if j > i else 0.)
                total += m/(2*i*(m-i))*(math.log(m/r)-gnew)/(m-r)
        formula = sum(math.log(m/k)/(m-k) for k in range(1, m))
        formula -= sum(math.log(r/k)/(m-k) for k in range(1, r+1))
        formula += r/(m-r)*sum(math.log(k/r)/k for k in range(r+1, m))
        max_delta_err = max(max_delta_err, abs(total-formula))
    deadline()
print('Separation drift from original cuts, all r<m<=64: max discrepancy %.3g' % max_delta_err, flush=True)

max_rect = (0., None)
for r in (1, 2, 3, 8, 32, 128, 512, 2048):
    for s in (1, 2, 3, 8, 32, 128, 512, 2048):
        mass = moment = 0.
        theta = np.arange(1, r+1, dtype=float)
        for j in range(1, s+1):
            i = j+theta-1
            w = 1/(i*(s+r-i))
            # Direct difference of the two AFTER-cut potentials.
            g = np.log(j*theta/i)-np.log((r+1-theta)*(s+1-j)/(s+r-i))
            mass += float(w.sum())
            moment += float(np.sum(w*g*g))
        val = moment/mass
        if val > max_rect[0]:
            max_rect = (val, (r, s))
        deadline()
print('Rectangle weighted moment, 64 aspect-ratio cases: max E[G^2]', max_rect, flush=True)
print('ALL INDEPENDENT CHECKS PASSED; wall_seconds=%.3f peak_RSS_MiB=%.2f' % (time.monotonic()-START, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2), flush=True)
