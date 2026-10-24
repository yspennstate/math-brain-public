"""Exact optimum of all recursively posterior-median rules, allowing arbitrary adaptive ties."""
import compute as C
from fractions import Fraction
from functools import cache
import pathlib,json,time
P=pathlib.Path(__file__).parent;C.start=time.monotonic();C.limit=120
@cache
def q(t):
 if t<2:return Fraction(t)
 if t==2:return Fraction(1,2)
 a,b,c=(q(x) for x in C.nodes[t]);return a*b+a*c+b*c-2*a*b*c
@cache
def allowed(t):
 if t<2:return ()
 if t==2:return ((0,1),)
 cs=C.nodes[t];median=sorted(q(c) for c in cs)[1];out=set()
 for i,c in enumerate(cs):
  if q(c)!=median or (i and c==cs[i-1]):continue
  assert c>=2
  for a,b in allowed(c):out.add((C.norm(cs[:i]+(a,)+cs[i+1:]),C.norm(cs[:i]+(b,)+cs[i+1:])))
 return tuple(sorted(out))
@cache
def best(t):
 if t<2:return 0
 C.guard();return min(C.step(t,a,b,best) for a,b in allowed(t))
rows=[]
try:
 for k in (1,2,3):
  t=C.full(k);d=Fraction(best(t),1<<C.sizes[t]);r=dict(k=k,optimal_median_cost=str(d),decimal=float(d),types=len(C.nodes),states=best.cache_info().currsize,seconds=time.monotonic()-C.start)
  rows.append(r);(P/'median_optimal_ties.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print(r,flush=True)
  if k==3:
   reachable=set()
   def visit(s):
    if s in reachable:return
    reachable.add(s)
    for a,b in allowed(s):visit(a);visit(b)
   visit(t)
   cert=dict(root=t,nodes=C.nodes,sizes=C.sizes,rows=[dict(id=s,weight=best(s),moves=allowed(s)) for s in sorted(reachable)])
   (P/'median_ties_certificate.json').write_text(json.dumps(cert),encoding='utf8')
except RuntimeError as e:print('INCOMPLETE',e,flush=True)
