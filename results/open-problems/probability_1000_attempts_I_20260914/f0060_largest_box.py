"""Janson's Problem 18.40 (ledger row F0060): with lambda > nu = 0, can Y_(1)/n -> 0 in probability?
Example 18.38 gives it along a subsequence; the question is the full sequence.

Setting: weights w on a support S, allocation B_{m,n} = n i.i.d. copies of the tilted law conditioned
on their sum being m.  Because rho = 0 the tilt depends on n: pick tau_n with mean(tau_n) = m/n.

What the per-ball bookkeeping predicts.  Normalising w_0 = 1 and writing f = log w, a configuration
made of r boxes of size s (and n - r empty) has weight  C(n,r) w_s^r, whose logarithm is
m * [ f(s)/s + (log(s/lambda) + 1)/s ] + o(m)  with r = m/s.  So the optimal box size maximises
    F(s) = ( f(s) + log(s/lambda) + 1 ) / s ,
the first term pushing towards large boxes (it diverges exactly because rho = 0) and the second,
the entropy of choosing which boxes, pushing towards small ones.  F -> infinity, so F has infinitely
many records, and at m equal to a record the maximiser is m itself: the largest box is the whole mass.
Hence along those n the ratio Y_(1)/n is about lambda, not 0.

This script computes the exact conditional law of Y_(1) for Janson's own Example 18.38 and reports
E[Y_(1)]/n over a range of n, to see the predicted oscillation.
"""
import numpy as np, sys
from math import lgamma, log, exp

def support_powers(K, c=1.0):
    """S = {0,1} u {2^j}, log w at 2^j equal to c * 2^j * sqrt(j): f(s)/s = c sqrt(log_2 s) -> infinity
    as slowly as we like, so rho = 0 with a dense support and small record gaps - the case an
    adversary would use to try to keep the largest box small."""
    import math
    lw = np.full(K + 1, -np.inf)
    lw[0] = 0.0
    if K >= 1: lw[1] = 0.0
    v, j = 2, 1
    while v <= K:
        lw[v] = c * v * math.sqrt(j)
        v *= 2; j += 1
    return lw, [k for k in range(K + 1) if lw[k] > -np.inf]

def support_factorial(K):
    """S = {0,1} u {i! : i >= 2}, w_k = k! on S and 0 off it; returns log w on 0..K (or -inf)"""
    S = {0, 1}
    v, i = 2, 2
    while v <= K:
        S.add(v); i += 1; v *= i
    lw = np.full(K + 1, -np.inf)
    for k in sorted(S):
        lw[k] = lgamma(k + 1)
    return lw, sorted(S)

def tilt(lw, K, target, lo=-60.0, hi=5.0):
    """find log tau so that the tilted law w_k tau^k / Phi has mean = target; returns the tilted pmf"""
    ks = np.arange(K + 1)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        a = lw + ks * mid
        a -= a.max()
        p = np.exp(a); p /= p.sum()
        mu = (ks * p).sum()
        if mu < target: lo = mid
        else: hi = mid
    a = lw + ks * (0.5 * (lo + hi)); a -= a.max()
    p = np.exp(a); p /= p.sum()
    return p

def conv_pow_trunc(p, n, m):
    """coefficient array up to m of p^n (probability convolution), by repeated squaring"""
    res = np.zeros(m + 1); res[0] = 1.0
    base = p[:m + 1].copy()
    while n:
        if n & 1: res = np.convolve(res, base)[:m + 1]
        n >>= 1
        if n: base = np.convolve(base, base)[:m + 1]
    return res

def largest_box(n, lam, K=None):
    m = int(round(lam * n))
    K = K or m
    lw, S = (support_powers(K, POWC) if MODE == 'pow' else support_factorial(K))
    p = tilt(lw, K, m / n)
    Z = conv_pow_trunc(p, n, m)[m]
    if Z <= 0: return None
    # P(Y_(1) < t) = [x^m] (sum_{k<t} p_k x^k)^n / Z
    out = []
    for t in S:
        if t == 0: continue
        q = p.copy(); q[t:] = 0.0
        out.append((t, conv_pow_trunc(q, n, m)[m] / Z))
    # E[Y_(1)] from the c.d.f. over the support values
    prev, ev = 0.0, 0.0
    for t, c in out:
        ev += t * 0 + 0  # placeholder, filled below
    cdf = dict(out)
    vals = [t for t, _ in out]
    e = 0.0; prevc = 0.0
    for i, t in enumerate(vals):
        c = cdf[t]
        # P(Y_(1) = the largest support value < t) = c - prevc
        if i > 0:
            e += vals[i - 1] * (c - prevc)
        prevc = c
    e += vals[-1] * (1.0 - prevc)
    return m, e, cdf, S

MODE = 'fact'; POWC = 1.0
if __name__ == '__main__':
    lam = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    MODE = sys.argv[2] if len(sys.argv) > 2 else 'fact'
    POWC = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    print(f"Example 18.38 of Janson (support {{0,1}} u {{i!}}, w_k = k!), lambda = {lam}")
    print(f"{'n':>6} {'m':>6} {'E Y(1)':>10} {'E Y(1)/n':>10} {'largest support <= m':>21}")
    NS = ((10, 20, 24, 25, 40, 60, 100, 119, 120, 121, 160, 240, 360, 500, 719, 720, 721) if MODE == 'fact'
          else (12, 16, 17, 24, 31, 32, 33, 48, 63, 64, 65, 96, 127, 128, 129, 200, 255, 256, 257))
    for n in NS:
        r = largest_box(n, lam)
        if not r: continue
        m, e, cdf, S = r
        smax = max(s for s in S if s <= m)
        print(f"{n:>6} {m:>6} {e:>10.2f} {e/n:>10.4f} {smax:>21}")
