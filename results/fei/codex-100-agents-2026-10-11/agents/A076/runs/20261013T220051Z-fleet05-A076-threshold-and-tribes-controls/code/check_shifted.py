"""A076 shifted-row v1: independently enumerated spectra and adaptive trees."""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json, time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def plus(*pairs):
    out=defaultdict(F)
    for expr,w in pairs:
        for x,c in expr.items(): out[x]+=w*c
    return {x:c for x,c in out.items() if c and x!=1}
def phi(p): return {} if not p else {1/p:p}
def Phi(p,q): return plus((phi(p),F(1)),(phi(q),F(1)),(phi(p+q),F(-1)))
@lru_cache(None)
def coeff(t):
    v=list(t); h=1
    while h<len(v):
        for k in range(0,len(v),2*h):
            for j in range(k,k+h): v[j],v[j+h]=v[j]+v[j+h],v[j]-v[j+h]
        h*=2
    return tuple(F(a,len(v)) for a in v)
def H(t): return plus(*[(phi(a*a),F(1)) for a in coeff(t)])
def I(t): return sum((s.bit_count()*a*a for s,a in enumerate(coeff(t))),F(0))
def inf(t,i): return sum((a*a for s,a in enumerate(coeff(t)) if s>>i&1),F(0))
def B(t,i):
    c=coeff(t)
    return plus(*[(Phi(c[s]**2,c[s|(1<<i)]**2),F(1)) for s in range(len(c)) if not s>>i&1])
def child(t,i,bit):
    return tuple(t[(z&((1<<i)-1))+((z>>i)<<(i+1))+(bit<<i)] for z in range(len(t)//2))
def wrap(t,orientation):
    return tuple((1 if x==0 else t[z]) if orientation=='OR' else (t[z] if x==0 else -1)
                 for z in range(len(t)) for x in range(2))
def D(mu,a):
    return plus((Phi((1+mu)**2,a*a),F(1,4)),(Phi((1-mu)**2,a*a),F(1,4)),(Phi(mu*mu,a*a),F(-1,2)))
def R(mu):
    # constant represented as log2(2)
    return plus(({F(2):1-mu*mu},F(1)),(phi((1+mu)**2/4),F(1)),
                (phi((1-mu)**2/4),F(1)),(phi(mu*mu),F(-1,2)))
TERMS=24; SCALE=1<<70
def lnseries(x):
    z=(x-1)/(x+1)
    low=sum((2*z**(2*k+1)/F(2*k+1) for k in range(TERMS)),F(0))
    return low,low+2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z*z))
