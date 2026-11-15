"""Exact rational checks at short horizons, independent of tilted FFT expansion."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
from fractions import Fraction as Q
import json
import numpy as np
from scipy.fft import next_fast_len
from iterate import initial,advance
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def conv(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
rows=[]
for m,b in [(2,2),(2,5),(3,1),(3,3)]:
 p=Q(1,1+((m-1)*b-1)*m**b);v=[Q(0)]*(b+1);v[0]=1-p;v[b]=p
 assert sum(((m-1)*k-1)*m**k*x for k,x in enumerate(v))==0
 history=[v.copy()]
 K=128;w=np.power(float(m),-np.arange(K+1,dtype=float));a=initial(m,b,K,np.float64);active=b
 for n in range(3):
  c=v
  for j in range(m-1):c=conv(c,v)
  v=[c[0]+c[1]]+c[2:]
  history.append(v.copy())
  assert sum(v)==1
  assert sum(((m-1)*k-1)*m**k*x for k,x in enumerate(v))==0
  a,_=advance(a,m,next_fast_len(m*active+1),w,active=active);active=min(K,m*active-1)
  err=max(abs(float(v[k])-a[k]*w[k])for k in range(len(v)))
  assert err<1e-14
 for n in range(4):
  for t in range(4-n):
   left=1-history[n+t][0]
   right=m**t*sum(history[n][t+1:])
   for i in range(n,n+t):right*=history[i][0]**(m-1)
   assert left>=right
 for n in range(3):
  mu=lambda law:sum(k*x for k,x in enumerate(law))
  assert mu(history[n+1])==m*mu(history[n])-1+history[n][0]**m
 rows.append({'spine_and_mean_identity_checked':True,'m':m,'b':b,'generations':3,'positive_probability':str(p),
              'last_max_absolute_coefficient_error':err,'mean_exact':str(sum(k*x for k,x in enumerate(v)))})
(ROOT/'data'/'exact_rational_checks.json').write_text(json.dumps(rows,indent=2));print(rows)
