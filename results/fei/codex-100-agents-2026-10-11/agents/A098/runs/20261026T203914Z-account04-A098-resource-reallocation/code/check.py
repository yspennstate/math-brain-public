from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import lcm
import json, time, sys

RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0; EDGES=0; GHOSTS=0; BIASED=0
PILOT='--pilot' in sys.argv
LIMIT=55 if PILOT else 180
def ck(x):
    global COUNT
    COUNT+=1
    assert x
    if COUNT%256==0: assert time.perf_counter()-START<LIMIT, 'runtime cap'

# Exact logarithms represented by rational exponents of prime integers.
def add(*vs):
    out={}
    for v in vs:
        for p,a in v.items(): out[p]=out.get(p,F(0))+a
    return {p:a for p,a in out.items() if a}
def scale(v,c): return {p:a*c for p,a in v.items() if a*c}
@lru_cache(None)
def log(q):
    q=F(q); assert q>0
    v={}
    for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=n:
            while n%p==0:
                v[p]=v.get(p,F(0))+sgn; n//=p
            p+=1
        if n>1:v[n]=v.get(n,F(0))+sgn
    return {p:a for p,a in v.items() if a}
def ce(p,q): return add(*(scale(log(y),-x) for x,y in zip(p,q) if x))
def ent(p): return ce(p,p)
def kl(p,q): return add(ce(p,q),scale(ent(p),-1))
def nonneg(v):
    den=lcm(*(x.denominator for x in v.values())) if v else 1
    lhs=rhs=1
    for p,x in v.items():
        e=int(x*den)
        if e>0:lhs*=p**e
        else:rhs*=p**(-e)
    return lhs>=rhs

@lru_cache(None)
def spectrum(tab):
    size=len(tab)
    return tuple(
        F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(tab)),size)**2 for s in range(size))
