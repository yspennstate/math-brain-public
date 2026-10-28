from fractions import Fraction as Q
from functools import lru_cache
def fw(v):
 v=list(v);j=1
 while j<len(v):
  for s in range(0,len(v),2*j):
   for k in range(s,s+j):v[k],v[k+j]=v[k]+v[k+j],v[k]-v[k+j]
  j*=2
 return v
def coeff(v):return [Q(x,len(v)) for x in fw(v)]
def law(v):return [x*x for x in coeff(v)]
def add(*terms):
 r={}
 for c,term in terms:
  for p,v in term.items():r[p]=r.get(p,Q(0))+c*v
 return {p:v for p,v in r.items() if v}
@lru_cache(None)
def fac(n):
 r=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:r.append((p,e))
  p+=1
 if n>1:r.append((n,1))
 return tuple(r)
@lru_cache(None)
def logq(x):
 ans={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  for p,e in fac(n):ans[p]=ans.get(p,Q(0))+s*e
 return {p:v for p,v in ans.items() if v}
def CE(p,q):
 assert len(p)==len(q)
 assert all(y>0 or x==0 for x,y in zip(p,q))
 return add(*[(-x,logq(y)) for x,y in zip(p,q) if x])
def H(p):return CE(p,p)
def D(p,q):return add((1,CE(p,q)),(-1,H(p)))
def restrict(v,i,b):
 lo=(1<<i)-1
 return [v[(x&lo)|((x&~lo)<<1)|(b<<i)] for x in range(len(v)//2)]
def marginal(v,i):return [x+y for x,y in zip(restrict(v,i,0),restrict(v,i,1))]
def erasure(p,i):return add((1,H(p)),(-1,H(marginal(p,i))))
def influence(p,i):return sum(v for t,v in enumerate(p) if t&(1<<i))
def enc(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
b=[1-x*x for x in a];A=coeff(a);B=coeff(b);beta=Q(3,8)
def wrap(h,sig):return [x+sig*y*z for z in h for x,y in zip(a,b)]
def reference(h,R,sig):
 m=Q(sum(h),len(h));ans=[(x+sig*m*y)**2 for x,y in zip(A,B)]
 for v in R[1:]:ans.extend(y*y*v for y in B)
 assert R[0]==m*m and sum(ans)==1
 return ans
def product_marginals(p):
 n=len(p).bit_length()-1;u=[influence(p,i) for i in range(n)];ans=[]
 for t in range(len(p)):
  v=Q(1)
  for i,s in enumerate(u):v*=s if t&(1<<i) else 1-s
  ans.append(v)
 return ans