LN2=lnseries(F(2))
@lru_cache(None)
def logbounds(x):
    if x==1:return F(0),F(0)
    k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
    while y<1:k-=1;y*=2
    while y>2:k+=1;y/=2
    lo,hi=lnseries(y)
    lo+=k*LN2[0 if k>=0 else 1];hi+=k*LN2[1 if k>=0 else 0]
    corners=[a/b for a in (lo,hi) for b in LN2];lo=min(corners);hi=max(corners)
    return F((lo.numerator*SCALE)//lo.denominator,SCALE),F(-((-hi.numerator*SCALE)//hi.denominator),SCALE)
def bounds(e):
    lo=hi=F(0)
    for x,c in e.items():
        a,b=logbounds(x);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def equal_expr(e):
    # Exact logarithmic equality via rational product, independent of log bases.
    global checks
    den=1
    from math import lcm
    for c in e.values():den=lcm(den,c.denominator)
    product=F(1)
    for x,c in e.items():product*=x**int(c*den)
    eq(product,F(1))
def leq(e,rhs):
    global checks
    if not e:eq(F(0)<=rhs,True);return
    lo,hi=bounds(e)
    if hi<=rhs:checks+=1;return
    if lo<=rhs<=hi:
        equal_expr(plus((e,F(1)),({F(2):rhs},F(-1))))
        return
    raise AssertionError(('inequality',e,rhs,lo,hi))
records=[];local_cases=tree_cases=0
def encoded(e):return [[str(x),str(c)] for x,c in sorted(e.items())]
def tree(t,orient,policy,stop):
    todo=[(t,F(1))];bg={};bw={};dt={};hx={};hg={};rw={};suffix={}
    spent=li=wx=F(0);nodecount=0
    while todo:
        g,w=todo.pop();n=len(g).bit_length()-1;mu=coeff(g)[0];W=wrap(g,orient)
        if len(set(g))==1 or (stop and n<=1):
            hg=plus((hg,F(1)),(H(g),w));hx=plus((hx,F(1)),(H(W),w))
            rw=plus((rw,F(1)),(R(mu),w));li+=w*I(g)
            suffix=plus((suffix,F(1)),(B(W,0),w))
            wx+=w*inf(W,0)
            # actual x children: constant and core
            equal_expr(plus((H(child(W,0,0)),F(1,2)),(H(child(W,0,1)),F(1,2)),(H(g),F(-1,2))))
            continue
        ds=[inf(g,i) for i in range(n)]
        i=min(range(n),key=lambda j:((-ds[j] if policy=='max' else ds[j]),j))
        a=coeff(g)[1<<i];d=ds[i];nodecount+=1
        bg=plus((bg,F(1)),(B(g,i),w));bw=plus((bw,F(1)),(B(W,i+1),w))
        dt=plus((dt,F(1)),(D(mu,a),w));spent+=w*d
        todo.extend((child(g,i,b),w/2) for b in range(2))
    eq(spent+li,I(t));eq(wx,inf(wrap(t,orient),0))
    equal_expr(plus((bw,F(1)),(bg,F(-1,2)),(dt,F(-1))))
    equal_expr(plus((hx,F(1)),(hg,F(-1,2)),(rw,F(-1))))
    leq(dt,spent);leq(plus((dt,F(-1))),spent)
    leq(suffix,4*wx)
    leq(plus((bw,F(1)),(suffix,F(1)),(bg,F(-1,2))),spent+4*wx)
    return dict(policy=policy,stop=stop,nodes=nodecount,spent=str(spent),leafI=str(li),
                correction=encoded(dt),terminal_entropy=encoded(hx),suffix_erasure=encoded(suffix))
for n in range(4):
    for mask in range(1<<(1<<n)):
        g=tuple(1-2*((mask>>z)&1) for z in range(1<<n));c=coeff(g);mu=c[0]
        for orient in ['OR','AND']:
            W=wrap(g,orient);cw=coeff(W)
            eq(sum(a*a for a in cw),F(1))
            for s,a in enumerate(c):
                eq(cw[2*s],(1+mu)/2 if s==0 and orient=='OR' else (mu-1)/2 if s==0 else a/2)
                eq(cw[2*s+1],(1-mu)/2 if s==0 and orient=='OR' else (mu+1)/2 if s==0 else (-a/2 if orient=='OR' else a/2))
            equal_expr(plus((H(W),F(1)),(H(g),F(-1,2)),(R(mu),F(-1))))
            eq(I(W),I(g)/2+inf(W,0))
            eq(inf(W,0),(1-mu)/2 if orient=='OR' else (1+mu)/2)
            bx=plus((Phi((1+mu)**2,(1-mu)**2),F(1,4)),({F(2):(1-mu*mu)/2},F(1)))
            equal_expr(plus((B(W,0),F(1)),(bx,F(-1))))
            leq(bx,1-mu*mu)
            for i in range(n):
                local_cases+=1;a=c[1<<i];d=inf(g,i);corr=D(mu,a)
                equal_expr(plus((B(W,i+1),F(1)),(B(g,i),F(-1,2)),(corr,F(-1))))
                eq(inf(W,i+1),d/2);eq(abs(a)<=d,True)
                leq(corr,abs(a));leq(plus((corr,F(-1))),abs(mu*a))
            rr=[]
            for policy in ['max','min']:
                for stop in [False,True]:
                    rr.append(tree(g,orient,policy,stop));tree_cases+=1
            records.append(dict(n=n,mask=mask,orientation=orient,trees=rr))
equal_expr(plus((D(F(0),F(1)),F(1)),({F(2):F(1)},F(-1))))
(ROOT/'out'/'EXACT_TREE_LEDGERS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
result=dict(helper_version='shifted-row-v1',cores=278,wrappers=556,local_cases=local_cases,
            tree_cases=tree_cases,exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,
            arithmetic='integer FWHT; Fraction log-product equalities; outward rational atanh intervals',
            log_terms=TERMS,dyadic_bits=70,status='PASS',memory_estimate_MB=100)
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
