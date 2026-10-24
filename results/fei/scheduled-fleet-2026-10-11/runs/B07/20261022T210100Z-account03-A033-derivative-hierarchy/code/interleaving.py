"""Frozen exact certificate. No numpy, no external dependencies, no subprocesses."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time,hashlib
START=time.monotonic(); ROOT=Path(__file__).resolve().parents[1]
SCALE=256; ZERO=(0,0,0,0); PRIMES=(3,5,7)
checks=0; cases=0; states=0; positives=0
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def avg(a,b):
 z=add(a,b)
 assert all(x%2==0 for x in z)
 return tuple(x//2 for x in z)
def mul(a,q):
 z=tuple(Q(x)*q for x in a)
 assert all(x.denominator==1 for x in z)
 return tuple(int(x) for x in z)
def ln_interval(x):
 t=(x-1)/(x+1); n=40
 lo=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
 hi=lo+2*t**(2*n+1)/Q(2*n+1)/(1-t*t)
 return lo,hi
L2=ln_interval(Q(2)); LOG=[]
for p in PRIMES:
 k=p.bit_length()-1; lo,hi=ln_interval(Q(p,2**k))
 LOG.append((Q(k)+lo/L2[1], Q(k)+hi/L2[0]))
@lru_cache(None)
def sign(a):
 if a==ZERO:return 0
 lo=hi=Q(a[0])
 for v,(l,u) in zip(a[1:],LOG):
  lo+=v*(l if v>=0 else u); hi+=v*(u if v>=0 else l)
 if lo>0:return 1
 if hi<0:return -1
 raise ArithmeticError(('uncertified comparison',a,str(lo),str(hi)))
def maximum(xs):
 best=ZERO
 for x in xs:
  if sign(sub(x,best))>0:best=x
 return best
def restrict(tt,j,b):
 return tuple(tt[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(tt)//2))
@lru_cache(None)
def entropy(tt):
 global checks
 n=(len(tt)).bit_length()-1; w=list(tt); step=1
 while step<len(w):
  for start in range(0,len(w),2*step):
   for j in range(start,start+step):u,v=w[j],w[j+step];w[j]=u+v;w[j+step]=u-v
  step*=2
 assert sum(x*x for x in w)==len(tt)**2
 a=[2*n*SCALE,0,0,0]; fac=2*SCALE//len(tt)**2
 for v in w:
  x=abs(v)
  if not x:continue
  e=0
  while x%2==0:e+=1;x//=2
  a[0]-=fac*v*v*e
  for j,p in enumerate(PRIMES):
   e=0
   while x%p==0:e+=1;x//=p
   a[j+1]-=fac*v*v*e
  assert x==1
 checks+=1
 return tuple(a)
def influence(tt,j):
 a,b=restrict(tt,j,0),restrict(tt,j,1)
 flips=sum(x!=y for x,y in zip(a,b))
 assert SCALE*flips%len(a)==0
 return SCALE*flips//len(a)
@lru_cache(None)
def value(tt,allowed,rate):
 global states,positives,checks
 states+=1; options=[ZERO]; H=entropy(tt)
 for j in allowed:
  a,b=restrict(tt,j,0),restrict(tt,j,1)
  nxt=tuple(i-(i>j) for i in allowed if i!=j)
  d=sub(H,avg(entropy(a),entropy(b)))
  d=sub(d,(rate*influence(tt,j),0,0,0))
  if sign(d)>0:positives+=1
  options.append(add(d,avg(value(a,nxt,rate),value(b,nxt,rate))))
 checks+=len(options)
 return maximum(options)
def table(mask,k,h):
 n=(len(h)).bit_length()-1; out=[]
 for x in range(1<<(k+1+n)):
  c=x&((1<<k)-1); ell=1-2*((x>>k)&1); y=x>>(k+1)
  m=mask[c]
  out.append((1 if m==0 else -1) if m<2 else (1 if m==2 else -1)*ell*h[y])
 return tuple(out)
def check(mask,k,h):
 global checks,cases
 n=len(h).bit_length()-1; F=table(mask,k,h); G=table(mask,k,(1,))
 beta=Q(sum(m>=2 for m in mask),len(mask))
 assert entropy(F)==add(entropy(G),mul(entropy(h),beta));checks+=1
 for rate in (2,4):
  U=value(G,tuple(range(k)),rate)
  V=value(h,tuple(range(n)),rate)
  predicted=add(U,mul(V,beta))
  actual=value(F,tuple(range(k))+tuple(range(k+1,k+1+n)),rate)
  assert predicted==actual,(mask,h,rate,predicted,actual)
  checks+=1
 cases+=1
def save(status,error=None):
 data={'status':status,'cases_completed':cases,'case_count_frozen':1280,'exact_assertions':checks,'Bellman_states':states,'positive_local_options':positives,'comparisons_certified':sign.cache_info().currsize,'seconds':time.monotonic()-START,'error':error,'seed_tag_protected':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (ROOT/'out/interleaving.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps(data))
try:
 for k,n in [(1,2),(2,1)]:
  for mask in product(range(4),repeat=1<<k):
   for h in product((-1,1),repeat=1<<n):
    if time.monotonic()-START>55:save('INCOMPLETE_RUNTIME');raise SystemExit(2)
    check(mask,k,h)
 assert cases==1280
 save('PASS')
except Exception as exc:
 save('FAIL',repr(exc));raise
