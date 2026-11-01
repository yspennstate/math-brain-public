"""Exhaustive k=1 two-sided rate at N=12 to firm up rho_1 -> 2H(1/2)=1.386.
Also reports the finite-N sequence N=8,10,12 to show the approach.
"""
import itertools, time
import numpy as np


def subsets(N, n):
    return np.array(list(itertools.combinations(range(N), n)))


def rho1(N, ntr, seed0):
    n = N // 2
    idx = subsets(N, n)
    m = len(idx)
    out = []
    for t in range(ntr):
        rng = np.random.default_rng(seed0 + t)
        A = rng.normal(0, 1/np.sqrt(N), (N, N))
        R = A[idx, :]              # (m, n, N)
        B = R[:, :, idx]           # (m, n, m, n)
        B = np.transpose(B, (0, 2, 1, 3)).reshape(m*m, n, n)
        sv = np.linalg.svd(B, compute_uv=False)[:, -1].min()
        out.append(-np.log(sv)/N)
    return np.array(out)


H = np.log(2.0)
t0 = time.time()
for N, ntr in ((8, 12), (10, 8), (12, 4)):
    r = rho1(N, ntr, 5000+N)
    print(f"N={N}: rho_1 mean {r.mean():.3f} (2H={2*H:.3f})  values {np.round(r,3)}")
print(f"{time.time()-t0:.1f}s")
