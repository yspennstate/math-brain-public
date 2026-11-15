#!/usr/bin/env python3
"""Compare the simulation against independently solved finite CTMC generators."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import itertools,json,subprocess,csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
MASK=(1<<64)-1
def draw(state):
 state=(state+0x9e3779b97f4a7c15)&MASK;z=state
 z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK
 z=((z^(z>>27))*0x94d049bb133111eb)&MASK
 return state,(z^(z>>31))&MASK
records=[]
for n,K,M,r,p,seed in [(6,1,3,1.,0.,125),(6,1,3,.3,.2,125),(5,2,5,.3,.4,125)]:
 s=seed;rates=[]
 for _ in range(n):
  s,z=draw(s);rates.append(r if (z>>11)*2**-53<p else 1.)
 states=[x for x in itertools.product(range(K+1),repeat=n) if sum(x)==M];ix={x:i for i,x in enumerate(states)}
 Q=np.zeros((len(states),len(states)));jump=np.zeros(len(states))
 for a,x in enumerate(states):
  for i in range(n):
   j=(i+1)%n
   if x[i]>0 and x[j]<K:
    y=list(x);y[i]-=1;y[j]+=1;Q[a,ix[tuple(y)]]+=rates[i];Q[a,a]-=rates[i];jump[a]+=rates[i]/n
 A=Q.T.copy();b=np.zeros(len(states));A[-1]=1;b[-1]=1;pi=np.linalg.solve(A,b)
 exact=float(pi@jump)
 raw=subprocess.check_output(['./code/ring_sim',str(n),str(K),str(M/n),str(r),str(p),str(seed),'777','2000','1000000','random'],text=True)
 row=next(csv.reader([raw]));observed=float(row[12]);sd=float(row[13])
 check={'n':n,'K':K,'M':M,'rates':rates,'states':len(states),'exact_current':exact,'simulated_current':observed,'error':observed-exact,'block_sd':sd,'generator_residual':float(np.max(np.abs(np.sum(pi[:,None]*Q,axis=0)))),'pass':abs(observed-exact)<max(.001,4*sd)}
 if r==1:
  check['closed_form']=M*(n-M)/(n*(n-1));assert abs(exact-check['closed_form'])<1e-12
 assert check['pass'];records.append(check)
Path('data/validation.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
