"""Run round 4 without writing there; independently integrate by midpoint."""
import json
import math
import os
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parent
PRIOR = Path('~/codex_op_1114r4/briefs/T324/verify.py')


def independent_midpoint(beta, dt):
    # These are the earlier six-token data, re-entered independently.
    ca, cb, p = [0.2, 0.3, 0.5], [0.5, 0.25, 0.25], 0.2
    masses = [p*z for z in ca] + [(1-p)*z for z in cb]
    y = []
    for raw, weights, center in (([-0.5, -0.1, 0.4], ca, 0.0),
                                 ([-0.4, 0.15, 0.6], cb, 1.2)):
        mean = sum(a*b for a, b in zip(raw, weights))
        y += [center + 0.2/beta*(z-mean)/(max(raw)-min(raw)) for z in raw]

    def drift(state):
        result = []
        for theta in state:
            denominator = numerator = 0.0
            for mass, phi in zip(masses, state):
                d = phi-theta
                k = mass*math.exp(-2*beta*math.sin(d/2)**2)
                denominator += k
                numerator += k*math.sin(d)
            result.append(numerator/denominator)
        return result

    def gap(state):
        return sum(a*b for a,b in zip(cb,state[3:]))-sum(a*b for a,b in zip(ca,state[:3]))

    t = 0.0
    while t < 300:
        before = gap(y)
        k = drift(y)
        v = drift([z+dt*f/2 for z,f in zip(y,k)])
        nxt = [z+dt*f for z,f in zip(y,v)]
        after = gap(nxt)
        if after <= 0.4:
            return t + dt*(before-0.4)/(before-after)
        y, t = nxt, t+dt
    raise AssertionError('time limit')


def main():
    started = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
        assert os.environ.get(key) == '1'
    ns = {'__file__':str(PRIOR), '__name__':'prior_read_only'}
    exec(compile(PRIOR.read_text(), str(PRIOR), 'exec'), ns)
    # The previous script's only output file is ROOT/verification.json.
    ns['ROOT'] = ROOT
    ns['main']()
    (ROOT/'verification.json').rename(ROOT/'prior_verification.json')
    prior = json.loads((ROOT/'prior_verification.json').read_text())
    rows = []
    for beta in (10,14):
        coarse = independent_midpoint(beta,0.01)
        fine = independent_midpoint(beta,0.005)
        rk4 = next(r['time'] for r in prior['full_token_solve'] if r['beta']==beta)
        row = dict(beta=beta, midpoint_coarse=coarse, midpoint_fine=fine,
                   earlier_rk4=rk4, relative_difference=abs(fine/rk4-1))
        rows.append(row)
        print('Independent midpoint:',json.dumps(row),flush=True)
        assert abs(fine/rk4-1) < 2e-6
        assert abs(fine/coarse-1) < 2e-6
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    assert peak < 1024
    out = dict(checks=rows,elapsed_seconds=time.monotonic()-started,peak_rss_mib=peak)
    (ROOT/'recheck.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Recheck passed:',json.dumps(out),flush=True)


if __name__=='__main__':
    main()
