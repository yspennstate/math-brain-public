import numpy as np,json
from scipy.optimize import minimize
from stratum import *
rng=np.random.default_rng(771)
for r in [0,1e-3,.01,.1,.25,.5,.75,1]:
 best=(1e9,None)
 for k in range(300):
  th=rng.uniform(-np.pi,np.pi,5);a=tmax(r,frame(th))*.8
  def obj(x):return ratio(closed(x[5],r*x[5],frame(x[:5])))
  def con(x):
   a=x[5];U=frame(x[:5]);lam,G,Pi,L,z=matrices(a,r*a,U)
   return np.r_[z,lam-a,sum(closed(a,r*a,U)[:3])-1e-8]
  re=minimize(obj,np.r_[th,a],method='SLSQP',bounds=[(-4*np.pi,4*np.pi)]*5+[(1e-7,1)],constraints={'type':'ineq','fun':con},options={'maxiter':400,'ftol':1e-12})
  if min(con(re.x))>=-1e-9 and re.fun<best[0]:best=(re.fun,re.x)
 print('r',r,'best',best[0],'a',best[1][-1],flush=True)
 np.savez('region_'+str(r)+'.npz',x=best[1],r=r)
