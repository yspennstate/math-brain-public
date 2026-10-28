from pathlib import Path
from fractions import Fraction as Q
import exact as e
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
for n in (1,2,3):
 for mask in range(1<<(1<<n)):
  g=tuple(1-2*((mask>>x)&1) for x in range(1<<n));count+=1
  direct=tuple(Q(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(g)),len(g)) for s in range(len(g)))
  e.ok(direct==e.walsh(g),'independent character-sum reproduction')
  for j in range(n):
   p=Q(sum(g[x]!=g[x^(1<<j)] for x in range(len(g))),len(g))
   e.ok(p==e.influence(direct,j),'independent edge normalization')
  e.ok(sum(x*x for x in direct)==1,'Boolean Parseval')
  if time.perf_counter()-start>55:raise RuntimeError('frozen audit cap')
# Omitting compulsory killing breaks the proposed SAME pending-potential update.
m=8;N=1<<m;c=Q(1,N);A=Q(58,13)
b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(N))
C=tuple(int(x==N-1) for x in range(N));K=tuple(b[x]-C[x] for x in range(N))
g=tuple(K[x]+v*C[x] for v in (1,-1) for x in range(N))
H=lambda h:e.entropy(e.walsh(h))
d=e.add(H(g),e.add(H(e.slice_table(g,m,0)),H(e.slice_table(g,m,1))),-Q(1,2))
p=e.influence(e.walsh(g),m)
e.ok(p==c,'literal rare tag influence')
gap=e.add(d,{2:A*p},-1);lo,hi=e.bounds(gap)
e.ok(lo>0,'no-killing refresh cannot be paid from pending influence drop')
e.le({2:7*c},d,'analytic lower bound D>=c*(m-1)')
# The growing-depth closed forms are rederived by a scalar dynamic program.
rows=[]
for n in range(1,33):
 fee=Q(0);occupation=Q(0);prob=Q(1)
 for j in range(n):
  fee+=2*prob;occupation+=prob*(n-Q(j,2));prob/=2
 e.ok(fee==4*(1-Q(1,2)**n),'exact geometric cost')
 e.ok(2*n-fee>=0,'all stopped terminal entropy retained')
 rows.append({'n':n,'fee':str(fee),'terminal_entropy':str(2*n-fee)})
out={'status':'PASS','direct_functions':count,'assertions':e.checks,'no_killing_gap_nats':[str(lo),str(hi)],'m':m,'p':str(p),'recurrence_rows':rows,'seconds':time.perf_counter()-start}
(R/'out/adversary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('recurrence_rows','no_killing_gap_nats')}))
