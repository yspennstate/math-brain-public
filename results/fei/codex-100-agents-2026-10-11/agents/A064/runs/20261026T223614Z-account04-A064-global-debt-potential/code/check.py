"""A064-order-lottery-v1. Exact small Boolean and finite-tree checks."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
PR=(2,3,5,7)
Z=(F(0),)*4
checks=0
def check(b):
    global checks
    checks+=1
    if not b: raise AssertionError(checks)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b): return tuple(x*b for x in a)
def const(x): return (F(x),F(0),F(0),F(0))
def logf(q):
    q=F(q); out=[]; a,b=q.numerator,q.denominator
    for p in PR:
        c=0
        while a%p==0: a//=p; c+=1
        while b%p==0: b//=p; c-=1
        out.append(F(c))
    assert a==b==1,(a,b)
    return tuple(out)
def ln_interval(x):
    z=(x-1)/(x+1); assert 0<=z<=F(1,3)
    value=sum((2*z**(2*j+1)/F(2*j+1) for j in range(40)),F(0))
    tail=2*z**81/(81*(1-z*z))
    return value,value+tail
L2=ln_interval(F(2))
def logp(p):
    e=p.bit_length()-1; a,b=ln_interval(F(p,2**e))
    return F(e)+a/L2[1],F(e)+b/L2[0]
LI=[(F(1),F(1))]+[logp(p) for p in PR[1:]]
@lru_cache(None)
def bounds(a):
    lo=hi=F(0)
    for c,(l,h) in zip(a,LI):
        lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
    return lo,hi
def positive(a):
    if a==Z: return Z
    l,h=bounds(a)
    assert l>0 or h<0,('unresolved sign',a)
    return a if l>0 else Z
def ge(a,b):
    q=sub(a,b)
    return q==Z or bounds(q)[0]>=0
def entropy(p):
    a=Z
    for x in p:
        if x: a=sub(a,mul(logf(x),x))
    return a
def fwht(t):
    a=list(t); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a
def spectral(t):
    w=fwht(t); N=len(t)
    return [F(x*x,N*N) for x in w]
def profile(t):
    p=spectral(t); n=(len(t)).bit_length()-1
    ds=[sum((p[s] for s in range(len(p)) if s>>j&1),F(0)) for j in range(n)]
    for j,d in enumerate(ds):
        check(d==F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)))
    H=entropy(p); M=Z
    for d in ds: M=add(M,entropy([d,1-d]))
    T=sub(M,H); check(ge(T,Z)); check(sum(p)==1)
    # Actual coordinate product, including zero-source and endpoint rows.
    q=[]
    for s in range(len(p)):
        mass=F(1)
        for j,d in enumerate(ds): mass*=d if s>>j&1 else 1-d
        q.append(mass)
    check(sum(q)==1)
    K=Z
    for x,y in zip(p,q):
        if x:
            check(y>0); K=add(K,mul(logf(x/y),x))
    check(K==T)
    return p,H,T,ds
def pivot(t,p,H):
    # bits u=0,v=1,y starts at2, matching the written piecewise definition.
    mask=[t[x>>2]*(-1 if (x&1) and (x&2) else 1) for x in range(4*len(t))]
    pf=spectral(mask); wf=fwht(mask); w=fwht(t)
    check(entropy(pf)==add(H,const(2)))
    for S,x in enumerate(p):
        for b in range(2):
            for c in range(2): check(pf[(S<<2)|(c<<1)|b]==x/4)
    pred=[F(0),F(0)]; children=[{},{}]
    for s in range(len(pf)):
        if s&2: continue
        a,b=wf[s],wf[s|2]; den=2*(a*a+b*b)
        q=pf[s]+pf[s|2]
        for e in range(2):
            k=F((a+(-1 if e else 1)*b)**2,den) if den else F(1,2)
            pred[e]+=q*k
            children[e][s]=q*k*2
    check(pred==[F(1,2)]*2)
    for e in range(2):
        ct=[t[y]*(-1 if e and u else 1) for y in range(len(t)) for u in range(2)]
        cp=spectral(ct)
        check(entropy(cp)==H)
        for s,x in children[e].items(): check(x==cp[(s>>2)*2+(s&1)])
    return sum(1 for x in pf if not x)
def lottery(T,k,kind):
    N=2**k
    costs=[T if ((i==0) if kind==0 else i%2==0) else Z for i in range(N)]
    avg=mul(sumlin(costs),F(1,N))
    after=add(const(2),positive(sub(avg,const(2))))
    before=add(const(2),mul(sumlin([positive(sub(c,const(2))) for c in costs]),F(1,N)))
    check(ge(before,after))
    check(ge(after,const(2))); check(ge(after,avg))
    # Backward optimal adapted stopping: before release, stop costs 2.
    before_values=[add(const(2),positive(sub(c,const(2)))) for c in costs]
    after_values=costs[:]
    for depth in range(k,0,-1):
        bv=[]; av=[]
        for i in range(0,len(before_values),2):
            bmean=mul(add(before_values[i],before_values[i+1]),F(1,2))
            bv.append(add(const(2),positive(sub(bmean,const(2)))))
            amean=mul(add(after_values[i],after_values[i+1]),F(1,2))
            av.append(positive(amean))
            check(ge(bmean,const(2)))
        before_values,after_values=bv,av
    check(before_values[0]==before)
    computed_after=add(const(2),positive(sub(after_values[0],const(2))))
    check(computed_after==after)
    if k and bounds(T)[0]>2:
        check(ge(T,avg))
    return before!=after
def sumlin(xs):
    r=Z
    for x in xs: r=add(r,x)
    return r
def algebra_census():
    # Scale every expected value by8, retaining exact integer arithmetic.
    count=0; strict=0
    for leaves in product(range(4),repeat=8):
        before=sum(max(2,x) for x in leaves)
        after=max(16,sum(leaves))
        values=[8*max(2,x) for x in leaves]
        while len(values)>1:
            values=[max(16,(values[i]+values[i+1])//2) for i in range(0,len(values),2)]
        check(values[0]==before); check(before>=after)
        strict+=before>after; count+=1
    return count,strict
def main():
    start=time.perf_counter(); pilot='pilot' in sys.argv
    nrange=range(2) if pilot else range(4)
    cores=strict=zeros=0
    for n in nrange:
        for mask in range(2**(2**n)):
            t=[-1 if mask>>x&1 else 1 for x in range(2**n)]
            p,H,T,ds=profile(t); zeros+=pivot(t,p,H); cores+=1
            for k in range(4):
                for kind in range(2): strict+=lottery(T,k,kind)
    tensor=[]
    if not pilot:
        p,H,T,ds=profile([-1]+[1]*7)
        for factor in [1,4,16,64]:
            for k in range(4):
                for kind in range(2): strict+=lottery(mul(T,factor),k,kind)
            tensor.append({'factor_count':factor,'TC_interval':list(map(str,bounds(mul(T,factor))))})
        ac,ast=algebra_census()
    else: ac=ast=0
    result={'status':'PASS','mode':'pilot' if pilot else 'main','cores':cores,'checks':checks,
            'strict_ordering_cases':strict,'zero_source_atoms':zeros,'algebra_vectors':ac,
            'algebra_strict':ast,'tensor_costs':tensor,'seconds':round(time.perf_counter()-start,6)}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='tensor_costs'}))
if __name__=='__main__': main()
