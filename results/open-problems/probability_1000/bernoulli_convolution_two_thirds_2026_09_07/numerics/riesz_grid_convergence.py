"""Is the continuum integral converged, or is the agreement riding on quadrature error?

At K = 26 the fastest factor has (3/2)^26 = 16834 periods on [1,2], and a 2^22 grid gives only 111
points per period. Agreement with the discrete A_K improved to 3e-7 there, but that means nothing if
I_K itself is not converged. Refine the grid at fixed K and watch I_K settle - or not.
"""
import numpy as np, sys

def I(K, N, CH=1 << 22):
    acc = 0.0; done = 0
    while done < N:
        n = min(CH, N - done)
        x = 1.0 + (np.arange(done, done + n) + 0.5) / N
        P = np.ones_like(x)
        for m in range(K + 1):
            P *= 1.0 + np.cos(2 * np.pi * x * (1.5 ** m) / 3.0)
        acc += float(P.sum()); done += n
    return acc / N

for K in (20, 24, 26):
    per = 1.5 ** K
    print(f"K = {K}  ({per:.0f} periods of the fastest factor on [1,2])")
    prev = None
    for e in (21, 22, 23, 24):
        N = 1 << e
        v = I(K, N)
        d = "" if prev is None else f"   change {abs(v-prev):.2e}"
        print(f"   N = 2^{e} = {N:>10}  pts/period {N/per:>8.0f}   I_K = {v:.9f}{d}")
        prev = v
        sys.stdout.flush()
    print()
