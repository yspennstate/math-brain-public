from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,time
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); SCALE=1<<96
def rounded(l,u): return Q((l*SCALE).numerator//(l*SCALE).denominator,SCALE),Q(-((-u*SCALE).numerator//(-u*SCALE).denominator),SCALE)
def add(*xs): return rounded(sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0)))
def scale(a,x): return rounded(a*x[0],a*x[1]) if a>=0 else rounded(a*x[1],a*x[0])
def neg(x): return -x[1],-x[0]
@lru_cache(None)
def ln(y):
    z=(y-1)/(y+1); assert 0<=z<=Q(1,3)
    s=Q(0); power=z
    for j in range(36): s+=2*power/(2*j+1); power*=z*z
    tail=2*power/(73*(1-z*z))
    return rounded(s,s+tail)
@lru_cache(None)
def log2(q):
    assert q>0
    e=q.numerator.bit_length()-q.denominator.bit_length()
    y=q/Q(2)**e
    if y<1: e-=1; y*=2
    l,u=ln(y); l2,u2=ln(Q(2)); return rounded(e+l/u2,e+u/l2)
def eta(q): return (Q(0),Q(0)) if not q else scale(-q,log2(q))
def combine(m,H,I,n,K,J):
    a=(1+n)/2; b=(1+m)/2; v=1-m*m; w=1-n*n; out=(1-m-n-m*n)/2
    HC=add(H,neg(eta(m*m))); KC=add(K,neg(eta(n*n)))
    E=add(eta(out*out),scale(a*a,HC),scale(v,eta(a*a)),scale(b*b,KC),scale(w,eta(b*b)),scale(w/4,HC),scale(v/4,KC),(v*w/2,v*w/2))
    return out,E,a*I+b*J
rows=[]; first=None
for sign in [1,-1]:
    m=Q(0); H=(Q(0),Q(0)); I=Q(1); table=(1,-1)
    for d in range(11):
        row=dict(sign=sign,depth=d,n=2**d,mean=str(m),H=[str(a) for a in H],I=str(I),margin=[str(a-Q(9,2)*I) for a in H])
        rows.append(row)
        if first is None and H[0]>Q(9,2)*I: first=row
        if d<=3:
            # Independently expand actual Boolean truth tables and use butterfly transform.
            from check import fwht,eta as etaprime,add as addprime,bounds
            sp=fwht(table); Hdirect=bounds(addprime(*(etaprime(a*a) for a in sp)))
            Idirect=sum((a*a*s.bit_count() for s,a in enumerate(sp)),Q(0))
            assert Idirect==I and not (Hdirect[1]<H[0] or H[1]<Hdirect[0])
            if d<3:
                table=tuple(-1 if a==1 and sign*b==1 else 1 for b in table for a in table)
        if d<10: m,H,I=combine(m,H,I,sign*m,H,I)
assert first is not None
result=dict(status='PASS',arithmetic='96-bit outward dyadic intervals; 36-term rational atanh plus explicit tail',first_certified_seed=first,rows=rows,seconds=time.perf_counter()-start)
(ROOT/'out/SEED_CERTIFICATE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(dict(status='PASS',seed_depth=first['depth'],variables=first['n'],margin=first['margin'],seconds=result['seconds'])))
