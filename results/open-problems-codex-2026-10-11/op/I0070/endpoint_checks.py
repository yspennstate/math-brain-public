"""Small diagnostic checks; not a verification of the SPDE theorem."""
from fractions import Fraction
import math, random, json
from pathlib import Path
random.seed(70)
def norm(v):return math.sqrt(sum(x*x for x in v))
def ynorm(v):return norm(v[:4])+norm(v[4:])
max_error=0.0
count=0
for rho in [Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(2),Fraction(10),Fraction(100)]:
 a=1/(rho+1)
 assert 0<a<1 and (1-a)*(rho+1)==rho and a*(rho+1)==1
for j in range(1000):
 eta=[0.0,1e-6,0.01,0.5][j%4]
 C=[0.0,0.2,3.0][j%3]
 x=[random.uniform(-2,2) for _ in range(17)] if j%10 else [0.0]*17
 nx=norm(x)
 h=[random.uniform(-1,1) for _ in range(16)]
 nh=ynorm(h)
 target=(C+eta*nx)*random.random()
 h=[z*target/nh for z in h]
 nh=ynorm(h)
 h0=h[:] if nh<=C else [C/nh*z for z in h]
 h1=[z-z0 for z,z0 in zip(h,h0)]
 if nx:
  phi=sum(z*z for z in x)/(nx*nx)
  Rx=[phi*z for z in h1]
  opnorm=ynorm(h1)/nx
 else:Rx=[0.0]*len(h);opnorm=0.0
 error=ynorm([z-z0-z1 for z,z0,z1 in zip(h,h0,Rx)])
 max_error=max(max_error,error)
 assert ynorm(h0)<=C+1e-12
 assert opnorm<=eta+1e-12
 assert error<1e-11
 count+=1
result={'critical_exponent_cases':6,'rank_one_cases':count,'maximum_reconstruction_error':max_error,
 'boundary_cases':'zero input, zero perturbation, zero remainder bound, small perturbation',
 'scope':'finite-dimensional factorization and exact exponent algebra only; no stochastic or infinite-dimensional certification'}
Path(__file__).with_name('endpoint_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
