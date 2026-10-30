import argparse, json, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
START=time.perf_counter(); count=0
ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def factor(x):
    out={}; d=2
    while d*d<=x:
        while x%d==0: out[d]=out.get(d,0)+1; x//=d
        d+=1
    if x>1: out[x]=out.get(x,0)+1
    return out
def logadd(expr,x,mult):
    if not mult: return
    assert x>0
    for p,ex in factor(x.numerator).items(): expr[p]=expr.get(p,F(0))+mult*ex
    for p,ex in factor(x.denominator).items(): expr[p]=expr.get(p,F(0))-mult*ex
def add(expr,other,mult):
    for p,x in other.items(): expr[p]=expr.get(p,F(0))+mult*x
def clean(expr): return {p:x for p,x in expr.items() if x}
def spectrum(table,p):
    n=len(p); poly=list(table)
    for i in range(n):
        for s in range(1<<n):
            if s>>i&1: poly[s]-=poly[s^(1<<i)]
    sp={}
    for s in range(1<<n):
        c=F(0); v=F(1)
        for u,alpha in enumerate(poly):
            if u&s !=s: continue
            term=F(alpha,2**s.bit_count())
            for i in range(n):
                if (u^s)>>i&1: term*=p[i]
            c+=term
        for i in range(n):
            if s>>i&1: v*=4*p[i]*(1-p[i])
        sp[s]=(c,v*c*c)
    assert sum(P for c,P in sp.values())==1
    return sp
def entropy(sp):
    expr={}
    for s,(c,P) in sp.items():
        if s and P: logadd(expr,abs(c),-2*P)
    return clean(expr)
def check(table,p,eps):
    global count
    sg=spectrum(table,p); a=(1-sg[0][0])/2
    V=sum(P for s,(c,P) in sg.items() if s)
    sf=spectrum(tuple(1 if not x&1 else table[x>>1] for x in range(2*len(table))),(eps,)+p)
    rhs={}; add(rhs,entropy(sg),eps)
    logadd(rhs,F(4),eps*(1-eps)*V)
    logadd(rhs,1/eps,2*eps**2*V)
    if a: logadd(rhs,a,-8*eps*(1-eps)*a*a)
    assert entropy(sf)==clean(rhs)
    Ig=sum(s.bit_count()*P for s,(c,P) in sg.items())
    If=sum(s.bit_count()*P for s,(c,P) in sf.items())
    w=sum(P for s,(c,P) in sf.items() if s)
    assert If-w==eps*Ig-eps**2*V
    count+=2
    if time.perf_counter()-START>55: raise RuntimeError('frozen 55-second limit exceeded')
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); args=parser.parse_args()
    laws=((F(1,2),F(1,2)),(F(1,3),F(2,5)),(F(1,16),F(15,16)),(F(3,4),F(1,8)))
    for p in laws[:1] if args.pilot else laws:
        for mask in range(16):
            table=tuple(1 if mask>>x&1 else -1 for x in range(4))
            for eps in ((F(1,3),) if args.pilot else (F(1,2),F(1,3),F(1,1024))): check(table,p,eps)
    result={'status':'PASS','cases':count//2,'exact_formula_assertions':count,'method':'independent Mobius polynomial and canonical prime-log dictionaries','runtime_seconds':time.perf_counter()-START,'pilot':args.pilot}
    (ROOT/'out'/('ENTROPY_PILOT.json' if args.pilot else 'ENTROPY_CHECKS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))
