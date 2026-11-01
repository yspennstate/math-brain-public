try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys
rng=np.random.default_rng(9)
def peak(Qv,bins):
    h,e=np.histogram(Qv,bins=bins); w=e[1]-e[0]; return h.max()/(len(Qv)*w)
def build(n,eps,sign):
    A=np.zeros((n,n)); c=1/np.sqrt(n-1)
    A[0,1:]=c; A[1:,0]=c                      # star: eigenvalues +-1
    r=rng.standard_normal(n); r[0]=0; a=np.zeros(n); a[1:]=1
    r-=r@a/(a@a)*a; r/=np.linalg.norm(r)      # r orthogonal to hub row and to e_1
    A+=sign*np.outer(r,r)
    G=rng.standard_normal((n,n)); A+=eps*(G+G.T)/np.sqrt(2*n)
    return A
for n in [30,120]:
  for eps in [0.0,0.02,0.1]:
    for sign in [1,-1]:
      A=build(n,eps,sign); ev=np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
      for law in ['unif','spread']:
        S=2_000_000
        if law=='unif': X=rng.uniform(-.5,.5,(S,n))
        else:
            Nint=5; w=1.0/Nint; st=np.sort(rng.uniform(0,6,(n,Nint)),axis=1)
            X=st[np.arange(n),rng.integers(0,Nint,(S,n))]+rng.uniform(0,w,(S,n))
        Qv=np.einsum('ij,jk,ik->i',X,A,X)
        lo,hi=np.quantile(Qv,[0.001,0.999]); span=hi-lo
        pk=[peak(Qv,int(b*span)) for b in (20,80)]
        print(f"n={n:3d} eps={eps:4.2f} sign={sign:+d} |lam|top3={ev[:3].round(2)} {law:6s} peak(bin 1/20,1/80)={pk[0]:.3f},{pk[1]:.3f}",flush=True)
