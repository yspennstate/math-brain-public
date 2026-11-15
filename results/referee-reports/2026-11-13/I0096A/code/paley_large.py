"""Three projected Paley candidates per M=10,11,12, with complete enumeration."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
 os.environ[k]='1'
import numpy as np
from numerics import normalize_rows, record

rng=np.random.default_rng(960129)
for m in (10,11,12):
 for q in (29,37,41):
  d=(q+1)//2
  sq={j*j%q for j in range(1,q)}
  c=np.zeros((q+1,q+1),dtype=np.int64);c[0,1:]=1;c[1:,0]=1
  for i in range(q):
   for j in range(q):c[i+1,j+1]=0 if i==j else 1 if (i-j)%q in sq else -1
  assert np.array_equal(c@c,q*np.eye(q+1,dtype=np.int64))
  _,v=np.linalg.eigh(c)
  a=np.sqrt(2)*v[:,-d:]
  contracted=sorted(rng.choice(q+1,d-m,replace=False).tolist())
  _,_,vh=np.linalg.svd(a[contracted],full_matrices=True)
  remaining=sorted(set(range(q+1))-set(contracted))
  chosen=sorted(rng.choice(remaining,2*m-1,replace=False).tolist())
  projected=normalize_rows(np.einsum('ij,jk->ik',a[chosen],vh[d-m:].T))
  record(projected,m,f'paley_q{q}','projected',0,
    {'q':q,'parent_m':d,'contracted_parent_indices':contracted,'chosen_parent_indices':chosen})
