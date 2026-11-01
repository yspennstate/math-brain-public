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
def check():
    start=time.monotonic();checks=0;balanced=[]
    for mask in range(16):
        a=[1 if mask>>i&1 else -1 for i in range(4)]
        if sum(a)==0:balanced.append(a)
    for a in balanced:
        for c in balanced:
            assert remainder(a,c)==rhs_remainder(a,c);checks+=1
            drift={};direct={};F=fixture(a,c);h=mux(a,c)
            for j in range(2):
                r=remainder(a,c)
                vf=value(F);wh=value(h,1)
                for b in (0,1):
                    ab,cb=restrict(a,j,b),restrict(c,j,b)
                    assert remainder(ab,cb)==rhs_remainder(ab,cb);checks+=1
                    r=add(r,remainder(ab,cb),-Q(1,2))
                    vf=add(vf,value(restrict(F,6+j,b)),-Q(1,2))
                    wh=add(wh,value(restrict(h,1+j,b),1),-Q(1,2))
                drift=add(drift,r);direct=add(direct,add(vf,wh,-Q(1,32)))
            assert direct==drift;checks+=1
            # Independent full marked-transition decomposition. y disappears at its query.
            wh=value(h,1)
            R=add(add(wh,value(a),-Q(1,2)),value(c),-Q(1,2))
            gmark=add(R,{})
            for j in range(2):
                v=wh
                for bit in (0,1):v=add(v,value(restrict(h,j+1,bit),1),-Q(1,2))
                gmark=add(gmark,v)
            gvF={};data={}
            for j in range(8):
                d=value(F)
                for bit in (0,1):d=add(d,value(restrict(F,j,bit)),-Q(1,2))
                gvF=add(gvF,d)
                if j<6:data=add(data,d)
            full=add(gvF,gmark,-Q(1,32))
            assert full==add(drift,add(data,R,-Q(1,32)));checks+=1
            certified_le(full,321);checks+=1
            certified_le(drift,243);checks+=1
            certified_le(add(data,R,-Q(1,32)),78);checks+=1
            for j in range(2):
                av=spectrum(a)[1<<j];cv=spectrum(c)[1<<j]
                ac=spectrum([x*y for x,y in zip(a,c)])[1<<j]
                r=Q(sum(x*y for x,y in zip(a,c)),4)
                for bit in (0,1):
                    aa,cc=restrict(a,j,bit),restrict(c,j,bit)
                    sg=1 if bit==0 else -1
                    assert Q(sum(aa),2)==sg*av and Q(sum(cc),2)==sg*cv
                    assert Q(sum(x*y for x,y in zip(aa,cc)),2)==r+sg*ac
                    checks+=2
            # Exact DATA influence floor, independently counted on edges.
            influence=sum(Q(sum(F[x]!=F[x^(1<<j)] for x in range(len(F))),len(F)) for j in range(6))
            assert influence>=Q(21,16);checks+=1
    # Boundary constants and curvature arithmetic: no floating logarithms.
    assert Q(3,2)*(Q(1,32)+Q(1,8)+2*36)+Q(5,64)<110;checks+=1
    assert Q(12,32)<110;checks+=1
    assert 3*55+6*13==243;checks+=1
    assert 243+6*13==321<256*Q(21,16);checks+=1
    # Independent direct character transform for a distinct dependent pair.
    a=[1,1,-1,-1];c=[1,-1,1,-1];F=fixture(a,c)
    fw=spectrum(F)
    for s in range(len(F)):
        d=Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(F)),len(F))
        assert d==fw[s];checks+=1
    # Fractional correlations absent from two-bit balanced pairs: explicit 3-bit guards.
    for am,cm in [(15,23),(15,232),(15,240),(23,105)]:
        a=[1 if am>>j&1 else -1 for j in range(8)]
        c=[1 if cm>>j&1 else -1 for j in range(8)]
        assert sum(a)==sum(c)==0;checks+=1
        assert remainder(a,c)==rhs_remainder(a,c);checks+=1
        h=mux(a,c);F=fixture(a,c);wh=value(h,1)
        gm=add(add(wh,value(a),-Q(1,2)),value(c),-Q(1,2));gv={}
        for j in range(3):
            d=wh
            for bit in (0,1):d=add(d,value(restrict(h,j+1,bit),1),-Q(1,2))
            gm=add(gm,d)
        for j in range(9):
            d=value(F)
            for bit in (0,1):d=add(d,value(restrict(F,j,bit)),-Q(1,2))
            gv=add(gv,d)
        certified_le(add(gv,gm,-Q(1,32)),321);checks+=1
    result={'status':'PASS','assertions':checks,'balanced_ordered_pairs':36,'three_bit_pair_guards':4,'max_total_bits':9,'seconds':time.monotonic()-start,'arithmetic':'Fraction spectra, exact prime-log vectors and rational32-term atanh sign certificates; no floating signs','scope':'finite corroboration of identities, not universal inference'}
    save('out/EXACT_CHECK.json',result);print(json.dumps(result))

if __name__=='__main__':
    import sys
    if sys.argv[1]=='orient':orient()
    else:check()
