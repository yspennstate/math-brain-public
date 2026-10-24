"""Is the flatness of I_K a balance between drift and variance, and is that balance forced?

I_K = I_(K-1)(1 + r_K),  r_K = Phi(f_K)/I_(K-1),  so log I_K - log I_(K-1) = log(1 + r_K).
Since log(1+r) = r - r^2/2 + ..., a MEAN-ZERO r would give E[log(1+r)] = -E[r^2]/2 < 0 and I_K would
DECAY geometrically. The measured log-drift is essentially zero (+0.00009 per step), so E[r] must sit at
about +E[r^2]/2. Measure both and see how close that balance is - if it is exact it is a mechanism, if it
is approximate it is a coincidence of the range.
Light compute: one grid, factors accumulated in place.
"""
import numpy as np

N = 1 << 21
x = 1 + (np.arange(N) + 0.5) / N
f = lambda K: (1.5 ** K) / 3.0

KMAX = 26
P = np.ones(N)
I = []
for K in range(KMAX + 1):
    P *= 1.0 + np.cos(2 * np.pi * x * f(K))
    I.append(float(P.mean()))

r = [(I[K] - I[K-1]) / I[K-1] for K in range(1, KMAX + 1)]
lg = [np.log(I[K] / I[K-1]) for K in range(1, KMAX + 1)]

for lo in (6, 10, 14):
    rr = np.array(r[lo:]); ll = np.array(lg[lo:])
    Er, Er2 = rr.mean(), (rr**2).mean()
    print(f"over K = {lo+1}..{KMAX}  (n={len(rr)})")
    print(f"   E[r]        = {Er:+.6f}")
    print(f"   E[r^2]/2    = {Er2/2:+.6f}      difference {Er - Er2/2:+.6f}")
    print(f"   E[log(1+r)] = {ll.mean():+.6f}   (this is the log-drift per step)")
    print(f"   sd(r)       = {rr.std():.4f}")
    print()
print("If E[r] - E[r^2]/2 is much smaller than either term, the flatness is a balance;")
print("if it is comparable, the flatness is just what a short range happens to show.")
