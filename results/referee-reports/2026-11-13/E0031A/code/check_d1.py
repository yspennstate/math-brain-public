#!/usr/bin/env python3
import os,csv,json
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=10
import numpy as np
rng=np.random.default_rng(3100131)
summary=[]
with Path('data/d1_samples.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['n','sample','length'])
 for n in [32,128,512,2048]:
  values=[]
  for offset in range(0,10000,250):
   u=np.sort(rng.random((250,n)),axis=1)
   values.extend(np.sum(u[:,1::2]-u[:,::2],axis=1))
  for i,x in enumerate(values):w.writerow([n,i,repr(x)])
  vals=np.array(values);exact=n/(4*(n+1)**2)
  summary.append({'n':n,'samples':len(vals),'mean':float(vals.mean()),'exact_mean':n/(2*(n+1)),'variance':float(vals.var(ddof=1)),'exact_variance':exact,'variance_ratio':float(vals.var(ddof=1))/exact})
Path('data/d1_summary.json').write_text(json.dumps({'seed':3100131,'summary':summary},indent=2)+'\n')
print(json.dumps(summary,indent=2))
