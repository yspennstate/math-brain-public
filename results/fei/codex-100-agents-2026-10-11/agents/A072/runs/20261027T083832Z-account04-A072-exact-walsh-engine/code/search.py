from pathlib import Path
from fractions import Fraction as F
import json, math, time, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
def save(name,x):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(x,indent=2,default=str)+'\n',encoding='utf-8')
def fw(a):
    a=list(a); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return a
def table(n,m):return [1-2*((m>>x)&1) for x in range(1<<n)]
def verify(n,m):
    a=table(n,m); N=len(a); w=fw(a)
    assert sum(v*v for v in w)==N*N
    assert fw(w)==[N*v for v in a]
    inf=[]
    for i in range(n):
        edge=sum(a[x]!=a[x^(1<<i)] for x in range(N))
        v=F(sum(w[s]**2 for s in range(N) if s>>i&1),N*N)
        assert v==F(edge,N); inf.append(v)
    return a,w,inf
def L(a,b):
    a,b=float(a),float(b)
    def e(x):return x*math.log2(x) if x else 0.0
    return (e((a+b)**2)+e((a-b)**2))/2-e(a*a)-e(b*b)
def run(pilot=False):
    start=time.perf_counter(); outerN=2 if pilot else 3; innerN=3
    inn=[]; checked=0
    for m in range(1<<(1<<innerN)):
        a,w,ds=verify(innerN,m); checked+=1
        for i,d in enumerate(ds):
            if d:inn.append((m,i,F(w[0],8),F(w[1<<i],8),d))
    # Global sign and input reflection preserve the scalar correction. Quotient
    # only identical absolute (mean, singleton, influence) signatures, retaining witnesses.
    signatures={}
    for m,i,mu,t,d in inn: signatures.setdefault((abs(mu),abs(t),d),(m,i,mu,t,d))
    best=(-1,None); rows=0; pairs=0; candidates=[]
    for hm in range(1<<(1<<outerN)):
        ha,hw,hi=verify(outerN,hm); checked+=1
        for j,q in enumerate(hi):
            if not q:continue
            ab=[(F(hw[s],1<<outerN),F(hw[s|(1<<j)],1<<outerN)) for s in range(1<<outerN) if not s>>j&1]
            for m,i,mu,t,d in signatures.values():
                # Sign orientation is retained: reflecting the physical inner coordinate
                # changes t only; global negation is absorbed by outer input reflection.
                for mu in sorted(set((abs(mu),-abs(mu)))):
                    val=float(q)*L(mu,t)-sum(L(a+mu*b,t*b) for a,b in ab)
                    ratio=val/float(q*d); rows+=1
                    if ratio>best[0]:best=(ratio,dict(outer_n=outerN,outer_mask=hm,outer_coordinate=j,inner_mask=m,inner_coordinate=i,mu=str(mu),t=str(t),d=str(d),q=str(q)))
                    if ratio>2+1e-10:candidates.append((ratio,best[1]))
        if time.perf_counter()-start>50:raise RuntimeError('frozen 50-second budget exhausted')
    result=dict(status='DISCOVERY_ONLY',domain=dict(outer_n=outerN,inner_n=innerN),verified_tables=checked,signature_count=len(signatures),rows=rows,best_ratio_float=best[0],best=best[1],candidate_count=len(candidates),runtime_seconds=time.perf_counter()-start)
    save('PILOT_V2.json' if pilot else 'SEARCH_V2.json',result)
    print(json.dumps(result))
if __name__=='__main__':
    if sys.argv[-1]=='freeze':
        save('FROZEN_SPEC_V2.json',dict(helper_version='A072-full-cancellation-v2-full-row-restored',helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),family='h(g(x), y) with arbitrary 3-bit h and g; all other outer cores distinct uniform dictator bits',domain='all 256 outer and 256 inner truth tables, all physical coordinates; pilot outer n=2',case_count='65536 labelled compositions before exact signature reduction',symmetry='identical absolute mean/singleton/influence signatures only; both mean signs retained; all outer tables retained',arithmetic='integer Walsh and Fraction edge/influence prechecks; float logs discovery ONLY; selected signs independently certified later',memory_estimate_mb=50,max_runtime_seconds=55,pilot_max_seconds=55,automatic_dimension_escalation=False))
        print('FROZEN')
    else:run(sys.argv[-1]=='pilot')
