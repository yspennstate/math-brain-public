from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=0
def check(ok):
    global checks
    checks+=1
    assert ok, checks
def add(*terms):
    out={}
    for scale,v in terms:
        for p,a in v.items(): out[p]=out.get(p,F(0))+scale*a
    return {p:a for p,a in out.items() if a}
@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logvec(x):
    x=F(x); out=dict(factors(x.numerator))
    for p,a in factors(x.denominator).items(): out[p]=out.get(p,0)-a
    return {p:F(a) for p,a in out.items() if a}
def phi(x):
    return {} if not x else add((-x,logvec(x)))
def fwht(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): u,w=a[k],a[k+h]; a[k],a[k+h]=u+w,u-w
        h*=2
    return a
def stats(v):
    n=(len(v)).bit_length()-1; den=len(v)**2
    p=[F(a*a,den) for a in fwht(v)]
    H=add(*[(1,phi(x)) for x in p])
    I=sum((x*s.bit_count() for s,x in enumerate(p)),F(0))
    return H,I
def child(v,i,b): return [v[x] for x in range(len(v)) if (x>>i)&1==b]
def influence(v,i): return F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
@lru_cache(None)
def ln_bounds(x):
    x=F(x); z=(x-1)/(x+1); terms=32
    low=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return low,low+tail
L2=ln_bounds(F(2))
@lru_cache(None)
def log_bounds(p):
    k=p.bit_length()-1; lo,hi=ln_bounds(F(p,2**k))
    return F(k)+lo/L2[1],F(k)+hi/L2[0]
def bounds(v):
    lo=hi=F(0)
    for p,a in v.items():
        l,h=log_bounds(p)
        lo+=a*(l if a>=0 else h); hi+=a*(h if a>=0 else l)
    return lo,hi
def enc(v): return {str(p):str(a) for p,a in v.items()}
def approx(v): return [float(x) for x in bounds(v)]
def rational_interval(v): return [str(x) for x in bounds(v)]
def activate(g,r): return [g[x] if z==0 else 1 for z in range(2**r) for x in range(len(g))]
count=0; activations=0
for n in range(4):
    for table in range(2**(2**n)):
        v=[1 if table>>x&1 else -1 for x in range(2**n)]; H,I=stats(v); count+=1
        for i in range(n):
            H0,I0=stats(child(v,i,0)); H1,I1=stats(child(v,i,1)); d=influence(v,i)
            check(I==d+(I0+I1)/2)
            D=add((1,H),(-F(1,2),H0),(-F(1,2),H1))
            signed=add((1,H),(-4,{2:I}))
            signed0=add((1,H0),(-4,{2:I0})); signed1=add((1,H1),(-4,{2:I1}))
            check(add((1,signed),(-F(1,2),signed0),(-F(1,2),signed1))==add((1,D),(-4,{2:d})))
        if not n: continue
        a=1-F(sum(v),len(v))
        for r in (1,2,3):
            p=F(1,2**r); w=activate(v,r); HW,IW=stats(w); activations+=1
            check(IW==p*I+r*p*a)
            Q=add((1,HW),(-p,H))
            check(bounds(add((8,{2:r*p*a}),(-1,Q)))[0]>=0)
            if r==1: qnext={}
            else:
                Hnext,_=stats(activate(v,r-1)); qnext=add((1,Hnext),(-2*p,H))
            Hnext,_=stats(activate(v,r-1))
            D=add((1,HW),(-F(1,2),Hnext))
            check(add((1,Q),(-F(1,2),qnext))==D)
records=[]
for r in (0,8):
    k=4; b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(2**k)]
    bp=list(b); bp[0]=-bp[0]
    G,H=activate(b,r),activate(bp,r); v=G+H
    hv,iv=stats(v); h0,i0=stats(G); h1,i1=stats(H)
    d=F(1,2**(r+k)); D=add((1,hv),(-F(1,2),h0),(-F(1,2),h1))
    mu0=F(G.count(-1),len(G)); mu1=F(H.count(-1),len(H)); mu=(mu0+mu1)/2
    minority_drift=add((1,phi(mu)),(-F(1,2),phi(mu0)),(-F(1,2),phi(mu1)))
    fail_a=add((1,D),(-4,{2:d}),(-1,minority_drift))
    fail_b=add((1,D),(-4,{2:d}),(1,{2:(i0+i1)/2}))
    fail_c=add((2,D),(-8,{2:d}))
    for fail in (fail_a,fail_b,fail_c): check(bounds(fail)[0]>0)
    # Entire named function and children satisfy FEI with C=4, independently certified here.
    for hh,ii in ((hv,iv),(h0,i0),(h1,i1)): check(bounds(add((4,{2:ii}),(-1,hh)))[0]>0)
    record={'k':k,'r':r,'d':str(d),'I':str(iv),'mu':str(mu),'D':enc(D),'D_over_d_interval':approx(add((1/d,D))),
            'minority_drift_over_d_interval':approx(add((1/d,minority_drift))),
            'candidate_failure_intervals':{'minority':rational_interval(fail_a),'history':rational_interval(fail_b),'slack':rational_interval(fail_c)}}
    if r:
        core=b+bp; hc,ic=stats(core); a=1-F(sum(core),len(core)); p=F(1,2**r)
        rootQ=add((1,hv),(-p,hc)); hn,_=stats(activate(core,r-1)); nextQ=add((1,hn),(-2*p,hc))
        check(bounds(add((1,nextQ),(-1,rootQ)))[0]>0)
        record.update({'control_reserve_over_control_I_interval':approx(add((1/(r*p*a),rootQ))),
                       'active_child_reserve_growth_interval':approx(add((1,nextQ),(-1,rootQ))),
                       'root_reserve':enc(rootQ),'active_child_reserve':enc(nextQ),'terminal_core_I':str(p*ic)})
    records.append(record)
out={'status':'PASS','exact_assertions':checks,'core_count':count,'activation_cases':activations,'witnesses':records,'runtime_seconds':time.perf_counter()-START,
     'log_certificate':'32-term rational atanh expansion after dyadic normalization, tail 2*z^(65)/(65*(1-z^2)); signed interval multiplication by extrema'}
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
for rec in records: print(json.dumps({k:v for k,v in rec.items() if k.endswith('interval') or k in ('k','r','d')},indent=2))
