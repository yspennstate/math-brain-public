# alpha_3 lower bound: for a fixed floor lam, is there a QSO on S^2 with all P_{ij,k} >= lam
# that is NOT regular?  Parametrise P = lam*1 + (1-3 lam) Q, rows of Q in the 2-simplex.
import numpy as np, sys
PAIRS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
MULT=np.array([1.,2.,2.,1.,2.,1.])
IDX_I=np.array([p[0] for p in PAIRS]); IDX_J=np.array([p[1] for p in PAIRS])
def step(P,x):
    c=MULT*x[IDX_I]*x[IDX_J]
    y=c@P
    s=y.sum()
    return y/s
STARTS=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.]),np.array([1/3,1/3,1/3]),
        np.array([.5,.3,.2]),np.array([.2,.5,.3]),np.array([.3,.2,.5]),np.array([.6,.3,.1]),
        np.array([.05,.9,.05]),np.array([.45,.45,.1])]
def score(P,iters=3000,tail=250):
    best=0.0
    for x0 in STARTS:
        x=x0.copy()
        for _ in range(iters): x=step(P,x)
        lo=x.copy(); hi=x.copy()
        for _ in range(tail):
            x=step(P,x); lo=np.minimum(lo,x); hi=np.maximum(hi,x)
        best=max(best,(hi-lo).sum())
        if best>1e-4: break
    return best
def mk(Q,lam): return lam+(1-3*lam)*Q
def search(lam, rng, restarts=250, steps=900):
    bs=0.0; bQ=None
    for _ in range(restarts):
        Q=rng.dirichlet(np.ones(3),size=6)
        s=score(mk(Q,lam))
        if s>bs: bs,bQ=s,Q.copy()
        if bs>1e-4: return bs,bQ
    # local refine
    cur=bQ if bQ is not None else rng.dirichlet(np.ones(3),size=6); cs=bs
    for k in range(steps):
        sc=0.3*(1-k/steps)+0.01
        Q=np.abs(cur+rng.normal(0,sc,size=(6,3))); Q=Q/Q.sum(1,keepdims=True)
        s=score(mk(Q,lam))
        if s>cs: cs,cur=s,Q.copy()
        if cs>1e-4: break
    return cs,cur
rng=np.random.default_rng(11)
lo,hi=0.0,1/3
bestQ=None
for it in range(22):
    lam=(lo+hi)/2
    s,Q=search(lam,rng)
    ok = s>1e-5
    print(f"lam={lam:.8f} score={s:.3e} nonregular={ok}",flush=True)
    if ok: lo=lam; bestQ=Q.copy()
    else: hi=lam
print("alpha_3 lower-bound estimate (largest lam with a non-regular example):",lo)
if bestQ is not None:
    P=mk(bestQ,lo); np.save('e0065_m3_bestP.npy',P)
    print(np.array2string(P,precision=8)); print("min entry",P.min())
