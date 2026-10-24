from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,math
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0
def check(ok):
 global count
 count+=1
 assert ok,count
 assert time.perf_counter()-start<58,'frozen time limit'
def fw(values):
 a=list(values);step=1
 while step<len(a):
  for p in range(0,len(a),2*step):
   for j in range(p,p+step):
    u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
  step*=2
 return [Q(x,len(a)) for x in a]
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 out={}
 for scale,item in terms:
  for p,v in item.items():out[p]=out.get(p,Q(0))+scale*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def xlog(x):
 if not x:return {}
 return add((x,factors(x.numerator)),(-x,factors(x.denominator)))
@lru_cache(None)
def phi(a,b):return add((1,xlog(a+b)),(-1,xlog(a)),(-1,xlog(b)))
def entropy(p):return add(*[(-1,xlog(v)) for v in p])
def edge(p,i):return add(*[(1,phi(p[t],p[t|(1<<i)])) for t in range(len(p)) if not t&(1<<i)])
def inf(p,i):return sum((v for t,v in enumerate(p) if t&(1<<i)),Q(0))
def majority(M,fixed):
 n=M-len(fixed)
 return [1 if sum(fixed)+n-2*b.bit_count()>0 else -1 for b in range(1<<n)]
def law(coeff):return [v*v for v in coeff]
def normalize(p,n):
 a=p[0];v=1-a
 if not v:return
 r=[Q(0)]+[x/v for x in p[1:]]
 B=add(*[(1,edge(p,i)) for i in range(n)])
 Br=add(*[(1,edge(r,i)) for i in range(n)])
 t0=add(*[(1,phi(a,p[1<<i])) for i in range(n)])
 check(B==add((v,Br),(1,t0)))
 check(add((1,entropy(p)),(-1,B))==add((1,phi(a,v)),(v,entropy(r)),(-v,Br),(-1,t0)))
endpoint=[]
for M in [3,5,7,9,11,13,15]:
 r=(M-1)//2;rho=Q(math.comb(2*r,r),4**r)
 for sigma in [-1,1]:
  c=fw(majority(M,[sigma]));p=law(c);n=M-1
  check(c[0]==sigma*rho)
  for i in range(n):
   check(c[1<<i]==rho);check(inf(p,i)==rho)
   # Exact algebraic certificate plus analytic Phi<=2sqrt(ab).
   upper=2*sum((abs(c[t]*c[t|(1<<i)]) for t in range(len(c)) if not t&(1<<i)),Q(0))
   check(upper==2*rho)
  normalize(p,n)
  endpoint.append({'M':M,'sigma':sigma,'rho':str(rho),'Hellinger_upper_over_influence':'2'})
 for s1 in [-1,1]:
  for s2 in [-1,1]:
   c=fw(majority(M,[s1,s2]));p=law(c)
   check(c[0]==(s1+s2)*rho)
   d=rho*Q(2*r if s1!=s2 else 2*(r-1),2*r-1)
   for i in range(M-2):check(inf(p,i)==d)
composed=0
for n in [1,2]:
 for table in range(1<<(1<<n)):
  outer=[1 if table&(1<<b) else -1 for b in range(1<<n)]
  A=fw([Q(outer[2*t]+outer[2*t+1],2) for t in range(1<<(n-1))])
  D=fw([Q(outer[2*t]-outer[2*t+1],2) for t in range(1<<(n-1))])
  delta=sum((x*x for x in D),Q(0))
  for M in [3,5,7]:
   for sigma in [-1,1]:
    h=majority(M,[sigma]);hc=fw(h);hp=law(hc);m=M-1
    values=[outer[2*t+(h[b]<0)] for t in range(1<<(n-1)) for b in range(1<<m)]
    coeff=fw(values);p=law(coeff)
    for i in range(m):
     gamma=hc[1<<i];mu=hc[0]
     collision=add(*[(1,phi((a+mu*d)**2,gamma**2*d**2)) for a,d in zip(A,D)])
     expected=add((delta,edge(hp,i)),(-delta,phi(mu*mu,gamma*gamma)),(1,collision))
     check(edge(p,i)==expected);check(inf(p,i)==delta*inf(hp,i))
    normalize(p,m+n-1);composed+=1
out={'status':'PASS','helper':'A003-sliced-majority-v1','assertions':count,'composed_slice_cases':composed,'encoder_slice_endpoints':len(endpoint),'twice_slice_endpoints':28,'arithmetic':'integer FWHT; Fraction; exact rational prime-log identities; exact Hellinger certificate with analytic entropy inequality','runtime_seconds':time.perf_counter()-start,'endpoints':endpoint}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='endpoints'}))
