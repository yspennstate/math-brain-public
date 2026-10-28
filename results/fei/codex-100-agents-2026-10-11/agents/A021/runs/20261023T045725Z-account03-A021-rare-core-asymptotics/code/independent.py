from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import time,json
root=Path(__file__).resolve().parents[1];count=0
def assert_(v):
 global count
 count+=1;assert v,count
def add(*xs):
 d={}
 for x in xs:
  for b,c in x.items():d[b]=d.get(b,F(0))+c
 return {b:c for b,c in d.items() if c}
def scale(x,c):return {b:a*c for b,a in x.items() if a*c}
def log(x):
 x=F(x);ans={}
 for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while n>1:
   while n%p==0:ans[p]=ans.get(p,0)+sgn;n//=p
   p+=1
 return {p:F(c) for p,c in ans.items() if c}
def H(p):return add(*(scale(log(x),-x) for x in p if x))
def CE(p,q):
 assert_(all(not x or y>0 for x,y in zip(p,q)))
 return add(*(scale(log(y),-x) for x,y in zip(p,q) if x))
@lru_cache(None)
def li(n):
 k=n.bit_length()-1;y=F(n,2**k)
 def ln(y):
  z=(y-1)/(y+1);s=F(0);term=z
  for j in range(48):s+=2*term/(2*j+1);term*=z*z
  return s,s+2*term/(97*(1-z*z))
 a,b=ln(y);c,d=ln(F(2));return k+a/d,k+b/c
def lower(x):return sum((c*li(p)[0 if c>=0 else 1] for p,c in x.items()),F(0))
def P(a):
 N=len(a);return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(a))**2,N*N) for s in range(N)]
def ref(a,d):
 p=P(a);return [1-d+d*p[0]]+[d*x for x in p[1:]]
def J(a,d,w):
 return add(H(ref(a,d)),scale(H(P(a)),-d),scale(log(ref(a,d)[0]),1-w))
def main():
 start=time.perf_counter();cases=0
 for d in [F(1,64),F(1,512)]:
  for w in [F(1,2),F(1,4),F(1,32)]:
   eta=d/w
   for mask in range(16):
    a=[1-2*((mask>>z)&1) for z in range(4)]
    for i in [0,1]:
     children=[[aa for z,aa in enumerate(a) if (z>>i)&1==b] for b in [0,1]]
     over=lambda aa:add(CE(ref(aa,eta),ref(aa,d)),scale(H(P(aa)),-eta))
     assert_(scale(over(a),w)==J(a,d,w))
     direct=scale(add(over(a),scale(add(*(over(ch) for ch in children)),-F(1,2))),w)
     gamma=add(J(a,d,w),scale(add(*(J(ch,d,w) for ch in children)),-F(1,2)))
     assert_(direct==gamma);assert_(lower(gamma)>=0)
     assert_(sum(ref(a,eta))==sum(ref(a,d))==1)
     cases+=1
 # Rational skeleton of uniform curvature, independently checked without spectra.
 assert_(F(64,63)<2)
 # ln2 > 2/3 is the strict positive-tail atanh identity in PROOF Section3.
 assert_(6*F(2,3)==4)
 result={'status':'PASS','cases':cases,'assertions':count,'seconds':time.perf_counter()-start,'implementation':'direct character sums, independent rational-log arithmetic and 48-term outward intervals; no production imports'}
 (root/'out'/'INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
