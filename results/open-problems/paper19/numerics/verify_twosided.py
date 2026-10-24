"""
Validate the two-sided base (III.C):  M = min over |R|=|C|=k of sigma_min(A_{R,C}),
A in F^{N x n}, N/k->gamma_R, n/k->gamma_C, base = -(h(gamma_R)+h(gamma_C))/d_F (entropy ADDS).
Square aspect gamma_R=gamma_C=2 (N=n=2k): real target -2 log4 = -2.7726.  Full enumeration over
row- and column-subsets.  Run: python verify_twosided.py
"""
import numpy as np
from itertools import combinations
from math import log
rng=np.random.default_rng(20260628)
def hgamma(g): return g*log(g)-(g-1)*log(g-1)
target=-2*hgamma(2.0)  # real, gamma_R=gamma_C=2

print(f"Two-sided base, real, gamma_R=gamma_C=2 (N=n=2k): target -(h(2)+h(2)) = {target:.4f}")
for k in [3,4,5,6]:
    N=2*k; n=2*k
    Rs=[list(S) for S in combinations(range(N),k)]
    Cs=[list(S) for S in combinations(range(n),k)]
    tr={3:400,4:150,5:40,6:8}[k]
    vals=[]
    for _ in range(tr):
        A=rng.standard_normal((N,n))
        best=min(np.linalg.svd(A[np.ix_(R,C)],compute_uv=False)[-1] for R in Rs for C in Cs)
        vals.append(log(best)/k)
    v=np.array(vals)
    print(f"  k={k}: (1/k)log M = {v.mean():+.4f}  (gap to target {v.mean()-target:+.4f})  "
          f"[#submatrices={len(Rs)*len(Cs)}, trials={tr}]")
print("DONE. Trend should approach -(h(2)+h(2)); compare to one-sided which approached -h(2)=-1.386.")
