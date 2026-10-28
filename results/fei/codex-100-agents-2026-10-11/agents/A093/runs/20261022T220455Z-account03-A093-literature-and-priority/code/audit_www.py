"""Frozen small exact controls for the WWW14 source audit. No numerical signs."""
from pathlib import Path
from fractions import Fraction as Q
from math import prod
import json, time

ROOT = Path(__file__).resolve().parents[1]
assert (ROOT/'out/FROZEN_SPEC.json').exists()
start = time.perf_counter()
checks = 0
def check(b):
    global checks
    checks += 1
    if time.perf_counter()-start>60: raise TimeoutError('frozen 60-second limit')
    assert b, checks

def walsh(values):
    z=list(values); step=1
    while step<len(z):
        for j in range(0,len(z),2*step):
            for t in range(j,j+step):
                u,v=z[t],z[t+step]; z[t],z[t+step]=u+v,u-v
        step*=2
    return [Q(v,len(z)) for v in z]

def influence(fn,n):
    return sum((Q(sum(fn(x)!=fn(x^(1<<i)) for x in range(1<<n)),1<<n) for i in range(n)),Q(0))

def trees(k):
    t=-1
    for b in reversed(range(k)):
        tail=t
        t=(3*b,(3*b+1,(3*b+2,1,tail),tail),tail)
    return t

def assignments(n,fixed):
    free=[i for i in range(n) if i not in fixed]
    base=sum(v<<i for i,v in fixed.items())
    for mask in range(1<<len(free)):
        yield base+sum(((mask>>j)&1)<<i for j,i in enumerate(free))

def refine(t,n,y,fixed=None):
    fixed={} if fixed is None else fixed
    if isinstance(t,int):
        if t==-1 or any(((y>>i)&1)!=v for i,v in fixed.items()): return t
        tail=-1
        for i in reversed([i for i in range(n) if i not in fixed]):
            tail=(i,tail,1) if (y>>i)&1 else (i,1,tail)
        return tail
    i,p,m=t
    return (i,refine(p,n,y,{**fixed,i:1}),refine(m,n,y,{**fixed,i:0}))

def covariance(t,fn,n,fixed=None):
    fixed={} if fixed is None else fixed
    if isinstance(t,int):
        check(all(fn(x)==t for x in assignments(n,fixed)))
        return Q(0)
    i,p,m=t
    check(i not in fixed)
    xs=list(assignments(n,{**fixed,i:0})); count=len(xs)
    plus=[fn(x|(1<<i)) for x in xs]; minus=[fn(x) for x in xs]
    cov=Q(sum(u*v for u,v in zip(plus,minus)),count)-Q(sum(plus)*sum(minus),count**2)
    mean=Q(sum(plus)+sum(minus),2*count)
    d=Q(sum(u!=v for u,v in zip(plus,minus)),count)
    mean_gap=Q(sum(plus)-sum(minus),2*count)**2
    check(1-mean**2==2*d+cov-mean_gap)
    return cov+(covariance(p,fn,n,{**fixed,i:1})+covariance(m,fn,n,{**fixed,i:0}))/2

def varsum(t,fn,n,fixed=None):
    fixed={} if fixed is None else fixed
    if isinstance(t,int): return Q(0)
    xs=list(assignments(n,fixed)); mean=Q(sum(fn(x) for x in xs),len(xs))
    i,p,m=t
    return 1-mean**2+(varsum(p,fn,n,{**fixed,i:1})+varsum(m,fn,n,{**fixed,i:0}))/2

a=Q(7,8); rows=[]
C=Q(0)
for k in range(1,13):
    r=a**k; eps=Q(1,8**k); prev=a**(k-1)
    C=4*prev*(1-prev)+a*C
    If=Q(3*k,4)*prev; IF=If+eps*(3*k-5)
    closed=4*prev*(k-8*(1-r))
    check(C==closed); check(C<=Q(16,3)*If)
    root=4*r*(1-r-eps)
    upper=C+12*k*eps+root
    if k>=2:
        check(IF>=If); check(3*k<=8*7**(k-1))
        check(upper<=Q(16,3)*IF)
    rows.append({'k':k,'I_f':str(If),'I_F':str(IF),'Cov_f':str(C),'Cov_F_upper':str(upper)})
    if k<=3:
        n=3*k; y=7<<(3*(k-1)); t=trees(k)
        f=lambda x: 1 if any((x>>(3*b))&7==7 for b in range(k)) else -1
        g=lambda x: -1 if x==y else f(x)
        F=lambda x: f(x&((1<<n)-1)) if (x>>n)&1 else g(x)
        tg=refine(t,n,y)
        cf=covariance(t,f,n); cg=covariance(tg,g,n)
        cF=covariance((n,t,tg),F,n+1)
        check(cf==C); check(abs(cg-cf)<=24*k*eps)
        check(cF==root+(cf+cg)/2)
        meanF=Q(sum(F(x) for x in range(1<<(n+1))),1<<(n+1))
        check(varsum((n,t,tg),F,n+1)==2*IF+cF-(1-meanF**2))
        check(influence(f,n)==If); check(influence(F,n+1)==IF)
        wf=walsh([F(x) for x in range(1<<(n+1))])
        check(sum(v*v for v in wf)==1)
        check(sum(s.bit_count()*v*v for s,v in enumerate(wf))==IF)
        rows[-1].update({'Cov_g_direct':str(cg),'Cov_F_direct':str(cF)})

for n in range(1,13):
    d=2*(1-Q(1,2**n)); I=Q(n,2**(n-1))
    check(d/I==Q(2**n-1,n))
    if n<=8:
        fand=lambda x: 1 if x==(1<<n)-1 else -1
        parity=lambda x: (-1)**x.bit_count()
        check(influence(fand,n)==I); check(influence(parity,n)==n)
        wa=walsh([fand(x) for x in range(1<<n)])
        wp=walsh([parity(x) for x in range(1<<n)])
        check(sum(v*v for v in wa)==1)
        check(sum(v*v for v in wp)==1)
        check(wp[-1]**2==1)
        chain=1
        for i in reversed(range(n)): chain=(i,chain,-1)
        check(covariance(chain,fand,n)==0)
        # Every parity sibling is the negative of the other until constants.
        cp=-(n-1)
        def pt(i,sign):
            if i==n: return sign
            return (i,pt(i+1,-sign),pt(i+1,sign))
        check(covariance(pt(0,1),parity,n)==cp)
        check(4*n+2*cp==2*n+2)

check(3**11<2**18)
# Nonconstant stopped terminal: AND2 has four equal squared coefficients.
w=walsh([-1,-1,-1,1]); check(all(v*v==Q(1,4) for v in w))
# An irrelevant prefix of length m adds exactly m*Var(AND2)=3m/4.
for m in range(13):
    check(Q(3*m,4)+Q(3,4)==Q(3*(m+1),4))
    if m<=3:
        t=(0,(1,1,-1),-1)
        for i in range(2,m+2): t=(i,t,t)
        core=lambda x: 1 if (x&3)==3 else -1
        check(covariance(t,core,m+2)==Q(3*m,4))

out={'status':'PASS','exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,
     'arithmetic':'integers and Fraction; no floating sign', 'rows':rows,
     'full_fei':'OPEN','formal_status':'analytic source-audit derivation; Lean not yet checked'}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
