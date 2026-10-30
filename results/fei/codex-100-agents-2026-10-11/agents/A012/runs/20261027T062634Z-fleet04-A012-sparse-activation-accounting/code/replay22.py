"""Independent direct characters and rational likelihood products; no author imports."""
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import json,time
T=time.monotonic();checks=0
def ck(b):
    global checks
    checks+=1;assert b,checks
    if time.monotonic()-T>55:raise TimeoutError('frozen replay cap')
def spec(tt,n,fixed=None):
    fixed=fixed or {};free=[i for i in range(n) if i not in fixed]
    inputs=[x for x in range(1<<n) if all((x>>i)&1==b for i,b in fixed.items())]
    out={}
    for s in range(1<<n):
        if any((s>>i)&1 for i in fixed):continue
        a=sum((1 if tt>>x&1 else -1)*(-1 if (s&x).bit_count()%2 else 1) for x in inputs)
        if a:out[s]=F(a*a,len(inputs)**2)
    return out
def project(p,i):
    q={}
    for s,v in p.items():q[s&~(1<<i)]=q.get(s&~(1<<i),F(0))+v
    return q
def kl(p,q):return [(v,v/q[s]) for s,v in p.items() if v]
def ent(p):return [(-v,v) for v in p.values() if v]
def mul(terms,c):return [(w*c,r) for w,r in terms]
def zero(terms):
    den=lcm(*(w.denominator for w,r in terms)) if terms else 1
    value=F(1)
    for w,r in terms:value*=r**int(w*den)
    return value==1
roots=edges=updates=0
for n in range(4):
    for tt in range(1<<(1<<n)):
        if n==3 and tt not in (0,1,7,8,23,42,69,85,105,127,128,150,170,215,254,255):continue
        p=spec(tt,n);roots+=1
        for kind in range(4):
            if kind==0:q=p
            elif kind==1:q={s:F(1,1<<n) for s in range(1<<n)}
            elif kind==2:q={s:(p.get(s,F(0))+F(1,1<<n))/2 for s in range(1<<n)}
            else:q={s:F(2**(n-s.bit_count()),3**n) for s in range(1<<n)}
            for i in range(n):
                a=spec(tt,n,{i:0});b=spec(tt,n,{i:1});pm=project(p,i);qm=project(q,i)
                ck(pm=={s:(a.get(s,F(0))+b.get(s,F(0)))/2 for s in set(a)|set(b)})
                js=mul(kl(a,pm)+kl(b,pm),F(1,2))
                ck(zero(js+mul(ent(pm),-1)+mul(ent(a)+ent(b),F(1,2))))
                loss=kl(p,q)+mul(kl(pm,qm),-1)
                ck(zero(mul(kl(a,qm)+kl(b,qm),F(1,2))+loss+mul(kl(p,q),-1)+mul(js,-1)))
                edges+=1
            cells=lambda s:int(s!=0)
            pc={c:sum((v for s,v in p.items() if cells(s)==c),F(0)) for c in (0,1)}
            qc={c:sum((v for s,v in q.items() if cells(s)==c),F(0)) for c in (0,1)}
            rc={c:(pc[c]+qc[c])/2 for c in (0,1)}
            r={s:v*rc[cells(s)]/qc[cells(s)] for s,v in q.items() if v}
            # Half-step saving = Jeffreys(rc,qc); all q-positive cells stay.
            ck(zero(kl(p,q)+mul(kl(p,r),-1)+mul(kl(r,q),-1)+mul(kl(rc,qc)+kl(qc,rc),-1)))
            updates+=1
result={'status':'PASS','roots':roots,'root_query_edges':edges,'half_profile_updates':updates,'assertions':checks,'elapsed_seconds':time.monotonic()-T,'method':'direct character sums and exact rational likelihood products, no author imports; algebra identities only, analytic proof supplies inequalities','domain':'All n<=2 plus16 explicitly frozen n=3 truth tables','independent_agent_review':False}
out=Path(__file__).resolve().parents[1]/'out/REPLAY.json';out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
