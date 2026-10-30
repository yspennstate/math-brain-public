from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import comb
import json,time,sys

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def require(b):
    global COUNT
    COUNT+=1
    assert b
def walsh(table):
    a=list(table); n=len(a); k=1
    while k<n:
        for j in range(0,n,2*k):
            for t in range(k):
                u,v=a[j+t],a[j+t+k]; a[j+t],a[j+t+k]=u+v,u-v
        k*=2
    return [F(x,n) for x in a]
@lru_cache(None)
def factors(n):
    result={}; d=2
    while d*d<=n:
        while n%d==0:
            result[d]=result.get(d,0)+1; n//=d
        d+=1
    if n>1: result[n]=result.get(n,0)+1
    return result
def add(a,b,w=F(1)):
    c=dict(a)
    for p,x in b.items():
        c[p]=c.get(p,F(0))+w*x
        if c[p]==0: del c[p]
    return c
def cost(p):
    if not p: return {}
    c={}
    for prime,k in factors(p.numerator).items(): c[prime]=c.get(prime,F(0))-p*k
    for prime,k in factors(p.denominator).items(): c[prime]=c.get(prime,F(0))+p*k
    return {q:v for q,v in c.items() if v}
def entropy(a):
    c={}
    for x in a:c=add(c,cost(x*x))
    return c
def lam(a,n):
    c={}
    for i in range(n):c=add(c,cost(a[1<<i]**2))
    return c
def influence(a):return sum(F(s.bit_count())*x*x for s,x in enumerate(a))
@lru_cache(None)
def ln(q):
    q=F(q); shift=0
    while q<1:q*=2;shift-=1
    while q>2:q/=2;shift+=1
    u=(q-1)/(q+1); total=F(0)
    for j in range(40):total+=2*u**(2*j+1)/F(2*j+1)
    tail=2*u**81/(81*(1-u*u))
    if shift:
        lo,hi=ln(F(2))
        return total+shift*(lo if shift>0 else hi),total+tail+shift*(hi if shift>0 else lo)
    return total,total+tail
def enclose(c):
    lo=hi=F(0)
    for p,w in c.items():
        l,h=ln(F(p));lo+=w*(l if w>=0 else h);hi+=w*(h if w>=0 else l)
    return lo,hi
def gate(r):
    # controls are bits 2..r+1; rare event is all control bits zero.
    return [(1-2*((x>>1)&1)) if x>>2==0 else (1-2*(x&1)) for x in range(1<<(r+2))]
def chain(r,d):
    n=1+d*(r+1);table=[]
    for x in range(1<<n):
        value=1-2*(x&1)
        for j in range(d):
            start=1+j*(r+1);y=(x>>start)&1
            z=(x>>(start+1))&((1<<r)-1)
            if z==0:value=1-2*y
        table.append(value)
    return table,n
def run(pilot):
    start=time.perf_counter();bs=0
    # Certify the slightly weaker Lambda<=7delta, using e>2 and hence K<7.
    for n in ([1,2] if pilot else [1,2,3]):
        size=1<<n
        for mask in range(1<<size):
            if mask.bit_count()!=size//2:continue
            a=walsh([1-2*((mask>>i)&1) for i in range(size)])
            require(a[0]==0);delta=influence(a)-1
            require(enclose(lam(a,n))[1]<=7*delta);bs+=1
    gate_records=[]
    for r in ([1] if pilot else [1,2,3,4,5]):
        a=walsh(gate(r));p=F(1,1<<r);n=r+2
        require(a[0]==0);require(a[1]==1-p);require(a[2]==p)
        require(influence(a)==1+r*p)
        q=add(cost((1-p)**2),cost(p*p),F((2<<r)-1))
        require(entropy(a)==q)
        lo,hi=enclose(q);l2,h2=ln(F(2))
        require(hi<=6*r*p*l2)
        gate_records.append({'r':r,'I':str(influence(a)),'entropy_log_vector':{str(k):str(v) for k,v in q.items()}})
    cr=[]
    for r,d in ([(1,2)] if pilot else [(1,1),(1,2),(1,3),(2,1),(2,2)]):
        tab,n=chain(r,d);a=walsh(tab);p=F(1,1<<r);q0=1-p
        require(a[0]==0);require(influence(a)==1+r*(1-q0**d))
        require(a[1]==q0**d)
        for j in range(d):require(a[1<<(1+j*(r+1))]==p*q0**(d-j-1))
        eg=entropy(walsh(gate(r)));require(entropy(a)==add({},eg,(1-q0**d)/p))
        # Independently expand exact first-charge factorization along the spine.
        rhs={};lg=lam(walsh(gate(r)),r+2)
        for depth in range(d):
            remaining=d-depth-1
            wchild=q0**(2*remaining)+p*p*sum(q0**(2*t) for t in range(remaining))
            fresh=add({},cost(q0*q0),wchild)
            fresh=add(fresh,cost(p*p))
            rhs=add(rhs,fresh,q0**(2*depth))
        require(lam(a,n)==rhs)
        local_bank=add({},lg,(1-q0**d)/p)
        require(enclose(local_bank)[1]<=7*(influence(a)-1))
        require(r*p*(1-q0**d)/p==influence(a)-1)
        cr.append({'r':r,'depth':d,'n':n,'I':str(influence(a))})
    symbolic=[]
    for k in ([] if pilot else range(2,13)):
        d=1<<(2*k);p=F(1,1<<(3*k));r=3*k
        require(1-2*d*p>=F(1,2));require(1+r*d*p<=F(5,2))
        lower=F(1,5)*(1<<k)*(1-F(1,d))
        symbolic.append({'k':k,'depth':d,'r':r,'S_over_I_proved_lower':str(lower)})
    out={'status':'PASS','assertions':COUNT,'balanced_tables':bs,'gates':gate_records,'chains':cr,'symbolic_counterfamily':symbolic,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot}
    name='pilot.json' if pilot else 'validation.json'
    (ROOT/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'status':'PASS','assertions':COUNT,'elapsed_seconds':out['elapsed_seconds'],'output':name}))
if __name__=='__main__':run('--pilot' in sys.argv)
