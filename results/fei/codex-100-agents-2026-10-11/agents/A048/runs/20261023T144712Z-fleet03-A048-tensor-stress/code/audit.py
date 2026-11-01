from pathlib import Path
from fractions import Fraction as F
import json
base=Path(__file__).resolve().parents[1]
checks=roots=edges=0
def ok(x):
 global checks
 assert x
 checks+=1
def coeff(t,s):return sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))/F(len(t))
for n in (1,2):
 for table in range(1<<(1<<n)):
  t=[(-1)**(table>>x&1) for x in range(1<<n)]
  for j in range(1,1<<n):
   roots+=1;a=coeff(t,j);p=[coeff(t,s)**2 for s in range(1<<n)]
   q=[F(5,6)*x for x in p];q[0]=p[0];q[j]+=F(1,6)*(1-p[0]);ok(sum(q)==1)
   for i in range(n):
    if j>>i&1:continue
    edges+=1;values=[]
    for y in (0,1):
     domain=[x for x in range(1<<n) if (x>>i&1)==y]
     values.append(sum(t[x]*(-1 if (x&j).bit_count()%2 else 1) for x in domain)/F(len(domain)))
    ok((values[0]**2+values[1]**2)/2>=a*a)
    r=n-j.bit_count();ar=1-a*a;ac=1-(values[0]**2+values[1]**2)/2
    ok(r*ar-(r-1)*ac>=ac)
ok(roots==52 and edges==32)
# Separate endpoint proof with integer inequalities only.
ok(6*10*4*64==15*1024);ok(6**15<16*5**15)
ok(741-4-64==673)
out={'status':'PASS','checks':checks,'roots':roots,'edges':edges,'representation':'literal character sums and integer cross-products; no producer import'}
(base/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
