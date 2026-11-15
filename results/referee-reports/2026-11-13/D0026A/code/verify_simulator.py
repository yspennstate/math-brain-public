#!/usr/bin/env python3
"""Independent finite-state generator vs Gillespie; single seed, healthy boundary."""
import csv, json, os, subprocess
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np
from scipy.linalg import expm
n=5;q=.3;p=1-q
states=list(range(1,1<<n)); idx={s:i for i,s in enumerate(states)}
Q=np.zeros((len(states),len(states)))
for s in states:
 for i in range(n):
  legal=(i>0 and s>>(i-1)&1) or (i+1<n and s>>(i+1)&1)
  if legal:
   r=p if s>>i&1 else q
   Q[idx[s],idx[s^(1<<i)]]+=r;Q[idx[s],idx[s]]-=r
weights=np.array([q**s.bit_count()*p**(n-s.bit_count()) for s in states]);weights/=weights.sum()
assert np.max(np.abs(weights@Q))<1e-14
assert np.max(np.abs(weights[:,None]*Q-(weights[:,None]*Q).T))<1e-14
subprocess.run(['code/simulate',str(q),'120000','4','2','0','data/verification_mc.csv','61946'],check=True)
rows=list(csv.DictReader(open('data/verification_mc.csv')));init=np.zeros(len(states));init[idx[1<<(n//2)]]=1
maxz=0.;checks=[];max_uniformization_error=0.
def uniformization(t):
 import math
 rate=n
 P=(np.eye(len(states))+Q/rate).tolist()
 v=init.tolist();weight=math.exp(-rate*t);answer=[weight*x for x in v]
 for k in range(1,300):
  v=[sum(v[i]*P[i][j] for i in range(len(states))) for j in range(len(states))]
  weight*=rate*t/k
  answer=[a+weight*x for a,x in zip(answer,v)]
  if k>rate*t+10 and weight<1e-18: break
 return np.array(answer)
for row in rows:
 t=float(row['time'])
 with np.errstate(all='ignore'): law=init@expm(t*Q)
 assert np.isfinite(law).all()
 independent=uniformization(t)
 max_uniformization_error=max(max_uniformization_error,float(np.max(np.abs(law-independent))))
 assert np.max(np.abs(law-independent))<1e-13
 assert abs(law.sum()-1)<1e-13
 functions={'infect0':lambda s:bool(s>>(n//2)&1),'infect01':lambda s:(s>>(n//2)&3)==3,'healthy3':lambda s:(s>>(n//2-1)&7)==0,'right_front':lambda s:s.bit_length()-1-n//2,'minus_left_front':lambda s:n//2-((s&-s).bit_length()-1),'diameter':lambda s:s.bit_length()-(s&-s).bit_length()}
 for name,f in functions.items():
  exact=float(law@np.array([f(s) for s in states]));mc=float(row[name]);se=float(row[name+'_se']);z=abs(mc-exact)/se if se else abs(mc-exact)
  maxz=max(maxz,z);checks.append({'time':t,'observable':name,'exact':exact,'mc':mc,'se':se,'abs_z':z})
assert maxz<6, maxz
result={'max_abs_z':maxz,'expm_uniformization_max':max_uniformization_error,'checks':checks,'rowsum_max':float(np.max(np.abs(Q.sum(axis=1)))),'stationarity_max':float(np.max(np.abs(weights@Q))),'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1}
open('data/verification.json','w').write(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
