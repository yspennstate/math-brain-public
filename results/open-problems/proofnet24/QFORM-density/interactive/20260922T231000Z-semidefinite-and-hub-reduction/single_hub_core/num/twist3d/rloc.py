# Local and global maximal functionals of the pair (L, P) for comb laws on the spread frame:
#   R_loc(l0) = int dp sup_{|l - l0| <= 1} rho_{L,P}(l, p),     M_glob = int dp sup_l rho_{L,P}(l, p),
# from a 2D histogram with square bins of side h (the maximum over noisy bins is biased upward; two bin sides are printed).
import sys, math, time
import numpy as np
from adapted_hub import frame, sample as sample0

def sample(rng, law, N, size):
    if law == "sqrt":       # N teeth of width 1/N at spacing 1/sqrt(N): range sqrt(N)
        return rng.integers(0, N, size=size) / math.sqrt(N) + rng.random(size) / N
    return sample0(rng, law, N, size)

def bounds(law, N):
    return {"int": (0.0, N), "fine": (-1.0, 1.0), "two": (0.0, N), "sqrt": (0.0, math.sqrt(N))}[law]

def run(N, law="int", which="irr2", n=40_000_000, chunk=2_000_000, hs=(0.05, 0.1), l0s=(0.0,), seed=7):
    E = frame(which)
    lo, hi = bounds(law, N)
    w, q = E[:, 0], E[:, 2]
    lr = (lo * w[w > 0].sum() + hi * w[w < 0].sum() - 0.2, hi * w[w > 0].sum() + lo * w[w < 0].sum() + 0.2)
    pr = (lo * q[q > 0].sum() + hi * q[q < 0].sum() - 0.2, hi * q[q > 0].sum() + lo * q[q < 0].sum() + 0.2)
    h0 = min(hs); nl = int(math.ceil((lr[1] - lr[0]) / h0)); npb = int(math.ceil((pr[1] - pr[0]) / h0))
    H = np.zeros((nl, npb)); rng = np.random.default_rng(seed)
    for _ in range(n // chunk):
        Y = sample(rng, law, N, (chunk, 8)) @ E
        H += np.histogram2d(Y[:, 0], Y[:, 2], bins=(nl, npb), range=((lr[0], lr[0] + nl * h0), (pr[0], pr[0] + npb * h0)))[0]
    out = []
    for h in hs:
        k = int(round(h / h0)); Hk = H[: (nl // k) * k, : (npb // k) * k].reshape(nl // k, k, npb // k, k).sum(axis=(1, 3))
        rho = Hk / (n * h * h)
        lc = lr[0] + (np.arange(Hk.shape[0]) + 0.5) * h
        mg = rho.max(axis=0).sum() * h
        rl = []
        for l0 in l0s:
            sel = np.abs(lc - l0) <= 1.0
            if sel.any():
                r = rho[sel].max(axis=0)
                rp = r[r > 0]
                # right side of Proposition 5.4 with lambda = 1 and a(p) replaced by its bound 2 sqrt 2
                bnd = 0.5 + h * np.sum(rp * (2 + 2 * np.maximum(0.0, np.log(8.0 / rp))))
                rl.append((r.sum() * h, bnd))
            else:
                rl.append((0.0, 0.5))
        out.append((h, mg, rl, rho.max()))
    return out

if __name__ == "__main__":
    law = sys.argv[1]; Ns = [int(x) for x in sys.argv[2].split(",")]
    for N in Ns:
        t0 = time.time()
        E = frame("irr2"); lo, hi = bounds(law, N)
        mid = (lo + hi) / 2 * E[:, 0].sum()
        l0s = (0.0, mid)
        for h, mg, rl, mx in run(N, law, l0s=l0s):
            print("%s N=%d h=%.2f  M_glob %.3f  R_loc(0) %.3f (bound %.2f)  R_loc(EL=%.2f) %.3f (bound %.2f)  max rho %.3f"
                  % (law, N, h, mg, rl[0][0], rl[0][1], mid, rl[1][0], rl[1][1], mx), flush=True)
        print("   (%.0fs)" % (time.time() - t0), flush=True)
