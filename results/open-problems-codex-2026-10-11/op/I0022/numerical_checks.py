"""Fast exact-arithmetic sanity checks; these do not prove tree asymptotics."""
from fractions import Fraction as F
import json, itertools, pathlib, math
root=pathlib.Path(__file__).parent
checks={}
count=0
for sizes in itertools.product(range(9),repeat=4):
 for K in range(9):
  small=[x for x in sizes if x<=K]
  assert sum(x*x for x in small)<=K*sum(small)
  count+=1
checks['finite_collision_inequality_cases']=count
# Geometric law of arm lengths: P(Y=k)=(1-m)m^(k-1), k>=1.
# Independent arms give P(Y1+Y2=s)=(s-1)(1-m)^2*m^(s-2).
for m in [F(1,4),F(1,2),F(3,4),F(9,10)]:
 for s in range(2,41):
  convolution=sum((1-m)*m**(k-1)*(1-m)*m**(s-k-1) for k in range(1,s))
  assert convolution==(s-1)*(1-m)**2*m**(s-2)
 assert sum((1-m)*m**(k-1) for k in range(1,101))==1-m**100
checks['geometric_convolution_cases']=4*39
# Illustrate the power in the packing proof, with the normalized model
# survival tail q=m^ceil(eta log n), not a simulation of conditioned trees.
rows=[]
for m in [0.25,0.5,0.9]:
 eta=1/(2*math.log(1/m))
 for n in [10**4,10**6,10**8]:
  k=math.ceil(eta*math.log(n)); q=m**k
  mu=math.floor((1-m)*n/2)*q
  rows.append({'m':m,'n':n,'threshold':k,'mean_packed_arms_proxy':mu,
               'log_n':math.log(n),'chebyshev_bound_proxy':min(1,mu/(mu-math.log(n))**2) if mu>math.log(n) else None})
checks['packing_exponent_proxy']=rows
(root/'numerical_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps(checks,indent=2))
