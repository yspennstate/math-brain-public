"""Independent finite review. No producer imports; all decisions exact."""
from pathlib import Path
from fractions import Fraction as F
import json, time, hashlib, sys, itertools
RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
START=time.perf_counter(); CHECKS=0
def check(v):
    global CHECKS
    CHECKS+=1
    if not v: raise AssertionError(CHECKS)
    if time.perf_counter()-START>50: raise TimeoutError('frozen 50-second cap')
def ln(x):
    x=F(x); assert x>0
    k=0
    while x>2: x/=2;k+=1
    while x<1: x*=2;k-=1
    def series(y):
        z=(y-1)/(y+1); s=F(0); power=z
        for j in range(18): s+=2*power/(2*j+1);power*=z*z
        return s,s+2*power/(37*(1-z*z))
    a,b=series(x);c,d=series(F(2))
    return (a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)
LOG={}
def log(x):
    if x not in LOG: LOG[x]=ln(x)
    return LOG[x]
def linear(terms):
    lo=hi=F(0)
    for coef,arg in terms:
        if not coef: continue
        a,b=log(arg)
        lo+=coef*(a if coef>=0 else b);hi+=coef*(b if coef>=0 else a)
    return lo,hi
def D(p,q):return [(v,v/q[i]) for i,v in enumerate(p) if v]
def neg(terms):return [(-a,b) for a,b in terms]
def zero(terms):
    # Exact equality by prime exponents; no logarithm evaluation.
    def factors(n):
        r={};d=2
        while d*d<=n:
            while n%d==0:r[d]=r.get(d,0)+1;n//=d
            d+=1
        if n>1:r[n]=r.get(n,0)+1
        return r
    ex={}
    for a,b in terms:
        for n,sgn in [(b.numerator,1),(b.denominator,-1)]:
            for p,k in factors(n).items():ex[p]=ex.get(p,F(0))+sgn*a*k
    check(all(v==0 for v in ex.values()))
def spectrum(vals):
    n=len(vals)
    return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)),n) for s in range(n)]
def project(p,i):
    ids=[s for s in range(len(p)) if not (s>>i)&1]
    return [p[s]+p[s|(1<<i)] for s in ids]
def child(vals,i,b):return [vals[x] for x in range(len(vals)) if (x>>i)&1==b]
def tests(pilot):
    roots=edges=updates=0
    # Exhaust n<=2; 16 explicit n=3 tables. No symmetry reduction.
    for n in range(4):
        tables=range(1<<(1<<n)) if n<3 else [0,1,3,7,15,23,30,60,85,105,127,128,150,170,254,255]
        if pilot and n>1:break
        for table in tables:
            vals=[1 if table>>x&1 else -1 for x in range(1<<n)]
            a=spectrum(vals);p=[v*v for v in a];roots+=1
            check(sum(p)==1)
            uniform=[F(1,len(p))]*len(p)
            qs=[p,uniform,[(x+y)/2 for x,y in zip(p,uniform)]]
            for q in qs:
                for i in range(n):
                    pp=project(p,i);qq=project(q,i)
                    cs=[[v*v for v in spectrum(child(vals,i,b))] for b in [0,1]]
                    check(all((x+y)/2==v for x,y,v in zip(*cs,pp)))
                    J=[(a/2,b) for c in cs for a,b in D(c,pp)]
                    L=D(p,q)+neg(D(pp,qq))
                    zero([(a/2,b) for c in cs for a,b in D(c,qq)]+neg(D(p,q))+L+neg(J))
                    # L >= 0: allow exact identity before interval comparison.
                    low,high=linear(L)
                    if low<0: zero(L)
                    inf=sum(p[s] for s in range(len(p)) if s>>i&1)
                    jl,jh=linear(J)
                    check(jh<=2*inf or (inf==0 and jh==0))
                    # Influence telescope, independently from edge disagreements.
                    I=sum(F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals)) for j in range(n))
                    Ic=[]
                    for b in [0,1]:
                        vs=child(vals,i,b)
                        Ic.append(sum(F(sum(vs[x]!=vs[x^(1<<j)] for x in range(len(vs))),len(vs)) for j in range(n-1)))
                    check(I==inf+sum(Ic)/2);edges+=1
                # Full singleton calibration includes p=0,q>0 and t endpoints.
                for t in [F(0),F(1,4),F(1,2),F(1)]:
                    r=[(1-t)*x+t*y for x,y in zip(q,p)]
                    slack=D(p,q)+neg(D(p,r))+neg(D(r,q))
                    if 0<t<1:
                        sym=[((1-t)/t*a,b) for a,b in D(r,q)+D(q,r)]
                        zero(slack+neg(sym))
                    else:zero(slack)
                    check(sum(r)==1);updates+=1
    return dict(roots=roots,query_edges=edges,calibrations=updates)
def bent_guard():
    rows=[]
    for m in [2,4,6,8]:
        N=1<<m
        c=[-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2 else 1 for x in range(N)]
        # O(N log N) independently verify actual Boolean bent spectrum.
        a=list(c);step=1
        while step<N:
            for k in range(0,N,2*step):
                for j in range(step):u,v=a[k+j],a[k+j+step];a[k+j]=u+v;a[k+j+step]=u-v
            step*=2
        check(all(v*v==N for v in a));check(sum(c)==1<<(m//2))
        g=[F(v,N) for v in a];h=[v-F(2,N) for v in g]
        check(sum(v*v for v in h)==1)
        ps=[[v*v for v in g],[v*v for v in h]];mix=[(x+y)/2 for x,y in zip(*ps)]
        J=[(coef/2,arg) for p in ps for coef,arg in D(p,mix)]
        lo,hi=linear(J);l2,u2=ln(F(2));d=F(1,N)
        ratio=(lo/(u2*d),hi/(l2*d))
        if m>=4:
            exact_bound=F(2)-F(4,N-2*(1<<(m//2)))
            check(lo/d>=exact_bound)
        rows.append({'m':m,'N':N,'selector_influence':str(d),'ratio_lower':str(ratio[0]),'ratio_upper':str(ratio[1]),'decimal_display':float(ratio[0])})
    return rows
if __name__=='__main__':
    pilot='pilot' in sys.argv
    result=tests(pilot)
    if not pilot:result['bent_sharpness']=bent_guard()
    result.update(checks=CHECKS,seconds=time.perf_counter()-START,arithmetic='Fraction, exact prime log identities and 18-term atanh enclosure')
    name='PILOT.json' if pilot else 'REVIEW.json'
    (RUN/'out'/name).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='bent_sharpness'}))
