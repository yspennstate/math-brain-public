from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
R=Path(__file__).resolve().parent.parent
start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
supports=[3,6];local=[[z for z in range(8) if z&~s==0] for s in supports]
def mass(z):return F(3,4) if z==0 else F(1,12)
runs={};out={};rho=F(1,2)
for j in range(2):
 for anchor in local[j][1:]:
  for other in local[1-j]:
   masks=[0,0];masks[j]=anchor;masks[1-j]=other
   actual=(j,tuple(masks));ck(actual not in runs)
   probability=F(1,2)*F(1,3)*mass(other)
   ck(probability==mass(masks[0])*mass(masks[1])/rho)
   runs[actual]=probability;A=masks[0]|masks[1]
   out[A]=out.get(A,F(0))+probability
ck(len(runs)==24 and sum(runs.values())==1 and sum(out.values())==1)
ck(set(out)==set(range(1,8)))
for A in out:
 alternative=sum((sum(bool(x) for x in masks)*mass(masks[0])*mass(masks[1])/rho for masks in product(*local) if masks[0]|masks[1]==A),F(0))
 ck(alternative==out[A])
center=[(key,value) for key,value in runs.items() if key[1][0]|key[1][1]==2]
ck(len(center)==4);ck(out[2]==F(5,18))
posterior=sorted(value/out[2] for key,value in center)
ck(posterior==[F(1,20),F(1,20),F(9,20),F(9,20)])
ck(len({key[1] for key,value in center})==3)
# The invalid unique-allocation shortcut discards two genuine ownership options.
invalid=2*mass(2)*mass(2)/rho
ck(invalid==F(1,36) and invalid!=out[2])
ck(time.monotonic()-start<10)
result={'status':'PASS','actual_runs':len(runs),'assertions':checks,'output_masses':{str(k):str(v) for k,v in out.items()},'center_posterior':list(map(str,posterior)),'invalid_unique_allocation_mass':str(invalid),'seconds':time.monotonic()-start}
(R/'out/OVERLAP.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
