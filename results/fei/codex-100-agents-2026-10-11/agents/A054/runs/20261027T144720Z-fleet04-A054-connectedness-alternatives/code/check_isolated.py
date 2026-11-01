from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,permutations
from functools import lru_cache
from math import lcm,isqrt
import json,time
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
start=time.perf_counter();checks=roots=coords=nontrivial=zero=one=orbits=0
def ck(b):
 global checks
 assert b;checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('55s frozen cap')
def factor(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def add(*terms):
 out={}
 for v,c in terms:
  for p,x in v.items():out[p]=out.get(p,Q(0))+c*x
 return {p:c for p,c in out.items() if c}
def entropy(prob):
 return add(*[(factor(p.denominator),p) for p in prob if p],*[(factor(p.numerator),-p) for p in prob if p])
def sign(v):
 den=lcm(*(x.denominator for x in v.values())) if v else 1;a=b=1
 for p,x in v.items():
  k=int(x*den)
  if k>0:a*=p**k
  else:b*=p**(-k)
 return (a>b)-(a<b)
def rank(vs):
 d={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in d:v^=d[k]
   else:d[k]=v;break
 return len(d)
@lru_cache(None)
def bases(n):return [b for b in combinations(range(1,1<<n),n) if rank(b)==n]
@lru_cache(maxsize=512)
def stats(f):
 N=len(f);n=N.bit_length()-1;a=list(f);k=1
 while k<N:
  for base in range(0,N,2*k):
   for j in range(k):u,v=a[base+j],a[base+j+k];a[base+j],a[base+j+k]=u+v,u-v
  k*=2
 p=tuple(Q(x*x,N*N) for x in a)
 counts=tuple(sum(f[x]!=f[x^v] for x in range(N)) for v in range(N))
 I=Q(sum(counts[1<<i] for i in range(n)),N)
 amin=Q(min(sum(min(counts[v],N-counts[v]) for v in b) for b in bases(n)),N)
 return a,p,entropy(p),counts,I,amin
def child(f,i,b):return tuple(f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2))
fixtures=[0,65535,1,65534,43690,27030,34952,30856]
for n,masks in [(n,range(1<<(1<<n))) for n in range(4)]+[(4,fixtures)]:
 N=1<<n
 for mask in masks:
  f=tuple(-1 if mask>>x&1 else 1 for x in range(N));a,p,H,c,I,amin=stats(f);roots+=1
  for i in range(n):
   bit=1<<i;T=[s for s in range(N) if not s&bit];marg=sum(p[s|bit] for s in T)
   ck(marg==Q(c[bit],N));ck(sum(p)==1)
   indep=all(p[s|bit]==marg*(p[s]+p[s|bit]) for s in T)
   h0=stats(child(f,i,0));h1=stats(child(f,i,1));disjoint=all(u*v==0 for u,v in zip(h0[0],h1[0]))
   ck(disjoint==(indep and marg==Q(1,2)))
   Hb=add((h0[2],Q(1,2)),(h1[2],Q(1,2)));L=add((H,1),(Hb,-1))
   Ib=(h0[4]+h1[4])/2;t=(h0[5]+h1[5])/2;rel=Ib-t
   ck(I==marg+Ib);ck(rel>=0)
   if indep:
    ck(marg in [Q(0),Q(1,2),Q(1)])
    if marg==0:zero+=1;ck(all(f[x]==f[x^bit] for x in range(N)))
    elif marg==1:one+=1;ck(not L)
    else:
     nontrivial+=1;ck(L=={2:Q(2)})
     ck(all(a[s]*a[s]==a[s|bit]*a[s|bit] for s in T))
     for K in [1,2,4,8,16]:
      D=add((H,1),({2:K*I},-1));S=add(({2:K*t},1),(Hb,-1))
      ck(add((D,1),(S,1),({2:K*rel},1))==({2:Q(2)-Q(K,2)} if K!=4 else {}))
      if K>=4:ck(not(sign(D)>0 and sign(S)>=0))
   # Direct mutual-information vector, zero iff independence.
   mu=[p[s]+p[s|bit] for s in T]
   MI=add((entropy([marg,1-marg]),1),(entropy(mu),1),(H,-1))
   ck((not MI)==indep);ck(sign(MI)>=0);coords+=1
  independent=[all(p[s|1<<i]==Q(c[1<<i],N)*(p[s]+p[s|1<<i]) for s in range(N) if not s&(1<<i)) for i in range(n)]
  if all(independent):ck(sign(add((H,1),({2:2*I},-1)))<=0)
# A052 modulo-four review: FULL actual ordered input bases, shifts and output characters.
for d in range(3):
 N=1<<d
 for mask in range(1<<N):
  f=tuple(-1 if mask>>x&1 else 1 for x in range(N));base=stats(f);costs=[];M=sum(x<0 for x in f)
  for v in range(1,N):
   ck(base[3][v]%2==0)
   if d>=2:ck(base[3][v]%4==(2*M)%4);ck((N-base[3][v])%4==(2*M)%4)
  for b in permutations(range(1,N),d):
   if rank(b)!=d:continue
   for shift in range(N):
    for char in range(N):
     g=[]
     for x in range(N):
      y=shift
      for j,v in enumerate(b):
       if x>>j&1:y^=v
      g.append(f[y]*(-1 if (x&char).bit_count()%2 else 1))
     total=sum(sum(g[x]!=g[x^(1<<i)] for x in range(N)) for i in range(d))
     if d>=2:ck(total%4==(d*2*M)%4)
     costs.append(Q(total,N))
  ck(min(costs)==base[5]);q=Q(1) if d==1 else Q(4,N)
  ck((base[4]-base[5])/q==int((base[4]-base[5])/q));orbits+=1
# Arithmetic boundary: all dyadics with denominator up to2^12.
arith=0
for m in range(1,13):
 for k in range(1,1<<m,2):
  if isqrt(k)**2==k and isqrt((1<<m)-k)**2==(1<<m)-k:ck(m==1)
  arith+=1
# Non-Boolean normalized real Fourier vector (3/5,4/5) has independent
# one-bit spectrum p16/25; dyadic p fails, so it is not a counterexample.
ck(Q(9,25)+Q(16,25)==1);ck(Q(16,25) not in [0,Q(1,2),1])
ck(roots==286);ck(orbits==22)
out={'status':'PASS','assertions':checks,'roots':roots,'coordinate_cases':coords,'independent_half_coordinates':nontrivial,'independent_zero_coordinates':zero,'independent_one_coordinates':one,'complete_review_orbits':orbits,'dyadic_arithmetic_cases':arith,'seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction/prime-log exact integer-product comparisons','scope':'exhaustive n0..3; eight fixed4bit controls; independent complete small-child orbit implementation; no universal finite-to-infinite inference'}
(R/'out/EXACT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
