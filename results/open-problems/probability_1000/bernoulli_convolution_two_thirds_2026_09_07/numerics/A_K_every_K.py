"""A_K at EVERY K, not every fourth - because a stride can manufacture a trend.

A_K = 2^(K+1) * (1/L) * sum_(k in [R, 2R)) F_K(k),  L = R = round((3/2)^K).
The paper quotes 0.0574, 0.0614, 0.0555, 0.0482, 0.0457, 0.0426 at K = 10, 14, 18, 22, 26, 30 and calls
that "bounded and slowly decreasing at a rate near R^-0.07". But the K = 12 value from another run is
0.0844, far above its neighbours, so the stride-4 subsample may be hiding the real variation. Measure the
full sequence and report what it actually does.
"""
import numpy as np, sys

def A(K):
    L = max(1, int(round(1.5 ** K))); k0 = L
    tot = 0.0; CH = 1 << 20; s = 0
    while s < L:
        e = min(s + CH, L)
        k = np.arange(k0 + s, k0 + e, dtype=np.float64)
        F = np.ones_like(k)
        for i in range(K + 1):
            F *= np.cos(np.pi * k * (2.0 ** i) / (3.0 ** (i + 1))) ** 2
        tot += float(F.sum()); s = e
    return (2.0 ** (K + 1)) * tot / L

vals = {}
print(f"{'K':>4} {'A_K':>12}")
for K in range(8, 29):
    v = A(K); vals[K] = v
    print(f"{K:>4} {v:>12.6f}"); sys.stdout.flush()

a = np.array([vals[K] for K in sorted(vals)])
ks = np.array(sorted(vals), float)
print()
print(f"min {a.min():.6f}  max {a.max():.6f}  ratio {a.max()/a.min():.2f}  mean {a.mean():.6f}")
sl, ic = np.polyfit(ks, np.log(a), 1)
print(f"log-linear fit over K = 8..28: slope {sl:+.5f} per K  (so A_K ~ R^{sl/np.log(1.5):+.4f})")
sl2, _ = np.polyfit(ks[::4], np.log(a[::4]), 1)
print(f"same fit on the stride-4 subsample:   slope {sl2:+.5f} per K  (R^{sl2/np.log(1.5):+.4f})")
