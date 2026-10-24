"""Deterministic, bounded-resource checks; not a proof of measure classification."""
import math, json, pathlib, random
root=pathlib.Path(__file__).resolve().parent
def simpson(f,a,b,n):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def cross(n,R=2):
 def inner(x):
  return simpson(lambda y:2/(y-x)**2*(-math.expm1(-(y-x)**2))**2,R,R+1,n)
 return simpson(inner,0,1,n)
out={'cross_laplace_gap':{str(n):cross(n) for n in [40,80,160,320]},
     'shared_intensity_exact':2*math.log(4/3),
     'shared_intensity_quadrature':simpson(lambda x:2*(1/(2-x)-1/(3-x)),0,1,320),
     'mixing_rate':{str(R):2*math.log(R*R/(R*R-1)) for R in [2,4,8,16,32,64]},
     'scaling_max_error':0.0}
for e in [0.1,0.25,0.5,0.9,1.0,2.0]:
 for r in [0.01,0.1,1.0,10.0,100.0]:
  val=2/(e*r)**2*e**2
  out['scaling_max_error']=max(out['scaling_max_error'],abs(val-2/r**2)/(2/r**2))
out['checks']={'positive_gap':all(v>0 for v in out['cross_laplace_gap'].values()),
 'integral_agreement':abs(out['shared_intensity_exact']-out['shared_intensity_quadrature'])<1e-9,
 'scaling':out['scaling_max_error']<1e-12}
(root/'numerical_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
