import singleton as s
import exact as e
from fractions import Fraction as Q
from pathlib import Path
import json,time
t0=time.perf_counter();rows=[]
for name,g in {'constant+':[1],'AND3':s.named()['AND3']}.items():
 m=4;c=Q(1,16);mu=Q(sum(g),len(g));var=1-mu*mu
 b=[s.bent(x,m) for x in range(16)];bm=[-1 if x==0 else s.bent(x,m) for x in range(16)]
 w=[g[y] for y in range(len(g)) for x in range(16)]+s.wrapper(g,m)
 old=s.D(w,m+len(g).bit_length()-1,e.direct)
 exterior=e.add(e.times(s.D(b,0,e.direct),(1+mu)/4),e.times(s.D(bm,0,e.direct),(1-mu)/4))
 dx=Q(1-c-mu*(Q(1,4)-c),2);tax=c*m*var/2
 over=e.add(old,exterior,e.times(e.ln(Q(2)),tax-6*dx))
 lo=e.bits(over)[0];assert lo>Q(49 if name=='constant+' else 39,100)
 if name=='constant+':
  sq=sorted(a*a for a in e.direct(w));assert sq==sorted([Q(25,64),Q(9,64)]+[Q(1,64)]*30)
  symbolic=e.add(e.times(e.ln(Q(2)),Q(11,4)),e.neg(e.times(e.ln(Q(25)),Q(25,64))),e.neg(e.times(e.ln(Q(9)),Q(9,64))))
  s.overlap(over,symbolic)
  cost=e.add(old,exterior);assert e.bits(cost)[0]/dx>Q(73,10)
 rows.append({'g':name,'positive_charge_over_source6':e.serial(over)})
elapsed=time.perf_counter()-t0;assert elapsed<55
out={'status':'PASS','cases':2,'checks':s.CHECKS+5,'elapsed_s':elapsed,'rows':rows}
Path(__file__).resolve().parents[1].joinpath('out/CHECK_reproduce_exterior.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
