from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import importlib.util,sys,time,json,hashlib
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261013T234248Z-account05-A088-booleanity-referee/code/check.py'
sp=importlib.util.spec_from_file_location('own_exact_arithmetic',old); h=importlib.util.module_from_spec(sp); sp.loader.exec_module(h)
checks=0
def ck(b):
    global checks
    checks+=1
    assert b
def nonnegative(a):
    ck(not a or h.interval(a)[0]>=0)
@lru_cache(None)
def controller(p):
    mask=sum(1<<i for i,s in enumerate(p) if s>=0)
    val=sum(s<<i for i,s in enumerate(p) if s>=0)
    return mask,val,tuple(int(z&mask==val) for z in range(1<<len(p)))
@lru_cache(None)
def cells(p,q):
    P,a,_=controller(p); Q,b,_=controller(q); n=len(p)
    ck(P|Q==(1<<n)-1)
    u=P&~Q; v=Q&~P; d=(a^b)&P&Q
    groups={}
    for s in range(1,1<<n):
        hits=bool(s&u),bool(s&v)
        key=hits+(((s&d).bit_count()%2,) if d and hits==(False,False) else ())
        groups.setdefault(key,[]).append(s)
    ans=tuple(tuple(g) for g in groups.values())
    ck(len(ans)<=(5 if d else 4))
    ck(sorted(s for c in ans for s in c)==list(range(1,1<<n)))
    ck(sum(F(1,len(ans)) for c in ans)==1 if ans else True)
    for c in ans:
        # Exact logarithmic cardinality inequality, no logarithm evaluation.
        ck(len(c)**len(c)<=1<<(2*sum(s.bit_count() for s in c)))
    return ans,bool(d)
def inspect(g,A,B,p,q,mode):
    m=(len(g)-1).bit_length(); r=len(p); nx,nz=len(g),1<<r
    _,_,pv=controller(p); _,_,qv=controller(q)
    e=[(A[x]*pv[z]^B[x]*qv[z]) if mode=='xor' else int(bool(A[x]*pv[z] or B[x]*qv[z])) for x in range(nx) for z in range(nz)]
    if any(sum(e[x*nz:(x+1)*nz])*4>nz for x in range(nx)): return False
    cs,bad=cells(p,q)
    v=[g[x]*(1-2*e[x*nz+z]) for x in range(nx) for z in range(nz)]
    spec=h.spectrum(v); inf=h.influences(v); iz=sum(inf[:r]); ix=sum(inf[r:]); alpha=sum(spec[s] for s in range(nx*nz) if s%nz)
    rho=F(sum(e),nx*nz)
    rowq=[sum(spec[t*nz:(t+1)*nz]) for t in range(nx)]
    child=[h.spectrum([v[x*nz+z] for x in range(nx)]) for z in range(nz)]
    ck(rowq==[sum(c[t] for c in child)/nz for t in range(nx)])
    cardcost={}
    for t in range(nx):
        for c in cs:
            ck(len({spec[t*nz+s] for s in c})==1)
            mass=sum(spec[t*nz+s] for s in c)
            cardcost=h.add(cardcost,h.factors(len(c)),mass)
    H=h.entropy(spec); HQ=h.entropy(rowq); HC={}
    for c in child: HC=h.add(HC,h.entropy(c),F(1,nz))
    bspec=h.add(H,HQ,-1); J=h.add(HQ,HC,-1); Q=h.add(H,HC,-1)
    ck(h.add(bspec,J)==Q)
    binary=h.entropy([alpha,1-alpha])
    refcost=h.add(h.add(binary,h.factors(len(cs)),alpha),cardcost) if cs else {}
    nonnegative(h.add(refcost,bspec,-1))
    ck(h.interval(cardcost)[1]<=2*iz)
    ck(alpha<=4*rho<=1 and alpha<=iz)
    mask=[1-2*a for a in e]; mi=h.influences(mask)
    ck(ix>=sum(mi[r:]) and iz==sum(mi[:r]))
    ck(h.interval(binary)[1]<=2*(ix+iz))
    Klo=4+h.log2(5 if bad else 4)[0]+2/h.U2
    ck(h.interval(Q)[1]<=Klo*iz+2*ix)
    ck(h.interval(J)[1]<=2*iz/h.U2)
    ck(all(h.U(c)<=sum(h.influences([v[x*nz+z] for x in range(nx)])) for z,c in enumerate(child)))
    ck(h.interval(H)[1]<=max(Klo,F(6))*(ix+iz))
    return True
