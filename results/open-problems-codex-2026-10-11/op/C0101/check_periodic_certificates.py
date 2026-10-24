from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,math
R=Path(__file__).parent
data=json.loads((R/'periodic_phase_results.json').read_text())
points=list(product(range(2),repeat=3));lookup={x:i for i,x in enumerate(points)}
nc=0
for rec in data['cases']:
 if not rec.get('exact_verified'):continue
 A=[[F(v) for v in row] for row in rec['A']];b=list(map(F,rec['linear_phase']));z=rec['witness_values']
 def q(x):return sum(A[i][j]*x[i]*x[j]/2 for i in range(3) for j in range(3))
 def g(x):
  y=tuple(t%2 for t in x)
  out=F(z[lookup[y]])+q(x)-q(y)+sum(b[i]*(x[i]-y[i]) for i in range(3))
  assert out.denominator==1
  return out
 for x in product(range(-3,4),repeat=3):
  delta=-6*g(x)
  for i in range(3):
   for sign in [-1,1]:
    y=list(x);y[i]+=sign;delta+=g(y)
  assert delta==rec['laplacian_values'][lookup[tuple(v%2 for v in x)]]<=5
  nc+=1
parity=[]
for a,b in product(range(2),repeat=2):
 def e(x,y):return F(-1,2) if x%2 or y%2 else F(0)
 val=2+2*e(1-a,b)+2*e(a,1-b)-4*e(a,b)
 parity.append({'parity':[a,b],'planar_laplacian':str(val)})
 assert val<=3
nd=0
for d in range(3,9):
 def g(x):return math.floor(F(x[0]**2+x[1]**2+x[0]*x[1],2))+sum(v*v for v in x[2:])
 for a,b in product(range(-4,5),repeat=2):
  x=[a,b]+[-2]*(d-2);delta=-2*d*g(x)
  for i in range(d):
   for sign in [-1,1]:
    y=x[:];y[i]+=sign;delta+=g(y)
  assert delta<=2*d-1
  nd+=1
out={'periodic_extended_grid_checks':nc,'explicit_witness_checks':nd,'parity_table':parity,'all_passed':True}
(R/'periodic_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(out,flush=True)
