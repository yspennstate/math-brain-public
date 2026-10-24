import numpy as np,itertools,json
from pathlib import Path
rng=np.random.default_rng(352413)

def quantities(K):
 n=len(K); masks=np.arange(1<<n); X=((masks[:,None]>>np.arange(n))&1).astype(float)
 p=np.array([np.linalg.det(K-np.diag(1-x))*(-1)**int(n-x.sum()) for x in X]).real
 if p.min()<=0:return None
 deriv=np.empty((len(p),n))
 for i in range(n):deriv[:,i]=(2*X[:,i]-1)*(p+p[masks^(1<<i)])
 J=deriv.T@(deriv/p[:,None]);C=np.zeros_like(J)
 for i in range(n):
  for j in range(i):
   at=(masks&(1<<i)==0)&(masks&(1<<j)==0)
   d=p[at];b=p[(masks^(1<<i))[at]];c=p[(masks^(1<<j))[at]];e=p[(masks^(1<<i)^(1<<j))[at]]
   C[i,j]=C[j,i]=np.sum((d+b+c+e)*np.log(b*c/(d*e)))
 Sigma=-(abs(K)**2); np.fill_diagonal(Sigma,np.diag(K).real*(1-np.diag(K).real))
 return p,J,C,Sigma
worst={x:(1e9,None) for x in ['covariance','fisher','diagonal']}
for trial in range(4000):
 n=int(rng.integers(2,8));Q=np.linalg.qr(rng.normal(size=(n,n)))[0];ev=1/(1+np.exp(-rng.normal(0,rng.uniform(.2,8),n)));K=(Q*ev)@Q.T
 q=quantities(K)
 if q is None:continue
 p,J,C,Sigma=q
 for name,M in [('covariance',np.linalg.inv(Sigma)-C),('fisher',J-C),('diagonal',np.diag(np.diag(J))-np.abs(C-J+np.diag(np.diag(J))))]:
  val=np.linalg.eigvalsh(M)[0]
  if val<worst[name][0]:worst[name]=(float(val),K.tolist())
 if trial%500==0:print(trial,{name:v[0] for name,v in worst.items()},flush=True)
Path(__file__).with_name('search_result.json').write_text(json.dumps(worst,indent=2))
print({name:v[0] for name,v in worst.items()})
