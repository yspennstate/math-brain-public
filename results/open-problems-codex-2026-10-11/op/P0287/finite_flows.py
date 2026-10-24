import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time
P=pathlib.Path(__file__).parent
rows=[]
for n in (3,5,7,9):
 for k in (0.4,1.0,2.0):
  start=time.monotonic(); size=2**n; center=n//2
  Q=np.zeros((size,size)); alpha=0.3;beta=0.7
  for s in range(size):
   events=[]
   if not s&1: events.append((s|1,alpha))
   if s&(1<<(n-1)): events.append((s^(1<<(n-1)),beta))
   if s&(1<<center): events.append((s^(1<<center),k))
   for j in range(n-1):
    if (s>>j)&3==1: events.append((s^(3<<j),1.0))
   for t,rate in events: Q[s,t]+=rate;Q[s,s]-=rate
  A=Q.T.copy();A[-1,:]=1;b=np.zeros(size);b[-1]=1
  pi=np.linalg.solve(A,b)
  assert pi.min()>-1e-10
  residual=float(np.max(np.abs(pi@Q)));assert residual<1e-10
  dens=[float(sum(pi[s] for s in range(size) if (s>>j)&1)) for j in range(n)]
  curr=[float(sum(pi[s] for s in range(size) if (s>>j)&3==1)) for j in range(n-1)]
  cov=[float(sum(pi[s] for s in range(size) if (s>>j)&3==3))-dens[j]*dens[j+1] for j in range(n-1)]
  balance=curr[center-1]-curr[center]-k*dens[center]
  assert abs(balance)<1e-10
  rows.append({'n':n,'kappa':k,'alpha':alpha,'beta':beta,'density':dens,'current':curr,'adjacent_covariance':cov,'stationarity_residual':residual,'defect_balance_residual':balance,'seconds':time.monotonic()-start})
(P/'finite_flows.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
for x in rows:print('n',x['n'],'kappa',x['kappa'],'Jleft',round(x['current'][x['n']//2-1],7),'Jright',round(x['current'][x['n']//2],7),'p0',round(x['density'][x['n']//2],7))