def geometry(r):
    # Fixed explicit controller assignments; relevant union contracted automatically.
    base=[((0,0,-1),(0,-1,0)),((0,0,-1),(1,-1,0)),((0,0,0),(0,-1,-1)),((0,0,0),(1,-1,-1)),((0,-1,-1),(-1,0,0)),((0,0,0),(0,0,0)),((0,0,0),(1,0,0)),((0,0,-1),(-1,0,0))]
    ans=[]
    for p,q in base:
        p=p+(0,)*(r-3); q=q+tuple(-1 if i%2 else 0 for i in range(r-3))
        ans.append((p,q))
    return ans
def domains(pilot):
    patterns=list(product((-1,0,1),repeat=2))
    pairs=[(p,q) for p in patterns for q in patterns if controller(p)[0]|controller(q)[0]==3]
    for p,q in pairs:
        for g,A,B in product(product((-1,1),repeat=2),product((0,1),repeat=2),product((0,1),repeat=2)):
            for mode in ('xor','or'): yield g,A,B,p,q,mode
    if not pilot:
        for r in (3,4,5):
            for p,q in geometry(r):
                for g,A,B in product(product((-1,1),repeat=2),product((0,1),repeat=2),product((0,1),repeat=2)):
                    for mode in ('xor','or'): yield g,A,B,p,q,mode
        for p,q in [((0,0,-1),(0,-1,0)),((0,0,-1),(1,-1,0)),((0,0,0),(0,-1,-1))]:
            for g,A,B in product(product((-1,1),repeat=4),product((0,1),repeat=4),product((0,1),repeat=4)):
                for mode in ('xor','or'): yield g,A,B,p,q,mode
def conversion():
    # Input coordinates c,u,v,y; tree internal cells all,cuv,uv.
    q=[]; y=[]
    for x in range(16):
        c,u,v,yy=[1 if x>>i&1 else -1 for i in range(4)]
        q.append(1 if c==-1 else u*v); y.append(yy)
    g=[a*b for a,b in zip(q,y)]; f=y
    cell_masks=[15,7,6]
    def gamma(a):
        return sum(w*(1+2*sum(bool(s&c) for c in cell_masks)) for s,w in enumerate(h.spectrum(a)))
    def refunds(a,b):
        total=F(0)
        for C in cell_masks:
            inside=[j for j in range(16) if j&~C==0]
            for x in range(16):
                for j in inside:
                    xp=(x&~C)|j
                    total+=8*F(int(a[x]!=a[xp] and b[x]!=b[xp]),16*len(inside))
        physical=2*sum(F(int(a[x]!=a[x^(1<<i)] and b[x]!=b[x^(1<<i)]),16) for i in range(4) for x in range(16))
        return total,physical
    rt,ri=refunds(g,q)
    ck(rt==F(13,2) and ri==3)
    ck([gamma(g),gamma(q),gamma(f)]==[F(11,2),F(5),F(3)])
    banks=[12*sum(h.influences(g))-gamma(g),12*sum(h.influences(q))-(gamma(q)-1),rt-12*ri]
    ck(banks==[F(49,2),F(14),F(-59,2)] and sum(banks)==9)
    ck(28800*169-100*42961==571100>0)
    return {'resampling_refund':str(rt),'physical_refund':str(ri),'complete_banks':list(map(str,banks)),'final_nonconstant_core_slack':'9','real_product_integer_gap':571100}
def main():
    pilot='pilot' in sys.argv; start=time.perf_counter(); raw=valid=0; digest=hashlib.sha256()
    for args in domains(pilot):
        if pilot and raw>=128: break
        ck(time.perf_counter()-start<(60 if pilot else 300))
        valid+=inspect(*args); raw+=1; digest.update(repr(args).encode())
    conv=conversion()
    out={'raw_inputs':raw,'valid_boolean_cases':valid,'outside_cap_rejected':raw-valid,'exact_assertions':checks,'certificate_domain_sha256':digest.hexdigest(),'runtime_seconds':time.perf_counter()-start,'failures':0,'conversion_guard':conv,'method':'own prior exact rational arithmetic imported; new cells/controllers and direct resampling-pair implementation; no other agent code'}
    (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__': main()
