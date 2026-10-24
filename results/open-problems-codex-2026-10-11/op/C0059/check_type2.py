import math,json,pathlib
import numpy as np
from scipy.integrate import quad
from fractions import Fraction
rows=[]
for n in [1,2,5,10,30,100,300,1000,3000]:
 def integrand(u):
  t=u/n
  return math.cos(t)*(1-math.pi/2*math.sin(t/2))**n
 # u=nt resolves the narrow peak; the omitted tail is bounded below.
 upper=min(n*math.pi,80.0)
 value,error=quad(integrand,0,upper,epsabs=1e-11,epsrel=1e-11,limit=200)
 tail_bound=0.0
 if upper<n*math.pi:
  # split positive and negative parts; positive phi <= exp(-t/2), since
  # sin(t/2)>=t/pi on [0,pi], and 1-z<=exp(-z).
  tail_bound=2*math.exp(-upper/2)+n*math.pi*(math.pi/2-1)**n
 rows.append({'n':n,'n_return_probability':value/math.pi,'quad_error':error/math.pi,'omitted_bound':tail_bound/math.pi,'target':4/math.pi**2})
checks=[]
for n in [0,1,2,10,100,1000]:
 lhs=sum((Fraction(1,4*k*k-1) for k in range(1,n+1)),Fraction(0))
 rhs=Fraction(n,2*n+1)
 assert lhs==rhs
 checks.append({'n':n,'exact_partial_mass':str(lhs)})
# Verify the characteristic-function formula against a rigorously truncated sum.
# Twice the positive tail beyond M equals 1/(2M+1).
M=10000
ks=np.arange(1,M+1,dtype=float)
cf=[]
for t in [0,.0001,.01,.2,1,2,math.pi]:
 approx=float(np.sum(2*np.cos(ks*t)/(4*ks**2-1)))
 exact=1-math.pi/2*abs(math.sin(t/2))
 bound=1/(2*M+1)
 assert abs(approx-exact)<=bound+1e-12
 cf.append({'t':t,'error':abs(approx-exact),'tail_bound':bound})
result={'scope':'type-2 perimeter walk, NOT dual-map SRW','exact_rational_checks':checks,'fourier_checks':cf,'return_integral':rows}
pathlib.Path('numerical_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
