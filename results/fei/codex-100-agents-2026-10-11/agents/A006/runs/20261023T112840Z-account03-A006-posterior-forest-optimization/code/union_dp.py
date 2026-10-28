from pathlib import Path
from fractions import Fraction as F
from itertools import product
import math,json,time
from check import log2,SCALE
R=Path(__file__).resolve().parent.parent;start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def normalized_union_law(supports):
 n=max(supports).bit_length();a={0:F(1)};b={0:F(0)};rho=F(0)
 for support in supports:
  width=support.bit_count();t=F(1,2**width);p=1-t;rho+=t
  masks=[s for s in range(1<<n) if s&~support==0];aa={};bb={}
  for union,mass in a.items():
   for s in masks:
    prob=p if s==0 else t*t/p;u=union|s
    aa[u]=aa.get(u,F(0))+mass*prob
    bb[u]=bb.get(u,F(0))+(b.get(union,F(0))+(mass if s else 0))*prob
  a,b=aa,bb
 return {u:z/rho for u,z in b.items() if u},a,rho
rows=[]
for supports in ([3,6],[3,6,24,48]):
 Q,a,rho=normalized_union_law(supports);n=max(supports).bit_length()
 local=[[s for s in range(1<<n) if s&~support==0] for support in supports]
 oracle={};count=0
 for j,support in enumerate(supports):
  t=F(1,2**support.bit_count())
  for masks in product(*local):
   if masks[j]==0:continue
   mass=t/rho*F(1,2**support.bit_count()-1);union=0
   for k,s in enumerate(masks):
    union|=s
    if k!=j:
     tk=F(1,2**supports[k].bit_count());mass*=1-tk if not s else tk*tk/(1-tk)
   oracle[union]=oracle.get(union,F(0))+mass;count+=1
 ck(Q==oracle);ck(sum(Q.values())==sum(a.values())==1)
 row={'supports':supports,'actual_anchor_oracle_events':count,'nonempty_outputs':len(Q),'total_mass':str(sum(Q.values()))}
 if len(supports)==2:
  ck(Q[2]==F(5,18));saved=json.loads((R/'out/OVERLAP.json').read_text(encoding='utf-8'))
  ck(Q=={int(k):F(v) for k,v in saved['output_masses'].items()})
 else:
  truth=[1 if all(x&s for s in supports[:2]) and any(x&s==s for s in supports[2:]) else -1 for x in range(64)]
  lo=hi=0
  for S in range(1,64):
   coefficient=sum(truth[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(64))
   l,h=log2(1/Q[S]);lo+=coefficient**2*l;hi+=coefficient**2*h
  interval=[F(lo,4096*SCALE),F(hi,4096*SCALE)]
  saved=json.loads((R/'out/PAIR.json').read_text(encoding='utf-8'))
  ck(interval==list(map(F,saved['C_interval'])));row['C_interval']=list(map(str,interval))
 rows.append(row)
ck(time.monotonic()-start<10)
result={'status':'PASS','helper_version':'A006-union-occupation-dp-v1','assertions':checks,'rows':rows,'seconds':time.monotonic()-start}
(R/'out/DP.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
