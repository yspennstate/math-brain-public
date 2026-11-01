# Independent check of J_2(kappa): integrate the 1D integral J(a, kappa) = int |E e^{i(aL + tV + kappa LP)}| dt over a,
# with the cell's (L, P)-part integrated analytically (exact 2D Gaussian with the bilinear phase) and the V-part
# deposited as Gaussian bumps (Gaussian gridding, spacing sigma/3) before a 1D FFT in t. J is even in a.
import sys, math, time
import numpy as np
from jperp import triple_law, rot

def setup(N, R, pad=4.0):
    z, p = triple_law(N)
    y = z @ R / math.sqrt(8.0)
    L, V, P = y[:, 0], y[:, 1], y[:, 2]
    s = 1.0 / (math.sqrt(12.0) * N); h = s / 3.0; W = 12
    v0 = V.min() - 5 * s
    M = 1 << int(math.ceil(math.log2(pad * (V.max() - V.min() + 10 * s) / h)))
    cv = np.rint((V - v0) / h).astype(np.int64)
    off = np.arange(-W, W + 1)
    gv = np.exp(-0.5 * ((v0 + (cv[:, None] + off[None, :]) * h - V[:, None]) / s) ** 2) / (math.sqrt(2 * math.pi) * s)
    idx = (cv[:, None] + off[None, :]).ravel()
    return dict(L=L, P=P, p=p, s=s, h=h, M=M, gv=gv, idx=idx, rngL=L.max() - L.min())

def J(S, a, kappa):
    s2 = S["s"] ** 2; L, P = S["L"], S["P"]
    al = a + kappa * P; ga = kappa * L; den = 1.0 + kappa * kappa * s2 * s2
    w = S["p"] * np.exp(1j * (a * L + kappa * L * P)) / math.sqrt(den) * \
        np.exp(-(s2 * (al * al + ga * ga) + 2j * kappa * s2 * s2 * al * ga) / (2 * den))
    wt = (w[:, None] * S["gv"]).ravel()
    A = np.bincount(S["idx"], weights=wt.real, minlength=S["M"]) + 1j * np.bincount(S["idx"], weights=wt.imag, minlength=S["M"])
    F = np.fft.fft(A) * S["h"]
    return float(np.abs(F).sum() * 2 * math.pi / (S["M"] * S["h"]))

if __name__ == "__main__":
    N = int(sys.argv[1]); kappas = [float(x) for x in sys.argv[2].split(",")]
    R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    S = setup(N, R); t0 = time.time()
    da = 1.0 / (3.0 * S["rngL"])
    for kappa in kappas:
        amax = 8.0 / S["s"] + abs(kappa) * np.abs(S["P"]).max()
        a = np.arange(0.0, amax, da)
        vals = np.array([J(S, x, kappa) for x in a])
        tot = 2 * (vals.sum() - 0.5 * vals[0]) * da
        print("N=%d kappa=%.2f  J2 = %.3f   (sup_a J = %.3f, %d a-values, %.0fs)" % (N, kappa, tot, vals.max(), len(a), time.time() - t0), flush=True)
