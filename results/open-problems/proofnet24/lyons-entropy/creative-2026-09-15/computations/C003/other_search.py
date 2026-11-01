import numpy as np
rng=np.random.default_rng(544)
worst=1e9
for tr in range(20000):
 n=int(rng.integers(2,7));masks=np.arange(1<<n);X=((masks[:,None]>>np.arange(n))&1)
 p=np.exp(rng.normal(0,rng.uniform(.1,6),len(masks)));p/=p.sum()
 deriv=np.array([(2*X[:,i]-1)*(p+p[masks^(1<<i)]) for i in range(n)]).T;J=deriv.T@(deriv/p[:,None]);C=np.zeros_like(J)
 for i in range(n):
  for j in range(i):
   at=(masks&(1<<i)==0)&(masks&(1<<j)==0)
   d=p[at];b=p[(masks^(1<<i))[at]];c=p[(masks^(1<<j))[at]];e=p[(masks^(1<<i)^(1<<j))[at]]
   C[i,j]=C[j,i]=np.sum((d+b+c+e)*np.log(b*c/(d*e)))
 val=np.linalg.eigvalsh(J-C)[0]
 if val<worst:worst=val
 if val<-.01: print('negative',tr,n,val,p.tolist());break
else:print('no negatives, lowest',worst)
