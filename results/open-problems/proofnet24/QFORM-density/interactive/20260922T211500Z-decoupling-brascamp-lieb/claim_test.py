try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
rng=np.random.default_rng(11)
def psi_unif(tau):
    x=tau/2.0
    out=np.ones_like(x); nz=np.abs(x)>1e-12
    out[nz]=np.sin(x[nz])/x[nz]; return np.abs(out)
def psi_spread(tau,starts,w):
    N=starts.shape[-1]
    base=np.where(np.abs(tau)>1e-12,(np.exp(1j*tau*w)-1)/(1j*tau*N*w+1e-300),1.0)
    return np.abs(base*np.exp(1j*tau[...,None]*starts).sum(-1))
ts=np.geomspace(1,2000,28)
for law in ['unif','spread']:
  for n in [40,80,160]:
    R,_=np.linalg.qr(rng.standard_normal((n,3)))
    A3=R@np.diag([1.,1.,-1.])@R.T
    G=rng.standard_normal((n,n)); Bw=(G+G.T)/np.sqrt(2*n)
    I=np.arange(n//2); J=np.arange(n//2,n)
    if law=='spread':
        Nint=8; w=1.0/Nint; starts=np.sort(rng.uniform(0,12,(n,Nint)),axis=1)
    for eps in [0.0,0.1,0.3,1.0]:
        M=(A3+eps*Bw)[np.ix_(I,J)]
        S=20000
        # W = X - X' for X ~ law (coordinates J)
        if law=='unif':
            Wm=rng.uniform(-.5,.5,(S,len(J)))-rng.uniform(-.5,.5,(S,len(J)))
        else:
            def draw():
                idx=rng.integers(0,Nint,(S,len(J))); U=rng.uniform(0,w,(S,len(J)))
                return starts[J][np.arange(len(J)),idx]+U
            Wm=draw()-draw()
        Y=Wm@M.T   # S x |I|
        best=0; tb=None; vals=[]
        for t in ts:
            arg=2*t*Y
            if law=='unif': F=np.prod(psi_unif(arg),axis=1)
            else:
                F=np.ones(S)
                for ii,i in enumerate(I):
                    F*=psi_spread(arg[:,ii],starts[i],w)
            T=F.mean(); vals.append(T)
            if T*t**3>best: best=T*t**3; tb=t
        print(f"{law:6s} n={n:4d} eps={eps:4.1f}  max_t T(t)*t^3 = {best:9.3f} at t={tb:7.1f};  T(100)={vals[np.argmin(abs(ts-100))]:.2e}")
