#!/usr/bin/env python3
"""Verify the certificate with integer arithmetic, without SymPy or NumPy."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
from math import comb
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
start = time.monotonic()


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def ua(a, b, scale=1):
    c = [0]*max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += scale*v
    return trim(c)


def um(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return trim(c)


def up(a, n):
    c = [1]
    for _ in range(n):
        c = um(c, a)
    return c


def ud(a):
    return [i*a[i] for i in range(1, len(a))] or [0]


def clean(a):
    return {k: v for k, v in a.items() if v}


def ba(a, b, scale=1):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0)+scale*v
    return clean(c)


def bm(a, b):
    c = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            pair = (i+k, j+l)
            c[pair] = c.get(pair, 0)+v*w
    return clean(c)


def bp(a, n):
    c = {(0, 0): 1}
    for _ in range(n):
        c = bm(c, a)
    return c


def tensor(a, b):
    return {(i, j): v*w for i, v in enumerate(a)
            for j, w in enumerate(b) if v*w}


cert = json.loads(Path(__file__).with_name('certificate.json').read_text())
Q = {(i, j): v for i, row in enumerate(cert['Q_coefficients'])
     for j, v in enumerate(row) if v}
assert all(Q.get((j, i), 0) == v for (i, j), v in Q.items())

# A=A0/(2d), f=F0/(6z); the recurrence gives their L derivatives,
# where L=(1+x^2)d/dx, with denominators 2d^(i+1),6z^(j+1).
d = um(um([0, 1], [1, -1]), um([3, 0, -1], [1, 4, 1]))
z = um(um([1, -1], [1, 1]), [3, 0, -1])
A = [up([1, 0, 1], 3)]
F = [[0, 7, 0, 0, 0, 1]]
for order in (1, 2):
    A.append(um([1, 0, 1], ua(um(ud(A[-1]), d),
                                  um(A[-1], ud(d)), -order)))
    F.append(um([1, 0, 1], ua(um(ud(F[-1]), z),
                                  um(F[-1], ud(z)), -order)))


def m(i, j=None):
    # Clear the common denominator d^5(1+x)^3. Every exponent is >=0.
    if j is None:
        return um(um(A[i], up(d, 4-i)), up([1, 1], 3))
    assert i+j <= 3
    return um(um(um(um(A[i], F[j]), up(d, 3-i-j)),
                 up([1, 1], 2-j)), up([0, 1, 4, 1], j+1))


raw = {}
# N=E(B1 A2-A1 B2)+E1(A B2-B A2)-E2(A B1-A1 B).
# B1=-L A(y), B2=L^2 A(y), Ej=L^j f(x)+(-1)^j L^j f(y).
for sign, i, k, j in ((-1, 2, 1, 0), (-1, 1, 2, 0),
                       (1, 0, 2, 1), (-1, 2, 0, 1),
                       (1, 0, 1, 2), (1, 1, 0, 2)):
    raw = ba(raw, tensor(m(i, j), m(k)), sign)
    raw = ba(raw, tensor(m(i), m(k, j)), sign*(-1)**j)

one = {(0, 0): 1}
X = {(1, 0): 1}
Y = {(0, 1): 1}
xy = bm(X, Y)
v = ba(ba(ba(one, X, -1), Y, -1), xy, -1)
uplus = ba(X, Y)
J = ba(bm(ba(one, bp(X, 2)), ba(one, bp(Y, 2))),
       bm(uplus, ba(one, xy, -1)), 4)
expected = {(0, 0): 6}
for factor in (tensor(up(d, 2), up(d, 2)), uplus, tensor(up([1, 0, 1], 3),
               up([1, 0, 1], 3)), ba(one, xy, -1), bp(v, 2), J, Q):
    expected = bm(expected, factor)
assert raw == expected, 'Rational curvature numerator identity failed'

# Second exact check: explicit binomial sums, independent of symbolic expansion.
R = [[0]*13 for _ in range(25)]
for (i, j), c in Q.items():
    for k in range(13-i):
        for l in range(13-j):
            first = c*comb(12-i, k)*comb(12-j, l)*2**l
            for h in range(13-j):
                R[i+k+l][j+h] += first*comb(12-j, h)
assert R == cert['R_coefficients'], 'Positive-quadrant substitution failed'
assert R[0][0] == 0
assert all(R[i][j] > 0 for i in range(25) for j in range(13) if i+j)
positive = [v for row in R for v in row if v]
assert len(positive) == 324

# The coefficient of r alone is already a strictly positive lower bound.
assert R[1][0] == 63 and R[0][1] == 63
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
summary = {'numerator_monomials': len(raw), 'positive_coefficients': len(positive),
    'minimum_positive_coefficient': min(positive),
    'maximum_coefficient': max(positive), 'coefficient_sum': sum(positive),
    'elapsed_seconds': time.monotonic()-start, 'peak_rss_MiB': rss_bytes/1024**2,
    'nice': os.getpriority(os.PRIO_PROCESS, 0)}
Path(__file__).with_name('integer_audit.json').write_text(json.dumps(summary, indent=2)+'\n')
print('PASS independent integer numerator identity and all coefficient signs')
print(json.dumps(summary, sort_keys=True))
