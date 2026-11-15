#!/usr/bin/env python3
"""Finite-horizon evidence, conditional on one fixed environment per case."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import json,resource,time
import numpy as np
from pathlib import Path
start=time.monotonic();N=2048;H=2048;axis=np.arange(-H,H+1)
def alt():return np.where(axis%2==0,1,-1)
def sparse_log(power):
 a=alt()
 # Positive odd rows +1, positive even rows -1 before the exceptional flips.
 a[axis>0]=np.where(axis[axis>0]%2==1,1,-1)
 m=1
 while 2*(2**(power*m*m))<=H:
  a[H+2*(2**(power*m*m))]=1;m+=1
 return a
rows=[];env_rng=np.random.default_rng(300300)
for i,name in enumerate(('alternating','iid_both','alternating_random','sparse_log_both')):
 e=alt();f=alt()
 if name=='iid_both':e=env_rng.choice([-1,1],2*H+1);f=env_rng.choice([-1,1],2*H+1)
 if name=='alternating_random':e=env_rng.choice([-1,1],2*H+1)
 if name=='sparse_log_both':e=sparse_log(1);f=sparse_log(2)
 np.savez_compressed('data/environment_'+name+'.npz',e=e,f=f)
 rng=np.random.default_rng(300301+i)
 x=np.zeros(N,dtype=np.int32);y=x.copy();visits=np.zeros(N,dtype=np.int32)
 for step in range(1,H+1):
  horizontal=rng.integers(0,2,size=N,dtype=np.int8).astype(bool)
  # Both increments use pre-step coordinates.
  dx=np.where(horizontal,e[y+H],0);dy=np.where(horizontal,0,f[x+H])
  x+=dx;y+=dy
  visits+=((x==0)&(y==0))
  if step in (128,512,2048):
   rows.append({'case':name,'time':step,'paths':N,'mean_visits_excluding_time_zero':float(visits.mean()),
    'visits_standard_error':float(visits.std(ddof=1)/np.sqrt(N)),
    'fraction_returned_by_time':float((visits>0).mean())})
summary={'description':'One fixed environment for each case; no infinite-time inference.',
'rows':rows,'environment_seed':300300,'path_seeds':[300301+i for i in range(4)],
'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1,
'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('data/monte_carlo.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
