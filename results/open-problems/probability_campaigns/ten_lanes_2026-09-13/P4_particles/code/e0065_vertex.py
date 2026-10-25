# alpha_m via the "vertex ansatz": P_{ij,.} = lam*1 + (1-m*lam) e_{sigma(ij)}.
# For m=2 this family contains the exact extremal operator, so it is a positive control.
import numpy as np, itertools, math, sys
np.seterr(all='ignore')
def pairs(m): return [(i,j) for i in range(m) for j in range(i,m)]
def mults(m): return np.array([1.0 if i==j else 2.0 for i,j in pairs(m)])
def orbit_nonregular(P, m, iters=4000, tail=400, tol=1e-9):
    PR=pairs(m); MU=mults(m)
    I=np.array([p[0] for p in PR]); J=np.array([p[1] for p in PR])
    starts=[np.eye(m)[k] for k in range(m)]
    rng=np.random.default_rng(0)
    starts+= [rng.dirichlet(np.ones(m)) for _ in range(9)]
    starts+= [np.ones(m)/m]
    worst=0.0
    for x0 in starts:
        x=x0.copy()
        for _ in range(iters):
            c=MU*x[I]*x[J]; x=c@P; s=x.sum()
            if not np.isfinite(s) or s<=0: return True,np.inf
            x=x/s
        lo=x.copy(); hi=x.copy()
        for _ in range(tail):
            c=MU*x[I]*x[J]; x=(c@P); x=x/x.sum()
            lo=np.minimum(lo,x); hi=np.maximum(hi,x)
        worst=max(worst,(hi-lo).sum())
        if worst>tol*100: break
    return worst>1e-7, worst
def build(m, sig, lam):
    PR=pairs(m); P=np.full((len(PR),m), lam)
    for idx,k in enumerate(sig): P[idx,k]+= 1-m*lam
    return P
def best_lam(m, sig, tol=1e-12):
    lo,hi=0.0,1.0/m
    if not orbit_nonregular(build(m,sig,0.0),m)[0]: return 0.0
    for _ in range(50):
        mid=(lo+hi)/2
        if orbit_nonregular(build(m,sig,mid),m)[0]: lo=mid
        else: hi=mid
        if hi-lo<tol: break
    return lo
for m in (2,3):
    PR=pairs(m); best=(-1,None)
    for sig in itertools.product(range(m),repeat=len(PR)):
        L=best_lam(m,sig)
        if L>best[0]: best=(L,sig); print(f"  m={m} sigma={sig} lam={L:.10f}",flush=True)
    print(f"m={m}: VERTEX-ANSATZ MAX lam = {best[0]:.12f}  sigma={best[1]}",flush=True)
    if m==2: print("   control target (3-sqrt7)/4 =",(3-math.sqrt(7))/4)
