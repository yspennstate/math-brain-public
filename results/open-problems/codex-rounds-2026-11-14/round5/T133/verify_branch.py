#!/usr/bin/env python3
"""Finite-B audit by scalar Neumann iteration and analytic quadrature derivatives."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import cmath
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import mpmath as mp

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
start = time.monotonic()
mp.mp.dps = 80
g = mp.pi/4
delta = 3*mp.pi/4


def critical_pair(B, u, theta, n=64):
    # Composite two-point Gauss rule on [-1,1]. All linear algebra is scalar.
    assert n % 2 == 0
    w = 2/n
    nodes = [-1+(2*j+1+v/math.sqrt(3))*w
             for j in range(n//2) for v in (-1, 1)]
    M = [[B*w/(2*math.pi*math.cosh(B*(r-s))) for s in nodes] for r in nodes]
    rho = [1.0]*n
    for _ in range(80):
        nxt = [1+sum(c*v for c, v in zip(row, rho)) for row in M]
        if max(abs(a-b) for a, b in zip(nxt, rho)) < 1e-15:
            rho = nxt
            break
        rho = nxt
    else:
        raise AssertionError('Neumann iteration did not converge')
    rhs = [sum(w*(1-B*(r-s)*math.tanh(B*(r-s)))*v/
               (2*math.pi*math.cosh(B*(r-s))) for s, v in zip(nodes, rho))
           for r in nodes]
    rhob = list(rhs)
    for _ in range(80):
        nxt = [f+sum(c*v for c, v in zip(row, rhob)) for f, row in zip(rhs, M)]
        if max(abs(a-b) for a, b in zip(nxt, rhob)) < 1e-15:
            rhob = nxt
            break
        rhob = nxt
    else:
        raise AssertionError('Derivative iteration did not converge')
    gf = math.pi/4
    T = 3*math.pi/4-u
    h = 4/3

    def Apair(z):
        den = cmath.cosh(z)+math.cos(gf)
        value = math.sin(gf)/(2*math.pi*den)
        return value, -value*cmath.sinh(z)/den

    def Epair(z):
        den = cmath.cosh(z)-math.cos(T)
        dh = cmath.cosh(h*z)-math.cos(h*T)
        first = math.sin(T)/(2*math.pi*den)
        second = h*math.sin(h*T)/(2*math.pi*dh)
        return first-second, -first*cmath.sinh(z)/den+second*h*cmath.sinh(h*z)/dh

    vals = []
    for evaluator, shift in ((Apair, theta-u), (Apair, theta+u), (Epair, theta)):
        samples = [evaluator(B*r+1j*shift) for r in nodes]
        db = w*sum((v+B*vb)*f+B*v*r*fs
                   for r, v, vb, (f, fs) in zip(nodes, rho, rhob, samples))
        dt = w*sum(v*1j*fs for v, (f, fs) in zip(rho, samples))
        assert abs(db.imag) < 1e-10 and abs(dt.imag) < 1e-10
        vals.append((db.real, dt.real))
    (a, ap), (b, bp), (e, ep) = vals
    W = a*bp-ap*b
    return ((e*bp-ep*b)/W, (a*ep-ap*e)/W)


rows = []
for fus, fts in (('.05', '.4'), ('.2', '-.6'), ('.5', '.3'), ('.9', '-.5')):
    fu, ft = mp.mpf(fus), mp.mpf(fts)
    u = fu*delta
    T = delta-u
    theta = ft*T
    a = lambda t: mp.sin(g)/(2*mp.pi*(mp.cos(t-u)+mp.cos(g)))
    b = lambda t: a(-t)
    e = lambda t: (mp.sin(T)/(mp.cos(t)-mp.cos(T)) -
        mp.mpf(4)/3*mp.sin(4*T/3)/(mp.cos(4*t/3)-mp.cos(4*T/3)))/(2*mp.pi)

    def point(t):
        A, B, E = a(t), b(t), e(t)
        ap, bp, ep = mp.diff(a, t), mp.diff(b, t), mp.diff(e, t)
        W = A*bp-ap*B
        return ((E*bp-ep*B)/W, (A*ep-ap*E)/W)

    base = point(theta)
    av = [mp.diff(a, theta, j) for j in range(4)]
    bv = [mp.diff(b, theta, j) for j in range(4)]
    ev = [mp.diff(e, theta, j) for j in range(4)]
    W = av[0]*bv[1]-av[1]*bv[0]
    C = base[0]*av[2]+base[1]*bv[2]-ev[2]
    D = base[0]*av[3]+base[1]*bv[3]-ev[3]
    V = ((3*C*bv[1]-D*bv[0])/(6*W), (av[0]*D-3*av[1]*C)/(6*W))
    scale = float(min(u, T-abs(theta), g))
    observations = []
    side = []
    for eps in (.04, .02, .01):
        B = scale*eps
        pair = critical_pair(B, float(u), float(theta))
        observations.append([(mp.mpf(pair[j])-base[j])/B**2 for j in (0, 1)])
        match = mp.findroot(lambda t: point(t)[0]-pair[0],
                            (theta-mp.mpf('.00001'), theta+mp.mpf('.00001')))
        side.append(mp.mpf(pair[1])-point(match)[1])
        assert side[-1] > 0
    predicted = max(abs(v) for v in V)
    extrapolated = [2*observations[-1][j]-observations[-2][j] for j in (0, 1)]
    error = max(abs(extrapolated[j]-V[j]) for j in (0, 1))/predicted
    assert error < mp.mpf('1e-4'), (fu, ft, error)
    B = scale*.04
    p64 = critical_pair(B, float(u), float(theta), 64)
    p128 = critical_pair(B, float(u), float(theta), 128)
    refinement = max(abs(x-y) for x, y in zip(p64, p128))
    assert refinement < 1e-10
    row = {'u_over_delta': float(fu), 'theta_over_T': float(ft),
           'predicted_B2': list(map(float, V)),
           'observed_B2': [[float(v) for v in pair] for pair in observations],
           'extrapolation_relative_error': float(error),
           'positive_graph_gaps': list(map(float, side)), 'refinement_error': refinement}
    rows.append(row)
    print('branch', json.dumps(row, sort_keys=True))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
summary = {'checks': rows, 'resources': {'elapsed_seconds': time.monotonic()-start,
    'peak_rss_MiB': rss_bytes/1024**2, 'nice': os.getpriority(os.PRIO_PROCESS, 0)}}
Path(__file__).with_name('branch_checks.json').write_text(json.dumps(summary, indent=2)+'\n')
print('PASS finite-B displacements and convex-side checks:', len(rows))
print('resources:', json.dumps(summary['resources'], sort_keys=True))
