import numpy as np,math,json
from scipy.linalg import eigh_tridiagonal
from pathlib import Path
out=[]
for theta in [0,.3,.7]:
 for epsilon in [.05,.005,.0005]:
  a=.5;b=1-epsilon;p=a*(1-b);q=(1-a)*b;r=p/q;h=1-p-q;t=math.sqrt(p*q);K=200;ks=np.arange(K)
  f=theta**ks;logd=np.zeros(K)
  if theta:logd[1:]=np.cumsum(np.log1p(-theta**np.arange(1,K)))
  logpi=ks*math.log(r)-logd;logpi-=max(logpi);pi=np.exp(logpi);pi/=sum(pi)
  vals,vecs=eigh_tridiagonal(h+q*f,t*np.sqrt(1-theta**np.arange(1,K)))
  v=np.sqrt(pi)*(f-pi@f);weights=q*q*(vecs.T@v)**2;weights[vals>1-1e-10]=0
  fixed=[]
  for n in [1,3,10]:
   c=float(weights@(vals**(n-1)));limit=.25*(1-theta)*(.5+.5*theta)**(n-1)
   fixed.append(dict(n=n,covariance_over_holes=c/epsilon,limit=limit))
  obj=dict(theta=theta,epsilon=epsilon,fixed_distance=fixed)
  if theta:
   assert theta>math.sqrt(r)
   lam=h+q*theta+p/theta;W=p*q*(1-theta)*(1-r/theta**2);bound=r*(theta**(-2)-1)/(1-r/theta**2)
   ratios=[]
   for n in [1,10,100,1000]:
    ratio=float(np.sum(weights*(vals/lam)**(n-1))/W)
    assert 1-1e-10<=ratio<=1+bound+1e-10
    ratios.append(dict(n=n,relative_ratio=ratio))
   obj.update(uniform_relative_error_bound=bound,ratios=ratios)
  out.append(obj)
Path('rare_holes_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print('Rare-hole checks passed; saved',len(out),'cases')