def delete(x,i):return (x&((1<<i)-1))|((x>>(i+1))<<i)
def marginal(p,i):
    v=[F(0)]*(len(p)//2)
    for x,a in enumerate(p):v[delete(x,i)]+=a
    return tuple(v)
def child(tab,i,t):return tuple(y for x,y in enumerate(tab) if (x>>i)&1==t)
def reference(p,kind):
    if kind==0:b=F(1,2); atoms=[(F(1,2),len(p)-1)]
    elif kind==1:b=F(1,2); atoms=[(F(1,4),0),(F(1,4),len(p)-1)]
    else:b=F(1,3); atoms=[(F(1,3),min(1,len(p)-1)),(F(1,3),len(p)-1)]
    q=[b*x for x in p]
    for c,w in atoms:q[w]+=c
    return tuple(q),b,atoms

def edge(tab,q,b,atoms,i,split):
    global EDGES,GHOSTS,BIASED
    EDGES+=1
    p=spectrum(tab);r=marginal(p,i);v=marginal(q,i)
    tabs=[child(tab,i,t) for t in [0,1]]; ps=[spectrum(t) for t in tabs]
    ck(all((ps[0][u]+ps[1][u])/2==r[u] for u in range(len(r))))
    kernels=[[],[]]
    for u,m in enumerate(r):
        if m:k0=ps[0][u]/(2*m)
        else:GHOSTS+=1;k0=F(1,2) if split==0 else F(1)
        kernels[0].append(k0);kernels[1].append(1-k0)
    rr=[sum(v[u]*kernels[t][u] for u in range(len(r))) for t in [0,1]]
    ck(sum(rr)==1 and min(rr)>=b/2)
    BIASED+=rr[0]!=F(1,2)
    qs=[];bs=[];ass=[]
    for t in [0,1]:
        qt=tuple(v[u]*kernels[t][u]/rr[t] for u in range(len(r)))
        bt=b/(2*rr[t]); ats=[(c*kernels[t][delete(w,i)]/rr[t],delete(w,i)) for c,w in atoms]
        rebuilt=[bt*x for x in ps[t]]
        for c,w in ats:rebuilt[w]+=c
        ck(tuple(rebuilt)==qt);ck(sum(qt)==1);ck(bt+sum(c for c,w in ats)==1)
        ck(all(qt[u]>0 for u,x in enumerate(ps[t]) if x))
        qs.append(qt);bs.append(bt);ass.append(ats)
    de=add(kl(p,q),scale(kl(r,v),-1))
    # Separate conditional-frequency reconstruction of erased KL.
    cond={}
    for u,m in enumerate(r):
        if not m:continue
        ids=[x for x in range(len(p)) if delete(x,i)==u]
        pp=tuple(p[x]/m for x in ids);qq=tuple(q[x]/v[u] for x in ids)
        cond=add(cond,scale(kl(pp,qq),m))
    ck(de==cond)
    outcome=kl((F(1,2),F(1,2)),rr)
    avgkl=scale(add(*(kl(ps[t],qs[t]) for t in [0,1])),F(1,2))
    ck(kl(p,q)==add(de,outcome,avgkl))
    erasure=add(ent(p),scale(ent(r),-1))
    js=add(ent(r),scale(add(ent(ps[0]),ent(ps[1])),F(-1,2)))
    avgce=scale(add(ce(ps[0],qs[0]),ce(ps[1],qs[1])),F(1,2))
    ck(not add(erasure,avgce,scale(ce(p,q),-1),js,de,outcome))
    envelope=add(log(1/b),scale(add(*(log(1/x) for x in bs)),F(-1,2)))
    ck(envelope==outcome)
    return tabs,qs,bs,ass,erasure,add(js,de,outcome)

def tree(tab,q,b,atoms,split):
    n=(len(tab)-1).bit_length()
    if n==0:return {},ce(spectrum(tab),q),{},log(1/b)
    i=n-1 if tab[0]>0 else 0
    tabs,qs,bs,ass,er,release=edge(tab,q,b,atoms,i,split)
    branches=[tree(tabs[t],qs[t],bs[t],ass[t],split) for t in [0,1]]
    bills=add(er,scale(add(*(z[0] for z in branches)),F(1,2)))
    terminal=scale(add(*(z[1] for z in branches)),F(1,2))
    released=add(release,scale(add(*(z[2] for z in branches)),F(1,2)))
    ck(ce(spectrum(tab),q)==add(bills,terminal,released))
    return bills,terminal,released,scale(add(*(z[3] for z in branches)),F(1,2))

def floors():
    cases=0; comps=0; derivative_errata=0
    t=F(3,4)
    for aa in range(1,9):
      a=F(aa,12)
      for bb in range(1,9):
       b=F(bb,12)
       for ee in [3,6,8]:
        ell=F(ee,12)
        if b>=ell:continue
        p=(1-t,a,(t-a)/3,2*(t-a)/3,F(0))
        q=(1-t,b,(t-b)/4,(t-b)/2,(t-b)/4)
        def target(z):return (1-t,z,(t-z)/4,(t-z)/2,(t-z)/4)
        z=max(a,ell);delta=add(ce(p,target(z)),scale(ce(p,q),-1))
        formula=add(scale(log(b/z),a),scale(log((t-b)/(t-z)),t-a))
        ck(delta==formula)
        for zz in range(ee,9):
            zc=F(zz,12);comps+=1
            ck(nonneg(add(ce(p,target(zc)),scale(ce(p,target(z)),-1))))
            deriv=-a/zc+(t-a)/(t-zc)
            ck(deriv==t*(zc-a)/(zc*(t-zc)))
            derivative_errata+=deriv!=(zc-a)/(zc*(t-zc))
        cases+=1
    # Both actual Boolean children in A097's signed contrast.
    tab=tuple(-1 if x in [0,7] else 1 for x in range(8))
    for side in [0,1]:ck(spectrum(child(tab,0,side))==(F(1,4),)*4)
    p=(F(1,4),)*4; qt=(F(1,4),F(5,24),F(5,24),F(1,3))
    for q,argument in [(p,F(27,25)),((F(1,4),F(5,16),F(5,16),F(1,8)),F(27,32))]:
        d=add(ce(p,qt),scale(ce(p,q),-1));ck(d==scale(log(argument),F(1,4)))
        ck(nonneg(d)==(argument>=1))
    # Unequal-depth physical frontier: BOTH siblings and a reached grandchild pair.
    reaches=(F(1,2),F(1,4),F(1,4)); betas=(F(3,8),F(1,2),F(0))
    currents=(p,(F(1,4),F(5,16),F(5,16),F(1,8)),p)
    full_current={}; full_next={}; signed={}
    for reach,beta,q in zip(reaches,betas,currents):
        cp=((1-beta)/3,2*(1-beta)/3)+tuple(beta*x for x in p)
        cq=((1-beta)/3,2*(1-beta)/3)+tuple(beta*x for x in q)
        nq=((1-beta)/3,2*(1-beta)/3)+tuple(beta*x for x in qt)
        delta=add(ce(p,qt),scale(ce(p,q),-1))
        ck(add(ce(cp,nq),scale(ce(cp,cq),-1))==scale(delta,beta))
        full_current=add(full_current,scale(ce(cp,cq),reach))
        full_next=add(full_next,scale(ce(cp,nq),reach))
        signed=add(signed,scale(delta,reach*beta))
    ck(full_next==add(full_current,signed))
    for margin in [F(0),F(1,128),F(1,8)]:
        old=F(1,4)
        original=add(full_current,scale(log(2),old+margin))
        final=add(full_next,scale(log(2),old))
        residual=add(original,scale(final,-1))
        ck(residual==add(scale(log(2),margin),scale(signed,-1)))
        ck(nonneg(residual)==nonneg(add(scale(log(2),margin),scale(signed,-1))))
    return dict(cases=cases,grid_comparisons=comps,missing_t_derivative_mismatches=derivative_errata,
                full_terminal_frontiers=1,full_terminal_leaves=3,old_booking_and_margin_tests=3)

maxn=2 if PILOT else 3
fixtures=0; trees=0
for n in range(1,maxn+1):
 for mask in range(1<<(1<<n)):
    tab=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));p=spectrum(tab)
    ck(sum(p)==1)
    for i in range(n):
     for kind in range(3):
      q,b,atoms=reference(p,kind)
      for split in [0,1]:edge(tab,q,b,atoms,i,split);fixtures+=1
    if n==maxn:
     for split in [0,1]:
      q,b,atoms=reference(p,2);tree(tab,q,b,atoms,split);trees+=1
fr=floors()
out=dict(status='PASS',helper_version='A098-stage21-v1',pilot=PILOT,exact_assertions=COUNT,
         direct_query_fixtures=fixtures,adaptive_trees=trees,visited_query_nodes=EDGES,
         source_zero_erased_rows=GHOSTS,biased_reference_outcomes=BIASED,floor=fr,
         seconds=time.perf_counter()-START,arithmetic='Fraction and exact prime-exponent identities; integer sign comparisons')
(RUN/'out'/('PILOT.json' if PILOT else 'VALIDATION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
