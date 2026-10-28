from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,time
import independent_arithmetic as z
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter()
checks=roots=0;branches={}
def ck(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-start>55:raise RuntimeError('55-second guard')
def verify(seed,E):
 global roots
 f=seed.copy();N=len(f);n=(N-1).bit_length();p=Q(1,N);R=len(E)
 for x in E:f[x]*=-1
 old=z.direct(seed);support=[s for s,v in enumerate(old) if v]
 ck(all((s^t).bit_count()>=3 for s,t in combinations(support,2)))
 h=z.ent(f);w=z.direct(f)
 for i in range(n):
  I=z.directional(f,1<<i);FI=z.directional(seed,1<<i)
  ck(abs(I-FI)<=2*R*p)
  if not I:continue
  h0,h1=[z.ent(z.restrict(f,i,b)) for b in (0,1)]
  up=h[1]-(h0[0]+h1[0])/2
  if not FI:
   key='independent'
   for s in support:ck(Q(abs(w[s|(1<<i)]),N)<=I)
  else:
   ck(FI>=Q(1,sum(bool(s>>i&1) for s in support)))
   key='dependent_high' if n+1>=4*R else 'dependent_low'
   if key=='dependent_high':ck(I>=Q(n+1,2)*p)
  branches[key]=branches.get(key,0)+1
  ck(up<Q(37,4)*R*I)
  ck(10*R*I-up>Q(3,2)*R*p)
 roots+=1
for s in range(8):
 for sign in (-1,1):
  seed=[sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)]
  for R in (1,2,3):
   for E in combinations(range(8),R):verify(seed,E)
for n,E in [(6,[0]),(6,[0,7]),(6,list(range(8))),(9,[0]),(9,[0,1]),(9,list(range(8)))]:
 seed=[]
 for x in range(1<<n):
  logical=sum((((x>>(3*j))&7).bit_count()%2)<<j for j in range(n//3))
  seed.append(-1 if logical==0 else 1)
 verify(seed,E)
# Exact occupied error-event replay for the reviewed stopping identity:
# a rare point error on three bits, query until the first1.
paths=[]
for x in range(8):
 tau=next((j+1 for j in range(3) if x>>j&1),3)
 paths.append((x==0,tau))
e=Q(1,8);depth=Q(sum(t for _,t in paths),8);occupation=Q(sum(t for err,t in paths if err),8)
ck(depth==Q(7,4));ck(occupation==Q(3,8));ck(occupation!=e*depth)
out={'status':'PASS','assertions':checks,'roots':roots,'branches':branches,'reviewed_occupation_guard':{'expected_depth':str(depth),'error_occupation':str(occupation),'false_independent_product':str(e*depth)},'runtime_seconds':time.perf_counter()-start,'method':'separate direct-character sums, physical edges and own atanh32 rational bounds; no main arithmetic imported'}
(RUN/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
