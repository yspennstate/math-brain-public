from fractions import Fraction as F
from pathlib import Path
import json, math, random
import numpy as np

def bootstrap(a,k):
 c=F(0); path=[c]; delta=(k-a*a/4)/a
 assert delta>0
 maxsteps=math.ceil(a/delta)+1
 for j in range(maxsteps):
  if c==a: return path,maxsteps
  nxt=min(a,k/(a-c))
  assert nxt*(a-c)<=k
  assert nxt>c
  if nxt<a: assert nxt-c>=delta
  path.append(nxt); c=nxt
 raise AssertionError('Failed to terminate within rigorous bound')

rng=random.Random(35812)
max_seen=0
for _ in range(250):
 a=F(rng.randrange(1,2000),1000)
 k=(a*a/4+1)/2
 path,limit=bootstrap(a,k)
 assert path[-1]==a
 max_seen=max(max_seen,len(path)-1)

examples=[]
for av in ['1','1.5','1.9','1.99','1.999']:
 a=F(av); k=(a*a/4+1)/2
 path,limit=bootstrap(a,k)
 examples.append({'a':str(a),'K':str(k),'steps':len(path)-1,'rigorous_step_cap':limit,
                  'floors_float':[float(v) for v in path]})

# Critical boundary: the recurrence converges to 1 and does not reach a=2.
c=F(0)
for j in range(1,1001):
 c=1/(2-c)
 assert c==F(j,j+1)

a=1.8; c=.5; b=.65; beta=.95; m=t=1.
lo=(a-c)**2/(2*m*m); hi=beta**2/(2*t*t*b*b); C=(lo+hi)/2
assert lo<C<hi
expected_exponent=t*b-beta/math.sqrt(2*C)
assert expected_exponent<0
samples=[]
# At most a few NumPy arrays of 1,000,001 elements: well below 1 GB.
idx=np.arange(2,1000002,dtype=np.float64)
r=np.floor(C*idx*idx*np.log(idx))
step=np.diff(r)
logs=np.cumsum(np.log(step))
for L in [100,1000,10000,100000,1000000]:
 j=L-2
 last=r[j]; prev=r[j-1]
 fn=lambda x:math.sqrt(x*math.log(x))
 incr_ratio=(a*fn(last)-c*fn(prev))/(last-prev)
 for fraction in [.01,.5,.99]:
  n=last+fraction*(r[j+1]-last)
  cost=logs[j-1]/fn(n)
  samples.append({'L':L,'endpoint_fraction':fraction,'corridor_increment_ratio':incr_ratio,
                  'target_increment_ratio':(a-c)/math.sqrt(2*C),
                  'log_bound_over_f':t*b-beta*cost,'target':expected_exponent})

out={'exact_bootstrap_cases':250,'max_steps_in_seeded_cases':max_seen,'examples':examples,
     'critical_boundary_exact_checks':1000,'critical_floor_after_1000':'1000/1001',
     'corridor_samples':samples,
     'scope':'Finite recurrence and deterministic all-generation exponent checks only; no simulation of an infinite ray.'}
Path('corridor_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='examples'},indent=2))
