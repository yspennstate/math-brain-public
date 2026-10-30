import primitives as z
from fractions import Fraction as Q
from pathlib import Path
import time,json,math
start=time.monotonic();count=0
e0=sum((Q(1,math.factorial(j)) for j in range(31)),Q(0));e1=e0+Q(32,31*math.factorial(31))
cdlo=1/z.logint(2)[1]+2/(e1*z.logint(2)[1])
for n in [2,3]:
 for mask in range(1<<(1<<n)):
  u=tuple(1 if mask>>j&1 else -1 for j in range(1<<n));m=Q(sum(u),len(u))
  for r in [1,2,3]:
   p=Q(1,1<<r)
   cap,_,_,_,_,I,V=z.core_ledger(u,r)
   bound=z.add(z.scale(z.log(2),cdlo*p*I),z.scale(z.log(2),r*p*V))
   assert z.le(cap,bound),'new variance coefficient'
   bank=z.add(cap,z.scale(z.defect_tail(r),(1-m)/2))
   assert z.le(bank,z.scale(z.log(2),5*p*(I+r*(1-m)))),'five influence bound'
   count+=1
   if time.monotonic()-start>55:raise RuntimeError('frozen watchdog')
result={'status':'PASS','roots':count,'new_bound_checks':2*count,'primitives_counts':z.COUNTS,'elapsed_seconds':time.monotonic()-start,'bound':'same capped core prefix plus physical point-defect suffix <=5 I(F)','arithmetic':'exact prime-log expressions with rational interval signs'}
(Path(__file__).resolve().parents[1]/'out'/'FRESH.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
