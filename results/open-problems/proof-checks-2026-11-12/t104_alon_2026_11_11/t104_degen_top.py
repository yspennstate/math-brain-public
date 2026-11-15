"""H on the stratum where the top eigenvalue of L is double (lam_1 = lam_2), the place where H >= s_inf is not
available (GAP_STATE_FORM.md, end).

H is continuous there (a pair with zero gap contributes nothing), so this measures how small H gets on the
stratum. A batched (1+1) evolution step (as in t104_np_hsearch.py, numpy only) on z (w = z^2, sum 1) minimises
H + P * gap12 / lam_1, with P raised from 10 to 1e4 over the run. End points are kept if gap12 / lam_1 < 1e-5 and
they are not near K_n (L1 distance to uniform > 0.05). Prints the smallest H, its slack and weights, per round.

usage: python t104_degen_top.py n pop iters minutes seed
"""
import importlib.util
import sys
import time
import numpy as np

here = __file__.replace("t104_degen_top.py", "t104_np_hsearch.py")
n, POP, ITERS = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
MINUTES, SEED = float(sys.argv[4]), int(sys.argv[5])
sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
spec = importlib.util.spec_from_file_location("hs", here)
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
m = h.m


def parts(w):
    w = w / w.sum(1, keepdims=True)
    val, sl, g = h.values(w + 1e-300, h.GRID)
    L = np.einsum("km,nk,kj->nmj", h.E, w, h.E)
    ev = np.linalg.eigvalsh(L)
    return val, sl, (ev[:, -1] - ev[:, -2]) / ev[:, -1], w


rng = np.random.default_rng(SEED)
t0 = time.time(); rnd = 0; best = (np.inf, None); tot = [0, 0]
print("degenerate-top search  n %d  pop %d  iters %d  minutes %g  seed %d" % (n, POP, ITERS, MINUTES, SEED), flush=True)
while time.time() - t0 < 60 * MINUTES:
    rnd += 1
    z = np.sqrt(h.starts(POP, rng))
    sig = np.full(POP, 0.05)
    for it in range(ITERS):
        P = 10.0 * 1e3 ** (it / max(1, ITERS - 1))
        if it == 0:
            v, _, g, _ = parts(z * z + 1e-300); cur = v + P * g
        else:
            v, _, g, _ = parts(z * z + 1e-300); cur = v + P * g   # re-score at the new penalty
        step = rng.standard_normal((POP, m)) * sig[:, None] * np.abs(z).mean(1, keepdims=True)
        zn = z + step
        if it % 7 == 3:
            j = rng.integers(0, m, POP); zn[np.arange(POP), j] = 0.0
        vn, _, gn, _ = parts(zn * zn + 1e-300)
        new = vn + P * gn
        ok = np.isfinite(new) & (new < cur)
        z = np.where(ok[:, None], zn, z)
        sig = np.clip(np.where(ok, sig * 1.5, sig * 0.92), 1e-12, 0.5)
    v, sl, g, w = parts(z * z + 1e-300)
    du = np.abs(w - 1.0 / m).sum(1)
    keep = (g < 1e-5) & (du > 0.05)
    tot[0] += int(keep.sum()); tot[1] += int((keep & (v < -1e-10)).sum())
    if keep.any():
        i = np.where(keep)[0][np.argmin(v[keep])]
        if v[i] < best[0]:
            best = (float(v[i]), w[i].copy())
        print("round %3d  on stratum %d of %d  negative %d  min H %+.6e (slack %+.4e gap12/lam %.1e dist K_n %.3f)  %.0fs"
              % (rnd, int(keep.sum()), POP, int((keep & (v < -1e-10)).sum()), v[i], sl[i], g[i], du[i],
                 time.time() - t0), flush=True)
        print("   weights %s" % h.fmt(w[i], 1e-6), flush=True)
    else:
        print("round %3d  none on the stratum  %.0fs" % (rnd, time.time() - t0), flush=True)
print("totals: on stratum %d, negative %d, smallest H %+.6e" % (tot[0], tot[1], best[0]), flush=True)
if best[1] is not None:
    print("best weights %s" % h.fmt(best[1], 1e-7), flush=True)
