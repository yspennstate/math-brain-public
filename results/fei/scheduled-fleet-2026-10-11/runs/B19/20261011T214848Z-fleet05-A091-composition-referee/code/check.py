from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, time, sys, math

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
ASSERTIONS=0
def check(a,b):
    global ASSERTIONS
    assert a==b,(a,b)
    ASSERTIONS+=1
def prod(xs):
    r=Q(1)
    for x in xs:r*=x
    return r
def table(mask,n=2):return tuple(1 if mask>>x&1 else -1 for x in range(1<<n))
@lru_cache(None)
def kernel(ps):
    n=len(ps)
    weights=[prod(ps[i] if x>>i&1 else 1-ps[i] for i in range(n)) for x in range(1<<n)]
    norms=[prod(ps[i]*(1-ps[i]) for i in range(n) if s>>i&1) for s in range(1<<n)]
    k=[[weights[x]*prod(Q((x>>i)&1)-ps[i] for i in range(n) if s>>i&1) for x in range(1<<n)] for s in range(1<<n)]
    # Each row has one common denominator: turn the transform into integer sums.
    ints=[]
    for row in k:
        d=math.lcm(*(z.denominator for z in row))
        ints.append((d,tuple(int(z*d) for z in row)))
    return ints,norms
@lru_cache(None)
def spectrum(t,ps):
    rows,norms=kernel(ps)
    raw=tuple(Q(sum(v*f for v,f in zip(row,t)),d) for d,row in rows)
    masses=tuple(v*v/norm for v,norm in zip(raw,norms))
    check(sum(masses),Q(1))
    return raw,masses
@lru_cache(None)
def factor(z):
    d={}
    for a,sgn in [(z.numerator,1),(z.denominator,-1)]:
        p=2
        while p*p<=a:
            while a%p==0:d[p]=d.get(p,0)+sgn;a//=p
            p+=1
        if a>1:d[a]=d.get(a,0)+sgn
    return {p:e for p,e in d.items() if e}
def add(*parts):
    out={}
    for c,d in parts:
        for p,v in d.items():out[p]=out.get(p,Q(0))+c*v
    return {p:v for p,v in out.items() if v}
def ent(ps):return add(*[(-p,factor(p)) for p in ps if p])
def corrected(P,ps):
    return add(*[(p,factor(prod(4*ps[i]*(1-ps[i]) for i in range(len(ps)) if s>>i&1)/p)) for s,p in enumerate(P) if s and p])
def inf(P):return sum(s.bit_count()*p for s,p in enumerate(P))
def delta(P):return inf(P)-(1-P[0])
def disjoint(outer,u,v,ps):
    rp,P=spectrum(u,ps[:2]);rq,Qp=spectrum(v,ps[2:])
    mu=(rp[0],rq[0]);vars=tuple(1-m*m for m in mu)
    active=[i for i in range(2) if vars[i]]
    op=tuple((1+mu[i])/2 for i in active)
    reduced=[]
    for a in range(1<<len(active)):
        idx=0
        for i in range(2):
            bit=((a>>active.index(i))&1) if i in active else int(mu[i]>0)
            idx|=bit<<i
        reduced.append(outer[idx])
    _,G=spectrum(tuple(reduced),op)
    Ft=tuple(outer[int(u[x&3]>0)|(int(v[x>>2]>0)<<1)] for x in range(16))
    rf,F=spectrum(Ft,ps)
    weights={i:sum(p for a,p in enumerate(G) if a>>j&1)/vars[i] for j,i in enumerate(active)}
    predicted=[]
    for s in range(16):
        blocks=(s&3,s>>2)
        if any(blocks[i] for i in range(2) if i not in active):predicted.append(Q(0));continue
        a=sum(int(bool(blocks[i]))<<j for j,i in enumerate(active))
        val=G[a]
        for i in active:
            if blocks[i]:val*=(P if i==0 else Qp)[blocks[i]]/vars[i]
        predicted.append(val)
    check(F,tuple(predicted))
    check(rf[0]*rf[0],G[0])
    check(inf(F),sum(weights[i]*inf((P,Qp)[i]) for i in active))
    check(delta(F),delta(G)+sum(weights[i]*delta((P,Qp)[i]) for i in active))
    check(corrected(F,ps),add((1,corrected(G,op)),*[(weights[i],corrected((P,Qp)[i],ps[i*2:i*2+2])) for i in active]))
    check(ent(F),add((1,ent(G)),*[(weights[i],add((1,ent((P,Qp)[i])),(-1,ent((vars[i],1-vars[i]))))) for i in active]))

