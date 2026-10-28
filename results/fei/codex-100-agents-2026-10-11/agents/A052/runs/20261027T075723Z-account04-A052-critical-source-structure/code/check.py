"""Exact dyadic complete-child savings certificate (A052 v1)."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time
BASE=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(x):
 global checks
 assert x
 checks+=1
 assert time.perf_counter()-start<55
def fw(t):
 a=list(t);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def fac(x):
 p=2;z={}
 while p*p<=x:
  while x%p==0:z[p]=z.get(p,0)+1;x//=p
  p+=1
 if x>1:z[x]=z.get(x,0)+1
 return z
def add(a,b):
 z=dict(a)
 for p,v in b.items():z[p]=z.get(p,F(0))+v
 return {p:v for p,v in z.items() if v}
def scale(a,c):return {p:v*c for p,v in a.items() if v*c}
def lg(x):return {p:F(v) for p,v in fac(x.numerator).items()} if x.denominator==1 else add(lg(F(x.numerator)),scale(lg(F(x.denominator)),-1))
@lru_cache(None)
def ln(x):
 z=(x-1)/(x+1);v=sum((2*z**(2*j+1)/F(2*j+1) for j in range(28)),F(0))
 return v,v+2*z**57/(57*(1-z*z))
def bounds(h):
 lo=hi=F(0);a,b=ln(F(2))
 for p,c in h.items():
  k=p.bit_length()-1;l,u=ln(F(p,1<<k));l,u=k+l/b,k+u/a
  lo+=c*(l if c>=0 else u);hi+=c*(u if c>=0 else l)
 return lo,hi
@lru_cache(None)
def data(t):
 N=len(t);n=N.bit_length()-1;w=fw(t);h={2:F(2*n)}
 for v in w:
  if v:h=add(h,scale(lg(F(v*v)),-F(v*v,N*N)))
 costs=[F(min(sum(t[x]!=t[x^v] for x in range(N)),sum(t[x]==t[x^v] for x in range(N))),N) for v in range(N)]
 basis={};a=F(0)
 for v in sorted(range(1,N),key=lambda v:costs[v]):
  u=v
  while u:
   j=u.bit_length()-1
   if j in basis:u^=basis[j]
   else:basis[j]=u;a+=costs[v];break
 I=F(sum(sum(t[x]!=t[x^(1<<i)] for x in range(N)) for i in range(n)),N)
 ck(0<=a<=I)
 return h,I,a
def child(t,A,x):
 n=len(t).bit_length()-1;B=[i for i in range(n) if i not in A]
 return tuple(t[sum(((x>>j)&1)<<i for j,i in enumerate(A))+sum(((y>>j)&1)<<i for j,i in enumerate(B))] for y in range(1<<len(B)))
roots=[]
for n in range(4):
 for v in range(1<<(1<<n)):roots.append(tuple(1 if (v>>x)&1 else -1 for x in range(1<<n)))
# Named n=4 boundary controls, not a fourth-bit exhaustive census.
for defect in [(),(0,), (0,1),(0,3),(0,1,2),(0,1,2,4)]:
 roots.append(tuple(-1 if x in defect else 1 for x in range(16)))
roots.append(tuple(-1 if ((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2 else 1 for x in range(16)))
blocks=eligible=rigid=0;guard=None
for t in roots:
 n=len(t).bit_length()-1;h,I,a=data(t)
 for mask in range(1,(1<<n)-1):
  A=[i for i in range(n) if (mask>>i)&1];r=len(A);d=n-r
  children=[data(child(t,A,x)) for x in range(1<<r)]
  gains=[ii-aa for _,ii,aa in children];q=F(1) if d==1 else F(4,1<<d)
  for g in gains:ck((g/q).denominator==1 and g>=0)
  m=sum(g>0 for g in gains);R=sum(gains,F(0))/(1<<r)
  rootq=q/(1<<r)
  ck(R>=m*rootq);ck((R/rootq).denominator==1)
  eh={}
  for hh,_,_ in children:eh=add(eh,scale(hh,F(1,1<<r)))
  E_I=sum((ii for _,ii,_ in children),F(0))/(1<<r)
  sigma=I-E_I;L=add(h,scale(eh,-1))
  for K in (1,2,3,4,8,16):
   D=add(h,{2:-K*I});S=add({2:K*(E_I-R)},scale(eh,-1))
   lhs=add(add(D,S),{2:K*R});rhs=add(L,{2:-K*sigma})
   ck(lhs==rhs)
   # Independent scalar envelope: L-K*sigma <= r log2(1+2^(3-K)).
   cap=scale(lg(1+F(2)**(3-K)),r)
   ck(bounds(add(cap,scale(rhs,-1)))[0]>=0)
   dl,du=bounds(D);sl,su=bounds(S)
   if dl>0 and (not S or sl>=0):
    eligible+=1;ck(bounds(add(cap,{2:-K*R}))[0]>0)
    ck(bounds(add(scale(cap,1/(K*rootq)),{2:-m}))[0]>0)
    if K*rootq>=r*F(2)**(4-K):ck(m==0);rigid+=1
   if guard is None and dl>0 and su<0:guard={'n':n,'table':list(t),'K':K,'D':str(D),'S':str(S)}
  blocks+=1
# Root affine-minimal bent2: removing D>0 makes claimed rigidity false.
t=(1,1,1,-1);h,I,a=data(t);ck(I==a==1)
g=[data(child(t,[0],x)) for x in range(2)];ck(sum(ii-aa for _,ii,aa in g)==1)
ck(16*F(2)**(16-2-3)>=1)
ck(guard is not None)
out={'status':'PASS','checks':checks,'seconds':time.perf_counter()-start,'roots':len(roots),'blocks':blocks,'eligible_cases':eligible,'rigidity_triggered_cases':rigid,'negative_reserve_guard':guard,'scope':'all labelled n<=3 plus seven named n4 controls; no high-K critical witness claimed'}
(BASE/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
