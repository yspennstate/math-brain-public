import numpy as np,itertools
from scipy.optimize import minimize

def E(v):
 v=np.maximum(v,1e-300);return -np.dot(v,np.log(v))
for m in [5,6,7,8]:
 sets=list(itertools.combinations(range(m),2));eps=np.array(list(itertools.product([-1,1],repeat=m)))
 W=np.array([np.prod(eps[:,S],axis=1) for S in sets]).T
 def gain(x):
  x=x/np.linalg.norm(x);return E(abs(W@x)**2/2**m)-E(abs(x)**2)
 best=(1,None)
 rng=np.random.default_rng(m)
 for j in range(5):
  x=np.ones(len(sets))+.1*rng.normal(size=len(sets)) if j==0 else rng.normal(size=len(sets))
  r=minimize(gain,x,method='BFGS',options={'maxiter':1000,'gtol':1e-9})
  if r.fun<best[0]:best=(r.fun,r.x/np.linalg.norm(r.x))
 print(m,best,flush=True)
