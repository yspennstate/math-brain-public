"""Second-exterior-power certificate for the nonlinear entropy term."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from dpp import *
from itertools import combinations
import json,time,resource
rng=np.random.default_rng(33340);rows=[];start=time.time()
def wedge_r(q):
 p,m=probabilities(q);v=np.linalg.inv(m);ix=np.array(list(combinations(range(len(q)),2)))
 i=ix[:,0];j=ix[:,1]
 w=v[:,i[:,None],i[None,:]]*v[:,j[:,None],j[None,:]]-v[:,i[:,None],j[None,:]]*v[:,j[:,None],i[None,:]]
 r=-np.einsum('s,sij->ij',p*np.log(p),w)
 return (r+r.conj().T)/2
for n in (3,4,5,6,8):
 vals=[];best=1e9;count=1000 if n<7 else 200
 for it in range(count):
  q=random_kernel(rng,n,True,('uniform','extreme','projection')[it%3]);r=wedge_r(q);e,u=np.linalg.eigh(r);vals.append(e[0])
  if e[0]<best:best=e[0];np.savez('data/wedge_n%d.npz'%n,Q=q,R=r,v=u[:,0],minimum=best)
 row=dict(n=n,trials=count,min_eigenvalue=float(min(vals)),max_min_eigenvalue=float(max(vals)),median_min_eigenvalue=float(np.median(vals)))
 rows.append(row);print(json.dumps(row),flush=True)
open('data/wedge_probe.json','w').write(json.dumps(dict(seed=33340,rows=rows,elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2)+'\n')
