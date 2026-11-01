import numpy as np
from explore import curvature

rng=np.random.default_rng(77183)
best=(0,None)
passed=0
for it in range(2000):
    z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    U,_=np.linalg.qr(z)
    e=1/(1+np.exp(-rng.normal(size=3)*4))
    K=(U*e)@U.conj().T
    p,_=curvature(K,np.arange(3))
    f=-np.log(p)
    c=np.array([f[6]-f[2]-f[4]+f[0],f[5]-f[1]-f[4]+f[0],f[3]-f[1]-f[2]+f[0]])
    tau=f[7]-f[6]-f[5]-f[3]+f[4]+f[2]+f[1]-f[0]
    M=np.diag(c)+tau*K
    delta=np.linalg.det(M).real
    if delta<1e-18 or abs(tau)<1e-8: continue
    g=np.array([np.prod(c+tau*np.array([s>>i&1 for i in range(3)])) for s in range(8)])
    var=p@(g-p@g)**2
    ratio=var/(tau*tau*delta)
    if ratio<=1: passed+=1
    if ratio>best[0]: best=(ratio,(it,e,K,tau,c,delta))
print('passed',passed,'of',it+1)
print('largest ratio',best)
