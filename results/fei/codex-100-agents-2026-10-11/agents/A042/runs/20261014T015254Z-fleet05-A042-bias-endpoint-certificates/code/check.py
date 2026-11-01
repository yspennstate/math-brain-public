from fractions import Fraction as Q
from itertools import product, combinations
from functools import lru_cache
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(x):
 global checks
 assert x
 checks+=1
@lru_cache(None)
def log(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(x):
  t=(x-1)/(x+1);N=24
  a=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
  return a,a+2*t**(2*N+1)/(Q(2*N+1)*(1-t*t))
 a,b=series(x);l,u=series(Q(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def entropy(P,W,select=lambda s:True):
 lo=hi=Q(0)
 for s in P:
  if s and P[s] and select(s):
   a,b=log(W[s]/P[s]);lo+=P[s]*a;hi+=P[s]*b
 return lo,hi
def spec(mask,p):
 n=len(p);P={};W={};c={};T={x:Q(1 if mask>>sum(a<<i for i,a in enumerate(x))&1 else -1) for x in product((0,1),repeat=n)}
 for s in range(1<<n):
  m=Q(0);den=Q(1);w=Q(1)
  for i in range(n):
   if s>>i&1:den*=p[i]*(1-p[i]);w*=4*p[i]*(1-p[i])
  for x,f in T.items():
   a=f
   for i in range(n):
    a*=p[i] if x[i] else 1-p[i]
    if s>>i&1:a*=x[i]-p[i]
   m+=a
  P[s]=m*m/den;W[s]=w;c[s]=m/(den*2**s.bit_count())
 ck(sum(P.values())==1)
 D=sum((s.bit_count()-1)*P[s] for s in P if s)
 R=sum((s.bit_count()-2)*P[s] for s in P if s.bit_count()>=3)
 # Independent physical derivative check, including signed cancellation.
 for i in range(n):
  mean=second=Q(0)
  for x in product((0,1),repeat=n-1):
   a=list(x);a.insert(i,0);b=a.copy();b[i]=1
   d=(T[tuple(b)]-T[tuple(a)])/2;mass=Q(1)
   for j in range(n):
    if j!=i:mass*=p[j] if a[j] else 1-p[j]
   mean+=mass*d;second+=mass*d*d
  ck(mean==c[1<<i]);ck(second>=abs(mean))
  ck(W[1<<i]*(second-mean*mean)==sum(P[s] for s in P if s>>i&1 and s!=(1<<i)))
 es=entropy(P,W,lambda s:s.bit_count()==1)
 ck(es[1]<=4*D-2*R)
 return P,W,c,D,R,entropy(P,W)
l2,u2=log(Q(2)); ck(u2<Q(52,75)); counts={}
for mask in (126,22,25):
 count=0
 for p in product((Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(7,8)),repeat=3):
  P,W,c,D,R,E=spec(mask,p);v=[4*x*(1-x) for x in p];T=P[7]
  if mask==126:
   ck(c[7]==0)
   for i,j in combinations(range(3),2):ck(c[(1<<i)|(1<<j)]==-Q(1,2))
   ck(E[1]<=(4+2*l2)*D)
  elif mask==22:
   ck(c[7]==Q(3,4))
   for i,j in combinations(range(3),2):
    k=3-i-j;ck(c[(1<<i)|(1<<j)]==-1+Q(3,2)*p[k])
   l9,u9=log(Q(9));ck(E[1]+u9*T<=(4+2*l2)*D)
  else:
   ck(c[3]==1-p[2]/2);ck(c[5]==-p[1]/2);ck(c[6]==-p[0]/2);ck(c[7]==-Q(1,4))
   ck(E[1]<=(4+2*l2)*D)
  count+=1
 counts[str(mask)]=count
line=[]
for z in [Q(k,64) for k in range(1,64)]+[Q(1,1024)]:
 P,W,c,D,R,E=spec(33152,[Q(1,2)]*3+[z]);v=4*z*(1-z)
 for s in range(1,8):ck(c[s]==((1+z) if s.bit_count()==2 else (1-z))/4)
 for s in range(8,16):ck(abs(c[s])==Q(1,8))
 ck(D==(5+14*z-7*z*z)/16)
 U=u2*(7+10*z-5*z*z)/4+z*(1-z)/2
 ck(E[1]<=U)
 ck((4+2*l2)*D-E[1] >= (10-9*u2)/8)
 if z==Q(1,1024):
  eh=entropy(P,W,lambda s:s.bit_count()>=2)
  ck(eh[0]-2*u2*D-2*R>Q(13,100));ck((4+2*l2)*D-E[1]>Q(9,20))
  obstruction={'delta':str(D),'R':str(R),'companion_excess_lower':str(eh[0]-2*u2*D-2*R),'total_margin_lower':str((4+2*l2)*D-E[1])}
 line.append(str(z))
# Independently check every essential coordinate and every proper block.
positive={7,8,15};n=4
ck(all(any(((x in positive)!=((x^(1<<i)) in positive)) for x in range(16)) for i in range(n)))
row_counts={}
for k in (2,3):
 for B in combinations(range(4),k):
  O=[i for i in range(4) if i not in B];rows=set()
  for a in product((0,1),repeat=k):
   rows.add(tuple(sum(a[j]<<i for j,i in enumerate(B))+sum(b[j]<<i for j,i in enumerate(O)) in positive for b in product((0,1),repeat=len(O))))
  ck(len(rows)>2);row_counts[str(B)]=len(rows)
out={'helper_version':'A042-reserve-review-v1','assertions_passed':checks,'ternary_cases':counts,'selector_cases':len(line),'obstruction':obstruction,'prime_row_counts':row_counts,'runtime_seconds':time.monotonic()-start,'continuum_proof':'PROOF.md; grids only validate algebra'}
(root/'out/CHECK_OUTPUT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='obstruction'},indent=2))
