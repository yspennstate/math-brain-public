from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json
checks=0;rows=[]
def ck(x):
 global checks
 checks+=1;assert x,checks
a=[Q(7,5),Q(-1,5)];b=[Q(1),Q(1)]
ck(sum(x*x for x in a)/2==1);ck(sum(x*x for x in b)/2==1)
for m in [1,2]:
 rho=Q(1,2**m);values=[];empty=Q(0);norms=[]
 for y in [0,1]:
  vv=[]
  for c,u,z in product([0,1],[0,1],range(1<<m)):
   g=[a[y],b[y],-b[y],-a[y]][c+2*u]
   vv.append(-g if c==0 and z==0 else g)
  values+=vv;empty+=Q(sum(vv),len(vv))**2/2;norms.append(sum(v*v for v in vv)/len(vv))
 ck(sum(v*v for v in values)/len(values)==1)
 ck(norms==[Q(37,25),Q(13,25)])
 ck(empty==rho*rho/5);ck(empty!=rho*rho)
 rows.append(dict(m=m,actual_empty_mass=str(empty),incorrect_Boolean_mass=str(rho*rho),physical_child_norms=[str(x) for x in norms]))
result=dict(status='PASS',exact_assertions=checks,rows=rows)
(Path(__file__).resolve().parents[1]/'out/REAL_GUARD.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','exact_assertions':checks}))
