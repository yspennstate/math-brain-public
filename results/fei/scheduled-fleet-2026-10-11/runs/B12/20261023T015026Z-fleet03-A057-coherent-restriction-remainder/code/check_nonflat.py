"""Exact v1 audit of inherited nonflat source and its unchanged reserve."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,itertools
ROOT=Path(__file__).resolve().parents[1];(ROOT/'out').mkdir(exist_ok=True)
start=time.monotonic();assertions=0;roots=queries=biased=zeroqueries=0
def ck(b):
 global assertions
 assert b;assertions+=1
def walsh(vals):
 w=list(vals);h=1
 while h<len(w):
  for j in range(0,len(w),h*2):
   for k in range(j,j+h):
    a,b=w[k],w[k+h];w[k],w[k+h]=a+b,a-b
  h*=2
 return w
@lru_cache(None)
def factors(n):
 ans={};p=2
 while p*p<=n:
  while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
  p+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def add(*terms):
 out={}
 for coef,a in terms:
  for p,v in a.items():out[p]=out.get(p,Q(0))+coef*v
 return {p:v for p,v in out.items() if v}
def entropy(vals):
 N=len(vals);n=N.bit_length()-1;ans={2:Q(2*n)}
 for w in walsh(vals):
  if w:
   for p,e in factors(abs(w)).items():ans[p]=ans.get(p,Q(0))-Q(2*w*w*e,N*N)
 return {p:v for p,v in ans.items() if v}
def lnseries(y):
 z=(y-1)/(y+1);total=Q(0);power=z
 for k in range(36):total+=2*power/(2*k+1);power*=z*z
 tail=2*abs(z)**73/(73*(1-z*z))
 return total-tail,total+tail
LN2=lnseries(Q(2))
@lru_cache(None)
def log2interval(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;lo,hi=lnseries(Q(p,1<<k))
 return k+lo/LN2[1],k+hi/LN2[0]
def interval(expr):
 lo=hi=Q(0)
 for p,c in expr.items():
  l,h=log2interval(p)
  lo+=c*(l if c>=0 else h);hi+=c*(h if c>=0 else l)
 return lo,hi
def nonneg(expr):
 if not expr:return True
 return interval(expr)[0]>=0
def phi(q):
 if q==0:return {}
 ans={}
 for p,e in factors(q.denominator).items():ans[p]=ans.get(p,Q(0))+q*e
 for p,e in factors(q.numerator).items():ans[p]=ans.get(p,Q(0))-q*e
 return {p:v for p,v in ans.items() if v}
def influence(vals,i):
 N=len(vals);return Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N)
worst_lower=None
for m,ns in [(4,range(4)),(6,range(3))]:
 c=Q(1,1<<m);s=Q(1,1<<(m//2));b=[]
 for x in range(1<<m):
  pairs=sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,m,2))
  b.append((-1)**pairs)
 ck(Q(sum(b),len(b))==s)
 for n in ns:
  for table in range(1<<(1<<n)):
   if time.monotonic()-start>55:raise RuntimeError('frozen55-second cap reached')
   g=[1 if (table>>y)&1 else -1 for y in range(1<<n)]
   mu=Q(sum(g),len(g));biased+=int(mu not in [-1,0,1])
   f0=[g[y] for y in range(1<<n) for x in range(1<<m)]
   f1=[g[y] if x==0 else b[x] for y in range(1<<n) for x in range(1<<m)]
   W=f0+f1
   d=influence(W,m+n);ck(d==(1-c-mu*(s-c))/2);ck(d>=Q(3,8));ck(d<=Q(9,16))
   D=add((1,entropy(W)),(-Q(1,2),entropy(g)),(-Q(1,2),entropy(f1)))
   ck(nonneg(D));ck(nonneg(add((1,{2:Q(2)}),(-1,D))))
   # Pay the maximum L=1 continuation bill, stronger than any single delta<=1.
   tax=m*c/2
   residual=add((1,{2:6*d-tax-d/3}),(-1,D));ck(nonneg(residual))
   lower=interval(add((1,{2:6*d-tax}),(-1,D)))[0]
   if worst_lower is None or lower<worst_lower:worst_lower=lower
   for i in range(n):
    delta=influence(g,i);actual=influence(f1,m+i);ck(actual==c*delta)
    Ti=m*c*delta/2;ck(Ti<=Q(1,8));queries+=1;zeroqueries+=delta==0
   roots+=1
# Exact original fine reserve cancellation, including biased/nonflat actual cores.
for m in [4,6,8]:
 c=Q(1,1<<m);a=(1+c)/2
 for ps in [[Q(1)],[Q(1,2),Q(1,2)],[Q(1,4),Q(3,8),Q(3,8)]]:
  for Vs in itertools.product([Q(0),Q(3,4),Q(1)],repeat=len(ps)):
   parent=add(*[(V,phi(a*p)) for p,V in zip(ps,Vs)])
   children=add(*[(V/2,phi(p)) for p,V in zip(ps,Vs)],*[(V/2,phi(c*p)) for p,V in zip(ps,Vs)])
   Vbar=sum(p*V for p,V in zip(ps,Vs))
   release=add((Vbar,phi(a)),(-Vbar/2,phi(c)))
   ck(add((1,parent),(-1,children),(-1,release))=={});ck(nonneg(release))
for m in range(4,129):ck(Q(m,2*(1<<m))<=Q(1,8))
# Analytic all-r obstruction reduced to finite rational comparisons, no huge table.
e_upper=Q(5,2)+Q(2,9);ck(e_upper<3);ck(Q(48,12)>Q(27,8))
out={'status':'PASS','roots':roots,'queried_core_coordinates':queries,'biased_nonconstant_core_roots':biased,
 'zero_influence_queries':zeroqueries,'exact_assertions':assertions,
 'worst_remaining_bank_lower_rational':[worst_lower.numerator,worst_lower.denominator],
 'elapsed_seconds':time.monotonic()-start,'arithmetic':'integer Walsh/Fraction/prime-log intervals with36 atanh terms and proved tail'}
(ROOT/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
