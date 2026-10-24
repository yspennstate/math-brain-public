import math,json,random
from pathlib import Path
from fractions import Fraction as F
import numpy as np

rng=random.Random(3581202)
cases=[]
for trial in range(100):
 s=rng.uniform(.1,3); h=1-math.exp(-s)
 depth=8
 leaves=[]
 def walk(history,prob,A):
  N=sum(history); L=len(history)
  if L==depth or (L>=3 and history[-3:]==[0,0,0]):
   leaves.append((prob,N,A)); return
  pi=rng.uniform(.02,.98)
  # The probability for later tests depends on already observed successes.
  if N>=2: pi*=.25
  walk(history+[0],prob*(1-pi),A+pi)
  walk(history+[1],prob*pi,A+pi)
 walk([],1.,0.)
 total=sum(w for w,n,a in leaves)
 em=sum(w*math.exp(-s*n+h*a) for w,n,a in leaves)
 assert math.isclose(total,1.,abs_tol=1e-12)
 assert em<=1+1e-12
 for K in [1,2,3]:
  for R in [.25,1,2,3,4]:
   event=sum(w for w,n,a in leaves if n<K and a>=R)
   bound=math.exp(s*K-h*R)
   assert event<=bound+1e-12
 cases.append({'trial':trial,'leaves':len(leaves),'s':s,'supermartingale_expectation':em})

coef=[]
for _ in range(1000):
 c,d,gamma=[rng.uniform(.05,5),rng.uniform(.05,5),rng.uniform(.05,.999)]
 lam=d/(2*c)
 a=(d+2*c*lam)/math.sqrt(2*gamma*lam)
 target=2*math.sqrt(c*d/gamma)
 assert math.isclose(a,target,rel_tol=1e-12)
 for k in [.1,.5,2.,10.]:
  val=(d+2*c*(lam*k))/math.sqrt(2*gamma*(lam*k))
  assert val>=target*(1-1e-12)

# Uniform integrability convex-average deterministic inequality.
for _ in range(1000):
 w=np.array([rng.random() for j in range(20)]); w/=w.sum()
 X=np.array([10**rng.uniform(-4,4) for j in range(20)])
 M=10**rng.uniform(-3,3); Y=float(w@X)
 lhs=Y if Y>M else 0.
 rhs=2*float(w@(X*(X>M/2)))
 assert lhs<=rhs+1e-9

# Exact power condition gained by allowing B_i potential reset times.
q=F(7,2); t=F(1); d=F(13,5)
assert t*d>q-1 and t*d<q
growth=[]
for i in [100,1000,10000,100000,1000000]:
 B=2*i*math.log(i)
 growth.append({'i':i,'variable_time_log_G':float(t*d)*math.log(i)+(1-float(q))*math.log(B),
                 'fixed_time_log_F':float(t*d)*math.log(i)-float(q)*math.log(B)})

out={'adaptive_bernoulli_cases':100,'compensator_event_checks':1500,
     'max_supermartingale_expectation':max(z['supermartingale_expectation'] for z in cases),
     'minimum_supermartingale_expectation':min(z['supermartingale_expectation'] for z in cases),
     'coefficient_cases':1000,'UI_average_cases':1000,
     'growth_samples_q3_5_d2_6':growth,
     'growth_at_large_log_i':[{'log_i':u,'log_G':float(t*d+1-q)*u+(1-float(q))*(math.log(2)+math.log(u))} for u in [30,100,1000,10000]],
     'scope':'Finite adaptive probability trees and deterministic estimates, not infinite-ray survival simulations.'}
Path('reset_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
