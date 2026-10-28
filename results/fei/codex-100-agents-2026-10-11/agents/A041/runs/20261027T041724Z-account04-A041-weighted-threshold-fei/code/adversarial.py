import check as C
from fractions import Fraction as F
import json,time
start=time.perf_counter()
t=C.truth(2);a=12;b=3
rows={tuple(t[x|y] for y in [0,1,2,3]) for x in [0,4,8,12]}
C.check(len(rows)==2)
C.check(C.truth(1)==[1 if x.bit_count()>=2 else -1 for x in range(8)])
for m in [3,4,5,6]:
 for w in [F(5,4),F(3,2),F(7,4)]:
  table=[1 if w*((x&1)>0)+w*((x&2)>0)+(x>>2).bit_count()>=w+1 else -1 for x in range(1<<(m+2))]
  C.check(table==C.truth(m))
r={'status':'PASS','checks':C.checks,'cases':14,'runtime_seconds':time.perf_counter()-start,'cuts':['m=1 symmetric','m=2 nonprime rare OR block'],'real_weight_identity':'checked rational w values only; all real w in(1,2) follows analytically'}
(C.ROOT/'out/ADVERSARIAL.json').write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r))
