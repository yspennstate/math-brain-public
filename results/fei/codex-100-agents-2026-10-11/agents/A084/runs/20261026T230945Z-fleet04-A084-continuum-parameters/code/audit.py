"""Independent direct-argument 64-term scalar interval audit (no factoring)."""
from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1]
def plus(*xs):return sum(x[0] for x in xs),sum(x[1] for x in xs)
def scale(x,c):return tuple(sorted((x[0]*c,x[1]*c)))
def lnunit(x):
 z=(x-1)/(x+1);v=z;s=F(0)
 for k in range(64):s+=2*v/(2*k+1);v*=z*z
 return s,s+2*v/(129*(1-z*z))
LN2=lnunit(F(2))
def lg(q):
 e=0
 while q<1:q*=2;e-=1
 while q>=2:q/=2;e+=1
 a,b=lnunit(q);return e+a/LN2[1],e+b/LN2[0]
def eta(q):return scale(lg(q),-q) if q else (F(0),F(0))
def val(b):return plus(eta((1-b)**2),eta(b*b),scale(eta((1-2*b)**2),F(-1,2)))
def slope(b):return plus(scale(lg(1-b),4*(1-b)),scale(lg(b),-4*b),scale(lg(1-2*b),-4*(1-2*b)))
def main():
 start=time.perf_counter();root=json.loads((R/'out/ROOT.json').read_text(encoding='utf-8'));a,b=map(F,root['root'])
 na=plus(scale(slope(a),a),scale(val(a),-1));nb=plus(scale(slope(b),b),scale(val(b),-1))
 assert na[0]>0 and nb[1]<0
 lo,hi=val(a)[0]/b,val(b)[1]/a
 assert 2<lo<=hi<F(9,4)
 # The independent enclosure and producer enclosure both contain the maximum.
 assert max(lo,F(root['price'][0]))<=min(hi,F(root['price'][1]))
 assert 2**74>3**9*5**25
 assert val(F(0))==(0,0) and val(F(1,2))==(1,1) and val(F(1))==(0,0)
 def pack(iv):
  scale=1<<192;x,y=iv
  return [x.numerator*scale//x.denominator,-((-y.numerator*scale)//y.denominator)]
 result={'status':'PASS','independent_method':'64-term direct-argument rational log intervals; saved endpoints rounded outward to multiples of 2^-192','scale_bits':192,'root_endpoint_signs':[pack(na),pack(nb)],'lambda_interval':pack((lo,hi)),'display_only':[float(lo),float(hi)],'controls':'zero, balanced, one, actual4-bit L>2d integer witness','runtime_seconds':time.perf_counter()-start}
 (R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k not in ['root_endpoint_signs','lambda_interval']}))
if __name__=='__main__':main()
