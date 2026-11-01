"""AND-prefix functional Lambda(g) = 4 I(g) - H(g) + 2 E(p),  E(p) = sum_{l>=0} 2^l eps(2^-l p),  p = Pr[g true].

For f_m = AND(x_1, ..., x_m, g) (an LTF whenever g is one), 2^m (4 I(f_m) - H(f_m)) -> Lambda(g) as m -> infinity,
while 2^m I(f_m) ~ 2 m p.  So an LTF g with Lambda(g) < 0 (or the same for not g, p -> 1-p) would give LTFs with
H/I > 4.  For the alternating chain (p -> 2/3) Lambda = D_inf(2/3) = 0.14412.  This scans:
  (a) every LTF with integer weights 1 <= w_n <= ... <= w_1 <= W and every threshold, n <= 8;
  (b) random real-weight LTFs, n = 10..14, all thresholds;
  (c) chains (as a control).
It also checks the prediction directly on the minimiser: H/I of AND_m(g) for m = 20, 40 from the exact AND formula.
"""
import sys, itertools, math
import numpy as np
import numba as nb
from ltfcore import linform, spectrum, HI
from chains_defect3 import eps

LN2 = math.log(2.0)


@nb.njit(cache=True)
def E_of(p):
    acc = 0.0
    for l in range(90):
        acc += (2.0 ** l) * eps(p * 2.0 ** (-l))
    return acc


@nb.njit(cache=True)
def scan_weight(w, out_min):
    """All thresholds for integer weight vector w: returns (min Lambda, H, I, p, theta index) over the thresholds."""
    v = linform(w)
    vals = np.unique(v)
    n = w.shape[0]
    N = v.shape[0]
    best = 1e300
    bH = 0.0; bI = 0.0; bp = 0.0; bth = 0.0
    for t in range(1, vals.shape[0]):
        theta = 0.5 * (vals[t - 1] + vals[t])
        f = np.empty(N)
        cnt = 0
        for x in range(N):
            if v[x] > theta:
                f[x] = 1.0
            else:
                f[x] = -1.0
                cnt += 1
        p = cnt / N          # Pr[f = -1] = Pr[true]
        c = spectrum(f)
        H, I = HI(c)
        D = 4.0 * I - H
        for q in (p, 1.0 - p):
            lam = D + 2.0 * E_of(q)
            if lam < best:
                best = lam; bH = H; bI = I; bp = q; bth = theta
    return best, bH, bI, bp, bth


def and_prefix_ratio(H, I, p, m):
    # AND with a fresh variable: H' = H/2 + A(p), I' = I/2 + p, p' = p/2 ; A(p) = 4p - eps(p)
    for _ in range(m):
        A = 4 * p - eps(p)
        H, I, p = H / 2 + A, I / 2 + p, p / 2
    return H / I


if __name__ == "__main__":
    rng = np.random.default_rng(20260923)
    overall = (1e300, None)
    for n, W in [(3, 12), (4, 12), (5, 10), (6, 9), (7, 8), (8, 6)]:
        best = (1e300, None)
        cnt = 0
        for wt in itertools.combinations_with_replacement(range(1, W + 1), n):
            w = np.array(sorted(wt, reverse=True), dtype=np.float64)
            lam, H, I, p, th = scan_weight(w, 0.0)
            cnt += 1
            if lam < best[0]:
                best = (lam, (tuple(int(a) for a in w), th, H, I, p))
        print("n=%d W=%d weight vectors=%d : min Lambda = %.8f at w=%s theta=%.1f (H=%.6f I=%.6f p=%.6f)"
              % (n, W, cnt, best[0], best[1][0], best[1][1], best[1][2], best[1][3], best[1][4]), flush=True)
        if best[0] < overall[0]:
            overall = best
    for n in [10, 12, 14]:
        best = (1e300, None)
        trials = {10: 300, 12: 120, 14: 30}[n]
        for tr in range(trials):
            kind = tr % 3
            if kind == 0:
                w = np.abs(rng.standard_normal(n))
            elif kind == 1:
                w = rng.random(n) ** 3
            else:
                w = 2.0 ** (-rng.random(n) * n / 2)
            w = np.sort(w)[::-1] + 1e-9 * rng.random(n)
            lam, H, I, p, th = scan_weight(w, 0.0)
            if lam < best[0]:
                best = (lam, (np.round(w, 4), th, H, I, p))
        print("n=%d random real weights (%d vectors, all thresholds): min Lambda = %.8f (H=%.6f I=%.6f p=%.6f)"
              % (n, trials, best[0], best[1][2], best[1][3], best[1][4]), flush=True)
    # chains as a control: weights 2^i
    for n in [8, 10, 12]:
        w = np.array([2.0 ** (n - 1 - i) for i in range(n)])
        lam, H, I, p, th = scan_weight(w, 0.0)
        print("chains n=%d: min Lambda = %.8f at p=%.6f (limit value 0.14412433 at p -> 2/3)" % (n, lam, p), flush=True)
    lam, (w, th, H, I, p) = overall
    print("overall minimiser over integer weights: Lambda=%.8f w=%s theta=%.1f p=%.6f" % (lam, w, th, p))
    for m in [10, 20, 40, 80]:
        print("  AND_m(minimiser), m=%d: H/I = %.10f" % (m, and_prefix_ratio(H, I, p, m)))