def uniform_coeff(t):
    n=(len(t)-1).bit_length()
    return tuple(Q(sum(f*(-1 if (s&x).bit_count()%2 else 1) for x,f in enumerate(t)),len(t)) for s in range(1<<n))
def shared(branches):
    N=len(branches);a=(N-1).bit_length()
    cs=[uniform_coeff(t) for t in branches]
    physical=tuple(branches[x&(N-1)][x>>a] for x in range(N*4))
    actual=uniform_coeff(physical)
    # uniform_coeff uses the bit-sign basis rather than x=(2bit-1); common signs cancel in squares.
    F=tuple(c*c for c in actual)
    R=[sum(c[t]*c[t] for c in cs)/N for t in range(4)]
    correction={};isel=Q(0)
    for t,rt in enumerate(R):
        if not rt:continue
        r=[c[t]*c[t]/(N*rt) for c in cs]
        tau=[]
        for s in range(N):
            c=sum(cs[b][t]*(-1 if (s&b).bit_count()%2 else 1) for b in range(N))/N
            check(c*c,F[s|(t<<a)])
            tau.append(c*c/rt)
        check(sum(tau),Q(1))
        correction=add((1,correction),(rt,ent(tau)),(-rt,ent(r)))
        isel+=rt*sum(s.bit_count()*p for s,p in enumerate(tau))
    avgH=add(*[(Q(1,N),ent([c*c for c in row])) for row in cs])
    check(ent(F),add((Q(a),{2:Q(1)}),(1,avgH),(1,correction)))
    data=sum(inf([c*c for c in row]) for row in cs)/N
    check(inf(F),data+isel)
    edge=sum(Q(sum(branches[b][y]!=branches[b^(1<<j)][y] for y in range(4)),4*N) for b in range(N) for j in range(a))
    check(isel,edge)
    return all(sum(branches[b][y]*branches[b^(1<<j)][y] for y in range(4))==0 for b in range(N) for j in range(a))

def main():
    pilot='--pilot' in sys.argv
    tabs=[table(i) for i in range(16)]
    laws=[(Q(1,2),)*4,(Q(1,8),Q(1,4),Q(1,3),Q(2,3)),(Q(1,3),Q(2,3),Q(1,8),Q(1,4))]
    dcount=0;scount=0;orth=0
    if pilot:
        for o in tabs:disjoint(o,tabs[1],tabs[6],laws[0]);dcount+=1
    else:
        selected=[int(sys.argv[sys.argv.index('--law')+1])] if '--law' in sys.argv else list(range(3))
        for law in selected:
            ps=laws[law]
            for u in tabs:
                for v in tabs:
                    for o in tabs:
                        if time.perf_counter()-START>58:
                            (ROOT/'out/timeout.json').write_text(json.dumps({'completed_disjoint':dcount,'law':law,'runtime_seconds':time.perf_counter()-START,'assertions':ASSERTIONS}))
                            raise RuntimeError('frozen runtime exhausted')
                        disjoint(o,u,v,ps);dcount+=1
        for u in tabs if 0 in selected else []:
            for v in tabs:
                for branches in [(u,v),(u,v,tuple(x*y for x,y in zip(u,v)),u)]:
                    orth+=shared(branches);scount+=1
    out={'helper':'A091-exact-composition-v1','pilot':pilot,'disjoint_cases':dcount,'shared_cases':scount,'orthogonal_neighbor_cases':orth,'exact_assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction; rational prime-log coefficient identities','status':'PASS'}
    filename='pilot.json' if pilot else ('checks-law'+str(selected[0])+'.json' if '--law' in sys.argv else 'checks.json')
    (ROOT/'out'/filename).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
