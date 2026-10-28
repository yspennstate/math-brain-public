from pathlib import Path
from fractions import Fraction as Q
import json,time,itertools
start=time.monotonic(); checks=cases=0
def require(x):
 global checks
 checks+=1
 if not x: raise AssertionError(checks)
 if time.monotonic()-start>55: raise TimeoutError('frozen cap')
def spectrum(t):
 a=list(t); j=1
 while j<len(a):
  for s in range(0,len(a),2*j):
   for k in range(j): u,v=a[s+k],a[s+k+j];a[s+k],a[s+k+j]=u+v,u-v
  j*=2
 return [Q(x*x,len(a)**2) for x in a]
def influence(t):
 return sum((Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)),Q(0))
def factor(n):
 d=2;ans={}
 while d*d<=n:
  while n%d==0: ans[d]=ans.get(d,0)+1;n//=d
  d+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def entropy(p):
 z={}
 for a in p:
  if not a:continue
  for prime,power in factor(a.denominator).items():z[prime]=z.get(prime,Q(0))+a*power
  for prime,power in factor(a.numerator).items():z[prime]=z.get(prime,Q(0))-a*power
 return {k:v for k,v in z.items() if v}
for n in range(3):
 for mask in range(2**(2**n)):
  h=[1 if mask>>x&1 else -1 for x in range(2**n)]; ph=spectrum(h); hh=entropy(ph); ih=influence(h)
  for m in range(1,4):
   cases+=1; data=[]
   for x in range(2**(m*n)):
    v=1
    for j in range(m):v*=h[(x>>(j*n))&((1<<n)-1)]
    data.append(v)
   t=[(-1 if (x&3)==0 else 1)*data[x>>2] for x in range(4*len(data))]
   p=spectrum(t); product=spectrum(data)
   require(all(p[4*s+u]==product[s]/4 for s in range(len(product)) for u in range(4)))
   require(influence(t)==m*ih+1)
   expected={k:v*m for k,v in hh.items()};expected[2]=expected.get(2,Q(0))+2
   require(entropy(p)=={k:v for k,v in expected.items() if v})
   eta=sum(p[i] for i in range(len(p)) if i&1);require(eta==Q(1,2))
   for i in range(0,len(p),2):
    if p[i]+p[i+1]:
     k=p[i+1]/(p[i]+p[i+1]);require(k==Q(1,2));require(Q(15,16)*k+eta/16==k)
out={'status':'PASS','actual_Boolean_carriers':cases,'exact_assertions':checks,'seconds':time.monotonic()-start,'all_dimensional_scope':'analytic disjoint tensor proof in DERIVATION section6, not finite extrapolation'}
(Path(__file__).resolve().parents[1]/'out'/'reduction.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
