from fractions import Fraction as R
from functools import lru_cache
def fw(v):
 v=list(v);step=1
 while step<len(v):
  for j in range(0,len(v),2*step):
   for i in range(j,j+step):
    x,y=v[i],v[i+step];v[i],v[i+step]=x+y,x-y
  step*=2
 return v
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 d={}
 for w,b in terms:
  for p,v in b.items():d[p]=d.get(p,R(0))+w*v
 return {p:v for p,v in d.items() if v}
@lru_cache(None)
def log(q):
 q=R(q);assert q>0
 return add((1,factors(q.numerator)),(-1,factors(q.denominator)))
def h(q):return add(*[(-v,log(v)) for v in (q,1-q) if v])
def ln(q):
 z=(q-1)/(q+1)
 lo=2*sum((z**(2*j+1)/R(2*j+1) for j in range(24)),R(0))
 return lo,lo+2*z**49/(49*(1-z*z))
ln2=ln(R(2))
@lru_cache(None)
def ilog(q):
 q=R(q);k=0
 while q<1:q*=2;k-=1
 while q>=2:q/=2;k+=1
 lo,hi=ln(q)
 return R(k)+lo/ln2[1],R(k)+hi/ln2[0]
def interval(ex):
 lo=hi=R(0)
 for p,w in ex.items():
  a,b=ilog(p);lo+=w*(a if w>0 else b);hi+=w*(b if w>0 else a)
 return lo,hi
def nonnegative(ex):return not ex or interval(ex)[0]>=0
