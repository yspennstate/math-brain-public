"""Independent direct enumeration of the actual sign witness; no prior imports."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();rows=[]
def f(x):return 1 if x[0]==0 else (-1)**(x[1]+x[2])
for assignment in product([-1,0,1],repeat=3):
 free=[i for i,b in enumerate(assignment) if b==-1];n=len(free);t=[]
 for xs in product([0,1],repeat=n):
  x=list(assignment)
  for i,b in zip(free,xs):x[i]=b
  t.append(f(x))
 # product iteration and binary masks use reversed variable order, irrelevant here.
 N=len(t);w=[Q(sum(t[x]*(-1)**((x&s).bit_count()%2) for x in range(N)),N) for s in range(N)]
 assert sum(c*c for c in w)==1
 H=Q(0)
 for c in w:
  if c:
   p=c*c;assert p.numerator==1 and p.denominator&(p.denominator-1)==0
   H+=p*(p.denominator.bit_length()-1)
 I=sum(Q(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n))
 assert H<=2*I
 rows.append({'assignment':assignment,'H':str(H),'I':str(I)})
for kap in [Q(9,2),Q(3)]:
 U=[0,2*kap];a=Q(13);credits=[u+a-sum(U)/2 for u in U]
 false=[credits[0],credits[1]-20];true=[credits[0],credits[1]+20]
 assert false[1]<0 and min(true)>=0
 assert sum(true)/2==26-3
out={'status':'PASS','partial_assignments':27,'method':'direct assignments/characters/rational power-of-two entropy/physical edges, no prior code imports','rows':rows,'runtime_seconds':time.perf_counter()-start}
(R/'out/INDEPENDENT_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
