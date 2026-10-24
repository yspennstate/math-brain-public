# Value iteration in the Berg-Dorsman-Harchol-Balter model: class-i departure rate = min(a_i,x_i) s_i(max(1,a_i/x_i)),
# s_i(k)=k^{p_i}, p1<p2 (so s1<=s2 everywhere, equal below one core). Checks the two claims of the memo:
#   (i)  V(x+e2) <= V(x+e1)  (Delta1 >= Delta2)   (ii) largest optimal a1 >= GREEDY* a1 in every state.
import numpy as np, itertools
def solve(p1,p2,lam1,lam2,n=4,N=50,A=161,alpha=0.0,iters=30000):
    s1=lambda k:np.minimum(k,k**p1); s2=lambda k:np.minimum(k,k**p2)
    acts=np.linspace(0,n,A)
    X1,X2=np.meshgrid(np.arange(N+1),np.arange(N+1),indexing='ij')
    r1=np.where(X1[...,None]>0, X1[...,None]*s1(acts[None,None,:]/np.maximum(X1[...,None],1)),0.0)
    r2=np.where(X2[...,None]>0, X2[...,None]*s2((n-acts)[None,None,:]/np.maximum(X2[...,None],1)),0.0)
    thr=r1+r2; Lam=lam1+lam2+thr.max()+1.0; V=np.zeros((N+1,N+1)); cost=(X1+X2).astype(float)
    def shifts(V):
        Vup1=np.empty_like(V); Vup1[:-1,:]=V[1:,:]; Vup1[-1,:]=V[-1,:]
        Vup2=np.empty_like(V); Vup2[:,:-1]=V[:,1:]; Vup2[:,-1]=V[:,-1]
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
out=[]
for (p1,p2,l1,l2,al) in [(0.5,0.75,0.5,0.5,0.0),(0.5,0.75,0.0,0.0,0.0),(0.3,0.9,1.0,1.0,0.0),(0.5,0.75,1.5,1.5,0.0),(0.6,0.7,0.4,1.4,0.0),(0.5,0.75,0.5,0.5,0.5),(0.2,0.99,2.0,0.5,0.0)]:
    V,Q,thr,acts,it=solve(p1,p2,l1,l2,alpha=al)
    N=V.shape[0]-1; tol=1e-9
    om=np.array([[acts[np.flatnonzero(Q[i,j]<=Q[i,j].min()+tol).max()] for j in range(N+1)] for i in range(N+1)])
    gs=np.array([[acts[np.flatnonzero(thr[i,j]>=thr[i,j].max()-tol).max()] for j in range(N+1)] for i in range(N+1)])
    D1=np.full((N+1,N+1),np.nan); D2=np.full((N+1,N+1),np.nan)
    D1[1:,:]=V[1:,:]-V[:-1,:]; D2[:,1:]=V[:,1:]-V[:,:-1]
    K=25; msk=(np.add.outer(np.arange(N+1),np.arange(N+1))<=K); msk[0,:]=False; msk[:,0]=False
    print(f"p=({p1},{p2}) lam=({l1},{l2}) alpha={al} it={it} | region x1+x2<={K}, x1,x2>=1 ({msk.sum()} states): "
          f"min(D1-D2)={np.nanmin((D1-D2)[msk]):+.3e}  min(D2)={np.nanmin(D2[msk]):+.3e}  min(OPTmax-GREEDY*)={np.min((om-gs)[msk]):+.3f}  "
          f"OPT>GREEDY* in {((om>gs+1e-9)&msk).sum()} states, equal in {((np.abs(om-gs)<=1e-9)&msk).sum()}")
    print("   OPT a1 (rows x1=1..4, cols x2=1..4):\n",np.round(om[1:5,1:5],3),"\n   GREEDY* a1:\n",np.round(gs[1:5,1:5],3))
