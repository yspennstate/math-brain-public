"""Independent queue reachability audit: never import the primary checker."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import prod
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); assertions=0; cases=0; references=0
def ck(b):
 global assertions
 assert b; assertions+=1
 assert time.monotonic()-start<55
def closure(initial,edges):
 reached=set(initial); pending=list(initial)
 while pending:
  e=pending.pop()
  for h in edges[e]:
   if h not in reached:reached.add(h);pending.append(h)
 return reached
for r,w in [(2,2),(3,2),(2,3)]:
 n=r*w; gates=[{j*w+a[j] for j in range(r)} for a in product(range(w),repeat=r)]
 N=len(gates); pi=Q(1,2**r)
 for mode in range(2):
  raw=[Q(1+(e%3 if mode else 0)) for e in range(N)]
  maxrow=max(sum(raw[e] for e,g in enumerate(gates) if i in g) for i in range(n))
  x=[pi*a/maxrow for a in raw]
  D=prod(1+a for a in x)-1
  masses=[(set(e for e in range(N) if mask>>e&1),prod(x[e] for e in range(N) if mask>>e&1)/D)
          for mask in range(1,1<<N)]
  ck(sum(q for _,q in masses)==1);references+=1
  for amask in range(1,1<<n):
   A={i for i in range(n) if amask>>i&1}
   allowed={e for e,g in enumerate(gates) if g&A}
   edges=[{h for h,g in enumerate(gates) if gates[e]&g&A} for e in range(N)]
   remaining=set(allowed); groups=[]
   while remaining:
    group=closure({min(remaining)},edges)
    ck(group<=allowed)
    groups.append(group);remaining-=group
   exact=Q(0)
   for initial,q in masses:
    reachable=closure(initial,edges) if initial<=allowed else set()
    coordinates=set().union(*(gates[e]&A for e in reachable)) if reachable else set()
    can_output=(coordinates==A)
    hit_all=initial<=allowed and all(initial&g for g in groups)
    ck(can_output==hit_all)
    if can_output:exact+=q
    cases+=1
   product_mass=prod(prod(1+x[e] for e in g)-1 for g in groups)/D
   ck(exact==product_mass)
   if len({i//w for i in A})==1:
    k=len(A)
    ck(len(groups)==k)
    ck(exact*k*(1-pi)**k<=pi**(k-1))
result={'status':'PASS','assertions':assertions,'root_target_pairs':cases,'references':references,
        'seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'meaning':'Allowed actual child attachments cannot reach a target component lacking an initial root; full root-set sum independently factors.'}
(ROOT/'out/graph_audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
