# E0065 / Problem 12: search for alpha_3 = sup{ min_{ijk} P_{ij,k} : V on S^2 NOT regular }
# A QSO on S^2 is 6 rows P_{ij,.} in S^2 (pairs 11,12,13,22,23,33).
import numpy as np, itertools, random, sys
PAIRS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
def apply(P,x):
    # P: (6,3)
    y=np.zeros(3)
    for idx,(i,j) in enumerate(PAIRS):
        c = x[i]*x[j] if i==j else 2*x[i]*x[j]
        y += c*P[idx]
    return y/y.sum()
def minentry(P): return P.min()
def nonregular(P, iters=20000, tail=400, tol=1e-8, starts=None):
    """True if some trajectory fails to converge."""
    if starts is None:
        starts=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.]),
                np.array([1/3,1/3,1/3]),np.array([.5,.3,.2]),np.array([.2,.5,.3]),
                np.array([.6,.2,.2]),np.array([.1,.1,.8])]
    for x0 in starts:
        x=x0.copy()
        for _ in range(iters-tail): x=apply(P,x)
        pts=[]
        for _ in range(tail):
            x=apply(P,x); pts.append(x.copy())
        pts=np.array(pts)
        if pts.max(0).sum()-pts.min(0).sum() > tol:   # orbit tail not a point
            return True
    return False
def project(P, lo):
    """clip to [lo,1-2lo] and renormalise rows to sum 1 keeping entries>=lo"""
    P=np.clip(P, lo, None)
    P=P/P.sum(1, keepdims=True)
    # after renormalisation entries can dip below lo; iterate
    for _ in range(60):
        if P.min()>=lo-1e-15: break
        P=np.clip(P,lo,None); P=P/P.sum(1,keepdims=True)
    return P

rng=np.random.default_rng(20260913)
best=(0.0,None)
LOG=[]
for trial in range(4000):
    # sample a random QSO, then binary-search the largest lo such that pushing the
    # operator toward the uniform row keeps it non-regular
    P=rng.dirichlet(np.ones(3),size=6)
    if not nonregular(P, iters=4000, tail=200): continue
    lo_hi=1/3.0; lo_lo=0.0
    # blend toward uniform: P(t) = (1-t)P + t*uniform ; min entry >= t/3
    # binary search largest t with nonregular
    a,b=0.0,1.0
    if not nonregular((1-0.0)*P+0.0/3, iters=4000, tail=200): continue
    for _ in range(28):
        t=(a+b)/2
        Q=(1-t)*P+t*np.ones((6,3))/3
        if nonregular(Q, iters=6000, tail=300): a=t
        else: b=t
    Q=(1-a)*P+a*np.ones((6,3))/3
    m=minentry(Q)
    if m>best[0] and nonregular(Q, iters=40000, tail=600, tol=1e-9):
        best=(m,Q.copy())
        LOG.append((trial,m))
        print("trial",trial,"min entry",m, flush=True)
print("BEST blend-search min entry:",best[0])
np.save('e0065_m3_best_blend.npy', best[1])
print(np.array2string(best[1],precision=8))
