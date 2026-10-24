"""Can the octave be COVERED by well-placed shorter windows, each with a bounded constant?

E(R) <= sum over any cover of [R,2R) of sum_{k in W_j} F_K(k), and each window contributes
2^-(K+1) L' A(k0_j) with A(k0) = 1 + Err(k0)/L'.  If a cover exists whose windows all have A = O(1),
then E(R) <= 2^-(K+1) R C = (C/2) R^-0.7095 and S converges.  The target weakens from "the single
position R is good" to "near each of a few places there EXISTS a good position".

Measured before: over ALL positions the median of Err/L is -0.34, the 99th percentile +6.4 (both stable
in K), while the maximum grows like (4/3)^K on the spike-containing windows.  So the question is whether
the spikes can be dodged locally.

Here: split [R, 2R) into m blocks of length L' = R/m, allow each window start to move within its block,
and record max over blocks of (min over the block of A).  If that stays bounded in K, a cover exists.
"""
import numpy as np

def A_profile(K, Lp, lo, hi):
    """A(k0) = 2^(K+1) * sum_{k in [k0, k0+Lp)} F_K(k) / Lp, for k0 in [lo, hi)."""
    k = np.arange(lo, hi + Lp, dtype=np.float64)
    F = np.ones_like(k)
    for i in range(K + 1):
        F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
    c = np.concatenate(([0.0], np.cumsum(F)))
    tot = c[Lp:] - c[:-Lp]           # window sums starting at lo, lo+1, ...
    return (2.0 ** (K + 1)) * tot[: hi - lo] / Lp

print(f"{'K':>4} {'R':>9} {'m':>4} {'Lp':>8} {'A at k0=R':>11} {'max_j min_block A':>19} {'median A':>10}")
for K in (10, 14, 18, 22, 26, 30):
    R = int(round(1.5 ** K))
    for m in (1, 4, 16):
        Lp = max(1, R // m)
        prof = A_profile(K, Lp, R, 2 * R)
        # block j: window must start near R + j*Lp; allow it to slide within [R+j*Lp - Lp//2, R+j*Lp]
        worst = 0.0
        for j in range(m):
            s = j * Lp - Lp // 2
            e = j * Lp + 1
            s = max(0, s); e = max(s + 1, min(e, prof.size))
            worst = max(worst, float(prof[s:e].min()))
        aR = float(prof[0])
        print(f"{K:>4} {R:>9} {m:>4} {Lp:>8} {aR:>11.4f} {worst:>19.4f} {float(np.median(prof)):>10.4f}")
    print()
