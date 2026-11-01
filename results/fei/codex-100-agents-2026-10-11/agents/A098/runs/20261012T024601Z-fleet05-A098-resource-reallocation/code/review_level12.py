from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
run=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(v):
 global checks
 checks+=1
 assert v
@lru_cache(None)
def ln(q):
 q=F(q);check(q>0);e=0
 while q>=2:q/=2;e+=1
 while q<1:q*=2;e-=1
 def core(z):
  t=(z-1)/(z+1); s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(20)),F(0));r=2*t**41/(41*(1-t*t))
  return s,s+r
 lo,hi=core(q);a,b=core(F(2))
 return (lo+e*a,hi+e*b) if e>=0 else (lo+e*b,hi+e*a)
@lru_cache(None)
def log(q):
 a,b=ln(F(q));c,d=ln(F(2));v=[a/c,a/d,b/c,b/d];return min(v),max(v)
def entropy_mass(v):
 if not v:return F(0),F(0)
 a,b=log(1/v);return v*a,v*b
def phi(x,y):
 if not x or not y:return F(0),F(0)
 a,b=log((x+y)/x);c,d=log((x+y)/y);return x*a+y*c,x*b+y*d
functions=0;max_t=F(0);max_h=F(0)
for n in range(4):
 N=1<<n
 for table in range(1<<N):
  vals=[1 if table>>x&1 else -1 for x in range(N)]
  coeff=[F(sum(vals[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N)]
  p=[v*v for v in coeff];check(sum(p)==1)
  influences=[]
  for i in range(n):
   eps=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N);influences.append(eps)
   row=sum((p[(1<<i)|(1<<j)] for j in range(n) if j!=i),F(0))
   check(eps==sum((p[s] for s in range(N) if s>>i&1),F(0)))
   # Reconstruct the signed derivative and its actual nonzero support explicitly.
   hs=[F(vals[x]-vals[x^(1<<i)],2) for x in range(N) if not x>>i&1]
   check(set(hs)<={F(-1),F(0),F(1)})
   check(sum(h*h for h in hs)/len(hs)==eps)
   if eps:
    lo,_=ln(2/eps);check(row<=2*eps*eps*lo)
   else:check(row==0)
  I=sum(influences,F(0));H2=sum((entropy_mass(p[s])[1] for s in range(N) if s.bit_count()==2),F(0))
  T12=sum((phi(p[1<<i],p[(1<<i)|(1<<j)])[1] for i in range(n) for j in range(n) if j!=i),F(0))
  check(H2<=F(155600,50301)*I);check(T12<=F(16700,2187)*I)
  if I:max_t=max(max_t,T12/I);max_h=max(max_h,H2/I)
  functions+=1
  if time.perf_counter()-start>60:raise RuntimeError('Frozen runtime exceeded')
check(functions==278)
controls=[]
for n in [8,16]:
 x=F(1,2*n);y=F(1,n*(n-1));lo,hi=phi(x,y);t=n*(n-1)*lo;ll,_=log(F(n-1,2))
 check(n*x+F(n*(n-1),2)*y==1)
 check(t>=ll)
 controls.append({'dimension':n,'actual_Boolean':False,'spectral_energy':'3/2','T12_lower':str(t),'divergent_family_lower':'(2/3) log2((n-1)/2) for T12/I'})
check(F(16700,2187)<8)
result={'helper':'A098-independent-level12-review-v1','Boolean_functions':278,'non_Boolean_controls':2,'assertions_passed':checks,'failures':0,'runtime_seconds':time.perf_counter()-start,'H2_over_I_upper_max':str(max_h),'T12_over_I_upper_max':str(max_t),'controls':controls,'scope':'Analytic proof supplies all-dimensional result; independent finite check supplies only n<=3'}
(run/'out/LEVEL12_REVIEW_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
