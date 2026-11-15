"""Independently enumerate the CTMC and solve stationary balance equations."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import itertools,json,subprocess,pathlib,math
import numpy as np
root=pathlib.Path(__file__).resolve().parents[1]
records=[]
for n,K,m,p,seed in [(6,1,3,0,14),(6,1,3,.4,13),(5,2,5,.4,13),(5,2,5,0,14)]:
 raw=subprocess.check_output([str(root/'code'/'ring_check'),str(n),str(K),str(m/n),str(p),str(seed),'123456','10000','2000000','20','random'],text=True)
 sim=json.loads(raw);alpha=np.ones(n);alpha[sim['slow_sites']]=.5
 states=[s for s in itertools.product(range(K+1),repeat=n) if sum(s)==m]
 index={s:i for i,s in enumerate(states)};Q=np.zeros((len(states),len(states)));rate=np.zeros(len(states))
 for i,s in enumerate(states):
  for x in range(n):
   y=(x+1)%n
   if s[x]>0 and s[y]<K:
    z=list(s);z[x]-=1;z[y]+=1;j=index[tuple(z)]
    Q[i,j]+=alpha[x];Q[i,i]-=alpha[x];rate[i]+=alpha[x]/n
 A=Q.T.copy();A[-1,:]=1;b=np.zeros(len(states));b[-1]=1
 pi=np.linalg.solve(A,b);exact=math.fsum(float(a)*float(b) for a,b in zip(pi,rate))
 row=dict(n=n,K=K,mass=m,alpha=alpha.tolist(),states=len(states),exact=float(exact),simulated=sim['current'],difference=float(sim['current']-exact),residual=max(abs(math.fsum(float(pi[i])*float(Q[i,j]) for i in range(len(states)))) for j in range(len(states))),block_sd=sim['block_sd'])
 assert np.min(pi)>-1e-12 and row['residual']<1e-12
 assert abs(row['difference'])<.002
 if K==1 and p==0:assert abs(exact-m*(n-m)/(n*(n-1)))<1e-12
 records.append(row);print(row,flush=True)
(root/'data'/'small_ring_validation.json').write_text(json.dumps(records,indent=2))
