from pathlib import Path
from fractions import Fraction as F
import json, time

RUN=Path(__file__).resolve().parents[1]
exec((RUN/'code/check.py').read_text(encoding='utf-8').split('parser=argparse.ArgumentParser()')[0])
rows=[]
def local(n,edges):
    t=max([1]+[(a&b).bit_count() for a,b in itertools.combinations(edges,2)])
    truth=[int(any(x&e==e for e in edges)) for x in range(1<<n)]
    result=[]
    for j in range(n):
        inc=[e for e in edges if e&(1<<j)]
        if not inc: continue
        V=0
        for e in inc: V|=e^(1<<j)
        distant=[e for e in edges if not e&(1<<j) and not e&V]
        near=[e for e in edges if not e&(1<<j) and e&V]
        other=[k for k in range(n) if k!=j]; size=1<<(n-1)
        xs=[sum(((z>>k)&1)<<other[k] for k in range(n-1)) for z in range(size)]
        cvals=[int(not any(x&e==e for e in distant)) for x in xs]
        c=F(sum(cvals),size)
        masses=[F(2,1<<e.bit_count()) for e in inc]; a=sum(masses)
        cross_pressure=F(1<<(t-1))*(a*a-sum(x*x for x in masses))/a
        theta=cross_pressure+F(1<<t)*sum((F(1,1<<e.bit_count()) for e in near),F(0))
        us=[[cv*int(x&(e^(1<<j))==e^(1<<j)) for x,cv in zip(xs,cvals)] for e in inc]
        ck(all(F(sum(row),size)==c*mass for row,mass in zip(us,masses)))
        d=[truth[x|(1<<j)]-truth[x] for x in xs]
        residual=[dd-sum(row[z] for row in us) for z,dd in enumerate(d)]
        alpha=F(sum(d),size); r2=F(sum(r*r for r in residual),size)
        cross=F(sum(sum(row[z] for row in us)*(sum(row[z] for row in us)-1) for z in range(size)),size)
        ck(r2<=c*a*theta); ck(alpha>=(1-theta)*c*a)
        ck(cross<=c*a*cross_pressure)
        for e,mass in zip(inc,masses):
            block=e^(1<<j)
            for b in near:
                joint=F(sum(cv*int(x&block==block)*int(x&b==b) for x,cv in zip(xs,cvals)),size)
                unconditioned=F(sum(int(x&block==block)*int(x&b==b) for x in xs),size)
                ck(joint<=c*unconditioned)
                ck(joint<=c*mass*F(1<<t)*F(1,1<<b.bit_count()))
        hats=[walsh(row) for row in us]; rh=walsh(residual); dh=walsh(d)
        cross_frequency=0
        for T in range(size):
            vals=[row[T] for row in hats]; cross_T=sum(vals)**2-sum(v*v for v in vals)
            ck(cross_T>=0); cross_frequency+=cross_T
            ck(dh[T]==sum(vals)+rh[T])
            ck(dh[T]**2<=2*(sum(v*v for v in vals)+cross_T)+2*rh[T]**2)
        ck(F(cross_frequency,size*size)==cross)
        if not near and len(inc)==1:
            ck(theta==0); ck(r2==0); ck(alpha==c*a)
        result.append({'j':j,'c':str(c),'a':str(a),'theta':str(theta),
                       'influence':str(alpha),'residual_norm2':str(r2),'cross_norm':str(cross)})
    return {'n':n,'edges':edges,'coordinates':result}

for edges in antichains4(): rows.append(local(4,edges))
ck(len(rows)==166)
for m in (1,2,3):
    edges=[(1<<(2*i))|(1<<(2*i+1)) for i in range(m)]
    rows.append(local(2*m,edges))
ck(len(rows)==169)
symbolic=[]
for w in (2,4,8):
    p=F(1,1<<w); a=2*p
    for m in range(1,65):
        c=(1-p)**(m-1); alpha=a*c; raw=a*(1-c)
        ck(raw/alpha==c**-1-1)
        symbolic.append({'w':w,'m':m,'raw_residual_over_influence':str(raw/alpha),
                         'conditioned_residual':0,'conditioned_pressure':0})
ck(F(4,3)**3-1>1)
local_rank_constant=(F(216,5)+F(11,20))*F(16,15)
ck(local_rank_constant==F(140,3)); ck(local_rank_constant<47)
out={'helper':'A014-local-blocking-v1','assertions':ASSERTIONS,
     'elapsed_seconds':time.monotonic()-START,'physical_cases':len(rows),
     'symbolic_cases':len(symbolic),'local_rank_constant':str(local_rank_constant),
     'rows':rows,'symbolic':symbolic}
(RUN/'out/local_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','symbolic')}))
