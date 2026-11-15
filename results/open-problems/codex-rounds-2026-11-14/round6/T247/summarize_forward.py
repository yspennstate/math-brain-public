"""Audit and summarize the saved exact-in-law forward paths."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
import math
from pathlib import Path
import signal
signal.alarm(30)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
r = json.loads(Path('forward_results.json').read_text())
assert len(r['paths']) == 27 and r['threads'] == 1 and r['niceness'] >= 15
assert r['peak_rss_bytes'] < 10**9 and r['runtime_seconds'] < 180
lines = []
for n in (16, 32, 64):
    depth = max(z['L'] for z in r['paths'] if z['n'] == n)
    xs = [x for x in r['paths'] if x['n'] == n and x['L'] == depth]
    mean = lambda key: sum(x[key] for x in xs)/len(xs)
    t = mean('La_over_n')
    s = mean('L')*xs[0]['a']
    K = 1+2/n
    y = K/(1+(K-1)*math.exp(-2*s))
    # A first-order finite-width ODE diagnostic; not an additional theorem.
    # dy/ds=y(2-c_n*y), y(0)=1; H=-4s/n+(1+2/n)log y(s).
    ode = -4*t+K*math.log(y)
    lines.append(f'n={n}, L={depth}, La/n={t:.9g}, La^2={mean("La_squared"):.9g}, '
                 f'mean H={mean("H"):.9g}, target={-4*t:.9g}, '
                 f'finite-width ODE diagnostic={ode:.9g}, '
                 f'max compensated error={max(abs(x["compensated_H"]) for x in xs):.6g}, '
                 f'certified log-S interval half-width={max(x["certified_logS_error"] for x in xs):.6g}')
for x in r['paths']:
    assert abs(x['compensated_H']) <= x['pathwise_comparison_bound']+1e-8
    assert x['max_abs_radius_error'] < .5
    assert abs(x['log_gain_squared']-2*x['a']) <= 15*x['a']**2
    assert 0 <= x['b'] <= 14*x['a']**3
    assert abs(-x['b']/x['a']) <= 14*x['a']**2
lines.append(f'27 path checkpoints passed; runtime={r["runtime_seconds"]:.3f} s, '
             f'RSS={r["peak_rss_bytes"]/2**20:.3f} MiB, niceness={r["niceness"]}.')
text = '\n'.join(lines)+'\n'
Path('forward_summary.txt').write_text(text)
print(text, end='')
