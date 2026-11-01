"""Different rational log implementation checks only the decisive root endpoints."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];C=0
def ck(v):
 global C
 assert v
 C+=1
def add(*xs):return sum(x[0] for x in xs),sum(x[1] for x in xs)
def scale(x,a):return tuple(sorted([x[0]*a,x[1]*a]))
def atanh_ln(x):
 z=(x-1)/(x+1);zz=z*z;t=z;s=F(0)
 for j in range(48):s+=2*t/(2*j+1);t*=zz
 return s,s+2*t/(97*(1-zz))
LN2=atanh_ln(F(2))
@lru_cache(None)
def lg(q):
 k=q.numerator.bit_length()-q.denominator.bit_length()
 x=q/(F(2)**k)
 if x<1:k-=1;x*=2
 ck(1<=x<=2)
 lo,hi=atanh_ln(x)
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def eta(q):return scale(lg(q),-q) if q else (F(0),F(0))
def value(p):return add(eta((1-p)**2),eta(p*p),scale(eta((1-2*p)**2),F(-1,2)),(4*p*(1-p),)*2)
def deriv(p):return add(scale(lg(1-p),4*(1-p)),scale(lg(p),-4*p),scale(lg(1-2*p),-4*(1-2*p)),(4-8*p,)*2)
def main():
 start=time.perf_counter();s=json.loads((R/'out/CRITICAL_POINT.json').read_text(encoding='utf-8'));a,b=map(F,s['root_bracket'])
 vals=[]
 for p,want in [(a,1),(b,-1)]:
  n=add(scale(deriv(p),p),scale(value(p),-1))
  ck(n[0]>0 if want==1 else n[1]<0);vals.append(n)
 lo=value(a)[0]/b;hi=value(b)[1]/a
 ck(lo>F(487,100) and hi<F(s['certified_rational_upper']))
 ck(value(F(7,32))[0]>F(487,100)*F(7,32))
 q=1<<192
 for independent,stored in zip(vals,s['root_endpoint_signs']):
  ck(independent[0]<=F(stored[0],q)<=F(stored[1],q)<=independent[1])
 # Negative controls: the reversed root ordering and underpriced owner must fail.
 ck(not (vals[0][1]<0 and vals[1][0]>0))
 ck(not(value(F(7,32))[1]<=F(487,100)*F(7,32)))
 result={'status':'PASS','method':'Exact Fraction48-term atanh with explicit nonnegative remainder, independent of fixed-grid producer','endpoint_signs_independently_checked':2,'strict_rational_price_bounds':s['rational_lower']+' < lambda_star < '+s['certified_rational_upper'],'negative_controls_rejected':2,'assertions':C,'runtime_seconds':time.perf_counter()-start}
 ck(time.perf_counter()-start<55)
 (R/'out/SCALAR_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
