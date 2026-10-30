"""Exact controls-first extension on actual full-support prime sources."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,math
import check as C
R=Path(__file__).resolve().parents[1]
def add(*x):return C.plus(*x)
def phi(x):return add((-x,C.log(x))) if x else {}
def AA(x):return add((-2*(1-x)**2,C.log(1-x))) if x<1 else {}
def activated(m,t):
    d=F(1,2**(m-1));N=2**(m-1);mu=(1-d)**N;a=1-mu;delta=F(1,2**t)
    hg=add((N,C.H(m)))
    h=add((1,AA(delta*a)),(delta,hg),(-delta,phi(mu*mu)),(2*t*delta*(1-mu*mu),C.const(1)),(2**t-1,phi(delta*delta*a*a)))
    return h,delta*(m+t*a),a
def direct(m,t):
    N=2**(m-1);ncore=m*N;mask=(1<<m)-1
    def g(x):return -1 if sum(((x>>(m*j))&mask)==0 for j in range(N))%2 else 1
    table=tuple(g(x>>t) if x&((1<<t)-1)==0 else 1 for x in range(2**(ncore+t)))
    w=C.walsh(table);p=tuple(x*x for x in w)
    h=add(*[(-F(mult)*mass,C.log(mass)) for mass,mult in Counter(p).items() if mass])
    ds=[F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(ncore+t)]
    return table,p,h,ds
def run(pilot):
    C.COUNT=0;start=time.perf_counter();count=0
    def ck(b,s):
        nonlocal count
        count+=1
        if not b:raise AssertionError(s)
    pairs=[(2,1),(2,2),(2,3),(3,1)] if pilot else [(2,t) for t in range(1,5)]+[(3,1),(3,2)]
    for m,t in pairs:
        table,p,h,ds=direct(m,t);ha,I,a=activated(m,t);d=F(1,2**(m-1));delta=F(1,2**t)
        ck(h==ha,'independent actual labelled Walsh/analytic activated entropy')
        ck(sum(ds)==I,'independent actual edge total influence')
        ck(all(x>0 for x in p),'FULL spectral support actual source')
        ck(all(x>0 for x in ds),'all physical coordinates relevant')
        ck(ds[:t]==[delta*a]*t and ds[t:]==[delta*d]*(m*2**(m-1)),'all exact coordinate influences')
        for i in range(t):ck(all(table[x]==1 for x in range(len(table)) if x>>i&1),'inactive control forces constant: physical-prime proof condition')
    rows=[]
    if not pilot:
      for m in range(2,5):
       for t in range(1,5):
        h,I,a=activated(m,t);delta=F(1,2**t)
        C.nn(add((1,C.const(7*I)),(-1,h)),'explicit original entropy source rate7')
        for r in range(1,m+1):
            K=add((2**(r-1),C.M(r)));base=C.maximum(add((2**(m-1),C.H(m))),K)
            previous=base
            for l in range(1,t+1):
                hl,Il,al=activated(m,l)
                vv=C.maximum(hl,add((F(1,2**l),base)))
                C.nn(add((1,vv),(F(-1,2),previous)),'every physical activation control drift')
                previous=vv
            target=C.maximum(h,add((delta,K)))
            ck(previous==target,'exact activated root capital max(H,delta*K)')
            if r<=math.isqrt(m):C.nn(add((1,C.const(7*I)),(-1,target)),'S8I with old debit I pays ALL selected cuts')
            C.nn(add((1,target),(-delta,C.const(r*(r-1)))),'matching terminal necessity')
            rows.append({'m':m,'t':t,'r':r,'A':C.show(target),'I':str(I)})
    elapsed=time.perf_counter()-start;ck(elapsed<(55 if pilot else 120),'frozen runtime')
    out={'status':'PASS','pilot':pilot,'direct_sources':len(pairs),'control_data_triples':len(rows),'exact_predicates':count,'interval_predicates':C.COUNT,'seconds':elapsed,'rows':rows}
    (R/'out'/('ACTIVATION_PILOT.json' if pilot else 'ACTIVATION_MAIN.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print({k:v for k,v in out.items() if k!='rows'},flush=True)
if __name__=='__main__':run(True);run(False)
