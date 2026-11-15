"""Full Hessian restricted to a fixed simultaneous eigenbasis."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,json,time,resource
from pathlib import Path
from scipy.optimize import minimize
from scipy.special import expit
from dpp import random_unitary,spectral,hessian,stats
rng=np.random.default_rng(33330);rows=[];start=time.time()
def eval_lam(u,lam):
 q=spectral(u,lam);b=np.array([np.outer(v,v.conj()) for v in u.T]);h=hessian(q,b);e,v=np.linalg.eigh(h)
 a=spectral(u,v[:,-1]);return e[-1],q,a
for n in (3,4,5,6,8):
 for cx in (False,True):
  vals=[];best=-np.inf;count=600 if n<8 else 150
  for it in range(count):
   u=random_unitary(rng,n,cx)
   if it%3==0:lam=rng.uniform(.001,.999,n)
   elif it%3==1:
    eps=10**rng.uniform(-6,-1,n);lam=np.where(rng.random(n)<.5,eps,1-eps)
   else:
    center=rng.uniform(.05,.95);lam=center+10**rng.uniform(-6,-1)*(rng.random(n)-.5)
   value,q,a=eval_lam(u,lam);vals.append(value)
   if value>best:best=value;np.savez('data/commuting_n%d_%s.npz'%(n,cx),Q=q,A=a,U=u,lambda_=lam,value=value)
  row=dict(n=n,field='complex' if cx else 'real',trials=count,min_curvature=float(min(vals)),max_curvature=float(max(vals)),median_curvature=float(np.median(vals)))
  rows.append(row);print(json.dumps(row),flush=True)
# Fixed eigenbasis optimization, including Fourier matrices which have singular |U|^2.
for n in (3,4,6):
 vals=[];calls=[0];best=[-np.inf,None,None,None,None]
 for kind in ('haar_real','haar_complex','fourier'):
  u=random_unitary(rng,n,kind=='haar_complex') if kind!='fourier' else np.fft.fft(np.eye(n))/np.sqrt(n)
  def objective(x):
   lam=.0001+.9998*expit(x);value,q,a=eval_lam(u,lam);calls[0]+=1
   if value>best[0]:best[:]=[value,q,a,u.copy(),lam]
   return -value
  res=minimize(objective,rng.normal(size=n)*2,method='Nelder-Mead',options=dict(maxfev=1800,xatol=1e-8,fatol=1e-11));vals.append(-res.fun)
 row=dict(n=n,field='mixed',family='spectral_optimization',restarts=3,evaluations=calls[0],max_curvature=float(max(vals)),results=vals)
 rows.append(row);np.savez('data/commuting_opt_n%d.npz'%n,Q=best[1],A=best[2],U=best[3],lambda_=best[4],value=best[0]);print(json.dumps(row),flush=True)
Path('data/commuting_search.json').write_text(json.dumps(dict(seed=33330,rows=rows,elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2)+'\n')
