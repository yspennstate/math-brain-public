# Is the leaking hub also largest for laws uniform on intervals?
#   Q = 2 (L + beta)(X_0 + eps P) + lam V^2,  L = <w, X'>, V = <v, X'>, P = <p, X'>, (w, v, p) orthonormal in R^m,
#   w_i^2 + v_i^2 + p_i^2 <= 1/2, X_0 (the hub) and X_1..X_m independent with densities <= 1.
# p_Q(s) = E[ f_0(x*) / (2 |L + beta|) ],  x* = (s - lam V^2)/(2 (L + beta)) - eps P.
# For given light laws the best hub law is the top level set (measure 1) of the weighted density g of x* (bathtub);
# g is estimated by a weighted histogram of Monte Carlo samples, and the top-set value is re-estimated on an
# independent sample (so the selection of the top bins does not inflate it).
# Light laws compared: uniform on [a_i, a_i + 1] (offsets on a grid of random draws) against comb laws
# (N teeth of width 1/N at spacing d, random offsets). Both sides of the hyperboloid: s < 0 (two-sheet) and s > 0.
import sys, math, json
import numpy as np

def frame3(m, rng, tries=100000):
    for _ in range(tries):
        Qm, _ = np.linalg.qr(rng.standard_normal((m, 3)))
        D = Qm.T
        if np.max(np.sum(D**2, axis=0)) <= 0.5:
            return D
    raise RuntimeError("no frame")

def sample_light(laws, n, rng):
    # laws: list of (kind, params); returns n x m samples
    m = len(laws)
    X = np.empty((n, m))
    for i, (kind, a, N, d) in enumerate(laws):
        if kind == 'int':
            X[:, i] = a + rng.random(n)
        else:
            k = rng.integers(0, N, size=n)
            X[:, i] = a + k*d + rng.random(n)/N
    return X

def best_hub_value(D, laws, eps, lam, beta, s, rng, n=2_000_000, h=0.02):
    # estimate g on one sample, choose the top set, evaluate on a fresh sample
    def xstar_w(nn):
        X = sample_light(laws, nn, rng)
        L = X @ D[0] + beta; V = X @ D[1]; P = X @ D[2]
        xs = (s - lam*V**2)/(2*L) - eps*P
        w = 1.0/(2*np.abs(L))
        return xs, w
    xs, w = xstar_w(n)
    lo, hi = np.percentile(xs, 0.5), np.percentile(xs, 99.5)
    lo, hi = max(lo, -60), min(hi, 60)
    nb = int((hi - lo)/h) + 1
    hist, edges = np.histogram(xs, bins=nb, range=(lo, lo + nb*h), weights=w)
    g = hist/(n*h)
    k = int(round(1.0/h))
    top = np.argsort(-g)[:k]
    sel = np.zeros(nb, bool); sel[top] = True
    xs2, w2 = xstar_w(n)
    idx = np.floor((xs2 - lo)/h).astype(int)
    ok = (idx >= 0) & (idx < nb)
    val = float(np.sum(w2[ok][sel[idx[ok]]]))/n
    return val, float(np.sum(g[top])*h)

if __name__ == "__main__":
    try:
        import psutil, os
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        psutil.Process().cpu_affinity(list(range(2, os.cpu_count())))
    except Exception:
        pass
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    D = frame3(m, rng)
    lam, beta = 1.0, 0.0
    for eps in (0.1, 0.01):
        for s in (-0.5, -2.0, 0.5):
            best = {}
            for kind in ('int', 'comb4', 'comb8'):
                vals = []
                for trial in range(8):
                    if kind == 'int':
                        laws = [('int', rng.uniform(-2, 1), 1, 1.0) for _ in range(m)]
                    else:
                        N = int(kind[4:]); d = rng.uniform(1.0, 3.0)
                        laws = [('comb', rng.uniform(-2, 1) - (N - 1)*d/2, N, d) for _ in range(m)]
                    v, v_in = best_hub_value(D, laws, eps, lam, beta, s, rng)
                    vals.append(v)
                best[kind] = (round(max(vals), 4), round(float(np.median(vals)), 4))
            print(json.dumps(dict(m=m, eps=eps, s=s, lam=lam, best_and_median=best)), flush=True)
