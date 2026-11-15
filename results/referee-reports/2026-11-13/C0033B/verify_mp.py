"""High precision audit of saved three-point near-zero witnesses."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import json,itertools,numpy as np,mpmath as mp
from dpp import mp_stats,mp_matrix
rows=[]
for f in ('three_False','three_True','normalized_three_False','normalized_three_True'):
 z=np.load('data/'+f+'.npz');q=z['Q'];a=z['A'];row=dict(witness=f,stored_search_score=float(z['value']))
 for dps in (110,160):
  row[str(dps)]=mp_stats(q,a,dps=dps)
 with mp.workdps(160):
  qm=mp_matrix(q);am=mp_matrix(a)
  def poly_det(ix):
   if not ix:return [mp.mpf(1)]
   acc=[mp.mpc(0)]*(len(ix)+1)
   for pm in itertools.permutations(range(len(ix))):
    sign=(-1)**sum(pm[j]>pm[k] for j in range(len(ix)) for k in range(j+1,len(ix)))
    pp=[mp.mpc(sign)]
    for j in range(len(ix)):
     i,k=ix[j],ix[pm[j]];new=[mp.mpc(0)]*(len(pp)+1)
     for l,c in enumerate(pp):new[l]+=c*qm[i,k];new[l+1]+=c*am[i,k]
     pp=new
    for l,c in enumerate(pp):acc[l]+=c
   return acc
  inclusion=[poly_det([i for i in range(3) if u>>i&1]) for u in range(8)]
  atoms=[]
  for s in range(8):
   pp=[mp.mpf(0)]*4
   for u in range(8):
    if u&s!=s:continue
    for l,c in enumerate(inclusion[u]):pp[l]+=(-1)**((u^s).bit_count())*mp.re(c)
   atoms.append(pp)
  dd=-sum(pp[1]**2/pp[0]+2*pp[2]*mp.log(pp[0]) for pp in atoms)
  row['independent_mobius_polynomial_second_160']=mp.nstr(dd,150)
  row['independent_discrepancy']=mp.nstr(abs(dd-mp.mpf(row['160']['second'])),8)
 rows.append(row);print(f,row['160']['second'][:65],flush=True)
Path('data/three_point_mp.json').write_text(json.dumps(rows,indent=2)+'\n')
