from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import time,json,sys
ROOT=Path(__file__).resolve().parents[1]
ns={'__file__':str(ROOT/'code/check_exterior.py')}
exec((ROOT/'code/check_exterior.py').read_text(encoding='utf-8').split('zs_all=')[0],ns)
entropy,add,influence,nonneg,restrict,phi=[ns[k] for k in ['entropy','add','influence','nonneg','restrict','phi']]
start=time.monotonic();pilot='--pilot' in sys.argv;cap=55 if pilot else 180
checks=states=edges=opened=firsts=0;cross=[(0,2),(0,3),(1,2),(1,3)]
def ck(x):
 global checks
 assert x;checks+=1
def account(vals,rem,zs):
 out=Q(0)
 for i,j in [(0,1),(2,3)]:
  rr=[x for x in [i,j] if x in rem]
  if len(rr)==2:out+=4*sum(influence(vals,rem.index(x)) for x in rr)
  elif len(rr)==1:out+=2
 return out
for code in range(1 if pilot else 16):
 graph=[(0,1),(2,3)]+[e for k,e in enumerate(cross) if code>>k&1]
 b=tuple((-1)**sum(((x>>i)&1)*((x>>j)&1) for i,j in graph) for x in range(16))
 for gt in range(16):
  g=tuple(1 if gt>>x&1 else -1 for x in range(4));mu=Q(sum(g),4)
  @lru_cache(None)
  def state(zs):
   bb,rem=restrict(b,zs);t=Q(1,1<<len(rem)) if 1 not in zs else Q(0)
   vals=tuple(g[y] if t and z==0 else bb[z] for y in range(4) for z in range(len(bb)))
   return vals,rem,t,account(vals,rem,zs)
  for zs in product([None,0,1],repeat=4):
   if time.monotonic()-start>cap:raise RuntimeError('frozen runtime')
   vals,rem,t,E=state(zs);states+=1
   for j,i in enumerate(rem):
    kids=[]
    for value in [0,1]:
     zc=list(zs);zc[i]=value;kids.append(state(tuple(zc)))
    D=add((1,entropy(vals)),(-Q(1,2),entropy(kids[0][0])),(-Q(1,2),entropy(kids[1][0])))
    release=E-(kids[0][3]+kids[1][3])/2
    ck(release>=2);ck(nonneg(add((1,{2:release}),(-1,D))))
    if zs[i^1] is None:
     ck(influence(vals,j)==(Q(1,2)+t*(1-mu) if t else Q(1,2)));firsts+=1
    else:opened+=1
    delta=add((1,phi(t)),(-Q(1,2),phi(kids[0][2])),(-Q(1,2),phi(kids[1][2])))
    ck(delta==({2:t} if t else {}));edges+=1
out={'status':'PASS','pilot':pilot,'graphs':1 if pilot else 16,'states':states,'exterior_edges':edges,'first_pair_edges':firsts,'open_partner_edges':opened,'exact_assertions':checks,'seconds':time.monotonic()-start,'source_scope':'exposed-splice exterior theorem only; no source6 claim for arbitrary graph bias'}
(ROOT/'out'/('graph_pilot.json' if pilot else 'graph_validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
