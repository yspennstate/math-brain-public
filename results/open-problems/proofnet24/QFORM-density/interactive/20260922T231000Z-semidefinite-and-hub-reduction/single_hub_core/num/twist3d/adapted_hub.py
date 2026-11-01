# A hub that may depend on P. For Q = 2 X_h L + V^2 + 2 eps L P (beta = 0, lambda = 1) the hub value that puts Q at s is
# x* = (s - V^2)/(2L) - eps P, under the weight 1/(2|L|), which does not depend on eps (run() also takes beta, for the
# eps = 0 form 2 Y (L + beta) + V^2 with a hub Y that sees P). Conditioning on P gives, for every
# eps, sup over hub laws of p_Q(s) <= Phi = int dp sup_{|A| = 1} int_A W(x, p) dx, W the weighted density of (x*_0, P):
# the eps = 0 density with a hub that is allowed to depend on P. Phi is estimated from a weighted 2D histogram in
# (x*_0, P): in each P-column the top unit set of x-bins is kept. Finer P-columns and finer x-bins raise the estimate
# (sampling noise is selected upward), so it is printed on several grids and for half of the samples.
import sys, math, time
import numpy as np
from jperp import S, rot

def frame(which):
    R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3))) if which == "irr" else \
        rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
    return S @ R / math.sqrt(8.0)

def sample(rng, law, N, size):
    if law == "int":        # teeth of width 1/N at the integers 0..N-1
        return rng.integers(0, N, size=size) + rng.random(size) / N
    if law == "fine":       # teeth of width 1/N at spacing 2/N in [-1, 1]
        return (2 * rng.integers(0, N, size=size) + rng.random(size)) / N - 1.0
    if law == "two":        # N^2 teeth of width 1/N^2 in groups spaced 1/N at the integers
        return rng.integers(0, N, size=size) + rng.integers(0, N, size=size) / N + rng.random(size) / N ** 2
    raise ValueError(law)

def run(N, law="int", s=0.0, which="irr2", n=40_000_000, chunk=2_000_000, xmax=6.0, b0=0.01, bp0=0.05, seed=5, beta=0.0,
        shuffle=False):
    E = frame(which)
    lo = {"int": 0.0, "fine": -1.0, "two": 0.0}[law]; hi = {"int": N, "fine": 1.0, "two": N}[law]
    q = E[:, 2]
    pmin = lo * q[q > 0].sum() + hi * q[q < 0].sum() - 0.1
    pmax = hi * q[q > 0].sum() + lo * q[q < 0].sum() + 0.1
    nx = int(round(2 * xmax / b0)); npb = int(math.ceil((pmax - pmin) / bp0))
    H = np.zeros((nx, npb)); H0 = np.zeros((nx, npb)) if shuffle else None
    rng = np.random.default_rng(seed)
    halves = []
    rg = ((-xmax, xmax), (pmin, pmin + npb * bp0))
    for c in range(n // chunk):
        X = sample(rng, law, N, (chunk, 8))
        Y3 = X @ E; L, V, P = Y3[:, 0], Y3[:, 1], Y3[:, 2]
        T = L + beta
        xs = (s - V * V) / (2 * T); wt = 1.0 / (2 * np.abs(T))
        h, _, _ = np.histogram2d(xs, P, bins=(nx, npb), range=rg, weights=wt)
        H += h
        if shuffle:
            # control: P shuffled across samples, so a gain over the bathtub can only come from the estimator's noise
            H0 += np.histogram2d(xs, rng.permutation(P), bins=(nx, npb), range=rg, weights=wt)[0]
        if c == n // chunk // 2 - 1:
            halves.append(H.copy())
    out = {}
    sets = [("full", H, n), ("half", halves[0], n // 2)] + ([("shuffled P", H0, n)] if shuffle else [])
    for tag, HH, nn in sets:
        for b in (0.01, 0.02):
            kx = int(round(b / b0)); Hx = HH[: (nx // kx) * kx].reshape(-1, kx, npb).sum(axis=1)
            top = int(round(1.0 / b))
            col = np.sort(Hx.sum(axis=1))[::-1][:top].sum() / nn        # eps = 0, one set for all P
            out[(tag, b, "B0")] = col
            for kp in (1, 4, 20, 10 ** 9):
                kp_ = min(kp, npb); m = (npb // kp_) * kp_
                Hp = Hx[:, :m].reshape(Hx.shape[0], -1, kp_).sum(axis=2)
                out[(tag, b, kp_ * bp0 if kp < 10 ** 9 else "all")] = np.sort(Hp, axis=0)[::-1][:top].sum() / nn
    return out, bp0

if __name__ == "__main__":
    law = sys.argv[1]; Ns = [int(x) for x in sys.argv[2].split(",")]
    xmax = float(sys.argv[3]) if len(sys.argv) > 3 else 6.0
    bp0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.05
    for N in Ns:
        t0 = time.time(); out, bp0 = run(N, law, xmax=xmax, bp0=bp0)
        for tag in ("full", "half"):
            for b in (0.01, 0.02):
                keys = [k for k in out if k[0] == tag and k[1] == b and k[2] not in ("B0",)]
                row = "  ".join("dP=%s: %.4f" % (("%.3f" % k[2]) if k[2] != "all" else "all", out[k]) for k in keys)
                print("%s N=%d %s bin %.2f  eps=0 bathtub %.4f  adapted Phi %s" % (law, N, tag, b, out[(tag, b, "B0")], row), flush=True)
        print("   (%.0fs)" % (time.time() - t0), flush=True)
