"""Vectorised search for a positive Cov(w_e,w_f) in FK(q<1) with arbitrary edge weights."""
import numpy as np, math, sys, time
from fk_lib import comps
from graphs_iso import connected_iso

def build(n, edges):
    m=len(edges); N=1<<m
    B=((np.arange(N)[:,None] >> np.arange(m)[None,:]) & 1).astype(np.float64)
    kk=np.array([comps(n,edges,x) for x in range(N)], dtype=np.float64)
    return B, kk, m, N

def cov_np(B, kk, t, u, i, j):
    p=1.0/(1.0+np.exp(-t))
    lp=np.log(p); lq=np.log1p(-p)
    s = kk*u + B@lp + (1.0-B)@lq
    s -= s.max()
    w = np.exp(s)
    Z=w.sum()
    bi=B[:,i]; bj=B[:,j]
    Ni=(w*bi).sum(); Nj=(w*bj).sum(); Nij=(w*bi*bj).sum()
    return Nij/Z-(Ni/Z)*(Nj/Z)

def hill(B,kk,m,i,j,restarts,iters,rng,ulo,uhi):
    best=-1e18; arg=None
    for _ in range(restarts):
        t=rng.uniform(-3,3,size=m); u=rng.uniform(max(ulo,-6.0), min(uhi,3.0))
        cur=cov_np(B,kk,t,u,i,j); step=1.0
        for _it in range(iters):
            imp=False
            for idx in range(m+1):
                for d in (step,-step):
                    if idx<m:
                        t[idx]+=d; v=cov_np(B,kk,t,u,i,j)
                        if v>cur+1e-15: cur=v; imp=True
                        else: t[idx]-=d
                    else:
                        nu=u+d
                        if nu<ulo or nu>uhi: continue
                        v=cov_np(B,kk,t,nu,i,j)
                        if v>cur+1e-15: u=nu; cur=v; imp=True
            if not imp:
                step*=0.5
                if step<1e-5: break
        if cur>best: best=cur; arg=(t.copy(),u)
    return best,arg

def run(nmax=6, mmax=9, restarts=6, iters=200, ulo=-12.0, uhi=-1e-6, seed=11, tag="q<1"):
    rng=np.random.default_rng(seed)
    worst=(-1e18,None); t0=time.time(); ng=0; npairs=0
    for n in range(2,nmax+1):
        for edges in connected_iso(n, mmax=mmax):
            B,kk,m,N=build(n,edges); ng+=1
            for i in range(m):
                for j in range(i+1,m):
                    npairs+=1
                    v,arg=hill(B,kk,m,i,j,restarts,iters,rng,ulo,uhi)
                    if v>worst[0]: worst=(v,(n,tuple(edges),i,j,arg))
    print("[%s] graphs %d  pairs %d  time %.1fs"%(tag,ng,npairs,time.time()-t0))
    print("   MAX Cov found: %.6g"%worst[0])
    print("   witness:", worst[1][:4] if worst[1] else None)
    if worst[1] is not None:
        t,u=worst[1][4]
        print("   p =", list(1/(1+np.exp(-t))), " q =", math.exp(u))
    return worst

if __name__=="__main__":
    mode=sys.argv[1] if len(sys.argv)>1 else "real"
    nmax=int(sys.argv[2]) if len(sys.argv)>2 else 6
    mmax=int(sys.argv[3]) if len(sys.argv)>3 else 9
    if mode=="control":
        run(nmax=nmax,mmax=mmax,restarts=3,iters=120,ulo=1e-6,uhi=3.0,tag="POSITIVE CONTROL q>1")
    else:
        run(nmax=nmax,mmax=mmax,tag="q<1")
