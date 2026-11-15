"""Minimize the exterior certificate on decomposable unit bivectors."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,json
from scipy.optimize import minimize
from itertools import combinations
from dpp import stats
rng=np.random.default_rng(33341);rows=[]
for n in (5,6,8):
 z=np.load('data/wedge_n%d.npz'%n);r=z['R'];q=z['Q'];ix=np.array(list(combinations(range(n),2)));best=[1e9,None]
 def decode(x):
  a=x[:n]+1j*x[n:2*n];b=x[2*n:3*n]+1j*x[3*n:]
  v=a[ix[:,0]]*b[ix[:,1]]-a[ix[:,1]]*b[ix[:,0]]
  return v/np.linalg.norm(v),a,b
 def fun(x):
  v,a,b=decode(x);value=np.einsum('i,ij,j->',v.conj(),r,v,optimize=False).real
  if value<best[0]:best[:]=[value,x.copy()]
  return value
 vals=[]
 for it in range(15):
  res=minimize(fun,rng.normal(size=4*n),method='BFGS',options=dict(maxiter=300,gtol=1e-9));vals.append(float(res.fun))
 vv,a,b=decode(best[1]);a/=np.linalg.norm(a);b-=a*np.vdot(a,b);b/=np.linalg.norm(b);direction=(np.outer(a,a.conj())-np.outer(b,b.conj()))/np.sqrt(2)
 row=dict(n=n,starts=15,min_rayleigh=best[0],curvature=float(stats(q,direction)[1]),optimization_results=vals)
 rows.append(row);np.savez('data/decomposable_n%d.npz'%n,Q=q,A=direction,bivector=vv,value=best[0]);print(json.dumps(row),flush=True)
open('data/decomposable_search.json','w').write(json.dumps(rows,indent=2)+'\n')
