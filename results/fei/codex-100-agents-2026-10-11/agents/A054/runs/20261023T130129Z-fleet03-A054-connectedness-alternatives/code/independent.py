from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
from functools import lru_cache
from math import lcm
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=maps=0
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen55s cap')
def span(vs):
 s={0}
 for v in vs:s|={x^v for x in s}
 return s
def ordered_bases(d):return [b for b in permutations(range(1,1<<d),d) if len(span(b))==1<<d]
def fac(z):
 p=2;d={}
 while p*p<=z:
  while z%p==0:d[p]=d.get(p,0)+1;z//=p
  p+=1
 if z>1:d[z]=d.get(z,0)+1
 return d
def add(*terms):
 d={}
 for a,b in terms:
  for p,q in a.items():d[p]=d.get(p,F(0))+q*b
 return {p:q for p,q in d.items() if q}
def sgn(d):
 L=lcm(*(q.denominator for q in d.values())) if d else 1;a=b=1
 for p,q in d.items():
  z=int(q*L)
  if z>0:a*=p**z
  else:b*=p**(-z)
 return (a>b)-(a<b)
@lru_cache(None)
def H(vals):
 N=len(vals);d={}
 for s in range(N):
  a=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals));q=F(a*a,N*N)
  if q:d=add((d,1),(fac(q.denominator),q),(fac(q.numerator),-q))
 return d
def I(vals):
 N=len(vals);n=N.bit_length()-1
 return F(sum(vals[x]!=vals[x^(1<<j)] for x in range(N) for j in range(n)),N)
def trans(vals,b):
 out=[]
 for y in range(len(vals)):
  x=0
  for j,v in enumerate(b):
   if y>>j&1:x^=v
  out.append(vals[x])
 return tuple(out)
@lru_cache(None)
def amin(vals):
 n=len(vals).bit_length()-1;N=len(vals)
 return min(I(trans(tuple(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(vals)),b)) for s in range(N) for b in ordered_bases(n))
def scatter(x,ids):return sum(((x>>j)&1)<<i for j,i in enumerate(ids))
def children(vals,A):
 C=[i for i in range(len(vals).bit_length()-1) if i not in A]
 return [tuple(vals[scatter(u,A)|scatter(x,C)] for x in range(1<<len(C))) for u in range(4)]
point=tuple(-1 if x==0 else 1 for x in range(8));Dpoint=add((H(point),1),({2:2*I(point)},-1));ck(sgn(Dpoint)>0)
for n in range(4):
 for mask in range(1<<(1<<n)):
  vals=tuple(-1 if mask>>x&1 else 1 for x in range(1<<n));D=add((H(vals),1),({2:2*I(vals)},-1))
  ck(sgn(D)<=0 if n<3 else sgn(add((Dpoint,1),(D,-1)))>=0)
  ck(sgn(add((H(vals),1),({2:3*I(vals)},-1)))<=0)
ck(2**20>3**9)
point4=tuple(-1 if x==0 else 1 for x in range(16));D4=add((H(point4),1),({2:3*I(point4)},-1))
ck(D4=={2:F(9,2),7:-F(49,32)});ck(sgn(D4)>0)
ex=json.loads((R/'out/EXAMPLES.json').read_text(encoding='utf-8'));results=[]
ex['explicit_critical_rematch']={'n':3,'mask':1,'A':[0,1],'branch':1,'character':1,'sign':1,'K':2,'critical_fixture':True,'J_count':8,'phase_price_sign':1}
for key,e in ex.items():
 n=e['n'];N=1<<n;A=e['A'];C=[i for i in range(n) if i not in A];Nc=1<<len(C);K=e['K']
 root=tuple(-1 if e['mask']>>x&1 else 1 for x in range(N));new=list(root)
 for x in range(Nc):new[scatter(e['branch'],A)|scatter(x,C)]*=e['sign']*(-1 if (e['character']&x).bit_count()%2 else 1)
 new=tuple(new);best=None;bestvals=None;count=0
 for qb in ordered_bases(2):
  for wb in ordered_bases(len(C)):
   for z in product(range(Nc),repeat=2):
    b=tuple(scatter(q,A)|scatter(t,C) for q,t in zip(qb,z))+tuple(scatter(v,C) for v in wb)
    ck(len(span(b))==N);out=trans(new,b);cost=I(out);maps+=1;count+=1
    if best is None or cost<best:best=cost;bestvals=out
 ck(best==F(e['J_count'],N));ck(H(bestvals)==H(new))
 oldch=children(root,A);newch=children(new,A);optch=children(bestvals,[0,1])
 hbar=add(*[(H(g),F(1,4)) for g in oldch]);t=sum(map(amin,oldch))/4
 ck(add(*[(H(g),F(1,4)) for g in newch])==hbar);ck(sum(map(amin,newch))/4==t)
 ck(add(*[(H(g),F(1,4)) for g in optch])==hbar);ck(sum(map(amin,optch))/4==t)
 release=I(new)-best;Pi=add((H(root),1),(H(new),-1),({2:K*(best-I(root))},1));Omega=add((Pi,1),({2:K*release},1))
 ck(sgn(Pi)==e['phase_price_sign']);D=add((H(root),1),({2:K*I(root)},-1));S=add(({2:K*t},1),(hbar,-1));L=add((H(new),1),(hbar,-1))
 for u in [F(0),release]:
  rhs=add((L,1),({2:K*(best+u-t)},-1),(Omega,1),({2:K*(release-u)},-1))
  ck(rhs==add((D,1),(S,1)))
 if e['critical_fixture']:ck(sgn(Pi)>=0);ck(sgn(S)>=0)
 results.append({'example':key,'ordered_actual_input_maps':count,'I0':str(I(root)),'Inew':str(I(new)),'J':str(best),'release':str(release),'phase_price_sign':sgn(Pi),'original_D_plus_S_sign':sgn(add((D,1),(S,1))),'uncompensated_new_bill_sign':sgn(add((L,1),({2:K*(best-t)},-1)))})
 if key=='explicit_critical_rematch':
  ck([x for x,v in enumerate(new) if v==-1]==[0,5]);ck(I(root)==F(3,4) and I(new)==F(3,2) and best==1 and release==F(1,2))
  ck(H(new)=={2:F(2)} and S=={});ck(Pi==Dpoint);ck(add((L,1),({2:K*(best-t)},-1))=={})
ck(2**144>7**49)
out={'status':'PASS','assertions':checks,'examples':len(ex),'ordered_actual_maps':maps,'seconds':time.perf_counter()-start,'method':'independent direct character sums, EVERY ordered partition-preserving input map, full character/basis child minima, exact integer-product signs','results':results}
(R/'out/INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='results'}))
