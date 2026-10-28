import argparse, itertools, json, time
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); assertions=0
def ck(ok):
    global assertions
    assertions+=1
    if not ok: raise AssertionError(assertions)
    if time.perf_counter()-START>55: raise RuntimeError('frozen 55-second runtime exceeded')

def cell(t):
    assert 0<t<=1
    j=0
    while t<=F(1,2): t*=2; j+=1
    return j

def spectrum(table, p):
    n=len(p); out={}
    # Independent direct expectation formula c_S=E[f prod_(i in S)(x_i-p_i)]/v_S.
    # Here x_i is 0/1, so normalized half-derivative requires division by
    # 2^|S| prod p_i(1-p_i), not the sign-coordinate variance v_S.
    for s in range(1<<n):
        moment=F(0); var=F(1); denom=F(1)
        for i in range(n):
            if s>>i&1: var*=4*p[i]*(1-p[i]); denom*=2*p[i]*(1-p[i])
        for x,fx in enumerate(table):
            weight=F(fx)
            for i,pi in enumerate(p):
                bit=x>>i&1
                weight*=pi if bit else 1-pi
                if s>>i&1: weight*=bit-pi
            moment+=weight
        c=moment/denom; mass=var*c*c
        out[s]={'c':c,'P':mass,'v':var,'j':cell(abs(c)) if c else None}
        out[s]['W']=var*F(1,4**out[s]['j']) if c else F(0)
    ck(sum(z['P'] for z in out.values())==1)
    return out

def aggregates(sp):
    V=sum(z['P'] for s,z in sp.items() if s)
    Z=sum(z['W'] for s,z in sp.items() if s)
    I=sum(s.bit_count()*z['P'] for s,z in sp.items())
    J=sum(z['P']*z['j'] for s,z in sp.items() if s and z['P'])
    R=sum(max(0,s.bit_count()-2)*z['P'] for s,z in sp.items() if s)
    return V,Z,I,J,R

def run_case(table,p,k):
    seed=spectrum(table,p); V,Z,I,J,R=aggregates(seed)
    eps=F(1,2**k); mu=seed[0]['c']; a=(1-mu)/2
    actual=tuple(1 if not (x&1) else table[x>>1] for x in range(2*len(table)))
    root=spectrum(actual,(eps,)+p); w,Zf,If,Jf,Rf=aggregates(root)
    ck(w==4*a*eps*(1-a*eps)); ck(If==eps*I+4*a*eps*(1-eps))
    ck(If-w==eps*I-eps**2*V)
    ck(If-w==eps*(I-V)+eps*(1-eps)*V)
    if not V:
        ck(a in (0,1)); ck(If-w==0); ck(Jf==0); ck(Zf==w)
        return 'constant'
    ja=cell(a); b=F(1,4**ja); B=V+4*a*a*ja
    ck(V==4*a*(1-a)); ck(4*a*a*ja<=V); ck(V<=B<=2*V)
    ck(Jf==eps*J+eps*(1-eps)*B+eps**2*k*V)
    Jo=eps*(1-eps)*B+eps**2*k*V
    ck(Jo<=3*eps*(1-eps)*V)
    ck(abs(Jf/eps-J-B)<=eps*(k+2)*V)
    ck(Zf==eps*Z+4*eps*(1-eps)*b)
    Zo=eps*V+4*eps*(1-eps)*b
    ck(Zf>=Zo>=w); ck(w*(Zf-Zo)/Zo<=eps*(Z-V))
    ck(Z-V<=9*(I-V)-6*R)
    ps=4*eps*(1-eps)*a*a/w; qs=4*eps*(1-eps)*b/Zf
    qso=4*eps*(1-eps)*b/Zo
    ck(0<ps<1 and 0<qs<1 and 0<qso<1)
    # Build complete flat and tree references independently from the outer gate.
    # Outer output Y=+1 with probability 1-a, F=1 except X=1,Y=-1.
    outer=spectrum((1,-1,1,1),(eps,1-a))
    wo,zo,io,jo,ro=aggregates(outer)
    ck(wo==w); ck(zo==Zo); ck(jo==Jo); ck(io-wo==eps*(1-eps)*V)
    qflat={s:(1-w if not s else w*z['W']/Zf) for s,z in root.items()}
    qtree={0:1-w,1:w*outer[1]['W']/Zo}
    for T,z in seed.items():
        if not T: continue
        for xbit,A in ((0,2),(1,3)):
            s=2*T+xbit
            qtree[s]=w*outer[A]['W']/Zo*z['W']/Z
    ck(sum(qflat.values())==1); ck(sum(qtree.values())==1)
    ck(qflat[0]==root[0]['P']==qtree[0])
    ck(qflat[1]==w*qs); ck(qtree[1]==w*qso)
    # Ordinary KL chain is checked by exact likelihood-ratio factorizations,
    # not by floating sums of logarithms. Include BOTH full empty terminals.
    for T,z in seed.items():
        if not T: continue
        for xbit in (0,1):
            s=2*T+xbit; rr=root[s]
            ck(rr['c']==z['c']*(F(1,2) if xbit else eps))
            ck(rr['P']==z['P']*eps*((1-eps) if xbit else eps))
            ck(rr['W']==z['W']*eps*((1-eps) if xbit else eps))
            if not z['P']:
                ck(qflat[s]==qtree[s]==0); continue
            ck(rr['j']==z['j']+(1 if xbit else k))
            ck(rr['P']/qflat[s]==(1-ps)/(1-qs)*(z['P']/V)/(z['W']/Z))
            ck(rr['P']/qtree[s]==(1-ps)/(1-qso)*(z['P']/V)/(z['W']/Z))
            ck(qflat[s]/qtree[s]==Zo*Z/(Zf*V))
    ck(root[1]['P']/qflat[1]==ps/qs)
    ck(root[1]['P']/qtree[1]==ps/qso)
    if a==eps==F(1,2): ck(Jo==3*eps*(1-eps)*V)
    return 'nonconstant'

def cases(pilot):
    laws=((F(1,2),F(1,2)),(F(1,3),F(2,5)),(F(1,16),F(15,16)),(F(3,4),F(1,8)))
    if pilot:
        for mask in range(16):
            yield tuple(1 if mask>>x&1 else -1 for x in range(4)),laws[0],1
        return
    for p in laws:
        for mask in range(16):
            for k in (1,2,4,10):
                yield tuple(1 if mask>>x&1 else -1 for x in range(4)),p,k
    for mask in range(256):
        for k in (1,4,10):
            yield tuple(1 if mask>>x&1 else -1 for x in range(8)),(F(1,2),)*3,k

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); args=parser.parse_args()
    counts={'constant':0,'nonconstant':0}
    for table,p,k in cases(args.pilot): counts[run_case(table,p,k)]+=1
    result={'status':'PASS','helper_version':'A042-dyadic-activation-v1','cases':sum(counts.values()),'case_types':counts,'exact_assertions':assertions,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction; pointwise density factorization, no floating sign decisions','pilot':args.pilot}
    dest=ROOT/'out'/('PILOT.json' if args.pilot else 'CHECKS.json'); dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))
