"""
Numerical check of the geometric generalizations:
  III.A rectangular fixed excess r:  M_m^{(r)} = min_{|T|=m+r} sigma_min(A_T)  ->  base h(gamma)/(d_F (r+1))
  III.B k-th smallest singular value: M_m[k] = min_{|T|=m} sigma_{m-k+1}(A_T)  ->  base h(gamma)/(d_F k^2)
Real and complex Gaussian, full enumeration, gamma=2 (N=2m).  Finite-m, so expect the empirical
(1/m)log to sit ABOVE the asymptote (the o(m) correction is large) but with the right ordering and trend:
square (-log4) < rectangular r=1 (-log4/2) and < k=2 (-log4/4) etc.  Run: python verify_geometric.py
"""
import numpy as np
from itertools import combinations
from math import log
rng=np.random.default_rng(20260628)
def rg(s): return rng.standard_normal(s)
def cg(s): return (rng.standard_normal(s)+1j*rng.standard_normal(s))/np.sqrt(2)
def hgamma(g): return g*log(g)-(g-1)*log(g-1)

print("="*72)
print("III.A  Rectangular fixed excess r:  target base = -h(2)/(d_F (r+1)),  N=2m")
print("="*72)
for name,gen,d in [("real",rg,1),("complex",cg,2)]:
    for r in [0,1,2]:
        tgt=-hgamma(2.0)/(d*(r+1))
        print(f"  {name} r={r}: target -h(2)/(d_F*{r+1}) = {tgt:+.4f}")
        for m in [5,6,7]:
            N=2*m; subs=[list(S) for S in combinations(range(N),m+r)]
            tr=200
            vals=[]
            for _ in range(tr):
                A=gen((N,m))
                Mm=min(np.linalg.svd(A[S],compute_uv=False)[-1] for S in subs)  # m-th s.v. of (m+r)x m
                vals.append(log(Mm)/m)
            v=np.array(vals)
            print(f"      m={m}: (1/m)log M_m^(r) = {v.mean():+.4f}  (gap {v.mean()-tgt:+.4f})")

print("="*72)
print("III.B  k-th smallest singular value:  target base = -h(2)/(d_F k^2),  N=2m-1")
print("="*72)
for name,gen,d in [("real",rg,1),("complex",cg,2)]:
    for k in [1,2,3]:
        tgt=-hgamma(2.0)/(d*k*k)
        print(f"  {name} k={k}: target -h(2)/(d_F*{k*k}) = {tgt:+.4f}")
        for m in [5,6,7]:
            if k>m: continue
            N=2*m-1; subs=[list(S) for S in combinations(range(N),m)]
            tr=200
            vals=[]
            for _ in range(tr):
                A=gen((N,m))
                # k-th smallest singular value = sigma_{m-k+1} = svd[-k]
                Mm=min(np.linalg.svd(A[S],compute_uv=False)[-k] for S in subs)
                vals.append(log(Mm)/m)
            v=np.array(vals)
            print(f"      m={m}: (1/m)log M_m[k] = {v.mean():+.4f}  (gap {v.mean()-tgt:+.4f})")
print("DONE.  (Ordering and trend matter; small-m gaps are the expected o(m) finite-size correction.)")
