"""Does shifting (the compression S_ij that makes coordinate i at least as desirable as j) move a
monotone function toward FEI-extremality?  For every monotone f on n variables and every ordered pair
(i, j), compute g = S_ij f and record

    dH = H(f) - H(g),   dI = I(f) - I(g).

If H(f) - C I(f) <= H(g) - C I(g) held for all f and all shifts (dH <= C dI), then FEI for shifted
(regular) functions would imply FEI for all monotone functions with the same constant.
Usage: python shift_test.py N
"""
import sys, time
import numpy as np
import numba as nb
from monolib import *


@nb.njit(cache=True)
def shift(tt, n, i, j):
    """On every 2-face in directions (i, j): if f(x_i=0,x_j=1)=1 and f(x_i=1,x_j=0)=0, swap."""
    N = 1 << n
    bi = 1 << i
    bj = 1 << j
    out = tt
    for x in range(N):
        if (x & bi) == 0 and (x & bj) != 0:
            y = x ^ (bi | bj)
            fx = (tt >> np.uint64(x)) & np.uint64(1)
            fy = (tt >> np.uint64(y)) & np.uint64(1)
            if fx == 1 and fy == 0:
                out = out & ~(np.uint64(1) << np.uint64(x))
                out = out | (np.uint64(1) << np.uint64(y))
    return out


@nb.njit(cache=True)
def is_monotone(tt, n):
    N = 1 << n
    for x in range(N):
        fx = (tt >> np.uint64(x)) & np.uint64(1)
        if fx == 1:
            for k in range(n):
                y = x | (1 << k)
                if ((tt >> np.uint64(y)) & np.uint64(1)) == 0:
                    return False
    return True


@nb.njit(cache=True)
def run(tabs, n):
    worst_ratio = -1e18       # max dH/dI over dI > 0
    worst_arg = (-1, -1, -1)
    zero_dI_bad = 0           # dI == 0 but dH > 0
    zero_dI_bad_max = 0.0
    zero_arg = (-1, -1, -1)
    dI_neg = 0                # influence increased
    nonmono = 0
    npairs = 0
    for t in range(tabs.size):
        tt = tabs[t]
        W = wht_int(tt, n)
        H, I = entropy_influence(W, n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                g = shift(tt, n, i, j)
                if g == tt:
                    continue
                npairs += 1
                if not is_monotone(g, n):
                    nonmono += 1
                Wg = wht_int(g, n)
                Hg, Ig = entropy_influence(Wg, n)
                dH = H - Hg
                dI = I - Ig
                if dI < -1e-12:
                    dI_neg += 1
                if abs(dI) <= 1e-12:
                    if dH > 1e-12:
                        zero_dI_bad += 1
                        if dH > zero_dI_bad_max:
                            zero_dI_bad_max = dH
                            zero_arg = (t, i, j)
                elif dI > 0:
                    r = dH / dI
                    if r > worst_ratio:
                        worst_ratio = r
                        worst_arg = (t, i, j)
    return npairs, nonmono, dI_neg, zero_dI_bad, zero_dI_bad_max, zero_arg, worst_ratio, worst_arg


def main():
    setup_process()
    n = int(sys.argv[1])
    tabs = monotone_tables(n)
    t0 = time.time()
    npairs, nonmono, dI_neg, zbad, zmax, zarg, wr, warg = run(tabs, n)
    print(f"n={n}: {tabs.size} monotone functions, {npairs} nontrivial shifts ({time.time()-t0:.1f}s)")
    print(f"  shifts producing a non-monotone table (must be 0): {nonmono}")
    print(f"  shifts that increase I: {dI_neg}")
    print(f"  shifts with dI = 0 and dH > 0: {zbad}, max dH {zmax:.6f} at f={int(tabs[zarg[0]]) if zarg[0]>=0 else -1}, (i,j)={zarg[1:]}")
    print(f"  max dH/dI over shifts with dI > 0: {wr:.6f} at f={int(tabs[warg[0]]) if warg[0]>=0 else -1}, (i,j)={warg[1:]}")


if __name__ == "__main__":
    main()
