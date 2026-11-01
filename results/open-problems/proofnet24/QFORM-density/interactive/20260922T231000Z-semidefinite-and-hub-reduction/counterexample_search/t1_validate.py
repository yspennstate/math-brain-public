try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time
from lib import *
t0=time.time()
# 1. separable: X1^2+X2^2+X3^2 uniform: p(s)=2 pi sqrt(s) for s<=1/4
A=np.eye(3); laws=[U()]*3
m,se=fibre_density(A,laws,[0.05,0.1,0.25],N=200000)
print("diag E2", np.round(m,4), np.round(se,4), "exact", np.round(2*np.pi*np.sqrt([0.05,0.1,0.25]),4), flush=True)
# 2. star + rank one, 30 leaves
rng=np.random.default_rng(5); n1=30; n=n1+1
Qm,_=np.linalg.qr(rng.normal(size=(n1,2))); w,v=Qm[:,0],Qm[:,1]
A=np.zeros((n,n)); A[0,1:]=w; A[1:,0]=w; A[1:,1:]+=np.outer(v,v)
laws=[U()]*n
sv=[-0.2,-0.05,0.0,0.05,0.15,0.3]
m1,s1=hub_density(A,laws,0,sv,N=1000000)
print("star E1", np.round(m1,4), np.round(s1,4), time.time()-t0, flush=True)
m2,s2=fibre_density(A,laws,sv,N=100000)
print("star E2", np.round(m2,4), np.round(s2,4), time.time()-t0, flush=True)
ph,ps=hist_density(A,laws,sv,[0.02,0.005],N=4000000)
print("star hist w=.02", np.round(ph[:,0],3), " w=.005", np.round(ph[:,1],3), "+-", np.round(ps[:,1],3), time.time()-t0, flush=True)
print("eig", np.round(np.sort(np.linalg.eigvalsh(A))[[0,1,-2,-1]],3))
