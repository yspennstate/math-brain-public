from fractions import Fraction as Q
from functools import lru_cache
def add(*terms):
 out={}
 for c,x in terms:
  for p,v in x.items():
   out[p]=out.get(p,Q(0))+c*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def factors(n):
 out={}; p=2
 while p*p<=n:
  while n%p==0: out[p]=out.get(p,0)+1; n//=p
  p+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def logvec(q):
 out={}
 for s,n in [(1,q.numerator),(-1,q.denominator)]:
  for p,v in factors(n).items():out[p]=out.get(p,Q(0))+s*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def g(q):
 if not q:return {}
 return {p:-q*q*v for p,v in logvec(q*q).items()}
def entropy(v):return add(*[(Q(1),g(x)) for x in v])
@lru_cache(None)
def ln_interval(q):
 shift=q.numerator.bit_length()-q.denominator.bit_length()
 r=q/Q(2)**shift
 if r<1:shift-=1;r*=2
 if r>=2:shift+=1;r/=2
 def part(x):
  z=(x-1)/(x+1); s=Q(0)
  for j in range(16):s+=2*z**(2*j+1)/Q(2*j+1)
  err=2*abs(z)**33/(33*(1-z*z))
  return s,s+err
 lo,hi=part(r); a,b=part(Q(2))
 return (lo+shift*a,hi+shift*b) if shift>=0 else (lo+shift*b,hi+shift*a)
@lru_cache(None)
def log2_interval(p):
 if p==2:return Q(1),Q(1)
 a,b=ln_interval(Q(p));c,d=ln_interval(Q(2));return a/d,b/c
def interval(x):
 lo=hi=Q(0)
 for p,c in x.items():
  a,b=log2_interval(p)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
def nonneg(x):return interval(x)[0]>=0
def scalar(x):return {2:Q(x)} if x else {}
def walsh(v):
 n=len(v);return tuple(Q(sum(v[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(n)),n) for s in range(n))
def fwht(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return tuple(Q(x,len(a)) for x in a)
def infl(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def restrict(v,i,b):
 return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
def xi(v,w,e):
 a,b=walsh(v),walsh(w)
 return add(*[(e/2,add((Q(1),g(a[t]+b[t])),(Q(1),g(a[t]-b[t])),(Q(-2),g(a[t])),(Q(-2),g(b[t])))) for t in range(1,len(a))])
def wrapper(v,w,d):
 return tuple(v[x>>d] if x%2**d==0 else w[x>>d] if x%2**d==1 else 1 for x in range(len(v)*2**d))
def mean(v):return Q(sum(v),len(v))
def reserve(v,w,d):return Q(d,2**d)*(2-mean(v)**2-mean(w)**2)
