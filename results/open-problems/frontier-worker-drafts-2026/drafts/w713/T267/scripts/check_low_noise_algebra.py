from fractions import Fraction as F
from pathlib import Path
import json
checks=0
for kappa in [F(1,2),F(1),F(3,2),F(2),F(5,2),F(3)]:
 for z in [F(0),F(1,4),F(1,2),F(1),F(2),F(3)]:
  h=kappa*z-z*z-1
  assert h==-(z-kappa/2)**2+kappa*kappa/4-1
  if kappa<2:assert h<0
  checks+=1
k=F(5,2)
assert [k*z-z*z-1 for z in [F(2),F(1,2)]]==[0,0]
assert -k*2+2*2**2>0
assert -k*F(1,2)+2*F(1,2)**2<0
zvals=[F(3),F(2),F(1,2),F(1,4)]
poly=[-k*z+z*z/2 for z in zvals]
assert poly==[F(-3),F(-3),F(-9,8),F(-19,32)]
log2_lower=F(1,2)/F(3,2)+F(1,2)/2
log2_upper=F(3,4)
assert log2_lower==F(7,12)
lower_margins=[F(1,3),F(15,8)-2*log2_upper,log2_lower-F(17,32)]
assert lower_margins==[F(1,3),F(3,8),F(5,96)]
assert all(z>0 for z in lower_margins)
# Coefficients of (1-x/2)(1+x)-1 = x(1-x)/2.
a=[F(1),F(-1,2)]; b=[F(1),F(1)]
left=[sum((a[i]*b[j] for i in range(2) for j in range(2) if i+j==d),F(0)) for d in range(3)]
left[0]-=1
assert left==[F(0),F(1,2),F(-1,2)]
out={'quadratic_completed_square_cases':checks,'concrete_kappa':'5/2','simple_roots':['2','1/2'],'primitive_polynomial_parts':[str(z) for z in poly],'strict_margin_lower_bounds':[str(z) for z in lower_margins],'scope':'Exact scalar certificate plus analytic logarithm bounds documented in proof; not a certification of kernel asymptotics or nonlinear dynamics.'}
with (Path(__file__).resolve().parent.parent/'logs/low_noise_algebra_checks.json').open('w',encoding='utf-8',newline='') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
