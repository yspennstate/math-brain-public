"""Replay the frozen 1/2/3-copy product and full-terminal check."""
import json,time
from fractions import Fraction as Q
import check as c

start=time.perf_counter();base=[1,1,1,-1];bs=c.fwht(base)
single=c.add(c.H(base),c.neg(c.times(c.add(c.H(base[:2]),c.H(base[2:])),Q(1,2))))
rows=[]
for copies in [1,2,3]:
 vals=[]
 for x in range(4**copies):
  prod=1
  for j in range(copies):prod*=base[(x>>(2*j))&3]
  vals.append(prod)
 for s,v in enumerate(c.fwht(vals)):
  product=Q(1)
  for j in range(copies):product*=bs[(s>>(2*j))&3]
  c.check(v==product)
 leaves=[]
 for zs in range(1<<copies):
  child=[]
  for aa in range(1<<copies):
   prod=1
   for j in range(copies):prod*=base[((aa>>j)&1)+2*((zs>>j)&1)]
   child.append(prod)
  leaves.append(c.H(child))
 D=c.add(c.H(vals),c.neg(c.times(c.add(*leaves),Q(1,1<<copies))))
 expected=c.times(single,Q(copies));c.check(not(D[1]<expected[0] or expected[1]<D[0]))
 rows.append({'copies':copies,'dimension':2*copies,'spent_query_influence':str(Q(copies,2)),'decrement':c.serial(D)})
c.check(time.perf_counter()-start<55)
result={'status':'PASS','checks':c.CHECKS,'seconds':time.perf_counter()-start,'rows':rows}
(c.ROOT/'out/TENSOR_REPLAY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','checks':c.CHECKS,'seconds':result['seconds']}))
