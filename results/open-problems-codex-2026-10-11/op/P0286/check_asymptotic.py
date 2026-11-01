from scipy.integrate import quad
from pathlib import Path
import math,json
out=[]
for a,b in [(0.1,0.2),(0.3,0.6),(0.5,0.6)]:
 p=a*(1-b);q=(1-a)*b;t=math.sqrt(p*q);h=1-p-q;lo=h-2*t;hi=h+2*t
 for n in [100,1000,10000,100000]:
  # Divide the integral by the proposed leading term before quadrature,
  # avoiding exponential underflow and subtractive cancellation.
  upper=min(100.,n*(hi-lo)/hi)
  integrand=lambda u: math.sqrt(u)*math.sqrt(max(0,4*t-hi*u/n))/(1-hi+hi*u/n)*max(0,1-u/n)**(n-1)
  ratio=(1-hi)/(math.sqrt(math.pi)*math.sqrt(t))*quad(integrand,0,upper,epsabs=1e-12)[0]
  out.append(dict(a=a,b=b,n=n,exact_integral_over_asymptotic=ratio))
 assert abs(out[-1]['exact_integral_over_asymptotic']-1)<.01
Path('asymptotic_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
