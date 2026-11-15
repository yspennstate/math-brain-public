#!/usr/bin/env python3
"""Exact rational curvature calculation at gamma=pi/4."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import resource
import signal
import time
import json
import sys
from pathlib import Path
import sympy as s

signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
start = time.monotonic()
x, y = s.symbols('x y')
A = (1+x*x)**3/(2*x*(x-1)*(x*x-3)*(x*x+4*x+1))
f = x*(x**4+7)/(6*(x-1)*(x+1)*(x*x-3))
ell = lambda v: s.factor((1+x*x)*s.diff(v, x))
Ap = ell(A)
App = ell(Ap)
fp = ell(f)
fpp = ell(fp)
at_y = lambda v: v.subs(x, y)
B, Bp, Bpp = at_y(A), -at_y(Ap), at_y(App)
E, Ep, Epp = f+at_y(f), fp-at_y(fp), fpp+at_y(fpp)
W = s.factor(A*Bp-Ap*B)
N = s.factor(E*(Bp*App-Ap*Bpp)+Ep*(A*Bpp-B*App)-Epp*W)
C = s.factor(N/W)
Path(__file__).with_name('rational_curvature.txt').write_text(
    'A = '+str(A)+'\nf = '+str(f)+'\nW = '+str(W)+'\nN = '+str(N)+'\nC = '+str(C)+'\n')
num, den = s.fraction(C)
P = max(s.factor_list(num)[1], key=lambda item:
        s.Poly(item[0], x, y).total_degree())[0]
Q = s.Poly(-P, x, y)
assert Q.degree(x) == Q.degree(y) == 12
assert Q.as_expr().subs({x: s.Rational(1, 10), y: s.Rational(1, 10)}) > 0
r, t = s.symbols('r t')
R = s.Poly(0, r, t)
for (i, j), c in Q.terms():
    R += s.Poly(c*r**i*t**j*(1+r)**(12-i)*(1+t)**(12-j)*
                (1+2*r)**(12-j), r, t)
assert R.degree(r) == 24 and R.degree(t) == 12
assert all(c > 0 for c in R.coeffs())
assert len(R.coeffs()) == 324 and R.coeff_monomial(1) == 0
qarray = [[int(Q.coeff_monomial(x**i*y**j)) for j in range(13)]
          for i in range(13)]
rarray = [[int(R.coeff_monomial(r**i*t**j)) for j in range(13)]
          for i in range(25)]
cert = {'Q_coefficients': qarray, 'R_coefficients': rarray,
        'convention': 'entry [i][j] is coefficient of first_variable^i second_variable^j'}
Path(__file__).with_name('certificate.json').write_text(json.dumps(cert, indent=2)+'\n')
Path(__file__).with_name('curvature_polynomial.txt').write_text(str(Q.as_expr())+'\n')
Path(__file__).with_name('positive_quadrant_polynomial.txt').write_text(str(R.as_expr())+'\n')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
summary = {'Q_bidegree': [12, 12], 'R_bidegree': [24, 12],
    'positive_coefficients': len(R.coeffs()), 'zero_coefficients': 1,
    'minimum_positive_coefficient': int(min(R.coeffs())),
    'maximum_coefficient': int(max(R.coeffs())),
    'coefficient_sum': int(sum(R.coeffs())),
    'elapsed_seconds': time.monotonic()-start, 'peak_rss_MiB': rss_bytes/1024**2,
    'nice': os.getpriority(os.PRIO_PROCESS, 0)}
Path(__file__).with_name('derivation_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
print('PASS exact rational certificate:', json.dumps(summary, sort_keys=True))
