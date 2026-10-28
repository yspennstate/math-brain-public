from pathlib import Path
import math,json,time
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
t0=time.perf_counter();best=(-1,None);count=0
def phi(a,b):
    assert a>=-1e-12 and b>=-1e-12
    return (a*math.log2(1+b/a) if a>0 else 0)+(b*math.log2(1+a/b) if b>0 else 0)
for i in range(129):
    for j in range(257):
        r=i/128;p=j/128
        if not .25<=r+p<=4/3:continue
        d=(r+p)/8;b=(p-r)/8;k=math.floor(p)
        delta=(r*r+k+(p-k)**2)/8;t=delta-b*b
        value=(2*d-2*delta+phi((.75-b)**2,b*b)+phi(7/16-2*d+1.5*b+t,t))/d
        count+=1
        if value>best[0]:best=(value,[r,p])
assert time.perf_counter()-t0<55
out={'status':'NUMERICAL_EVIDENCE_ONLY','count':count,'best_upper_ratio':best[0],'parameters':best[1],'seconds':time.perf_counter()-t0}
(R/'out'/'PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
