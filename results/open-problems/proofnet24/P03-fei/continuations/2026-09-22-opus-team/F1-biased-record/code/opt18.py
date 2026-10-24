"""One layer of g with all 18 inputs biased, inputs priced by a slack function V (saved fixed point).

s(mu) = sum_i It_i(mu) a_i - Htilde(mu),  a_i = (V(p_i) + h(V_i)) / V_i,  p_i = (1 - mu_i)/2,  V_i = 1 - mu_i^2.
Gradient (exact): with w_T = Ghat_T^2, omega_T = sum_{i in T} a_i, Psi_T = omega_T + log2 w_T + 1/ln 2,
  ds/dmu_j = (2/sigma_j) sum_{T not ni j} Ghat_T Ghat_{T u j} Psi_T - (2 mu_j/sigma_j^2) sum_{T ni j} w_T Psi_T + It_j da_j/dmu_j,
since dGhat_T/dmu_j = Ghat_{T u j}/sigma_j (j not in T) and -mu_j Ghat_T/sigma_j^2 (j in T).  E F = Ghat_empty,
dE F/dmu_j = Ghat_{j}/sigma_j.
Modes: 'bal'  minimise s - C subject to E F = 0 (SLSQP);  'bell' minimise s - V(p_out) (L-BFGS-B).
Usage: python opt18.py <vig npz> <mode> <nstarts> <seed> [scale]
"""
import sys, os, time, math
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from scipy.optimize import minimize
from gate import load_table, biased_spectrum, N
from ro_gamma import Grid

LN2 = math.log(2.0)
TAB = load_table()
IDX = np.arange(1 << N, dtype=np.int64)
BITS = [((IDX >> i) & 1).astype(bool) for i in range(N)]


def h2s(v):
    if v <= 0 or v >= 1:
        return 0.0
    return -v * math.log2(v) - (1 - v) * math.log2(1 - v)


class Pricer:
    def __init__(self, npz):
        d = np.load(npz)
        self.C = float(d["C"]); self.G = d["G"]; self.grid = Grid(int(d["M"]), int(d["K"]))

    def V(self, p):
        return float(self.grid.gamma_at(self.G, np.array([p]))[0])

    def dV(self, p, eps=1e-7):
        return (self.V(min(p + eps, 1 - 1e-12)) - self.V(max(p - eps, 1e-12))) / (2 * eps)


def evaluate(mu, pr, grad=True):
    mu = np.asarray(mu, dtype=float)
    p = (1 - mu) / 2
    sig2 = 1 - mu * mu
    sig = np.sqrt(sig2)
    Gh = biased_spectrum(TAB, p)
    w = Gh * Gh
    pos = w > 0
    lw = np.zeros_like(w); lw[pos] = np.log2(w[pos])
    Ht = -float((w[pos] * lw[pos]).sum())
    It = np.array([w[BITS[i]].sum() for i in range(N)])
    A = np.array([pr.V(p[i]) + h2s(sig2[i]) for i in range(N)])
    a = A / sig2
    s = float((It * a).sum()) - Ht
    EF = float(Gh[0])
    if not grad:
        return s, EF, It, Ht
    omega = np.zeros_like(w)
    for i in range(N):
        omega[BITS[i]] += a[i]
    Psi = np.where(pos, omega + lw + 1 / LN2, 0.0)
    GPsi = Gh * Psi
    g = np.zeros(N); dEF = np.zeros(N)
    for j in range(N):
        b = BITS[j]
        lo = ~b
        # pairs (T, T u j) for T not containing j: index T and T | (1<<j)
        Tlo = IDX[lo]
        t1 = (GPsi[Tlo] * Gh[Tlo | (1 << j)]).sum()
        t2 = (w[b] * Psi[b]).sum()
        # da_j/dmu_j
        dA = pr.dV(p[j]) * (-0.5) + (math.log2((1 - sig2[j]) / sig2[j]) if 0 < sig2[j] < 1 else 0.0) * (-2 * mu[j])
        da = dA / sig2[j] + 2 * mu[j] * A[j] / sig2[j] ** 2
        g[j] = 2 * t1 / sig[j] - 2 * mu[j] * t2 / sig2[j] + It[j] * da
        dEF[j] = Gh[1 << j] / sig[j]
    return s, EF, It, Ht, g, dEF


def check_grad(pr, seed=0):
    rng = np.random.default_rng(seed)
    mu = rng.uniform(-0.6, 0.6, N)
    s, EF, It, Ht, g, dEF = evaluate(mu, pr)
    err = 0.0; errE = 0.0
    for j in range(N):
        e = np.zeros(N); e[j] = 1e-6
        sp = evaluate(mu + e, pr, grad=False); sm = evaluate(mu - e, pr, grad=False)
        fd = (sp[0] - sm[0]) / 2e-6; fdE = (sp[1] - sm[1]) / 2e-6
        err = max(err, abs(fd - g[j])); errE = max(errE, abs(fdE - dEF[j]))
    print("gradient check: max |fd - analytic| = %.2e (s), %.2e (E F); |grad| = %.3f" % (err, errE, np.abs(g).max()), flush=True)


def run_bal(pr, mu0):
    C = pr.C
    cache = {}

    def ev(z):
        key = z.tobytes()
        if key not in cache:
            cache.clear(); cache[key] = evaluate(z, pr)
        return cache[key]
    fun = lambda z: ev(z)[0] - C
    jac = lambda z: ev(z)[4]
    con = {"type": "eq", "fun": lambda z: ev(z)[1], "jac": lambda z: ev(z)[5]}
    res = minimize(fun, mu0, jac=jac, constraints=[con], bounds=[(-0.995, 0.995)] * N, method="SLSQP",
                   options={"maxiter": 300, "ftol": 1e-12})
    s, EF = evaluate(res.x, pr, grad=False)[:2]
    return res.x, s - C, EF, res.nit


def run_bell(pr, mu0):
    def f(z):
        s, EF, It, Ht, g, dEF = evaluate(z, pr)
        po = (1 - EF) / 2
        Vo = pr.V(po)
        dVo = pr.dV(po)
        return s - Vo, g - dVo * (-0.5) * dEF
    res = minimize(f, mu0, jac=True, bounds=[(-0.995, 0.995)] * N, method="L-BFGS-B", options={"maxiter": 400})
    s, EF = evaluate(res.x, pr, grad=False)[:2]
    return res.x, s - pr.V((1 - EF) / 2), EF, res.nit


if __name__ == "__main__":
    pr = Pricer(sys.argv[1]); mode = sys.argv[2]; nst = int(sys.argv[3]); seed = int(sys.argv[4])
    scale = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
    check_grad(pr)
    rng = np.random.default_rng(seed)
    best = None
    t0 = time.time()
    for k in range(nst):
        mu0 = rng.uniform(-scale, scale, N) * rng.choice([0.2, 0.5, 1.0])
        if mode == "bal":
            x, val, EF, nit = run_bal(pr, mu0)
        else:
            x, val, EF, nit = run_bell(pr, mu0)
        print("start %3d: value %+.6e  E F %+.2e  nit %3d  |mu|max %.3f  p_out %.5f  mu=%s  (%.0f s)" % (
            k, val, EF, nit, np.abs(x).max(), (1 - EF) / 2, np.array2string(x, precision=3, max_line_width=400), time.time() - t0), flush=True)
        if best is None or val < best[0]:
            best = (val, x)
    print("BEST value %+.6e at mu=%s" % (best[0], np.array2string(best[1], precision=4, max_line_width=400)))
