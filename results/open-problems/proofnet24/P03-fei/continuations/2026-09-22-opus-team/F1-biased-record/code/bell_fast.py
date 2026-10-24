"""Fast global Bellman search for one layer of g with all 18 biases free (numba transform and gradient).
D(mu) = s(mu) - V(p_out),  s = sum_i It_i a_i - Htilde,  a_i = (V(p_i) + h(V_i))/V_i  (see opt18.py for the gradient).
Usage: python bell_fast.py <vig npz> <seed> <nstarts> [mode]   mode 'bell' (default) or 'bal' (penalised balance)
"""
import sys, time, math
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from scipy.optimize import minimize
import fast_gate as FG
from opt18 import Pricer, h2s
from gate import N


def ev(mu, pr, grad=True):
    mu = np.asarray(mu, dtype=float)
    p = (1 - mu) / 2; sig2 = 1 - mu * mu; sig = np.sqrt(sig2)
    Ht, It, po, c = FG.evaluate(p)
    A = np.array([pr.V(p[i]) + h2s(sig2[i]) for i in range(N)])
    a = A / sig2
    s = float((It * a).sum()) - Ht
    EF = float(c[0])
    if not grad:
        return s, EF
    t1, t2 = FG.grad_parts(c, a, mu)
    g = np.empty(N); dEF = np.empty(N)
    for j in range(N):
        dA = pr.dV(p[j]) * (-0.5) + (math.log2((1 - sig2[j]) / sig2[j]) if 0 < sig2[j] < 1 else 0.0) * (-2 * mu[j])
        da = dA / sig2[j] + 2 * mu[j] * A[j] / sig2[j] ** 2
        g[j] = 2 * t1[j] / sig[j] - 2 * mu[j] * t2[j] / sig2[j] + It[j] * da
        dEF[j] = c[1 << j] / sig[j]
    return s, EF, g, dEF


def D(z, pr):
    s, EF, g, dEF = ev(z, pr)
    po = (1 - EF) / 2
    return s - pr.V(po), g - pr.dV(po) * (-0.5) * dEF


def starts(rng, nst):
    out = []
    for a in (-0.6, -0.3, -0.1, -0.03, 0.03, 0.1, 0.3, 0.6):
        m = np.zeros(N); m[:9] = a; out.append(("core-uniform %.2f" % a, m))
        m = np.zeros(N); m[9:] = a; out.append(("aux-uniform %.2f" % a, m))
        m = np.full(N, a); out.append(("all-uniform %.2f" % a, m))
    for k in range(nst):
        kind = k % 5
        m = np.zeros(N)
        if kind == 0:
            sz = rng.integers(1, 8); idx = rng.choice(N, sz, replace=False)
            m[idx] = rng.uniform(-0.95, 0.95, sz); out.append(("sparse%d" % sz, m))
        elif kind == 1:
            sgn = rng.choice([-1, 1], 9); mag = rng.uniform(0.02, 0.9)
            m[:9] = sgn * mag; m[9:] = rng.uniform(-0.3, 0.3, 9); out.append(("signed-core %.2f" % mag, m))
        elif kind == 2:
            m = rng.normal(0, rng.choice([0.02, 0.05, 0.1]), N); out.append(("near-centre", m))
        else:
            sc = rng.choice([0.3, 0.6, 0.95]); m = rng.uniform(-sc, sc, N); out.append(("random %.2f" % sc, m))
    return out


if __name__ == "__main__":
    pr = Pricer(sys.argv[1]); seed = int(sys.argv[2]); nst = int(sys.argv[3])
    rng = np.random.default_rng(seed)
    # gradient check
    mu = rng.uniform(-0.5, 0.5, N)
    s, EF, g, dEF = ev(mu, pr)
    err = max(abs((ev(mu + e, pr, False)[0] - ev(mu - e, pr, False)[0]) / 2e-6 - g[j]) for j, e in enumerate(np.eye(N) * 1e-6))
    print("gradient check max err %.2e" % err, flush=True)
    t0 = time.time(); best = None
    for name, m0 in starts(rng, nst):
        res = minimize(lambda z: D(z, pr), m0, jac=True, bounds=[(-0.995, 0.995)] * N, method="L-BFGS-B", options={"maxiter": 800})
        s, EF = ev(res.x, pr, grad=False)
        po = (1 - EF) / 2; val = s - pr.V(po)
        print("%-18s D %+.6e  p_out %.5f  s-C %+.4e  nit %3d  |mu|max %.3f  mu=%s  (%.0f s)" % (
            name, val, po, s - pr.C, res.nit, np.abs(res.x).max(), np.array2string(res.x, precision=4, max_line_width=500), time.time() - t0), flush=True)
        if best is None or val < best[0]:
            best = (val, res.x, po)
    print("BEST D = %+.6e at p_out %.6f, mu=%s" % (best[0], best[2], np.array2string(best[1], precision=5, max_line_width=500)))
