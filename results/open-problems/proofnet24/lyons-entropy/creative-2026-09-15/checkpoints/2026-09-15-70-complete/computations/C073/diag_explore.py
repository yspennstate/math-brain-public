import numpy as np
from scipy.optimize import minimize
from time import time
rng=np.random.default_rng(73)
for n in [3,4,5,6]:
 masks=np.arange(1<<n);X=((masks[:,None]>>np.arange(n))&1);sg=2*X-1;flips=np.array([masks^(1<<i) for i in range(n)])
 pairs=[]
 for i in range(n):
  for j in range(i):
   inds=masks[((masks&(1<<i))==0)&((masks&(1<<j))==0)]
   pairs.append((i,j,inds,inds^(1<<i),inds^(1<<j),inds^(1<<i)^(1<<j)))
 def mat(v):
  p=np.exp(v-v.max());p=np.r_[p,p[::-1]];p/=p.sum();der=sg*(p[:,None]+p[flips].T);J=der.T@(der/p[:,None]);C=np.zeros_like(J)
  for i,j,ids,idb,idc,ide in pairs:
   d,b,c,e=p[ids],p[idb],p[idc],p[ide];C[i,j]=C[j,i]=np.sum((d+b+c+e)*np.log(b*c/(d*e)))
  return J-C,p
 def f(v):
  M,p=mat(v);return np.linalg.eigvalsh(M)[0]
 for t in range(6):
  v=rng.normal(0,2,1<<(n-1));res=minimize(f,v,method='BFGS',options={'maxiter':120});M,p=mat(res.x)
  print(n,t,res.fun,res.success,flush=True)
  if res.fun<3.999:print(p.tolist(),flush=True);break
