"""Direct simulation of omega(A) = min over M-subsets of rows of sigma_min(A_S),
   A a (2M-1) x M standard real Gaussian matrix.  Tests omega = 4^{-M} * Theta~(1)."""
import numpy as np, itertools, math
from math import comb, log
rng = np.random.default_rng(11)

def omega(A, M):
    n = A.shape[0]
    best = np.inf
    for S in itertools.combinations(range(n), M):
        s = np.linalg.svd(A[list(S)], compute_uv=False)[-1]
        if s < best: best = s
    return best

print(" M   trials   median omega     median log4(omega)/M   median omega*4^M   #subsets")
for M in range(2, 11):
    tr = {2:4000,3:4000,4:3000,5:2000,6:1200,7:600,8:300,9:150,10:60}[M]
    vals = []
    for _ in range(tr):
        A = rng.standard_normal((2*M-1, M))
        vals.append(omega(A, M))
    v = np.array(vals)
    med = np.median(v)
    print(f"{M:2d} {tr:7d}   {med:.6e}      {math.log(med,4)/M:+.4f}            {med*4**M:8.3f}       {comb(2*M-1,M)}")
