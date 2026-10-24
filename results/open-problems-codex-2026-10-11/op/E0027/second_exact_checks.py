from pathlib import Path
from fractions import Fraction as F
import random,json,math
random.seed(27002)
counts={'tuples':6000,'noncancellation_cases':0,'complement_cases':0,'exceptional_cases':0,'hellinger_cases':3000}
def f(a):return 1+a/(1+a)
for j in range(6000):
 r1=F(random.randrange(0,300),10);r2=F(random.randrange(0,300),10)
 a1=1+r1;a2=1+r2;a=1+r1+r2
 g1=F(random.randrange(-100,101),100)*a1*f(a1)
 g2=F(random.randrange(-100,101),100)*a2*f(a2)
 h1=F(random.randrange(-4000,4001),10);h2=F(random.randrange(-4000,4001),10)
 u=g1+h1;v=g2+h2;i=u+v
 d1=a1*a1+u*u;d2=a2*a2+v*v;d=a*a+i*i
 G=2*a*f(a);e=max(abs(i)-G,F(0));hh=(1 if i>0 else -1 if i<0 else 0)*e;gg=i-hh
 assert abs(g1+g2)<=G and abs(gg)<=G and e<=abs(h1)+abs(h2)
 assert e*e<=d
 if u*v>=0:
  counts['noncancellation_cases']+=1;assert d>=d1 and d>=d2
 if d>=F(1,4)*max(d1,d2):
  counts['complement_cases']+=1
  assert e/d<=4*(abs(h1)/d1+abs(h2)/d2)
 else:counts['exceptional_cases']+=1
for j in range(3000):
 t=F(random.randrange(0,10000),1000);k=t*t+2*t
 assert (k*k<=6*t*t) if k<=1 else (k<=6*t*t)
model=[]
for R in [10,100,1000,10000]:
 val=math.log((1+R*R)/5)-4*(math.atan(R)-math.atan(2))
 model.append({'R':R,'sum_clipped_remainder_integral_exact_formula':val,'sum_unclipped_remainder_integral_exact_formula':math.log(1+R*R)})
result={'seed':27002,'counts':counts,'passed':True,'envelope':'f(a)=1+a/(1+a), bounded nondecreasing and admissible','free_scalar_model':model,'limitations':'Finite rational checks of algebra; analytic proofs establish integrability. The free scalar model is not realizable as Levy exponents.'}
Path('second_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
