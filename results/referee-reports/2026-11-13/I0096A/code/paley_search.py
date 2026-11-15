"""Search projected/deleted Paley conference frames; enumerate each candidate fully."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
 os.environ[k]='1'
import itertools
import json
import numpy as np
from numerics import out, omega, record, normalize_rows

rng=np.random.default_rng(960123)
rows=list(map(json.loads,(out/'numerics.jsonl').read_text().splitlines()))
for m in range(3,9):
 best=max(r['omega'] for r in rows if r['m']==m)
 for bigm in (7,9):
  if bigm<=m:continue
  src=np.loadtxt(out/f'candidate_m{bigm:02}_paley_conference.csv',delimiter=',')
  # The saved frame has already lost one row; contracting bigm-m rows
  # leaves 2*bigm-1-(bigm-m) rows, then delete bigm-m additional rows.
  for trial in range(18):
   contracted=sorted(rng.choice(len(src),bigm-m,replace=False).tolist())
   _,_,vh=np.linalg.svd(src[contracted],full_matrices=True)
   basis=vh[bigm-m:].T
   remaining=sorted(set(range(len(src)))-set(contracted))
   chosen=sorted(rng.choice(remaining,2*m-1,replace=False).tolist())
   a=normalize_rows(src[chosen]@basis)
   val=omega(a)
   if val>best:
    best=val
    row=record(a,m,f'paley{bigm}_contract_{trial}','projected',0,
      {'parent_m':bigm,'contracted_parent_indices':contracted,'chosen_parent_indices':chosen})
    rows.append(row)
 print('dimension',m,'best',best,flush=True)
