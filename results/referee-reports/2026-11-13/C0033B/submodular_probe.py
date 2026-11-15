"""Does arbitrary submodularity control the nonlinear rank-two entropy term?"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from dpp import *
from scipy.optimize import linprog
import json
rng=np.random.default_rng(33321);rows=[]
for n in (3,4,5,6):
 constraints=[]
 for s in range(1<<n):
  for i in range(n):
   if s>>i&1:continue
   for j in range(i):
    if s>>j&1:continue
    v=np.zeros(1<<n);v[s]=v[s|1<<i|1<<j]=1;v[s|1<<i]=v[s|1<<j]=-1
    constraints.append(v)
 cs=np.array(constraints);vals=[]
 for it in range(100):
  q=random_kernel(rng,n,True,'uniform');u=random_unitary(rng,n,True);a=spectral(u,np.r_[1,-1,np.zeros(n-2)])
  p,m=probabilities(q);c=np.einsum('sij,jk->sik',np.linalg.inv(m),a);tr=np.trace(c,axis1=1,axis2=2).real;tr2=np.einsum('sij,sji->s',c,c).real
  dd=p*(tr*tr-tr2)
  res=linprog(dd,A_ub=cs,b_ub=np.zeros(len(cs)),bounds=[(-1,1)]*(1<<n),method='highs',options={'threads':1});val=res.fun;vals.append(val)
  if val < -1e-8:
   np.savez('data/submod_counter_n%d.npz'%n,Q=q,A=a,f=res.x,second=dd,value=val);break
 row=dict(n=n,trials=len(vals),min_second=float(min(vals)),max_second=float(max(vals)))
 print(json.dumps(row),flush=True);rows.append(row)
open('data/submodular_probe.json','w').write(json.dumps(rows,indent=2)+'\n')
