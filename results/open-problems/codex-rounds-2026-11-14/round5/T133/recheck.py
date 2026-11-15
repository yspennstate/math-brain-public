#!/usr/bin/env python3
"""Independent midpoint audit. No earlier script is imported or executed."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
from pathlib import Path
import resource
import signal
import sys
import time
import mpmath as mp

signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
start = time.monotonic()
mp.mp.dps = 90
rows = []
for g in (mp.mpf('.0001'), mp.mpf('.4'), mp.pi/3,
          mp.mpf('1.4'), mp.pi/2-mp.mpf('.0001')):
    delta = mp.pi-g
    h = mp.pi/delta
    for fraction in map(mp.mpf, ('0', '.01', '.5', '.99', '.9999')):
        u = g+fraction*(delta-g)
        T = delta-u
        a = lambda s: mp.sin(g)/(2*mp.pi*(mp.cos(s-u)+mp.cos(g)))
        b = lambda s: a(-s)
        e = lambda s: (mp.sin(T)/(mp.cos(s)-mp.cos(T)) -
                      h*mp.sin(h*T)/(mp.cos(h*s)-mp.cos(h*T)))/(2*mp.pi)
        # Direct symmetric differences provide a separate derivative route.
        step = min(g, T)*mp.mpf('1e-17')
        alpha = a(0)
        C_fd = e(0)/alpha*(a(step)-2*a(0)+a(-step))/step**2 - (
            e(step)-2*e(0)+e(-step))/step**2
        C = e(0)*mp.diff(a, 0, 2)/alpha-mp.diff(e, 0, 2)
        R = (2*mp.sin(u)**2+mp.cos(u)*(mp.cos(u)+mp.cos(g)))/(
            mp.cos(u)+mp.cos(g))**2
        q = 1/(1-mp.cos(T))
        qh = 1/(1-mp.cos(h*T))
        E = mp.cot(T/2)-h*mp.cot(h*T/2)
        lower = h*mp.cot(h*T/2)*(h*h*qh-q)/(2*mp.pi)
        formula = E*(R-q)/(2*mp.pi)+lower
        assert C > 0 and lower > 0
        assert abs(C-formula) < mp.mpf('1e-50')*abs(C)
        assert abs(C-C_fd) < mp.mpf('1e-25')*abs(C)
        assert C >= lower-mp.mpf('1e-50')*abs(C)
        p = mp.diff(b, 0)
        W = 2*alpha*p
        V = C/(4*alpha)
        speed = C/(2*p)
        jac_direct = -2*V*speed
        jac_formula = -C*C/(2*W)
        assert abs(jac_direct-jac_formula) < mp.mpf('1e-80')*abs(jac_formula)
        rows.append({'gamma': float(g), 'u': float(u), 'C': float(C),
                     'fd_relative_error': float(abs(C-C_fd)/abs(C)),
                     'decomposition_relative_error': float(abs(C-formula)/abs(C)),
                     'jacobian': float(jac_direct)})
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
result = {'checks': rows, 'resources': {'elapsed_seconds': time.monotonic()-start,
    'peak_rss_MiB': rss_bytes/1024**2, 'nice': os.getpriority(os.PRIO_PROCESS, 0)}}
Path(__file__).with_name('recheck.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS earlier midpoint sign/decomposition/collar checks:', len(rows))
print('max relative finite-difference error:', max(r['fd_relative_error'] for r in rows))
print('max relative decomposition error:', max(r['decomposition_relative_error'] for r in rows))
print('resources:', json.dumps(result['resources'], sort_keys=True))
