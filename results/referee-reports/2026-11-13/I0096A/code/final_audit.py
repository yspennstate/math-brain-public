"""Check best frames with a second full enumeration, using QR before SVD."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
 os.environ[k]='1'
import itertools
import json
import math
import resource
import time
import numpy as np
from numerics import out

rows=list(map(json.loads,(out/'numerics.jsonl').read_text().splitlines()))
audits=[]
for m in range(2,13):
 r=max((r for r in rows if r['m']==m),key=lambda r:r['omega'])
 a=np.loadtxt(out/r['matrix_file'],delimiter=',')
 it=iter(itertools.combinations(range(2*m-1),m))
 value=float('inf');seen=0;witness=None
 start=time.monotonic()
 while True:
  sub=list(itertools.islice(it,2048))
  if not sub:break
  q,rmat=np.linalg.qr(a[np.array(sub)])
  vals=np.linalg.svd(rmat,compute_uv=False)[:,-1]
  i=int(np.argmin(vals))
  if vals[i]<value:value=float(vals[i]);witness=sub[i]
  seen+=len(sub)
 assert seen==math.comb(2*m-1,m)
 assert abs(value-r['omega'])<5e-14
 assert np.isfinite(a).all()
 assert np.linalg.norm(a,axis=1).max()<=1+1e-13
 entry={'m':m,'direct_svd_min':r['omega'],'qr_svd_min':value,
        'absolute_difference':abs(value-r['omega']),'all_subsets_rechecked':seen,
        'qr_witness_zero_based':witness,'elapsed_seconds':time.monotonic()-start}
 audits.append(entry)
 print(json.dumps(entry),flush=True)
(out/'full_independent_audit.json').write_text(json.dumps(audits,indent=2))
(out/'audit_resource_usage.json').write_text(json.dumps({'nice':os.getpriority(os.PRIO_PROCESS,0),
 'peak_rss_native_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'native_unit':'bytes on macOS, KiB on Linux','batch':2048},indent=2))
