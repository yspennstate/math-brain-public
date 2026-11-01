from pathlib import Path
import runpy, json, time
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
# Load helper definitions only: the frozen tree job has already executed.
src=(ROOT/'code'/'check_transfer.py').read_text(encoding='utf-8')
ns={'__file__':str(ROOT/'code'/'check_transfer.py')}
exec(src.split('start=time.perf_counter();cases=0;')[0],ns)
spec,ent,ce,kl,add,scale,check=(ns[k] for k in ['spec','ent','ce','kl','add','scale','check'])
start=time.perf_counter();cases=0;multibit=0
for n in range(1,4):
    for fmask in range(1<<(1<<n)):
        values=[1 if fmask>>x&1 else -1 for x in range(1<<n)]
        ap=spec(values,tuple(range(n)));p={s:a*a for s,a in ap.items()}
        for block in range(1,1<<n):
            A=[i for i in range(n) if block>>i&1];C=[i for i in range(n) if not block>>i&1]
            m=1<<len(A);children=[]
            for y in range(m):
                vals=[]
                for x in range(1<<len(C)):
                    full=sum(((y>>j)&1)<<i for j,i in enumerate(A))+sum(((x>>j)&1)<<i for j,i in enumerate(C))
                    vals.append(values[full])
                a=spec(vals,tuple(C));children.append({s:v*v for s,v in a.items()})
            marginal={t:sum(child[t] for child in children)/m for t in children[0]}
            B=add(ent(p),scale(ent(marginal),-1))
            J=add(ent(marginal),scale(add(*(ent(ch) for ch in children)),-F(1,m)))
            for mode in range(2):
                refs=[]
                for y in range(m):
                    rho=F(2+y%2,5);mass=F(1,2+y%3)
                    refs.append({t:F(1,1<<len(C)) if mode==0 else mass*rho**t.bit_count()*(1-rho)**(len(C)-t.bit_count()) for t in children[y]})
                r={t:sum(ref[t] for ref in refs)/m for t in marginal}
                Q={};K={}
                for t,w in marginal.items():
                    labels={s:p[s]/w for s in p if s&~block==t} if w else {s:F(1,m) for s in p if s&~block==t}
                    check(sum(labels.values()),F(1))
                    for s,a in labels.items():Q[s]=r[t]*a
                    if w:
                        kp={y:children[y][t]/(m*w) for y in range(m)}
                        kq={y:refs[y][t]/(m*r[t]) for y in range(m)}
                        K=add(K,scale(kl(kp,kq),w))
                leafCE=scale(add(*(ce(ch,ref) for ch,ref in zip(children,refs))),F(1,m))
                leafKL=scale(add(*(kl(ch,ref) for ch,ref in zip(children,refs))),F(1,m))
                check(ce(p,Q),add(B,J,leafCE,scale(K,-1)))
                check(kl(p,Q),add(leafKL,scale(K,-1)))
                check(sum(Q.values()),sum(sum(ref.values()) for ref in refs)/m)
                cases+=1;multibit+=len(A)>1
elapsed=time.perf_counter()-start
assert elapsed<60
res=dict(helper_version='A097-block-reference-lift-v1',cases=cases,multicoordinate_block_cases=multibit,exact_assertions=ns['checks'],failures=0,runtime_seconds=elapsed)
(ROOT/'out'/'BLOCK_RESULTS.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps(res,indent=2))
