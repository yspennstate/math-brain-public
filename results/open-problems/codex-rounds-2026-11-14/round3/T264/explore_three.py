"""Small angular-grid LP to identify candidate exposed atoms; not a proof."""
import os, resource, signal, time
assert os.environ['OMP_NUM_THREADS']=='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_CPU,(50,50))
import numpy as np
from scipy.optimize import linprog
N=8192
ph=2*np.pi*np.arange(N)/N
z=np.array([np.cos(ph),np.sin(ph)])
for th in (.4,.1,.02):
 a,b=np.cos(th/2),np.sin(th/2)
 X=np.array([[a,b],[a,-b],[0,1]])
 A=np.maximum(X@z,0)
 for tau in (-1,1):
  y=np.array([1,-1,tau])
  sol=linprog(-y,A_ub=np.concatenate((A.T,-A.T)),b_ub=np.ones(2*N),bounds=[(None,None)]*3,method='highs',options={'threads':1})
  assert sol.success,sol.message
  print('theta',th,'tau',tau,'Q',-sol.fun,'dual',sol.x)
  for j in np.flatnonzero(sol.ineqlin.marginals < -1e-7):
   print(' atom',ph[j%N],'sign',1 if j<N else -1,'coefficient',-sol.ineqlin.marginals[j])
print('RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
