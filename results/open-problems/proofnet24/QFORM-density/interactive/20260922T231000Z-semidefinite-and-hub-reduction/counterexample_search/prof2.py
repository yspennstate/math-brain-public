import time, numpy as np
from lib import *
k=3; laws=[U()]+[GaussLaw()]*k
A=np.zeros((4,4)); A[0,1]=A[1,0]=1; A[2,2]=1
sv=np.linspace(-0.3,0.3,61)
t0=time.time(); m,se=fibre_density_v(A,laws,sv,N=20000); print("vec N=2e4 S=61:",round(time.time()-t0,2), m.max(), flush=True)
t0=time.time(); m2,se2=fibre_density(A,laws,sv[25:36],N=20000); print("old S=11:",round(time.time()-t0,2), np.abs(m2-m[25:36]).max(), flush=True)
# star 30 leaves check vs earlier
rng=np.random.default_rng(5); n1=30; n=n1+1
Qm,_=np.linalg.qr(rng.normal(size=(n1,2))); w,v=Qm[:,0],Qm[:,1]
A=np.zeros((n,n)); A[0,1:]=w; A[1:,0]=w; A[1:,1:]+=np.outer(v,v)
t0=time.time(); m,se=fibre_density_v(A,[U()]*n,[-0.2,-0.05,0.0,0.05,0.15,0.3],N=100000); print("star31 vec:",np.round(m,4),np.round(se,4),round(time.time()-t0,2),flush=True)
