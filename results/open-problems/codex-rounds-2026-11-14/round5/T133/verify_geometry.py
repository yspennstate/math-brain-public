#!/usr/bin/env python3
"""Check the exact certificate against the original trigonometric geometry."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
from pathlib import Path
import resource
import signal
import sys
import time
import mpmath as mp

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
start = time.monotonic()
mp.mp.dps = 160
cert = json.loads(Path(__file__).with_name('certificate.json').read_text())
g = mp.pi/4
delta = 3*mp.pi/4
h = mp.mpf(4)/3
rows = []
for fu in map(mp.mpf, ('.000001', '.001', '.05', '.2', '0.333333333333333333',
                       '.5', '.9', '.999', '.999999')):
    u = fu*delta
    T = delta-u
    a = lambda t: mp.sin(g)/(2*mp.pi*(mp.cos(t-u)+mp.cos(g)))
    b = lambda t: a(-t)
    e = lambda t: (mp.sin(T)/(mp.cos(t)-mp.cos(T)) -
                  h*mp.sin(h*T)/(mp.cos(h*t)-mp.cos(h*T)))/(2*mp.pi)

    def point(t):
        A, B, E = a(t), b(t), e(t)
        Ap, Bp, Ep = mp.diff(a, t), mp.diff(b, t), mp.diff(e, t)
        W = A*Bp-Ap*B
        return ((E*Bp-Ep*B)/W, (A*Ep-Ap*E)/W)

    for ft in map(mp.mpf, ('-.999999', '-.9', '-.3', '0', '.3', '.9', '.999999')):
        theta = ft*T
        av = [mp.diff(a, theta, j) for j in range(4)]
        bv = [mp.diff(b, theta, j) for j in range(4)]
        ev = [mp.diff(e, theta, j) for j in range(4)]
        X, Y = point(theta)
        W = av[0]*bv[1]-av[1]*bv[0]
        C = X*av[2]+Y*bv[2]-ev[2]
        D = X*av[3]+Y*bv[3]-ev[3]
        assert W > 0 and C > 0
        x = mp.tan((T+theta)/6)
        y = mp.tan((T-theta)/6)
        Aq = lambda z: (1+z*z)**3/(2*z*(1-z)*(3-z*z)*(z*z+4*z+1))
        fq = lambda z: z*(z**4+7)/(6*(1-z)*(1+z)*(3-z*z))
        scale_error = max(abs(Aq(x)/(2*mp.pi)-av[0])/av[0],
                          abs(Aq(y)/(2*mp.pi)-bv[0])/bv[0],
                          abs((fq(x)+fq(y))/(2*mp.pi)-ev[0])/ev[0])
        assert scale_error < mp.mpf('1e-70'), (fu, ft, scale_error)
        Q = sum(c*x**i*y**j for i, row in enumerate(cert['Q_coefficients'])
                for j, c in enumerate(row))
        J = (1+x*x)*(1+y*y)+4*(x+y)*(1-x*y)
        d = lambda z: z*(1-z)*(3-z*z)*(z*z+4*z+1)
        N = ((x+y)*(1+x*x)**3*(1+y*y)**3*(1-x*y)*
             (1-x-y-x*y)**2*J*Q/(4*d(x)**3*d(y)**3*(1+x)**3*(1+y)**3))
        # W=(A B1-A1 B)/(24 pi^2), C=N/(72 pi Wscaled).
        Wscaled = 24*mp.pi**2*W
        C_rational = N/(72*mp.pi*Wscaled)
        relative_error = abs(C_rational-C)/C
        assert relative_error < mp.mpf('1e-60'), (fu, ft, relative_error)
        # Independent envelope differentiation checks the tangent and graph curvature.
        xp = mp.diff(lambda t: point(t)[0], theta)
        yp = mp.diff(lambda t: point(t)[1], theta)
        xpp = mp.diff(lambda t: point(t)[0], theta, 2)
        ypp = mp.diff(lambda t: point(t)[1], theta, 2)
        assert xp > 0 and yp < 0
        assert abs(xp-C*bv[0]/W) < mp.mpf('1e-55')*abs(xp)
        graph2 = (ypp*xp-yp*xpp)/xp**3
        graph2_formula = W**2/(C*bv[0]**3)
        assert graph2 > 0
        assert abs(graph2-graph2_formula) < mp.mpf('1e-50')*graph2
        vx = (3*C*bv[1]-D*bv[0])/(6*W)
        vy = (av[0]*D-3*av[1]*C)/(6*W)
        jac = vx*yp-vy*xp
        target = -C*C/(2*W)
        assert abs(jac-target) < mp.mpf('1e-55')*abs(target)
        assert av[0]*vx+bv[0]*vy > 0
        rows.append({'u_over_delta': float(fu), 'theta_over_T': float(ft),
            'C': float(C), 'rational_relative_error': float(relative_error),
            'coefficient_relative_error': float(scale_error),
            'graph_second_derivative': float(graph2), 'collar_jacobian': float(jac)})

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
summary = {'checks': rows, 'resources': {'elapsed_seconds': time.monotonic()-start,
    'peak_rss_MiB': rss_bytes/1024**2, 'nice': os.getpriority(os.PRIO_PROCESS, 0)}}
Path(__file__).with_name('geometry_checks.json').write_text(json.dumps(summary, indent=2)+'\n')
print('PASS trigonometric/rational/tangent/convexity/collar checks:', len(rows))
print('maximum rational curvature relative error:', max(r['rational_relative_error'] for r in rows))
print('maximum coefficient relative error:', max(r['coefficient_relative_error'] for r in rows))
print('resources:', json.dumps(summary['resources'], sort_keys=True))
