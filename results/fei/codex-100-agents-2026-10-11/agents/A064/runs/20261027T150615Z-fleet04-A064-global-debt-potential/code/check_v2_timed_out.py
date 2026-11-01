"""Exact ordinary-query inherited-reference/lottery transactions, v1."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
Z=()
checks=0
def ck(b):
    global checks
    checks+=1
    if not b: raise AssertionError(checks)
def lin(d): return tuple(sorted((p,F(c)) for p,c in d.items() if c))
def add(a,b):
    d=dict(a)
    for p,c in b: d[p]=d.get(p,F(0))+c
    return lin(d)
def scale(a,c): return tuple((p,x*c) for p,x in a if x*c)
def sub(a,b): return add(a,scale(b,-1))
def const(c): return ((2,F(c)),) if c else Z
def suml(xs):
    r=Z
    for x in xs: r=add(r,x)
    return r
@lru_cache(None)
def factor(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1: d[n]=d.get(n,0)+1
    return d
@lru_cache(None)
def logq(q):
    q=F(q); assert q>0
    d=dict(factor(q.numerator))
    for p,c in factor(q.denominator).items(): d[p]=d.get(p,0)-c
    return lin(d)
def ln(x):
    z=(x-1)/(x+1); assert 0<=z<=F(1,3)
    a=sum((2*z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
    return a,a+2*z**65/(65*(1-z*z))
L2=ln(F(2))
@lru_cache(None)
def lp(p):
    if p==2:return F(1),F(1)
    e=p.bit_length()-1; a,b=ln(F(p,2**e))
    low,high=F(e)+a/L2[1],F(e)+b/L2[0]
    unit=2**96
    return F((low*unit).__floor__(),unit),F((high*unit).__ceil__(),unit)
@lru_cache(None)
def interval(a):
    lo=hi=F(0)
    for p,c in a:
        l,h=lp(p); lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
    return lo,hi
@lru_cache(None)
def pos(a):
    if not a:return Z
    l,h=interval(a)
    assert l>0 or h<0,('unresolved sign',a)
    return a if l>0 else Z
def ge(a,b):
    return a==b or interval(sub(a,b))[0]>=0
def entropy(p):return entropy_cached(tuple(p))
@lru_cache(maxsize=4096)
def entropy_cached(p): return suml([scale(logq(x),-x) for x in p if x])
def kl(p,q):return kl_cached(tuple(p),tuple(q))
@lru_cache(maxsize=8192)
def kl_cached(p,q):
    r=Z
    for a,b in zip(p,q):
        if a:
            assert b>0
            r=add(r,scale(logq(a/b),a))
    return r
def fw(t):
    a=list(t); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def spec(t):
    w=fw(t); return [F(x*x,len(t)**2) for x in w]
def productref(p):return productref_cached(tuple(p))
@lru_cache(maxsize=4096)
def productref_cached(p):
    n=len(p).bit_length()-1
    ds=[sum((x for s,x in enumerate(p) if s>>j&1),F(0)) for j in range(n)]
    q=[]
    for s in range(len(p)):
        v=F(1)
        for j,d in enumerate(ds):v*=d if s>>j&1 else 1-d
        q.append(v)
    assert sum(q)==1
    return q
def child(t,i,e):
    return [x for j,x in enumerate(t) if j>>i&1==e]
def erase_index(j,i):return (j&((1<<i)-1))|((j>>(i+1))<<i)
def kernel(t,Q,i):
    w=fw(t); P=spec(t); N=len(P)
    p=[F(0)]*(N//2); q=p.copy(); joint=[p.copy(),p.copy()]
    for s in range(N):
        if s>>i&1:continue
        T=erase_index(s,i); a,b=w[s],w[s|(1<<i)]
        p[T]=P[s]+P[s|(1<<i)]; q[T]=Q[s]+Q[s|(1<<i)]
        for e in range(2):
            k=F((a+(-1 if e else 1)*b)**2,2*(a*a+b*b)) if a*a+b*b else F(1,2)
            joint[e][T]=q[T]*k
    ts=[sum(x) for x in joint]
    Qs=[[x/ts[e] for x in joint[e]] for e in range(2)]
    Ps=[spec(child(t,i,e)) for e in range(2)]
    for e in range(2):
        ck(ts[e]>0);ck(sum(Qs[e])==1);ck(sum(Ps[e])==1)
    return p,q,ts,Ps,Qs
def patterns():
    for x in product(range(2),repeat=4):yield [(x[0],x[1]),(x[2],x[3])]
    yield [(0,0),(0,0),(0,0),(1,1)]
    yield [(0,1),(1,0),(0,1),(1,0)]
    yield [(0,0),(1,0),(0,0),(1,0)]
    yield [(1,1),(1,1),(1,1),(1,1)]
    yield [(1,1)]+[(0,0)]*7

def lottery(C,R,O,Cs,Js,bs,actions):
    N=len(actions)
    ls=[scale(add(scale(bs[0],a),scale(bs[1],b)),F(1,2)) for a,b in actions]
    lam=scale(suml(ls),F(1,N))
    ga=pos(sub(lam,R)); gb=scale(suml([pos(sub(l,R)) for l in ls]),F(1,N))
    ck(ge(gb,ga))
    ck(ge(add(C,ga),add(O,scale(suml(Cs),F(1,2)))))
    # All single-child stopping choices before/after each actual reset.
    vals=[]
    for a0,a1 in actions:
        branch=[]
        for e,a in enumerate([a0,a1]):
            before=add(Cs[e],scale(bs[e],a))
            actual=add(Cs[e],scale(Js[e],a))
            ck(ge(before,Cs[e])); ck(ge(before,actual))
            branch.append(before)
        value=add(O,scale(suml(branch),F(1,2)))
        vals.append(value)
    # Literal charged source/reference cut expectation, independently expanded.
    avg=scale(suml(vals),F(1,N))
    ck(avg==add(sub(C,R),lam))
    ck(add(C,ga)==add(C,pos(sub(avg,C))))
    before_expected=scale(suml([add(C,pos(sub(v,C))) for v in vals]),F(1,N))
    ck(before_expected==add(C,gb))
    return ga!=gb
def run(pilot):
    begin=time.perf_counter(); transactions=lotteries=strict=zero_rows=neg=outcome=erased=0
    witness=None
    for n in ([1,2] if pilot else [1,2,3,4]):
      for mask in range(256 if n==4 else 2**(2**n)):
        if n==4:
            core=[-1 if mask>>x&1 else 1 for x in range(8)]
            t=[(-1 if x&1 else 1)*core[x>>1] for x in range(16)]
        else:t=[-1 if mask>>x&1 else 1 for x in range(2**n)]
        P=spec(t); N=len(P); U=[F(1,N)]*N
        refs=[P,productref(P),U,[(a+b)/2 for a,b in zip(P,U)],[F(s+1,N*(N+1)//2) for s in range(N)]]
        if n==4:
            pc=spec(core)
            refs.extend([[pc[s>>1]*(q1 if s&1 else 1-q1) for s in range(16)] for q1 in [F(31,32),F(1,2)]])
        for i in ([0] if n==4 else range(n)):
          for name,Q in enumerate(refs):
            ck(sum(Q)==1)
            p,q,ts,Ps,Qs=kernel(t,Q,i)
            H=entropy(P); K=kl(P,Q); C=add(H,K)
            E=sub(K,kl(p,q)); O=kl([F(1,2)]*2,ts)
            Hs=[entropy(x) for x in Ps]; Ks=[kl(x,y) for x,y in zip(Ps,Qs)]
            D=sub(H,scale(suml(Hs),F(1,2))); R=add(D,E)
            Cs=[add(h,k) for h,k in zip(Hs,Ks)]
            ck(ge(E,Z));ck(ge(O,Z));ck(ge(D,Z));ck(ge(R,Z))
            ck(K==add(add(E,O),scale(suml(Ks),F(1,2))))
            ck(C==add(add(R,O),scale(suml(Cs),F(1,2))))
            T=[kl(x,productref(x)) for x in Ps]
            Js=[sub(a,b) for a,b in zip(T,Ks)]; bs=[pos(j) for j in Js]
            neg+=sum(1 for j in Js if j and interval(j)[1]<0)
            outcome+=bool(O); erased+=bool(E)
            zero_rows+=sum(1 for a,b in zip(p,q) if a==0 and b>0)
            for acts in patterns():
                strict+=lottery(C,R,O,Cs,Js,bs,acts); lotteries+=1
            # Dropping actual query O is detected by the exact charged identity.
            if O and witness is None:
                witness={'n':n,'truth_mask':mask,'coordinate':i,'reference':name,
                         'O_prime_log':[(p,str(x)) for p,x in O],
                         'O_interval':list(map(str,interval(O)))}
            transactions+=1
            if time.perf_counter()-begin>(55 if pilot else 180):raise TimeoutError('frozen runtime cap')
    out={'status':'PASS','mode':'pilot' if pilot else 'main','transactions':transactions,
         'lotteries':lotteries,'checks':checks,'strict_ordering_cases':strict,
         'negative_signed_child_bills':neg,'positive_outcome_queries':outcome,
         'positive_erasure_queries':erased,'reference_only_erased_rows':zero_rows,
         'outcome_witness':witness,'seconds':round(time.perf_counter()-begin,6)}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='outcome_witness'}))
if __name__=='__main__':run('pilot' in sys.argv)
