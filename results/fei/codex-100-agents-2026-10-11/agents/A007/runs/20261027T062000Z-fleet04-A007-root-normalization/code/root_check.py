import hashlib,json,time
from pathlib import Path
from fractions import Fraction as Q
import check as c

start=time.perf_counter();root=Path(__file__).resolve().parents[1]
# Physical bit order z1,z2,y1,y2, using c's fixed Walsh convention.
f=[1 if ((x&1) or (x&4)) and ((x&2) or (x&8)) else -1 for x in range(16)]
g=[1 if x==3 else -1 for x in range(4)]
w=c.fw(f);wg=c.fw(g);E=range(1,4)
p={k:Q(wg[k]**2,16) for k in E};u={k:Q(w[k]**2,256) for k in E}
a=Q(1,16);v=sum(p.values());mass=sum(u.values())
c.ck(all(u[k]>=a*p[k] for k in E),'actual domination')
cases=0
for profile in (0,1):
    weights={k:1 if profile==0 else k for k in E};total=sum(weights.values())
    r={k:Q(z,total) for k,z in weights.items()};cp=c.ce(p,r)
    for j in (1,7,128):
        Z=Q(1,1<<j);R={k:Z*r[k] for k in E}
        DR=c.ce(u,R);BR=c.ce({k:u[k]-a*p[k] for k in E},R)
        for k in (1,7,128):
            theta=Q(1,1<<k);raw={x:theta*R[x] for x in E};QE=sum(raw.values())
            DQ=c.ce(u,raw);BQ=c.ce({x:u[x]-a*p[x] for x in E},raw)
            c.ck(DR==c.add((1,DQ),(mass,c.logq(theta))),'root D conversion')
            c.ck(BR==c.add((1,BQ),(mass-a*v,c.logq(theta))),'root surplus conversion')
            c.ck(cp==c.add((1/a,DQ),(-1/a,BQ),(v,c.logq(QE))),'nested refund')
            c.ck(cp==c.add((1/a,DR),(-1/a,BR),(v,c.logq(Z))),'conditioned refund')
            # Known surplus is positive, so dropping it cannot give the exact equality.
            wrong=c.add((1/a,DQ),(v,c.logq(QE)),(-1,cp))
            c.ck(c.log_interval(wrong)[0]>0,'omitted surplus countercontrol')
            cases+=1
result={'verdict':'PASS','cases':cases,'checks':c.CHECKS,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_helper_sha256':hashlib.sha256((root/'code/check.py').read_bytes()).hexdigest(),'physical_table':f,'a':str(a),'p':{k:str(z) for k,z in p.items()},'u':{k:str(z) for k,z in u.items()}}
(root/'out/root_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:z for k,z in result.items() if k not in ('physical_table','p','u')}))
