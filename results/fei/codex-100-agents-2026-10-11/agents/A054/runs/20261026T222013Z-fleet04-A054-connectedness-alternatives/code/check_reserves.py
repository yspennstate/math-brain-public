from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
from math import lcm
import time,json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
start=time.perf_counter();checks=blocks=comparisons=0
def ck(b):
 global checks
 assert b
 checks+=1
 if time.perf_counter()-start>55: raise RuntimeError('55s frozen cap')
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def add(*terms):
 d={}
 for v,c in terms:
  for p,b in v.items():d[p]=d.get(p,Q(0))+c*b
 return {p:b for p,b in d.items() if b}
def logq(q):
 q=Q(q);return add((factors(q.numerator),1),(factors(q.denominator),-1))
def sign(v):
 d=lcm(*(b.denominator for b in v.values())) if v else 1
 a=b=1
 for p,c in v.items():
  k=int(c*d)
  if k>0:a*=p**k
  else:b*=p**(-k)
 return (a>b)-(a<b)
def entropy(probs):
 return add(*[(logq(q),-q) for q in probs if q])
def rank(vs):
 piv={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in piv:v^=piv[k]
   else:piv[k]=v;break
 return len(piv)
@lru_cache(None)
def bases(n):return tuple(b for b in combinations(range(1,1<<n),n) if rank(b)==n)
@lru_cache(None)
def stats(f):
 N=len(f);n=N.bit_length()-1
 # Direct characters, independent of the previous stage's FWHT.
 coeff=tuple(sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N))
 p=tuple(Q(c*c,N*N) for c in coeff)
 w=tuple(Q(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N))
 a=min(sum((min(w[v],1-w[v]) for v in b),Q(0)) for b in bases(n))
 return coeff,p,entropy(p),w,sum((w[1<<i] for i in range(n)),Q(0)),a
def pack(x,ids):return sum(((x>>j)&1)<<i for j,i in enumerate(ids))
critical=0;negative_reserve=0;maxrelease=Q(0);example=None
for n in range(4):
 N=1<<n
 for mask in range(1<<N):
  f=tuple(-1 if mask>>x&1 else 1 for x in range(N));cf,p,H,w,I,a=stats(f)
  ck(sum(p)==1);ck(I==sum((p[s]*s.bit_count() for s in range(N)),Q(0)))
  for r in range(1,n):
   for A in combinations(range(n),r):
    C=tuple(i for i in range(n) if i not in A)
    children=[tuple(f[pack(x,A)|pack(y,C)] for y in range(1<<len(C))) for x in range(1<<r)]
    ch=[stats(g) for g in children];den=1<<r
    Hb=add(*[(v[2],Q(1,den)) for v in ch]);Ib=sum(v[4] for v in ch)/den;t=sum(v[5] for v in ch)/den
    sig=sum(w[1<<i] for i in A);rel=Ib-t
    ck(I==sig+Ib);ck(rel>=0);maxrelease=max(maxrelease,rel)
    L=add((H,1),(Hb,-1))
    # Direct block marginal entropy/conditional term and physical-row JS.
    mu=[sum(p[pack(z,A)|pack(T,C)] for z in range(den)) for T in range(1<<len(C))]
    B=add((H,1),(entropy(mu),-1));JS=add((entropy(mu),1),(Hb,-1))
    ck(sign(B)>=0);ck(sign(JS)>=0)
    marg=add(*[(entropy([w[1<<i],1-w[1<<i]]),1) for i in A])
    ck(sign(add((B,1),(marg,-1)))<=0)
    ck(sign(add((JS,1),({2:3*sig},-1)))<=0)
    for K in [2,3,4,8,16]:
     D=add((H,1),({2:K*I},-1));S=add(({2:K*t},1),(Hb,-1))
     lhs=add((D,1),(S,1),({2:K*rel},1));rhs=add((L,1),({2:K*sig},-1))
     ck(lhs==rhs)
     x=sig/r;binary=entropy([x,1-x])
     intermediate=add((binary,r),({2:(3-K)*sig},1))
     ck(sign(add((lhs,1),(intermediate,-1)))<=0)
     cap=logq(1+Q(2)**(3-K));cap={p:r*b for p,b in cap.items()}
     ck(sign(add((intermediate,1),(cap,-1)))<=0)
     ck(sign(add((lhs,1),(cap,-1)))<=0)
     if sign(S)<0:negative_reserve+=1
     if n==3 and mask==1 and K==2:
      ck(sign(S)>=0);ck(sign(D)>0);critical+=1
      if example is None:example={'n':n,'mask':mask,'A':A,'sigma':str(sig),'Rchild':str(rel),'K':K}
     comparisons+=1
    blocks+=1
ck(blocks==1568);ck(comparisons==7840);ck(critical==6)
# Independent scalar capacity check at the optimizer and both boundaries.
scalar=0
for K in [2,3,4,8,16]:
 p=1/(1+Q(2)**(K-3));cap=logq(1+Q(2)**(3-K))
 for x in [Q(0),p,Q(1)]:
  val=add((entropy([x,1-x]),1),({2:(3-K)*x},1))
  ck(sign(add((cap,1),(val,-1)))>=0)
  if x==p:ck(cap==val)
  scalar+=1
out={'status':'PASS','roots':278,'blocks':blocks,'block_rate_comparisons':comparisons,'assertions':checks,'critical_guard_blocks':critical,'negative_reserve_comparisons':negative_reserve,'maximum_child_release':str(maxrelease),'critical_example':example,'scalar_boundary_optimizer_checks':scalar,'seconds':time.perf_counter()-start,'arithmetic':'integer character sums; Fraction; exact prime-log integer-product comparisons','formal_status':'analytic proof plus exact finite validation; independent review pending'}
(R/'out/EXACT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
