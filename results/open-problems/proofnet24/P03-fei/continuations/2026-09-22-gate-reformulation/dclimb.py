"""Search for a Boolean function that breaks the read-once potential.

With Gamma the read-once fixed point (Gamma(1/2) = C0 = 6.4548) the induction over read-once formulas built from
ARBITRARY gates closes iff  D(f) = C0 I(f) - H(f) - Gamma(Pr f) >= 0  for every Boolean f, i.e. iff

    R(f) = ( H(f) + Gamma(Pr f) ) / I(f)  <=  C0 .

R is the sharpened FEI functional: R >= H/I always, and R = C0 already at a single variable (H = 0, I = 1,
Gamma(1/2) = C0), so C0 is the conjectured maximum and anything above it is a counterexample.  Hill climb on
single truth-table flips; a whole neighbourhood of 2^n functions is one Hadamard product.
usage: dclimb.py <n> <restarts> <seed> [npz] [mode: R|HI]"""
import numpy as np, math, sys, time
import bexp, gam
from bclimb import popcount_table, chi_block
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def objective(fh, n, sizes, Gm, mode):
    mu = fh * fh
    I = (mu * sizes).sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        H = -np.where(mu > 1e-300, mu * np.log2(np.maximum(mu, 1e-300)), 0.0).sum(axis=1)
    ok = I > 1e-9
    if mode == "HI":
        return np.where(ok, H / np.maximum(I, 1e-300), -1e9)
    pr = np.clip((1.0 - fh[:, 0]) * 0.5, 0.0, 1.0)
    return np.where(ok, (H + Gm(pr)) / np.maximum(I, 1e-300), -1e9)

def climb(n, f0, Gm, mode, max_sweeps=400, chunk=512):
    N = 1 << n
    sizes = popcount_table(n)[:N].astype(float)
    f = np.asarray(f0, float).copy()
    cur = float(objective(bexp.fwht(f[None, :]) / N, n, sizes, Gm, mode)[0])
    sw = 0
    for sw in range(max_sweeps):
        fh = bexp.fwht(f[None, :])[0] / N
        best, bx = cur, -1
        for st in range(0, N, chunk):
            xs = np.arange(st, min(st + chunk, N))
            X = chi_block(n, xs)
            cand = fh[None, :] - (2.0 * f[xs] / N)[:, None] * X
            sc = objective(cand, n, sizes, Gm, mode)
            j = int(np.argmax(sc))
            if sc[j] > best:
                best, bx = float(sc[j]), int(xs[j])
        if bx < 0:
            break
        f[bx] = -f[bx]; cur = best
    return cur, f, sw

def seeds(n, r, rng):
    N = 1 << n
    if r == 0:
        f = np.ones(N); f[N - 1] = -1.0; return f                       # AND_n
    if r == 1:
        return 1.0 - 2.0 * (popcount_table(n)[:N] >= (n + 1) // 2)      # majority
    if r == 2:
        return np.where((np.arange(N) & 1) == 1, -1.0, 1.0)             # a single variable (R = C0 exactly)
    if r == 3:                                                          # tribes: OR of ANDs of width ~n/2
        k = max(1, n // 2); xs = np.arange(N); hit = np.zeros(N, bool)
        for b in range(0, n, k):
            m = 0
            for i in range(b, min(b + k, n)): m |= (1 << i)
            hit |= ((xs & m) == m)
        return np.where(hit, -1.0, 1.0)
    f = 1.0 - 2.0 * (rng.random(N) < rng.uniform(0.02, 0.5))
    if np.all(f == f[0]): f[0] = -f[0]
    return f

if __name__ == "__main__":
    n = int(sys.argv[1]); restarts = int(sys.argv[2]); seed = int(sys.argv[3])
    npz = sys.argv[4] if len(sys.argv) > 4 else "cert_vi_h96k40_f4.npz"
    mode = sys.argv[5] if len(sys.argv) > 5 else "R"
    Gm = gam.Gam(npz, 0.0); C0 = Gm.cap
    rng = np.random.default_rng(seed)
    best = (-1e9, None); t0 = time.time()
    print("n=%d mode=%s  C0 = Gamma(1/2) = %.7f   (conjecture: max R = C0, attained at a single variable)"
          % (n, mode, C0), flush=True)
    for r in range(restarts):
        v, f, sw = climb(n, seeds(n, r, rng), Gm, mode)
        if v > best[0]:
            best = (v, f.copy())
            s = bexp.stats(f[None, :], n); pr = float((1 - np.mean(f)) / 2)
            print("  r=%3d  R=%.7f  margin C0-R = %+.3e   H/I=%.6f I=%.4f Pr=%.5f Gamma=%.4f B/I=%.4f rho0=%.4f sweeps=%d %.0fs"
                  % (r, v, C0 - v, s["HI"][0], s["I"][0], pr, float(Gm(pr)), s["BI"][0], s["rho0"][0], sw, time.time() - t0), flush=True)
    v, f = best
    s = bexp.stats(f[None, :], n); pr = float((1 - np.mean(f)) / 2)
    print("BEST n=%d  max %s = %.8f   C0 = %.8f   margin %+.3e   H/I=%.6f I=%.5f H=%.5f Pr=%.5f Gamma=%.5f  (%.0f s)"
          % (n, mode, v, C0, C0 - v, s["HI"][0], s["I"][0], s["H"][0], pr, float(Gm(pr)), time.time() - t0))
    np.save("dclimb_%s_n%d_s%d.npy" % (mode, n, seed), f)
