# alpha_3: maximise lam = min_{ijk} P_{ij,k} subject to V NON-REGULAR.
# Certificate used: EVERY fixed point of V in S^2 has a tangent eigenvalue of modulus > 1
# (then no trajectory converges, except the countably many that land on a fixed point).
import numpy as np
np.seterr(all='ignore')
PAIRS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
MULT=np.array([1.,2.,2.,1.,2.,1.])
I=np.array([p[0] for p in PAIRS]); J=np.array([p[1] for p in PAIRS])
def V(P,x):
    return (MULT*x[I]*x[J])@P
def Jac(P,x):
    # Jkl = 2 sum_i P_{il,k} x_i
    M=np.zeros((3,3))
    for idx,(i,j) in enumerate(PAIRS):
        for k in range(3):
            M[k,j]+=P[idx,k]*x[i]
            M[k,i]+=P[idx,k]*x[j]
    return M
def tangent_eigs(P,x):
    M=Jac(P,x); ev=np.linalg.eigvals(M)
    # drop the eigenvalue equal to 2 (left eigenvector (1,1,1))
    k=np.argmin(np.abs(ev-2.0))
    return np.delete(ev,k)
def fixed_points(P,rng,tries=60):
    pts=[]
    for _ in range(tries):
        x=rng.dirichlet(np.ones(3))
        for _ in range(200):
            F=V(P,x)-x
            Mt=Jac(P,x)-np.eye(3)
            # solve on the simplex: append constraint sum dx = 0
            A=np.vstack([Mt,np.ones(3)]); b=np.concatenate([-F,[0.0]])
            try: dx,*_=np.linalg.lstsq(A,b,rcond=None)
            except Exception: break
            x=x+dx
            if not np.all(np.isfinite(x)): break
            if np.max(np.abs(dx))<1e-14: break
        if np.all(np.isfinite(x)) and x.min()>-1e-9 and abs(x.sum()-1)<1e-8:
            x=np.clip(x,0,None); x=x/x.sum()
            if np.max(np.abs(V(P,x)-x))<1e-10:
                if not any(np.max(np.abs(x-q))<1e-7 for q in pts): pts.append(x)
    return pts
def nonregular(P,rng):
    fps=fixed_points(P,rng)
    if not fps: return False,0.0   # unreliable
    r=min(max(abs(tangent_eigs(P,x))) for x in fps)
    return r>1.0+1e-9, r
def mk(Q,lam): return lam+(1-3*lam)*Q
rng=np.random.default_rng(4242)
def best_at(lam, restarts=400, steps=1200):
    bs=-1; bQ=None
    for _ in range(restarts):
        Q=rng.dirichlet(np.ones(3)*0.4,size=6)
        ok,r=nonregular(mk(Q,lam),rng)
        if r>bs: bs,bQ=r,Q.copy()
        if ok: return True,r,Q
    cur,cs=bQ,bs
    for k in range(steps):
        sc=0.35*(1-k/steps)+0.02
        Q=np.abs(cur+rng.normal(0,sc,size=(6,3))); Q=Q/Q.sum(1,keepdims=True)
        ok,r=nonregular(mk(Q,lam),rng)
        if r>cs: cs,cur=r,Q.copy()
        if ok: return True,r,Q
    return False,cs,cur
lo,hi=0.0,1/3.
bestP=None
for it in range(20):
    lam=(lo+hi)/2
    ok,r,Q=best_at(lam)
    print(f"lam={lam:.9f}  min-over-fixed-points spectral radius={r:.6f}  nonregular={ok}",flush=True)
    if ok: lo=lam; bestP=mk(Q,lam)
    else: hi=lam
print("LOWER BOUND for alpha_3 (largest lam with a certified non-regular QSO):",lo)
if bestP is not None:
    np.save('e0065_m3_bestP_eig.npy',bestP)
    print(np.array2string(bestP,precision=9)); print("min entry",bestP.min())
