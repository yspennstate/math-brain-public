from pathlib import Path
import json, hashlib, time
from fractions import Fraction as Q
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
OWN=ROOT.parents[1]
def save(name,obj):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def orient():
    base=Path(r'math-open-problems/reports\fei-2026-10-11')
    push=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
    ctx=Path(r'context')
    files=[Path(r'~\AGENTS.md')]+[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
    files += [push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    files += [p for p in (push/'sources').rglob('*') if p.suffix in ('.txt','.md','.tex','.json')]+list(ctx.glob('*.txt'))
    files += [Path(r'BOARD.md'),Path(r'claude\B05\STREAM_NOTES.md')]
    files += list((base/'runs').glob('B05/*/REPORT.md'))
    files += [p/'REPORT.md' for p in (OWN/'runs').iterdir() if p!=ROOT and (p/'REPORT.md').exists()]
    receipts=[]; relevant=[]
    for p in files:
        if not p.is_file():
            receipts.append({'path':str(p),'missing':True});continue
        b=p.read_bytes()
        try:s=b.decode('utf-8-sig');encoding='utf-8-sig'
        except UnicodeDecodeError:s=b.decode('cp1252');encoding='cp1252-fallback-explicit'
        receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':encoding})
        lines=s.splitlines()
        keys=('A021','A022','C024','C019','balanced','composition','Proposition 8.9','Corollary 8.10','entropy','singular')
        hits=[{'line':i+1,'text':v[:400]} for i,v in enumerate(lines) if any(k in v for k in keys)]
        relevant.append({'path':str(p),'hits':hits[:12]})
    save('out/SOURCE_RECEIPTS.json',receipts);save('out/SOURCE_EXCERPTS.json',relevant)
    print('Source bytes read and hashed:',len(receipts),'(not a claim of full semantic review)')
    print(json.dumps(relevant[-3:],ensure_ascii=False)[:1200])

@lru_cache(None)
def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(x,y,scale=Q(1)):
    z=dict(x)
    for p,c in y.items():
        z[p]=z.get(p,Q(0))+scale*c
        if not z[p]:del z[p]
    return z
def logterm(w,r):
    if not w:return {}
    z={p:w*k for p,k in factor(r.numerator).items()}
    return add(z,{p:Q(k) for p,k in factor(r.denominator).items()},-w)
@lru_cache(None)
def ln_interval(n):
    def series(x):
        y=(x-1)/(x+1)
        low=2*sum((y**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
        return low,low+2*y**65/(65*(1-y*y))
    lo2,hi2=series(Q(2));k=n.bit_length()-1
    lo,hi=series(Q(n,1<<k))
    return k*lo2+lo,k*hi2+hi
def certified_le(z,bound):
    # Compare sum coefficients*log2(prime) to a rational bound, exactly.
    terms=add(z,{2:Q(bound)},-Q(1));upper=Q(0)
    for p,v in terms.items():
        lo,hi=ln_interval(p);upper+=v*(hi if v>=0 else lo)
    assert upper<=0
def spectrum(f):
    a=list(f);N=len(a);h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return [Q(x,N) for x in a]
def restrict(f,j,b):
    return [f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(f)//2)]
def value(f,skip=0):
    a=spectrum(f);p=[x*x for x in a];u=list(p);n=(len(f)).bit_length()-1
    for j in range(n):
        for s in range(len(f)):
            if not s>>j&1:u[s]+=u[s|1<<j]
    z={}
    for s in range(1,len(f)):
        if s!=skip and p[s]:z=add(z,logterm(p[s],u[s]/p[s]))
    return z
def fixture(a,c):
    def seed(x):return (-1 if (x&7)==0 else 1)*(-1 if (x>>3)==0 else 1)
    return [seed(x)*(a[z] if x==0 else c[z] if x==1 else 1) for z in range(len(a)) for x in range(64)]
def mux(a,c):return [a[z] if y==0 else -c[z] for z in range(len(a)) for y in range(2)]
def remainder(a,c):
    F=fixture(a,c);h=mux(a,c)
    return add(value(F),value(h,1),-Q(1,32))
def rhs_remainder(a,c):
    F=fixture(a,c);aa=spectrum(a);cc=spectrum(c)
    # DATA marginal and empty-controller row obtained independently from full F spectrum.
    ff=spectrum(F);p=[x*x for x in ff]
    m=[sum(p[s+64*t] for t in range(len(a))) for s in range(64)]
    u=list(m)
    for j in range(6):
        for s in range(64):
            if not s>>j&1:u[s]+=u[s|1<<j]
    E={}
    for s in range(1,64):
        if p[s]:E=add(E,logterm(p[s],u[s]/p[s]))
    return add(E,{2:Q(5,128)*(2-aa[0]**2-cc[0]**2)})
