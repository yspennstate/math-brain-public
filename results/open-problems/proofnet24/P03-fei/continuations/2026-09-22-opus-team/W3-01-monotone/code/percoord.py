"""Refutation check: a per-coordinate form of FEI fails for monotone threshold functions.

For a coordinate i put  L_i(f) = E[ log2(1/fhat(S)^2) / |S|  |  i in S ]  (S the spectral sample).
FEI is the Inf-weighted average statement  H(f) - phi(fhat(0)^2) = sum_i Inf_i L_i(f) <= C I(f).
The per-coordinate strengthening  L_i(f) <= C  for every i  fails: take f = z AND [sum of m others >= t]
with Pr[threshold] about 1/8; L_z grows like log2(m / log(1/mu)) while H/I stays bounded.
Usage: python percoord.py
"""
import math
import numpy as np
from monolib import setup_process, fwht_float, popcounts


def main():
    setup_process()
    for m in (8, 11, 14, 17, 19):
        n = m + 1
        N = 1 << n
        xs = np.arange(N)
        pc_x = popcounts(n) - (xs & 1)          # weight of the m threshold coordinates (1..m)
        z = xs & 1                               # coordinate 0 is z
        # threshold t with Pr[sum >= t] closest to 1/8
        from math import comb
        best = None
        for t in range(m + 1):
            mu = sum(comb(m, k) for k in range(t, m + 1)) / 2 ** m
            if best is None or abs(mu - 0.125) < abs(best[1] - 0.125):
                best = (t, mu)
        t, mu = best
        f = ((z == 1) & (pc_x >= t)).astype(np.float64)
        c = fwht_float(1.0 - 2.0 * f)
        p = c * c
        pc = popcounts(n)
        nz = p > 1e-300
        H = float(-(p[nz] * np.log2(p[nz])).sum())
        I = float((pc * p).sum())
        sel = nz & ((xs & 1) == 1)
        Infz = float(p[sel].sum())
        Lz = float((p[sel] * (-np.log2(p[sel])) / pc[sel]).sum()) / Infz
        # the x coordinates (by symmetry take coordinate 1)
        sel1 = nz & ((xs >> 1) & 1 == 1)
        Inf1 = float(p[sel1].sum())
        L1c = float((p[sel1] * (-np.log2(p[sel1])) / pc[sel1]).sum()) / Inf1
        print(f"m={m:2d} t={t:2d} mu={mu:.4f}: H/I={H/I:.4f}  Inf_z={Infz:.4f} L_z={Lz:.4f}  "
              f"Inf_x={Inf1:.4f} L_x={L1c:.4f}  (Inf_z L_z)/I={Infz*Lz/I:.4f}", flush=True)


if __name__ == "__main__":
    main()
