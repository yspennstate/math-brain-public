from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json, time, hashlib

def factors(k):
    out = {}; p = 2
    while p*p <= k:
        while k % p == 0:
            out[p] = out.get(p,0)+1; k //= p
        p += 1
    if k > 1: out[k] = out.get(k,0)+1
    return out

def add(*terms):
    r = defaultdict(F)
    for scale, expr in terms:
        for p,v in expr.items(): r[p] += scale*v
    return {p:v for p,v in r.items() if v}

def logq(q):
    r = defaultdict(F)
    for p,v in factors(q.numerator).items(): r[p] += v
    for p,v in factors(q.denominator).items(): r[p] -= v
    return {p:v for p,v in r.items() if v}

def entropy(ps):
    return add(*[(-q,logq(q)) for q in ps if q])

def walsh(t):
    m=len(t)
    return [F(sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(m)),m) for s in range(m)]

def metrics(t):
    a=walsh(t); p=[v*v for v in a]
    return a,entropy(p),sum((F(s.bit_count())*p[s] for s in range(len(p))),F())

def insert(x,i,b): return (x & ((1<<i)-1)) | ((x>>i)<<(i+1)) | (b<<i)
def child(t,i,b): return tuple(t[insert(x,i,b)] for x in range(len(t)//2))

checks=0; nodes=0; trees=0; density_nodes=0
def eq(a,b):
    global checks
    assert a==b,(a,b); checks+=1

def split(t,i):
    global nodes,density_nodes
    a,H,I=metrics(t); g=child(t,i,0); h=child(t,i,1)
    ag,Hg,Ig=metrics(g); ah,Hh,Ih=metrics(h)
    q=[]; e=[]; B={}; J={}; lam={}
    for w in range(len(g)):
        u=a[insert(w,i,0)]; v=a[insert(w,i,1)]
        eq(ag[w],u+v); eq(ah[w],u-v)
        z=u*u+v*v; mismatch=v*v; q.append(z); e.append(mismatch)
        if z:
            B=add((1,B),(z,entropy([mismatch/z,1-mismatch/z])))
            J=add((1,J),(z,{2:F(1)}),(-z,entropy([ag[w]**2/(2*z),ah[w]**2/(2*z)])))
            if mismatch: lam=add((1,lam),(mismatch,logq(z/mismatch)))
    d=sum(e,F()); D=add((1,H),(-F(1,2),Hg),(-F(1,2),Hh))
    eq(sum(q,F()),F(1)); eq(D,add((1,B),(1,J)))
    eq(I,d+(Ig+Ih)/2)
    eq(d,F(sum(x!=y for x,y in zip(g,h)),len(g)))
    if all(not ev or ev/qv>=F(1,8) for qv,ev in zip(q,e)):
        density_nodes+=1
    nodes+=1
    return d,D,g,h

def tree(t,early):
    # Leaves are constants, or arbitrary <=2-coordinate functions when early=True.
    a,H,I=metrics(t); n=(len(t)).bit_length()-1
    if not n or len(set(t))==1 or (early and n<=2):
        return {},F(),H,I
    ds=[sum((a[s]**2 for s in range(len(a)) if s&(1<<i)),F()) for i in range(n)]
    i=min((i for i in range(n) if ds[i]),key=lambda i:(ds[i],i))
    d,D,g,h=split(t,i)
    cg,pg,hg,ig=tree(g,early); ch,ph,hh,ih=tree(h,early)
    charge=add((1,D),(F(1,2),cg),(F(1,2),ch))
    paid=d+(pg+ph)/2; terminalH=add((F(1,2),hg),(F(1,2),hh)); terminalI=(ig+ih)/2
    eq(H,add((1,charge),(1,terminalH))); eq(I,paid+terminalI)
    return charge,paid,terminalH,terminalI

start=time.perf_counter(); functions=0
for n in range(4):
    for mask in range(1<<(1<<n)):
        t=tuple(1 if mask&(1<<x) else -1 for x in range(1<<n)); functions+=1
        for i in range(n): split(t,i)
        for early in (False,True): tree(t,early); trees+=1
out={"status":"PASS","functions":functions,"coordinate_splits_including_tree_rechecks":nodes,"adaptive_trees":trees,"exact_assertions":checks,"density_qualified_splits_including_rechecks":density_nodes,"elapsed_seconds":time.perf_counter()-start,"arithmetic":"Fraction plus exact prime-log coefficient dictionaries; no floating logarithms","scope":"finite identity certificates only; drift inequality supplied by analytic proof"}
dest=Path(__file__).resolve().parent.parent/'out'; dest.mkdir(exist_ok=True)
(dest/'CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
