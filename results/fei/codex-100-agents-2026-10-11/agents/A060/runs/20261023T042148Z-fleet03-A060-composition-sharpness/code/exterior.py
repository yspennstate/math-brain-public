import singleton as s
import exact as e
from fractions import Fraction as Q
from pathlib import Path
import time,json
t0=time.perf_counter();rows=[]
for m in (4,6,8,10):
 c=Q(1,1<<m);b=[s.bent(x,m) for x in range(1<<m)];bm=[-1 if x==0 else s.bent(x,m) for x in range(1<<m)]
 db=s.D(b,0);dm=s.D(bm,0)
 for name,g in {'constant+':[1],'constant-':[-1],**s.named()}.items():
  mu=Q(sum(g),len(g));var=1-mu*mu;f=s.wrapper(g,m)
  w=[g[y] for y in range(len(g)) for x in range(1<<m)]+f
  dx=Q(1-c-mu*(Q(1,1<<(m//2))-c),2);old=s.D(w,m+len(g).bit_length()-1)
  tax=c*m*var/2
  exterior=e.add(e.times(db,(1+mu)/4),e.times(dm,(1-mu)/4))
  over=e.add(old,e.times(e.ln(Q(2)),tax-6*dx),exterior)
  rows.append({'m':m,'g':name,'actual_source_influence':str(dx),'old_DX':e.serial(old),'booked_density_ticket':str(tax),'new_exterior_D_root_weighted':e.serial(exterior),'charge_minus_original_source6':e.serial(over)})
elapsed=time.perf_counter()-t0
assert elapsed<55
out={'status':'COMPUTED_EXACT_INTERVAL_SIGNS','elapsed_s':elapsed,'rows':rows}
Path(__file__).resolve().parents[1].joinpath('out/CHECK_exterior.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'elapsed_s':elapsed,'rows':[(r['m'],r['g'],r['charge_minus_original_source6']['display']) for r in rows]}))
