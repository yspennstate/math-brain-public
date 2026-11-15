import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from dpp import *
from scipy.optimize import linprog
import json
rng=np.random.default_rng(33322);rows=[]
for n in (4,5,6,7,8):
 constraints=[]
 for s in range(1<<n):
  for i in range(n):
   if s>>i&1:continue
   for j in range(i):
    if s>>j&1:continue
    v=np.zeros(1<<n);v[s]=v[s|1<<i|1<<j]=1;v[s|1<<i]=v[s|1<<j]=-1;constraints.append(v)
 cs=np.array(constraints);vals=[]
 for it in range(200):
  u=random_unitary(rng,n,True);k=rng.integers(1,n-2+1);q=spectral(u,np.r_[np.ones(k),np.zeros(n-k)])
  aa=np.outer(u[:,k],u[:,k].conj());bb=np.outer(u[:,k+1],u[:,k+1].conj())
  def atoms(q):
   bits=((np.arange(2**n)[:,None]>>np.arange(n))&1);m=np.broadcast_to(q,(2**n,n,n)).copy();m[:,np.arange(n),np.arange(n)]-=1-bits
   return (np.linalg.det(m)*(-1.)**(n-bits.sum(axis=1))).real
  dd=atoms(q+aa+bb)-atoms(q+aa)-atoms(q+bb)+atoms(q)
  res=linprog(-dd,A_ub=cs,b_ub=np.zeros(len(cs)),bounds=[(-1,1)]*(1<<n),method='highs',options={'threads':1});val=-res.fun;vals.append(val)
  if val >1e-8:
   np.savez('data/submod_boundary_counter_n%d.npz'%n,Q=q,aa=aa,bb=bb,f=res.x,second=dd,value=val);break
 row=dict(n=n,trials=len(vals),max_mixed_second=float(max(vals)),min_mixed_second=float(min(vals)))
 print(json.dumps(row),flush=True);rows.append(row)
open('data/submod_boundary.json','w').write(json.dumps(rows,indent=2)+'\n')
