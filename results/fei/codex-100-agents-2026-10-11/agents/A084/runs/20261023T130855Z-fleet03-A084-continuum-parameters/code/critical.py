"""Outward root certificate; a unique-critical-point proof covers all real biases."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal,localcontext
import json,time,sys
from arithmetic import Q,log2
R=Path(__file__).resolve().parents[1];CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
def smul(a,q):
 q=F(q);x,y=sorted([q*a[0],q*a[1]])
 return x.numerator//x.denominator,-((-y.numerator)//y.denominator)
def const(q):return smul((Q,Q),q)
def add(*a):return sum(z[0] for z in a),sum(z[1] for z in a)
def neg(a):return -a[1],-a[0]
@lru_cache(None)
def lg(q):return log2(F(q))
def eta(q):return smul(lg(q),-q) if q else (0,0)
def h2(q):return add(eta(q),eta(1-q))
def C(p):return add(eta((1-p)**2),eta(p*p),smul(eta((1-2*p)**2),F(-1,2)),const(4*p*(1-p)))
def Cp(p):return add(smul(lg(1-p),4*(1-p)),smul(lg(p),-4*p),smul(lg(1-2*p),-4*(1-2*p)),const(4-8*p))
def N(p):return add(smul(Cp(p),p),neg(C(p)))
def pack(a):return list(a)
def save(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def decimal(a):
 with localcontext() as ctx:
  ctx.prec=24
  return [str(Decimal(z)/Decimal(Q)) for z in a]
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;steps=8 if pilot else 40
 a,b=F(1,8),F(3,8);ck(N(a)[0]>0 and N(b)[1]<0)
 history=[]
 for step in range(steps):
  m=(a+b)/2;n=N(m)
  ck(n[0]>0 or n[1]<0)
  history.append({'step':step,'p':str(m),'N_interval':pack(n),'side':'left' if n[0]>0 else 'right'})
  if n[0]>0:a=m
  else:b=m
 root_bounds=(a,b);price_lo=smul(C(a),1/b)[0];price_hi=smul(C(b),1/a)[1]
 ck(N(a)[0]>0 and N(b)[1]<0)
 upper=None
 if not pilot:
  ck(price_lo>const(F(487,100))[1])
  for candidate in [F(39,8),F(49,10)]:
   if price_hi<const(candidate)[0]:upper=candidate;break
  ck(upper is not None)
  # A literal five-bit core realizes this exact dyadic scalar lower control.
  p=F(7,32);witness=add(C(p),const(-F(487,100)*p))
  ck(witness[0]>0)
  for p in [F(0),F(1,8),F(7,32),F(1,4),F(1,2),F(3,4),F(1)]:
   compact=add(smul(h2(p),2),smul(h2((1-2*p)**2),F(-1,2)))
   x=C(p);ck(max(x[0],compact[0])<=min(x[1],compact[1]));ck(C(p)==C(1-p))
  ck(C(F(0))==(0,0) and C(F(1))==(0,0) and C(F(1,2))==(2*Q,2*Q))
 result={'status':'PASS','arithmetic':'192-bit outward80-term log intervals','steps':steps,'root_bracket':[str(z) for z in root_bounds],'root_endpoint_signs':[pack(N(a)),pack(N(b))],'lambda_interval':[price_lo,price_hi],'lambda_decimal_for_display_only':decimal((price_lo,price_hi)),'rational_lower':'487/100','certified_rational_upper':str(upper) if upper else None,'unique_global_maximum':'PROOF.md section2; not a grid inference','physical_scope':'sharp scalar correction/p charge; not an optimal full-hull threshold','assertions':CHECKS,'runtime_seconds':time.perf_counter()-start,'bisection_history':history}
 ck(time.perf_counter()-start<55)
 save('PILOT_ROOT.json' if pilot else 'CRITICAL_POINT.json',result)
 print(json.dumps({k:v for k,v in result.items() if k not in ['bisection_history','root_endpoint_signs']}))
if __name__=='__main__':main()
