"""Is Err/L at the OCTAVE position bounded for large K, or does the (4/3)^K growth reach it?

My closure argument bounded sum_m c(m)|G|, which is a bound on sup over window positions k0.
A verifier's objection: that sup does grow like (4/3)^K, but the lane needs only k0 = R, where the
quantity may stay bounded. Settle it directly, with no character expansion at all:

    Err/L = ( 2^(K+1) * sum_{k in W} F_K(k)  -  L ) / L,   W = [k0, k0+L), k0 = L = round((3/2)^K).

That needs only L terms, so it reaches K far beyond the 3^(K+1) enumeration.
"""
import numpy as np, sys

print(f"{'K':>4} {'L':>10} {'Err/L at k0 = R':>18}")
for K in (6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30):
    L = max(1, int(round(1.5 ** K)))
    k0 = L
    tot = 0.0
    CH = 1 << 20
    s = 0
    while s < L:
        e = min(s + CH, L)
        k = np.arange(k0 + s, k0 + e, dtype=np.float64)
        F = np.ones_like(k)
        for i in range(K + 1):
            F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
        tot += float(F.sum())
        s = e
    err = ((2.0 ** (K + 1)) * tot - L) / L
    print(f"{K:>4} {L:>10} {err:>+18.6f}")
    sys.stdout.flush()
