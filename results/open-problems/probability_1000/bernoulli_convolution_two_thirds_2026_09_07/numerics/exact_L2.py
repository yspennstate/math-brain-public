# -*- coding: utf-8 -*-
"""Exact L^2 norms of the prefix densities g_D of the two-thirds Bernoulli measure.

g_D = law of (1/3) sum_{k<D} B_k lam^k + lam^D V, V ~ Unif[0,1]:  a mixture of 2^D uniform densities on
intervals of length lam^D.  Then
   int g_D^2 = lam^{-D} * E_eps[ (1 - |S_eps| lam^{-D})_+ ],   S_eps = (1/3) sum_{k<D} eps_k lam^k,
with eps_k = B_k - B'_k i.i.d. taking 0 w.p. 1/2 and +-1 w.p. 1/4.  Multiplying by 3^D:
   3^D S_eps = (1/3) sum eps_k 2^k 3^{D-k} ... use integer T = sum_k eps_k 2^k 3^{D-1-k}; then S = T / 3^D and
   |S| < lam^D  <=>  |T| < 2^D, and (1 - |S| lam^{-D})_+ = (1 - |T|/2^D)_+.
Meet in the middle: enumerate the 3^{D1} integer half-sums (weights = product of 1/2, 1/4) for k < D1 and the
3^{D2} half-sums for k >= D1; sort the second; for each a in the first, the window of b with |a+b| < 2^D gives
sum_b w_b (1 - |a+b|/2^D) by prefix sums.  Exact in the integers, floating point only in the weights.
Prints int g_D^2 for the requested depths, and the bounded-L2 diagnostic ratio.
"""
import numpy as np, math, sys, time

def half_sums(coeffs):
    """All sums sum_k eps_k c_k with eps in {-1,0,1}, returned as (values int64, weights float64)."""
    vals = np.array([0], dtype=np.int64); w = np.array([1.0])
    for c in coeffs:
        vals = np.concatenate([vals - c, vals, vals + c])
        w = np.concatenate([w * 0.25, w * 0.5, w * 0.25])
    return vals, w

def l2_norm(D):
    coeffs = [2**k * 3**(D - 1 - k) for k in range(D)]        # exact ints
    if max(coeffs) >= 2**62: raise SystemExit("D too large for int64")
    D1 = D // 2
    a, wa = half_sums(coeffs[:D1]); b, wb = half_sums(coeffs[D1:])
    order = np.argsort(b, kind="stable"); b = b[order]; wb = wb[order]
    cw = np.concatenate([[0.0], np.cumsum(wb)])                # prefix sums of weights
    cwb = np.concatenate([[0.0], np.cumsum(wb * b.astype(np.float64))])   # prefix sums of w*b
    M = 2**D
    # window for each a: b in (-a-M, -a+M); split at b = -a (sign of a+b)
    lo = np.searchsorted(b, -a - M, side="right")   # first index with b > -a-M
    mid = np.searchsorted(b, -a, side="left")       # first index with b >= -a
    hi = np.searchsorted(b, -a + M, side="left")    # first index with b >= -a+M
    af = a.astype(np.float64)
    # b in [lo, mid): a+b < 0 -> (1 - (-(a+b))/M) = 1 + (a+b)/M
    W1 = cw[mid] - cw[lo]; S1 = cwb[mid] - cwb[lo]
    part1 = W1 + (af * W1 + S1) / M
    # b in [mid, hi): a+b >= 0 -> 1 - (a+b)/M
    W2 = cw[hi] - cw[mid]; S2 = cwb[hi] - cwb[mid]
    part2 = W2 - (af * W2 + S2) / M
    E = float(np.sum(wa * (part1 + part2)))
    return (1.5 ** D) * E, E

if __name__ == "__main__":
    depths = [int(x) for x in sys.argv[1:]] or list(range(6, 31, 2))
    prev = None
    for D in depths:
        t0 = time.time(); L2, E = l2_norm(D)
        print(f"D={D:2d}  int g_D^2 = {L2:.6f}   (E=(near-cancellation mass)={E:.3e}, {time.time()-t0:.1f}s)", flush=True)
