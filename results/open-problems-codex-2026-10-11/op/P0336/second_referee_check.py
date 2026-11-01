from pathlib import Path
import json,math,itertools
import numpy as np
from scipy.optimize import linear_sum_assignment
rng=np.random.default_rng(5336);out=[]
for n in range(2,8):
 a=rng.random((n,2));b=rng.random((n,2));b[:,0]+=2
 d=b[None,:,0]-a[:,None,0];h=b[None,:,1]-a[:,None,1]
 e=h*h/(np.hypot(d,h)+d);q=h*h/(2*d);ii=np.arange(n)
 _,pe=linear_sum_assignment(e);_,pq=linear_sum_assignment(q)
 ve=[];vq=[]
 for p in itertools.permutations(range(n)):
  ve.append(float(np.mean(e[ii,p])));vq.append(float(np.mean(q[ii,p])))
 assert abs(np.mean(e[ii,pe])-min(ve))<1e-14
 assert abs(np.mean(q[ii,pq])-min(vq))<1e-14
 for p in [pe,pq]:
  z1=a[:,1]+h[ii,p]*(1-a[:,0])/d[ii,p]
  z2=a[:,1]+h[ii,p]*(2-a[:,0])/d[ii,p]
  assert np.min(np.diff(z2[np.argsort(z1)]))>=-1e-12
 # Independently minimize the two-leg kinetic action analytically at its stationary point.
 A=float(rng.uniform(.1,3));B=float(rng.uniform(.1,3));s=float(rng.normal());t=float(rng.normal())
 v=(B*s+A*t)/(A+B)
 lhs=(v-s)**2/(2*A)+(t-v)**2/(2*B);rhs=(t-s)**2/(2*(A+B))
 assert abs(lhs-rhs)<1e-12
 out.append({'n':n,'permutations':math.factorial(n),'euclidean_excess':min(ve),'quadratic':min(vq),'passed':True})
Path('second_referee_checks.json').write_text(json.dumps(out,indent=2));print('All',sum(x['permutations'] for x in out),'finite permutations checked; both optima, no crossings, and kinetic semigroup minimization passed.')
