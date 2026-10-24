# Mixed norms J_{p,1}(kappa) = int dt ( int dy |T(y, t)|^p )^{1/p}, T(y, t) = E exp(i(yL + tV + kappa L P)), along the
# one-dimensional path of j1check.py: for each y the whole t-profile comes from one FFT, and sum_y |T(y, t)|^p dy is
# accumulated for every t. T(-y, t) and T(y, t) have the same modulus pattern in t up to t -> -t (the law of z is
# symmetric), so y >= 0 is computed and doubled.
import sys, math, time
import numpy as np
from jperp import rot
from j1check import setup

PS = (1.0, 1.25, 1.5, 1.75, 2.0)

def profile(S, a, kappa):
    s2 = S["s"] ** 2; L, P = S["L"], S["P"]
    al = a + kappa * P; ga = kappa * L; den = 1.0 + kappa * kappa * s2 * s2
    w = S["p"] * np.exp(1j * (a * L + kappa * L * P)) / math.sqrt(den) * \
        np.exp(-(s2 * (al * al + ga * ga) + 2j * kappa * s2 * s2 * al * ga) / (2 * den))
    wt = (w[:, None] * S["gv"]).ravel()
    A = np.bincount(S["idx"], weights=wt.real, minlength=S["M"]) + 1j * np.bincount(S["idx"], weights=wt.imag, minlength=S["M"])
    return np.abs(np.fft.fft(A) * S["h"])

if __name__ == "__main__":
    N = int(sys.argv[1]); kappas = [float(x) for x in sys.argv[2].split(",")]
    which = sys.argv[3] if len(sys.argv) > 3 else "irr"
    if which == "irr":
        R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    else:   # the second irrational rotation of j2dp.py
        R = rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
    S = setup(N, R); t0 = time.time()
    da = 1.0 / (3.0 * S["rngL"]); dt = 2 * math.pi / (S["M"] * S["h"])
    for kappa in kappas:
        amax = 8.0 / S["s"] + abs(kappa) * np.abs(S["P"]).max()
        a = np.arange(0.0, amax, da)
        acc = {p: np.zeros(S["M"]) for p in PS}
        for k, x in enumerate(a):
            f = profile(S, x, kappa)
            wgt = da * (1.0 if k else 0.5)
            for p in PS:
                acc[p] += wgt * f ** p
        # the negative y half: |T(-y, t)| = |T(y, -t)|
        out = []
        for p in PS:
            tot = acc[p] + acc[p][(-np.arange(S["M"])) % S["M"]]
            out.append(float((tot ** (1.0 / p)).sum() * dt))
        print("N=%d frame=%s kappa=%.2f  " % (N, which, kappa) + "  ".join("p=%.2f: %7.3f" % (p, v) for p, v in zip(PS, out)) +
              "   (%d y-values, %.0fs)" % (len(a), time.time() - t0), flush=True)
