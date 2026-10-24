"""Global search for a Bellman improvement by one layer of g with ALL 18 input biases free:
minimise D(mu) = s(mu) - V(p_out(mu)) (L-BFGS-B, exact gradient from opt18.evaluate), inputs priced by the saved
fixed point V.  Starts: structured (uniform core, uniform aux, signed core patterns, sparse k-input) and random.
D < 0 anywhere would lower V at p_out; min D >= 0 means V is closed under every single-layer g move.
Usage: python bell_multi.py <vig npz> <seed> <nstarts>
"""
import sys, time
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from scipy.optimize import minimize
from opt18 import Pricer, evaluate, N

pr = Pricer(sys.argv[1]); seed = int(sys.argv[2]); nst = int(sys.argv[3])
rng = np.random.default_rng(seed)


def D(z):
    s, EF, It, Ht, g, dEF = evaluate(z, pr)
    po = (1 - EF) / 2
    return s - pr.V(po), g - pr.dV(po) * (-0.5) * dEF


def starts():
    out = []
    for a in (-0.8, -0.5, -0.2, 0.2, 0.5, 0.8):
        m = np.zeros(N); m[:9] = a; out.append(("core-uniform %.1f" % a, m))
        m = np.zeros(N); m[9:] = a; out.append(("aux-uniform %.1f" % a, m))
    for k in range(nst):
        kind = k % 4
        m = np.zeros(N)
        if kind == 0:
            sz = rng.integers(1, 7); idx = rng.choice(N, sz, replace=False)
            m[idx] = rng.uniform(-0.95, 0.95, sz); out.append(("sparse%d" % sz, m))
        elif kind == 1:
            sgn = rng.choice([-1, 1], 9); mag = rng.uniform(0.1, 0.9)
            m[:9] = sgn * mag; m[9:] = rng.uniform(-0.3, 0.3, 9); out.append(("signed-core %.2f" % mag, m))
        else:
            sc = rng.choice([0.3, 0.6, 0.95]); m = rng.uniform(-sc, sc, N); out.append(("random %.2f" % sc, m))
    return out


t0 = time.time(); best = None
for name, m0 in starts():
    res = minimize(D, m0, jac=True, bounds=[(-0.995, 0.995)] * N, method="L-BFGS-B", options={"maxiter": 500})
    s, EF = evaluate(res.x, pr, grad=False)[:2]
    val = s - pr.V((1 - EF) / 2)
    print("%-18s D_min %+.6e  p_out %.5f  nit %3d  |mu|max %.3f  mu=%s  (%.0f s)" % (
        name, val, (1 - EF) / 2, res.nit, np.abs(res.x).max(), np.array2string(res.x, precision=3, max_line_width=400), time.time() - t0), flush=True)
    if best is None or val < best[0]:
        best = (val, res.x, (1 - EF) / 2)
print("BEST D = %+.6e at p_out %.6f, mu=%s" % (best[0], best[2], np.array2string(best[1], precision=4, max_line_width=400)))
