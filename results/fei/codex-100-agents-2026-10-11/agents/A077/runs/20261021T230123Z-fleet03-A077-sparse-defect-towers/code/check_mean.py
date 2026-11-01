from pathlib import Path
from fractions import Fraction as Q
import check_profiles as C
import sys,time,json
start=time.monotonic(); pilot='--pilot' in sys.argv; roots=queries=assertions=0; first=None
for n in ([1] if pilot else [1,2]):
  for d in ([1] if pilot else [1,2]):
    carriers=[(1,)*(1<<d)]+([(1,1,1,-1)] if d==2 else [])
    e=Q(1,1<<d)
    for h in carriers:
      for v in C.allfunc(n):
        for w in C.allfunc(n):
            roots+=1
            mu,nu=C.mean(v),C.mean(w); vv,ww=C.fw(v),C.fw(w)
            base=C.baseline(h,v,w)
            for i in range(n):
                queries+=1; vs=[C.restrict(v,i,b) for b in [0,1]]; ws=[C.restrict(w,i,b) for b in [0,1]]
                delta=C.add(base,C.mul(Q(-1,2),C.add(*(C.baseline(h,vs[b],ws[b]) for b in [0,1]))))
                dv=C.add(C.H(v),C.mul(Q(-1,2),C.add(*(C.H(t) for t in vs))))
                dw=C.add(C.H(w),C.mul(Q(-1,2),C.add(*(C.H(t) for t in ws))))
                release=d*e*(vv[1<<i]**2+ww[1<<i]**2)
                actual=d*e*(2-mu*mu-nu*nu)-sum((d*e*(2-C.mean(vs[b])**2-C.mean(ws[b])**2) for b in [0,1]),Q(0))/2
                assert actual==release; assertions+=1
                margin=C.add(C.mul(e,C.add(dv,dw)),C.number(release+12*e*(C.inf(v,i)+C.inf(w,i))),C.mul(-1,delta))
                assert not margin or C.interval(margin)[0]>=0; assertions+=1
                if queries%100==0 and time.monotonic()-start>55: raise TimeoutError('55 second frozen cap')
r={'status':'PASS','roots':roots,'queries':queries,'exact_assertions':assertions,'elapsed_seconds':time.monotonic()-start,'claim':'PROOF.md(11), no assertion on unpaid DeltaXi'}
name='mean_pilot.json' if pilot else 'mean_full.json'
(Path(__file__).resolve().parents[1]/'out'/name).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r))
