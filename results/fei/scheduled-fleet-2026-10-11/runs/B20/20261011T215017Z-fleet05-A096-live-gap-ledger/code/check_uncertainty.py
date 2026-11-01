from fractions import Fraction as F
from pathlib import Path
import json,time
start=time.perf_counter(); rows=[]; checks=0
for t in [F(1,4),F(1,8),F(1,16)]:
    sn=2*t/(1+t*t); cs=(1-t*t)/(1+t*t)
    p=sn*sn; delta=1-cs
    assert p<=F(1,2) and cs*cs==1-p; checks+=1
    for s in [F(-4),F(-3),F(-2),F(-1),F(-1,2),F(-1,4),F(0),F(1,4),F(1,2),F(1),F(2),F(3),F(4)]:
        x=(1-s*s)/(1+s*s); y=2*s/(1+s*s)
        z=cs*x-sn*y; w=sn*x+cs*y
        assert x*x+y*y==1 and z*z+w*w==1; checks+=1
        u=min(x*x,y*y); v=min(z*z,w*w)
        assert u+v>=delta; checks+=1
        rows.append({'p':str(p),'s':str(s),'u_plus_v':str(u+v),'delta':str(delta)})
result={'cases':len(rows),'assertions_passed':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'Fraction, exact','rows':rows}
(Path(__file__).resolve().parent.parent/'out/UNCERTAINTY_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
