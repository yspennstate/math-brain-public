import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from pathlib import Path
rng=np.random.default_rng(19103);start=time.time();out=[];localchecks=0;covchecks=0
for n in [2,3,4,8]:
 for sample in range(8):
  x=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n)
  lam,v=np.linalg.eig(x);v=v/np.linalg.norm(v,axis=0);vi=np.linalg.inv(v);kap=float(np.linalg.cond(v))
  S=np.kron(v.T,vi)
  mask=(~np.eye(n,dtype=bool)).reshape(-1,order='F');P=np.diag(mask.astype(float))
  cases=[('power_commutator',[(1,2,0),(-1,0,2)]),('nested_commutator',[(1,2,0),(-2,1,1),(1,0,2)]),('variable_leading_coefficient',[(1,2,1),(1,2,0),(1,1,0),(1,0,3)])]
  for name,terms in cases:
   weights=sum(c*lam[:,None]**r*lam[None,:]**s for c,r,s in terms)
   diag=np.diag(weights.reshape(-1,order='F'));B=diag@S
   Sigma=B@B.conj().T/n
   delta=float(np.min(np.abs(weights.reshape(-1,order='F')[mask])))
   floor=delta**2/(n*kap**2)
   mineig=float(np.linalg.eigvalsh(Sigma-floor*P)[0])
   assert mineig>=-1e-9
   direct=sum(c*np.kron(np.linalg.matrix_power(x,s).T,np.linalg.matrix_power(x,r)) for c,r,s in terms)
   err=float(np.linalg.norm(S@direct-diag@S))
   assert err<1e-9
   covchecks+=1
   out.append({'n':n,'sample':sample,'channel':name,'offdiag_min_coefficient':delta,'condition_number':kap,'covariance_floor_min_eigenvalue':mineig,'intertwining_error':err})
  # Adversarial means deliberately force a column normal near a coordinate vector.
  g=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n);np.fill_diagonal(g,0)
  for size in [0.,1.,1000.]:
   d=np.diag([0.]+[size]*(n-1));m=g+d;K=float(np.linalg.norm(m,2))
   for j in range(n):
    others=np.delete(m,j,axis=1);u=np.linalg.svd(others,full_matrices=True)[0][:,-1]
    delt=float(np.linalg.norm(np.delete(u,j)))
    if delt<=.5:
     row=np.delete(m[j,:],j);bound=delt*K/np.sqrt(1-delt**2)
     assert np.linalg.norm(row)<=bound+1e-8
     localchecks+=1
  if time.time()-start>90:raise RuntimeError('Research job time cap reached')
report={'seed':19103,'seconds':time.time()-start,'covariance_and_intertwining_checks':covchecks,'localized_normal_checks':localchecks,'results':out,'scope':'Deterministic checks of the sparse-channel proof, including large deformations; no inferred probability theorem.'}
Path('retry_mask_checks.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
