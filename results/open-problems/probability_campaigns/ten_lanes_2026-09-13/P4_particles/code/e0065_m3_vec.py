# alpha_3 = sup{ min_ijk P_ij,k : V on S^2 not regular }.
# Vectorised population search: for a floor lam, look for P = lam + (1-3lam)Q whose orbits
# do not converge.  Score = max over starts of the diameter of the orbit tail.
import numpy as np, sys, time
np.seterr(all='ignore')
PAIRS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
MULT=np.array([1.,2.,2.,1.,2.,1.])
I=np.array([p[0] for p in PAIRS]); Jj=np.array([p[1] for p in PAIRS])
STARTS=np.array([[1.,0,0],[0,1.,0],[0,0,1.],[1/3,1/3,1/3],[.5,.3,.2],[.2,.5,.3],
                 [.3,.2,.5],[.6,.3,.1],[.05,.9,.05],[.45,.45,.1],[.8,.1,.1],[.1,.1,.8]])
S=len(STARTS)
def scores(P, iters=2500, tail=250):
    """P: (K,6,3) -> (K,) max tail diameter over starts"""
    K=P.shape[0]
    X=np.broadcast_to(STARTS,(K,S,3)).copy()
    for _ in range(iters):
        C=MULT*X[:,:,I]*X[:,:,Jj]            # (K,S,6)
        X=np.einsum('ksp,kpc->ksc',C,P)
        X/=X.sum(2,keepdims=True)
    lo=X.copy(); hi=X.copy()
    for _ in range(tail):
        C=MULT*X[:,:,I]*X[:,:,Jj]
        X=np.einsum('ksp,kpc->ksc',C,P)
        X/=X.sum(2,keepdims=True)
        lo=np.minimum(lo,X); hi=np.maximum(hi,X)
    d=(hi-lo).sum(2)                          # (K,S)
    d=np.nan_to_num(d,nan=0.0,posinf=0.0)
    return d.max(1)
def mk(Q,lam): return lam+(1-3*lam)*Q
rng=np.random.default_rng(99)
def probe(lam, gens=26, K=1500):
    Q=rng.dirichlet(np.ones(3)*0.35,size=(K,6))
    s=scores(mk(Q,lam))
    best=s.max()
    for g in range(gens):
        if best>1e-5: break
        keep=np.argsort(s)[-K//5:]
        elite=Q[keep]
        sc=0.4*(1-g/gens)+0.01
        rep=np.repeat(elite,5,axis=0)[:K]
        Qn=np.abs(rep+rng.normal(0,sc,size=rep.shape)); Qn/=Qn.sum(2,keepdims=True)
        Qn[:len(elite)]=elite
        Q=Qn; s=scores(mk(Q,lam)); best=max(best,s.max())
    i=int(np.argmax(s))
    return best, Q[i]
t0=time.time()
lo,hi=0.0,1/3.
bestP=None
for it in range(18):
    lam=(lo+hi)/2
    b,Q=probe(lam)
    ok=b>1e-5
    print(f"[{time.time()-t0:7.1f}s] lam={lam:.9f} best tail-diameter={b:.3e} nonregular={ok}",flush=True)
    if ok: lo=lam; bestP=mk(Q,lam)
    else: hi=lam
print("ALPHA_3 LOWER BOUND (search):",lo,flush=True)
if bestP is not None:
    np.save('e0065_m3_bestP_vec.npy',bestP)
    print(np.array2string(bestP,precision=9)); print("min entry",bestP.min())
