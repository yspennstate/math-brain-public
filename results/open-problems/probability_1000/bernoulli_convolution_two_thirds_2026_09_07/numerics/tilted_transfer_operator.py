"""The tilted transfer operator for Mahler's map, and its leading eigenvalue.

T theta = (3/2) theta mod 1 on [0,1). Preimages of y: x = (2/3)(y + j) for j with x in [0,1) - so
j = 0 always (x = 2y/3), and j = 1 only when y < 1/2 (x = 2(y+1)/3 < 1). Two branches below 1/2, one
above: the map is NOT Markov, which is where its difficulty lives.

With weight e^phi = 1 + cos 2 pi x and |T'| = 3/2 everywhere,

    (L g)(y) = (2/3) [ (1 + cos 2 pi (2y/3)) g(2y/3)
                     + [y < 1/2] (1 + cos 2 pi (2(y+1)/3)) g(2(y+1)/3) ].

I_K is a Laplace average of Birkhoff sums, so its growth rate is the leading eigenvalue of L. Flatness of
I_K predicts that eigenvalue is 1. Compute it by power iteration on a grid, and refine to check.
"""
import numpy as np

def leading_eig(N, iters=300):
    y = (np.arange(N) + 0.5) / N
    x0 = 2 * y / 3.0
    x1 = 2 * (y + 1) / 3.0
    w0 = 1.0 + np.cos(2 * np.pi * x0)
    w1 = np.where(y < 0.5, 1.0 + np.cos(2 * np.pi * x1), 0.0)
    i0 = np.minimum((x0 * N).astype(int), N - 1)
    i1 = np.minimum((x1 * N).astype(int), N - 1)
    g = np.ones(N)
    lam = 1.0
    for it in range(iters):
        g2 = (2.0 / 3.0) * (w0 * g[i0] + w1 * g[i1])
        s = g2.mean()
        if s <= 0: return np.nan
        lam = s / g.mean()
        g = g2 / s
    return lam

print(f"{'grid N':>10} {'leading eigenvalue':>20}")
for e in (10, 12, 14, 16):
    N = 1 << e
    print(f"{N:>10} {leading_eig(N):>20.9f}", flush=True)
print()
print("If this converges to 1, the growth rate vanishes and boundedness is about the prefactor.")
