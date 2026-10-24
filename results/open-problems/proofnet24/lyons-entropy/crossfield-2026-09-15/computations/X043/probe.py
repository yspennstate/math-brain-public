import numpy as np,itertools
from scipy.optimize import minimize

def entropy(p):
 p=p[p>0];return -p@np.log(p)
for m in [2,3,4,5,6,8]:
 y=np.array(list(itertools.product([0,1],repeat=m)))
 rng=np.random.default_rng(100+m)
 for t in [.01,.05,.15,.25,.35,.5]:
  mu=t**y.sum(axis=1)*(1-t)**(m-y.sum(axis=1));z=(y-t)/np.sqrt(t*(1-t));W=np.sqrt(mu)[:,None]*z
  def gain(x):
   c=x/np.linalg.norm(x);return entropy((W@c)**2)-entropy(c*c)
  candidates=[np.ones(m),np.array([1.,-1.]+[0.]*(m-2))]+[rng.normal(size=m) for i in range(4)]
  best=min((minimize(gain,x,method='BFGS',options={'gtol':1e-8,'maxiter':300}) for x in candidates),key=lambda r:r.fun)
  print(m,t,best.fun,np.round(best.x/np.linalg.norm(best.x),4).tolist(),flush=True)
