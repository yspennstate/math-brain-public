from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ok(x):
 global checks
 assert x;checks+=1
 assert time.perf_counter()-start<55
def transform(v):
 return [F(sum(-x if (t&s).bit_count()%2 else x for t,x in enumerate(v)),len(v)) for s in range(len(v))]
def e23(x):
 a=b=0
 for sign,n in [(1,x.numerator),(-1,x.denominator)]:
  while n%2==0:n//=2;a+=sign
  while n%3==0:n//=3;b+=sign
  assert n==1
 return a,b
def cost(p,q):
 c=[F(0),F(0)]
 for x,y in zip(p,q):
  if x:
   a,b=e23(y);c[0]-=x*a;c[1]-=x*b
 return c
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-v*v for v in a]
ah=transform(a);bh=transform(b)
# Literal g(v1,v2) negative only when both signs are plus. Bit0 is plus.
def core(s):return -1 if s==0 else 1
def make(tags):
 out=[]
 for s in range(1<<(tags+4)):
  parity=-1 if (s&((1<<tags)-1)).bit_count()%2 else 1
  c=s>>tags;x=c&3;y=c>>2
  out.append(parity*core(x^y))
 return out
terminal_count=0
for sigma in [-1,1]:
 h=make(3);v=[a[u]+sigma*b[u]*h[s] for s in range(len(h)) for u in range(16)]
 parent=[x*x for x in transform(v)]
 for outcome in [0,1]:
  child=[v[(s&15)|((s>>4)<<5)|(outcome<<4)] for s in range(len(v)//2)]
  ph=[x*x for x in transform(child)];terminal_count+=1
  expected=[F(0)]*len(ph)
  for u in range(16):expected[u]=ah[u]**2
  for s in range(4):
   for u in range(16):expected[u+16*(3+4*(s+4*s))]=bh[u]**2/F(4)
  ok(ph==expected);ok(sum(ph)==1);ok(len(set(child))==2)
  parent_H=cost(parent,parent)
  for k in [0,1,2]:
   M=1<<k;qcore=[F(0)]*16
   for j in range(M):
    for x in range(4):
     for y in range(4):
      if x%M==j and y%M==j:qcore[x+4*y]+=F(1,M*2**(2*(2-k)))
   target=[F(0)]*len(ph)
   for u in range(16):target[u]=ah[u]**2
   for s,x in enumerate(qcore):
    for u in range(16):target[u+16*(3+4*s)]=bh[u]**2*x
   ok(sum(target)==1)
   ce=cost(ph,target)
   ok([ce[i]-parent_H[i] for i in range(2)]==[F(3,8)*(2-k),F(0)])
# Independent four-atom normalizer witness and prepaid ghost variant.
for ghost in [F(0),F(1,8)]:
 p=[F(1,4)]*4;q1=[F(x,8)*(1-ghost) for x in [3,3,1,1]];q2=[F(x,8)*(1-ghost) for x in [1,1,3,3]]
 z2=F(3,4)*(1-ghost)**2
 ok(all(q1[i]*q2[i]==p[i]**2*z2 for i in range(4)))
 ok(0<z2<1)
result={'status':'PASS','assertions':checks,'full_complete_terminals':terminal_count,'exact_sharp_target_transactions':12,'normalizer_cases':2,'runtime_seconds':time.perf_counter()-start,'method':'direct character sums; literal complete references; independent two-prime CE arithmetic; no primary/author helper import','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out'/'independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
