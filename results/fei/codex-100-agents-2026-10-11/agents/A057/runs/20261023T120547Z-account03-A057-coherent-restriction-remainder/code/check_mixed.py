from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import time,json
ROOT=Path(__file__).resolve().parents[1]
ns={'__file__':str(ROOT/'code/check_character.py')}
exec((ROOT/'code/check_character.py').read_text(encoding='utf-8').split('domains=')[0],ns)
add,phi,entropy,nonneg,physical=[ns[k] for k in ['add','phi','entropy','nonneg','physical']]
start=time.monotonic();checks=states=xedges=tagedges=oldpositive=0;c=Q(1,16);B=Q(7);qseen=set()
def ck(b):
 global checks
 assert b;checks+=1
 if time.monotonic()-start>55:raise RuntimeError('frozen55s cap')
def restrict(vals,fix):
 n=len(vals).bit_length()-1;rem=[i for i in range(n) if i not in fix]
 return tuple(vals[sum(v<<i for i,v in fix.items())+sum((a>>j&1)<<i for j,i in enumerate(rem))] for a in range(1<<len(rem)))
def ticket(t,q):return add((q,phi(t)),(t,phi(q)),(1,{2:Q(9,2)*t*q}))
G=tuple(-1 if y==0 else 1 for y in range(8));HH=entropy(physical(4,G,2,1))
cores=[tuple(G[y] for y in range(8) if y&1==bit) for bit in [0,1]]
old=add((1,HH),(-Q(1,2),entropy(physical(4,cores[0],2,1))),(-Q(1,2),entropy(physical(4,cores[1],2,1))))
ck(nonneg(add((1,old),(-1,{2:c/1000}))));oldpositive=1
for g in cores:
 q=Q(sum(g),len(g))**2;qseen.add(str(q));full=physical(4,g,2,1)
 @lru_cache(None)
 def state(xs,ts):
  fix={i:v for i,v in enumerate(xs) if v is not None};fix.update({6+i:v for i,v in enumerate(ts) if v is not None})
  vals=restrict(full,fix);r=sum(v is not None for v in xs)
  t=Q(1,1<<(4-r)) if 0 not in xs else Q(0)
  T=ticket(t,q) if None in ts else {};return vals,t,T
 for xs in product([None,0,1],repeat=4):
  r=sum(v is not None for v in xs)
  if r>2:continue
  for ts in product([None,0,1],repeat=2):
   vals,t,T=state(xs,ts);states+=1;H=entropy(vals)
   # Uniform pathwise cash proof includes either already-spent or pending last-tag bill, once.
   ck(B-2*c-2*r-Q(13,8)>=B/8)
   for i,v in enumerate(xs):
    if v is not None or r==2:continue
    cs=[];tickets=[]
    for bit in [0,1]:
     xx=list(xs);xx[i]=bit;vv,tt,tic=state(tuple(xx),ts);cs.append(entropy(vv));tickets.append(tic)
    D=add((1,H),(-Q(1,2),cs[0]),(-Q(1,2),cs[1]));ck(nonneg(D));ck(nonneg(add((1,{2:2}),(-1,D))))
    if None in ts:
     diff=add((1,T),(-Q(1,2),tickets[0]),(-Q(1,2),tickets[1]))
     ck(diff==({2:t*q} if t*q else {}))
    xedges+=1
   for j,v in enumerate(ts):
    if v is not None:continue
    cs=[]
    for bit in [0,1]:
     ss=list(ts);ss[j]=bit;vv,tt,tic=state(xs,tuple(ss));cs.append(entropy(vv))
    D=add((1,H),(-Q(1,2),cs[0]),(-Q(1,2),cs[1]))
    if ts.count(None)>1:ck(D=={})
    else:ck(nonneg(add((1,T),(-1,D))))
    tagedges+=1
for m in range(4,257,4):
 cc=Q(1,1<<m);bank=2*m-4*m*cc;maxT=Q(1,1<<(m//2))*(m/Q(2)+Q(9,2))
 ck(bank-2*cc-m-maxT>=bank/8)
out={'status':'PASS','states':states,'X_query_edges':xedges,'tag_query_edges':tagedges,'positive_old_core_fixture':oldpositive,'current_q_values':sorted(qseen),'exact_assertions':checks,'seconds':time.monotonic()-start,'scope':'all local edges of594 states; arbitrary policies by analytic pathwise invariant, not exhaustive policy enumeration'}
(ROOT/'out/mixed.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
