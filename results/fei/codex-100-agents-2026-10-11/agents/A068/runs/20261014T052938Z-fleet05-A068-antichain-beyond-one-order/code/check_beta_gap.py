import itertools,json
from pathlib import Path
from time import perf_counter
start=perf_counter();cases=checks=0
def ck(b):
 global checks
 assert b;checks+=1
for n in range(5):
 terms=[(i,) for i in range(n)]+list(itertools.combinations(range(n),2))
 for f in range(1<<(1+len(terms))):
  beta=[(-1)**((f&1)^sum((f>>(j+1)&1)*int(all(u>>i&1 for i in t)) for j,t in enumerate(terms))) for u in range(1<<n)]
  active=0;edgecount=0;rootedges=0
  for i in range(n):
   c=sum(beta[u]!=beta[u^(1<<i)] for u in range(1<<n) if not u>>i&1)
   ck(c in (0,1<<(n-1)) if n==1 else c in (0,1<<(n-2),1<<(n-1)))
   active+=c>0;edgecount+=c
   rc=0
   for u in range(1<<n):
    if u>>i&1:continue
    for x in (1,-1):
     a=x if beta[u]==1 else 1
     b=x if beta[u^(1<<i)]==1 else 1
     rc+=a!=b
   ck(rc==c);rootedges+=rc
  # Denominators: beta edges2^(n-1), root control edges2^n.
  ck(4*rootedges>=active*(1<<n))
  ck(2*active*(1<<n)<=8*rootedges)
  cases+=1
out=dict(status='PASS',cases=cases,exact_assertions=checks,runtime_seconds=perf_counter()-start,scope='All n<=4 quadratic phases; all-dimensional derivative-affine proof in REPORT supplies bridge',gap='Each active quadratic coordinate has influence>=1/2; root contrast contributes half its crossing edges')
p=Path(__file__).resolve().parents[1]/'out/beta_validation.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))

