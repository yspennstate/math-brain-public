#!/usr/bin/env python3
"""Independent quadrature checks for the scalar comparison in PROOF.md."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import csv
import json
import math
import resource
import sys
import time
import warnings
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
state_path = Path('~/.claude/compute/compute_state.json')
if state_path.exists():
    state = json.loads(state_path.read_text())
    if state.get('status') == 'distress':
        raise SystemExit('Compute governor reports distress; audit not run.')
from scipy.integrate import quad, IntegrationWarning
warnings.simplefilter('error', IntegrationWarning)

TOL = 3e-10

def integrate(f, lo, hi, points=()):
    if lo == hi:
        return 0.0
    cuts = sorted(set([lo, hi] + [p for p in points if lo < p < hi]))
    return sum(quad(f, left, right, epsabs=0, epsrel=TOL, limit=180)[0]
               for left, right in zip(cuts[:-1], cuts[1:]))

def check(alpha, lam, nu):
    d = alpha-lam
    r, q = lam/alpha, 1-lam/alpha
    x0 = math.exp(-r)
    def F(x):
        return 2*alpha*x+2*lam*math.log1p(-x)
    V = 2*(alpha-lam+lam*math.log(r))
    C = alpha*math.sqrt(math.pi)/(math.sqrt(lam)*d*d)
    points = (q, 1/(nu*d), q/2, x0)
    # Original positive double integral. Both methods return u*exp(-nu*V).
    def outer_z(z):
        inside = integrate(lambda y: math.exp(nu*(F(y)-V))/(y*(1-y)),
                           z, 1.0, (q,))
        return math.exp(-nu*F(z))*inside
    direct = 2*nu*integrate(outer_z, 0.0, x0, points)
    # Tonelli reversal; the inner integral now has no 1/y singularity.
    def outer_y(y):
        inside = integrate(lambda z: math.exp(-nu*F(z)),
                           0.0, min(x0,y), points)
        return math.exp(nu*(F(y)-V))*inside/(y*(1-y))
    swapped = 2*nu*integrate(outer_y, 0.0, 1.0, points)
    relative_gap = abs(direct-swapped)/direct
    if relative_gap > 2e-7:
        raise AssertionError(('quadrature disagreement', alpha, lam, nu, relative_gap))
    # Independent barrier: integrate the drift/covariance ratio directly.
    V_integrated = integrate(lambda y: 2*(d-alpha*y)/(1-y), 0.0, q)
    if abs(V_integrated-V) > 1e-12:
        raise AssertionError(('barrier', V_integrated, V))
    # Independent leading constant from bulk normalization and boundary flux.
    # F''(q)=2 b'(q)/a(q), b'(q)=-d; loss flux = d*bulk_amplitude.
    aq = q*(1-q)
    C_flux = math.sqrt(math.pi)/(d*math.sqrt(aq*d))
    if abs(C_flux/C-1) > 1e-12:
        raise AssertionError(('prefactor', C_flux, C))
    # Time scaling: u(alpha,lambda,nu)=alpha^-1 u(1,r,alpha*nu).
    C_scaled = math.sqrt(math.pi)/(math.sqrt(r)*(1-r)**2*alpha**1.5)
    if abs(C_scaled/C-1) > 1e-12:
        raise AssertionError(('time scaling', C_scaled, C))
    return dict(alpha=alpha, lam=lam, nu=nu, V=V, C=C,
                scaled_u_direct=direct, scaled_u_swapped=swapped,
                quadrature_relative_gap=relative_gap,
                ratio_to_asymptotic=direct*math.sqrt(nu)/C,
                log_u=math.log(direct)+nu*V,
                barrier_integral_error=abs(V_integrated-V),
                prefactor_relative_error=abs(C_flux/C-1))

start = time.monotonic()
print('Python', sys.version.split()[0], 'nice', os.getpriority(os.PRIO_PROCESS,0))
print('CPU cap 120 seconds; all numerical library thread counts = 1')
rows=[]
for alpha, lam in ((1.0,.25),(1.0,.5),(1.0,.8),(2.0,1.0)):
    for nu in (25,50,100,200,400):
        row=check(alpha,lam,nu)
        rows.append(row)
        print(f'a={alpha:g} l={lam:g} nu={nu:3d} '
              f'ratio={row["ratio_to_asymptotic"]:.10f} '
              f'order_gap={row["quadrature_relative_gap"]:.3g}', flush=True)
with Path('audit_data.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print('maximum order-of-integration gap',max(r['quadrature_relative_gap'] for r in rows))
print('maximum barrier error',max(r['barrier_integral_error'] for r in rows))
print('maximum prefactor error',max(r['prefactor_relative_error'] for r in rows))
print('elapsed_seconds',round(time.monotonic()-start,3))
# Darwin reports ru_maxrss in bytes.
print('peak_rss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('PASS: 20 scalar checks; no full-diffusion simulation or rate estimate.')
