import json,math,random
from pathlib import Path
import mpmath as mp
mp.mp.dps=50
rows=[]
for C in [0.2,1.0,5.0]:
 for i in [100,10000,1000000,100000000]:
  r=math.floor(C*i*i*math.log(i)); prev=math.floor(C*(i-1)**2*math.log(i-1))
  rows.append({'C':C,'i':i,'height_ratio':math.sqrt(r*math.log(r))/(math.sqrt(2*C)*i*math.log(i)),
               'step_ratio':(r-prev)/(2*C*i*math.log(i))})
rng=random.Random(358)
for _ in range(1000):
 m,t,beta=[10**rng.uniform(-2,2) for _ in range(3)]
 a=math.sqrt(m*beta/t)*rng.uniform(.05,.99)
 lo=a*a/(2*m*m); hi=beta*beta/(2*a*a*t*t); C=math.sqrt(lo*hi)
 assert lo<C<hi
 assert a/math.sqrt(2*C)<m
 assert t*a*math.sqrt(2*C)<beta
 c,d=[10**rng.uniform(-2,2) for _ in range(2)]
 lam=d/(2*c)
 value=(d+2*c*lam)/math.sqrt(2*lam)
 assert math.isclose(value,2*math.sqrt(c*d),rel_tol=1e-12)
 for offset in [.01,.1,.5,2,10,100]:
  l=lam*offset
  assert (d+2*c*l)/math.sqrt(2*l)>=value*(1-1e-12)
p0=mp.mpf('2.5'); eps=mp.mpf('0.1'); b=mp.mpf('2')
m=(1-eps)*b-eps*p0/(p0-1)
M=(1-eps)*mp.exp(b)+eps*p0*mp.quad(lambda y:mp.exp(-y)*y**(-p0-1),[1,mp.inf])
tails=[]
for y in [10,100,1000]:
 y=mp.mpf(y)
 # Factored integral is numerically stable even for exp(-1000).
 fac=mp.quad(lambda w:mp.exp(-w)*(1+w/y)**(-p0-1),[0,mp.inf])
 A=eps*p0*mp.exp(-y)*y**(-p0-1)*fac
 theta=-mp.expm1(-A)
 tails.append({'y':str(y),'laplace_ratio':str(fac),
               'theta_ratio':str(theta/(eps*p0*mp.exp(-y)*y**(-p0-1))),
               'log_ratio_to_source_bound_q4':str(mp.log(theta)+y+4*mp.log(y))})
out={'scope':'Deterministic asymptotics, optimization, and an admissible family. No a1 estimate is claimed.',
     'random_algebra_cases':1000,'normalization_checks':rows,
     'family':{'p0':str(p0),'epsilon':str(eps),'b':str(b),'m':str(m),'mean_offspring':str(M),
               'a1_lower':str(mp.sqrt(m*(p0-1))),'a1_upper':str(2*mp.sqrt(m*(p0+1)))},
     'tail_checks':tails}
Path('numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
