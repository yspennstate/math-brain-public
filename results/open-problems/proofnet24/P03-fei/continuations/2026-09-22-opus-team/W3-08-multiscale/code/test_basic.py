"""Controls for mslib: hand values, brute-force restrictions, F4's coordinate quantities, M_J <= L_J."""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mslib import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "F4-proof-attempt", "code"))
import feilib

polite()


def brute_EH(tt, n, J):
    """E_x H(f_{J,x}) by explicit restriction and transform."""
    free = [i for i in range(n) if (J >> i) & 1]
    fixed = [i for i in range(n) if not (J >> i) & 1]
    tot = 0.0
    for xv in itertools.product([0, 1], repeat=len(fixed)):
        sub = np.empty(1 << len(free), dtype=np.int64)
        for y in range(1 << len(free)):
            idx = 0
            for k, i in enumerate(free):
                idx |= ((y >> k) & 1) << i
            for k, i in enumerate(fixed):
                idx |= xv[k] << i
            sub[y] = tt[idx]
        fh = fwht(sub)
        tot += entropy_bits(fh * fh)
    return tot / (1 << len(fixed))


maj3 = np.array([1 if bin(x).count("1") < 2 else -1 for x in range(8)])
and2 = np.array([1, 1, 1, -1])
out, EH, HT, inf, H, I = multiscale_summary(maj3, 3)
print("Maj3", {k: round(v, 6) for k, v in out.items()}, " expected kappa_0.5 = 4/3")
out, EH, HT, inf, H, I = multiscale_summary(and2, 2)
print("AND2", {k: round(v, 6) for k, v in out.items()}, " expected kappa_0.5 = 3")

rng = np.random.default_rng(1)
maxerr = 0.0
worst_ML = -1e9
for trial in range(40):
    n = int(rng.integers(3, 8))
    tt = rng.choice([-1, 1], size=1 << n).astype(np.int64)
    EH, HT = restr_profile(tt, n, True)
    fh, p, Hf, inf = basic(tt, n)
    for J in rng.integers(0, 1 << n, size=6):
        b = brute_EH(tt, n, int(J))
        maxerr = max(maxerr, abs(b - EH[J]))
    full = (1 << n) - 1
    maxerr = max(maxerr, abs(EH[full] - Hf))
    worst_ML = max(worst_ML, np.max((HT - EH) - (Hf - HT)))
    # coordinate drops against F4
    cq = feilib.coord_quantities(fh[None, :], n)
    for i in range(n):
        maxerr = max(maxerr, abs(cq["Delta"][0, i] - (Hf - EH[full & ~(1 << i)])))
print("max |profile - brute force| over random functions:", maxerr)
print("max over (f,J) of M_J - L_J (must be <= 0 by Maassen-Uffink):", worst_ML)
