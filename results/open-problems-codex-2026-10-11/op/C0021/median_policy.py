"""Exact cost of the recursive discrete posterior-median rule; bounded job."""
import compute as C
from fractions import Fraction
from functools import cache
import pathlib,json,time,math
P=pathlib.Path(__file__).parent;C.limit=150;C.start=time.monotonic()
@cache
def q(t):
 if t<2:return Fraction(t)
 if t==2:return Fraction(1,2)
 a,b,c=(q(x) for x in C.nodes[t]);return a*b+a*c+b*c-2*a*b*c
@cache
def key(t):
 if t<3:return str(t)
 return '('+','.join(key(c) for c in C.nodes[t])+')'
@cache
def policy(t):
 if t==2:return (0,1)
 assert t>=3
 cs=C.nodes[t];indices=sorted(range(3),key=lambda i:(q(cs[i]),key(cs[i])))
 i=indices[1];assert cs[i]>=2
 a,b=policy(cs[i]);return C.norm(cs[:i]+(a,)+cs[i+1:]),C.norm(cs[:i]+(b,)+cs[i+1:])
@cache
def E(t):
 if t<2:return 0
 C.guard();a,b=policy(t)
 assert C.sizes[a]<C.sizes[t] and C.sizes[b]<C.sizes[t]
 return C.step(t,a,b,E)
rows=[]
try:
 for k in range(1,5):
  t=C.full(k);w=E(t);d=Fraction(w,1<<C.sizes[t]);row=dict(k=k,cost=str(d),decimal=float(d),block_exponent=1-math.log(float(d))/(k*math.log(3)),types=len(C.nodes),policy_states=E.cache_info().currsize,seconds=time.monotonic()-C.start,working_set_bytes=C.memory())
  rows.append(row);(P/'median_policy_results.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print(row,flush=True)
except RuntimeError as e:print('INCOMPLETE',e,'seconds',time.monotonic()-C.start,flush=True)
