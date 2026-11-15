"""Sign test of the nonlinear logarithmic term in Gu's rank-two extension."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from dpp import *
import json
rng=np.random.default_rng(33320);rows=[]
for n in (3,4,5,6):
 vals=[];curves=[];best=1e9
 for i in range(1000):
  q=random_kernel(rng,n,True,('uniform','extreme','projection')[i%3]);u=random_unitary(rng,n,True)
  a=spectral(u,np.r_[1,-10**rng.uniform(-1,1),np.zeros(n-2)]);a/=np.linalg.norm(a)
  p,m=probabilities(q);v=np.linalg.inv(m);c=np.einsum('sij,jk->sik',v,a)
  tr=np.trace(c,axis1=1,axis2=2).real;tr2=np.einsum('sij,sji->s',c,c).real
  term=np.sum(p*(tr*tr-tr2)*np.log(p));vals.append(term)
  curve=-np.sum(p*tr*tr)-term;curves.append(curve)
  if term<best:best=term;np.savez('data/ranktwo_term_n%d.npz'%n,Q=q,A=a,term=term,second=curve)
 row=dict(n=n,trials=len(vals),min_logarithmic_term=float(min(vals)),max_logarithmic_term=float(max(vals)),max_curvature=float(max(curves)),negative_log_terms=int(sum(x< -1e-9 for x in vals)))
 print(json.dumps(row),flush=True);rows.append(row)
open('data/ranktwo_probe.json','w').write(json.dumps(rows,indent=2)+'\n')
