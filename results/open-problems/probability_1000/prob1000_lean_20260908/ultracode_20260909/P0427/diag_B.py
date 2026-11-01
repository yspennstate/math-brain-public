import numpy as np
def solve(p1,p2,lam1,lam2,n=4,N=60,A=81,alpha=0.0,iters=20000,boundary='block'):
    s1=lambda k:k**p1; s2=lambda k:k**p2
    acts=np.linspace(0,n,A)
    X1,X2=np.meshgrid(np.arange(N+1),np.arange(N+1),indexing='ij')
    r1=np.where(X1[...,None]>0, X1[...,None]*s1(acts[None,None,:]/np.maximum(X1[...,None],1)),0.0)
    r2=np.where(X2[...,None]>0, X2[...,None]*s2((n-acts)[None,None,:]/np.maximum(X2[...,None],1)),0.0)
    thr=r1+r2; Lam=lam1+lam2+thr.max()+1.0; V=np.zeros((N+1,N+1)); cost=(X1+X2).astype(float)
    def shifts(V):
        Vup1=np.empty_like(V); Vup1[:-1,:]=V[1:,:]; Vup1[-1,:]=V[-1,:]
        Vup2=np.empty_like(V); Vup2[:,:-1]=V[:,1:]; Vup2[:,-1]=V[:,-1]
        if boundary=='extrap':   # linear extrapolation of V beyond the box instead of blocking
            Vup1[-1,:]=2*V[-1,:]-V[-2,:]; Vup2[:,-1]=2*V[:,-1]-V[:,-2]
        Vdn1=np.empty_like(V); Vdn1[1:,:]=V[:-1,:]; Vdn1[0,:]=V[0,:]
        Vdn2=np.empty_like(V); Vdn2[:,1:]=V[:,:-1]; Vdn2[:,0]=V[:,0]
        return Vup1,Vup2,Vdn1,Vdn2
    for it in range(iters):
        Vup1,Vup2,Vdn1,Vdn2=shifts(V)
        Q=cost[...,None]+lam1*Vup1[...,None]+lam2*Vup2[...,None]+r1*Vdn1[...,None]+r2*Vdn2[...,None]+(Lam-lam1-lam2-thr)*V[...,None]
        Vn=Q.min(axis=2)/(Lam+alpha)
        if alpha==0: Vn=Vn-Vn[0,0]
        if np.abs(Vn-V).max()<1e-12: V=Vn; break
        V=Vn
    Vup1,Vup2,Vdn1,Vdn2=shifts(V)
    Q=cost[...,None]+lam1*Vup1[...,None]+lam2*Vup2[...,None]+r1*Vdn1[...,None]+r2*Vdn2[...,None]+(Lam-lam1-lam2-thr)*V[...,None]
    return V,Q,thr,acts,it
for (p1,p2,l1,l2,al,bd) in [(0.3,0.7,0.5,0.5,0.0,'block'),(0.3,0.7,0.5,0.5,0.0,'extrap'),(0.3,0.7,0.5,0.5,1.0,'block'),(0.5,0.9,1.0,1.0,0.0,'block')]:
    V,Q,thr,acts,it=solve(p1,p2,l1,l2,alpha=al,boundary=bd)
    N=V.shape[0]-1
    tol=1e-9
    om=np.array([[acts[np.flatnonzero(Q[i,j]<=Q[i,j].min()+tol).max()] for j in range(N+1)] for i in range(N+1)])
    gs=np.array([[acts[np.flatnonzero(thr[i,j]>=thr[i,j].max()-tol).max()] for j in range(N+1)] for i in range(N+1)])
    D1=np.full((N+1,N+1),np.nan); D2=np.full((N+1,N+1),np.nan)
    D1[1:,:]=V[1:,:]-V[:-1,:]; D2[:,1:]=V[:,1:]-V[:,:-1]
    print(f"p=({p1},{p2}) lam=({l1},{l2}) alpha={al} boundary={bd} it={it}")
    for K in [10,20,30,40]:
        msk=(np.add.outer(np.arange(N+1),np.arange(N+1))<=K)
        m1=msk.copy(); m1[0,:]=False; m1[:,0]=False
        viol=(D1<D2-1e-9)&m1
        vo=(om<gs-1e-9)&m1
        print(f"  x1+x2<={K}: D1<D2 in {viol.sum()} states (worst {np.nanmin((D1-D2)[m1]):+.4f}); OPT<GREEDY* in {vo.sum()} states (worst {np.min((om-gs)[m1]):+.3f}); OPT>GREEDY* in {((om>gs+1e-9)&m1).sum()}")
    ii=np.argwhere((D1<D2-1e-9)&m1)
    if len(ii): 
        i,j=ii[0]; print("  first violation at",(i,j),"D1,D2=",D1[i,j],D2[i,j], " V row:",V[i-1:i+2,j-1:j+2])
    print("  V near origin:\n",np.round(V[:4,:4],4))
    print("  OPT a1 near origin:\n",np.round(om[:5,:5],3),"\n  GREEDY* a1:\n",np.round(gs[:5,:5],3))
