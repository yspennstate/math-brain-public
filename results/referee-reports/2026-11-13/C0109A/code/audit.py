"""Independent numerical checks of the CDF, metric implementation, and formulas."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from simulate import circular_cdf,kolmogorov,radial,I
rng=np.random.default_rng(774109)
metric_errors=[]
for n in [1,2,3,7,12]:
 for rep in range(5):
  z=rng.normal(size=n)+1j*rng.normal(size=n)
  if rep%2==0:z.imag[:(n+1)//2]=0
  if n>2:z[1]=z[0]
  ans=0.
  for x in list(np.unique(z.real))+[np.inf]:
   for y in list(np.unique(z.imag))+[np.inf]:
    f=float(circular_cdf(x,y))
    for side in [0,1]:
     empirical=np.mean((z.real<=x)&(z.imag<=y)) if side else np.mean((z.real<x)&(z.imag<y))
     ans=max(ans,abs(empirical-f))
  metric_errors.append(abs(ans-kolmogorov(z)))
assert max(metric_errors)<1e-12
normalizers=[]
for eps in [.25,.5,1,2]:
 p=2+eps
 # Independent t=1/(1+y) substitution integrates the endpoint on a compact interval.
 def integral(a):
  return quad(lambda t:math.exp(-a*(1/t-1)) if t else 0,0,1,epsabs=1e-12)[0]
 v=integral(eps)/integral(p)
 normalizers.append({'eps':eps,'analytic_second_moment':I(eps)/I(p),'quadrature_second_moment':v})
 assert abs(v-I(eps)/I(p))<1e-10
 # lower construction identities q B^2=a and q B^p=k^(-p-2)
 n=1e8;k=3;b=2*eps/p
 q=n**-2/k**2;B=n**(2/p)/k;a=n**-b/k**4
 assert abs(q*B*B/a-1)<1e-12
 assert abs(q*B**p*k**(p+2)-1)<1e-12
# Check real-marginal derivative by finite differences over representative variances.
derivative_errors=[]
for v in [1,1.2,1.8]:
 s=math.sqrt(v)/2
 def F(u):return .5+(math.asin(s/math.sqrt(u))+s*math.sqrt(u-s*s)/u)/math.pi
 for u in np.linspace(v,2,4):
  derivative=-s*math.sqrt(u-s*s)/(math.pi*u*u)
  finite_diff=(F(u+1e-5)-F(u-1e-5))/(2e-5)
  derivative_errors.append(abs(derivative-finite_diff))
  assert -derivative>=1/(16*math.pi)
assert max(derivative_errors)<1e-9
out={'metric_bruteforce_max_error':max(metric_errors),'normalizers':normalizers,
 'real_marginal_derivative_max_error':max(derivative_errors),
 'lower_bound_identities':'q B^2=a; q B^p=k^(-p-2), checked independently',
 'upper_exponent_identities':'alpha=kappa/12; s=alpha/(2+1/r); limit r->infinity is kappa/24'}
Path('data/audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
