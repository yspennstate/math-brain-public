"""Independent two-reset referee; symbolic bookkeeping retains every old terminal."""
from pathlib import Path
from fractions import Fraction as F
from time import perf_counter
import importlib.util,hashlib,json,sys
R=Path(__file__).resolve().parents[1]; O=R/'out'; O.mkdir(exist_ok=True)
LIB=R.parent/'20261021T203248Z-account03-A086-joint-code-referee'/'code/check.py'
assert hashlib.sha256(LIB.read_bytes()).hexdigest()=='48cd9de1ec443e89be969dd3eac40569c413ddbfafaa9df70e9db1ef238907bc'
spec=importlib.util.spec_from_file_location('own_prior_referee',LIB); lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
START=perf_counter(); N=0
def ck(value,label):
    global N
    N+=1
    if not value: raise AssertionError(label)
    if perf_counter()-START>55: raise TimeoutError('frozen55-second limit')
def add(*terms):
    result={}
    for scalar,expr in terms:
        for q,c in expr.items(): result[q]=result.get(q,F(0))+scalar*c
    return {q:c for q,c in result.items() if c}
def ce(P,Q):
    ck(len(P)==len(Q) and sum(P)==sum(Q)==1,'normalized complete laws')
    expr={}
    for p,q in zip(P,Q):
        ck(not p or q>0,'never log zero with positive true mass')
        if p: expr[q]=expr.get(q,F(0))-p
    return {q:c for q,c in expr.items() if c and q!=1}
def interval(expr):
    lo=hi=F(0)
    for q,c in expr.items():
        a,b=lib.log2(q)
        lo+=c*(a if c>0 else b); hi+=c*(b if c>0 else a)
    return lo,hi
def law(table): return tuple(a*a for a in lib.spectrum(table))
def canonical(source,actual):
    a=lib.spectrum(source); support=[i for i,v in enumerate(a) if v]
    epsilon=F(2,len(source)); W=2*epsilon-len(support)*epsilon*epsilon
    ck(0<W<=1,'canonical new-sector mass')
    Q=tuple((1-W)*v*v if v else epsilon*epsilon for v in a)
    P=law(actual)
    ck(sum(Q)==1,'canonical true-support completion')
    for s,v in enumerate(lib.spectrum(actual)):
        ck(v==a[s]-epsilon if a[s] else abs(v)==epsilon,'actual residual, not surrogate spectrum')
    ck(all(not p or q>0 for p,q in zip(P,Q)),'fresh support covers actual residual')
    return Q,ce(P,Q)
def query(tab,Q,j):
    P=law(tab); parent=ce(P,Q)
    tabs=[lib.child(tab,j,b) for b in (0,1)]; Ps=[law(t) for t in tabs]
    p=tuple((x+y)/2 for x,y in zip(*Ps))
    r=tuple(Q[lib.bitmask_insert(t,j,0)]+Q[lib.bitmask_insert(t,j,1)] for t in range(len(p)))
    pis=[tuple(Ps[b][t]/(2*p[t]) if p[t] else F(1,2) for t in range(len(p))) for b in (0,1)]
    raws=[tuple(2*r[t]*pis[b][t] for t in range(len(p))) for b in (0,1)]; Z=[sum(row) for row in raws]
    ck(Z[0]>0 and Z[1]>0 and sum(Z)==2,'BOTH physical normalizers retained')
    Qs=[tuple(v/Z[b] for v in raws[b]) for b in (0,1)]
    costs=[ce(Ps[b],Qs[b]) for b in (0,1)]
    release=add((1,parent),(-F(1,2),costs[0]),(-F(1,2),costs[1]))
    exactzero=Ps[0]==Ps[1] and Z==[1,1] and all(not p[t] or all(P[lib.bitmask_insert(t,j,b)]*r[t]==Q[lib.bitmask_insert(t,j,b)]*p[t] for b in (0,1)) for t in range(len(p)))
    ck(exactzero or interval(release)[0]>=0,'nonnegative FULL complete query release')
    Ip=lib.influence(tab); Is=[lib.influence(t) for t in tabs]
    Inf=F(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab))
    ck(Ip==Inf+(Is[0]+Is[1])/2,'literal physical influence telescope')
    # Preserve an arbitrary terminal reference even where its true probability is zero.
    Rh=(F(1,3),F(2,3))
    for b in (0,1):
        rawprod=tuple(2*r[t]*pis[b][t]*rh for t in range(len(p)) for rh in Rh)
        ck(sum(rawprod)==Z[b],'product-compatible terminal zero fibers preserve Z')
        ck(tuple(v/Z[b] for v in rawprod)==tuple(q*rh for q in Qs[b] for rh in Rh),'full independent terminal reference retained')
    return tabs,Qs,costs,release,Inf,{'nonunit_Z':sum(z!=1 for z in Z),'zero_true_fibers':sum(v==0 for v in p)}
def fixture(w,m):
    n=w+2+m; D=n+1
    def g(x): return (-1 if x%(2**w)==0 else 1)*(-1 if (x>>w)%4==0 else 1)
    source=tuple(g(x) for x in range(2**D))
    table=tuple(g(x)-2*int(x==2**n) for x in range(2**D))
    rootQ,rootcost=canonical(source,table); rootI=lib.influence(table)
    ck(rootI==1+w*F(2,2**w)+F(1,2**n)*(m-w-1),'actual original influence')
    S0=4*rootI-interval(rootcost)[1]
    ck(S0>F(451,256),'sharper original quota, not terminal quota')
    rows=[]
    for d in range(w+1):
        for eta in (F(0),F(1,8),F(1,4)):
            tab=table; src=source; Q=rootQ; labels=list(range(D)); reach=F(1)
            G={}; T={}; otherI=F(0); Pi=F(0); nonunit=zeros=0
            for _ in range(d):
                j=next(i for i,a in enumerate(labels) if a<w)
                tabs,Qs,Cs,release,Inf,stats=query(tab,Q,j)
                G=add((1,G),(reach,release)); T=add((1,T),(reach/2,Cs[1]))
                otherI+=reach*lib.influence(tabs[1])/2; Pi+=reach*Inf
                nonunit+=stats['nonunit_Z'];zeros+=stats['zero_true_fibers']
                tab=tabs[0];src=lib.child(src,j,0);Q=Qs[0];labels.pop(j);reach/=2
            ck(add((1,G),(1,T),(reach,ce(law(tab),Q)))==rootcost,'all old releases and complete off-path terminals')
            charges=[]; costs=[]; zero_boundary=False
            for physical in (w,w+1):
                j=labels.index(physical)
                tabs,Qs,Cs,release,Inf,stats=query(tab,Q,j)
                G=add((1,G),(reach,release)); T=add((1,T),(reach/2,Cs[1]))
                otherI+=reach*lib.influence(tabs[1])/2;Pi+=reach*Inf
                nonunit+=stats['nonunit_Z'];zeros+=stats['zero_true_fibers']
                src=lib.child(src,j,0);tab=tabs[0];labels.pop(j);reach/=2
                canQ,canCost=canonical(src,tab)
                if physical==w:
                    U=F(1,len(canQ));Q=tuple((1-eta)*q+eta*U for q in canQ)
                    fresh=ce(law(tab),Q)
                    ck(interval(add((1,fresh),(-1,canCost)))[1]<F(1,2),'all-eta mixture surcharge at sampled eta')
                    ck(reach*interval(fresh)[1]<F(5,4),'first reached FULL fresh cost')
                else:
                    Q=canQ;fresh=canCost
                    ck(reach*interval(fresh)[1]<F(1,2),'second reached FULL fresh cost')
                    zero_boundary=any(q==0 for q in Q)
                    if w-d==0 and m==0:
                        ck(zero_boundary and interval(fresh)==(0,0),'t0m0 dictator ZERO old atom has ZERO true mass')
                charge=add((reach,fresh),(-reach,Cs[0]))
                charges.append(charge);costs.append(reach*interval(fresh)[1])
                # At second iteration Cs[0] comes from CURRENT Q1, never old root Q.
                ck(add((1,G),(1,T),(reach,fresh))==add((1,rootcost),*((1,e) for e in charges)),'exact cumulative signed reset substitution')
            T=add((1,T),(reach,ce(law(tab),Q)))
            ledger=add((1,G),(1,T)); target=add((1,rootcost),*((1,e) for e in charges))
            ck(ledger==target,'complete two-reset final expectation, symbolic exact equality')
            ck(rootI==Pi+otherI+reach*lib.influence(tab),'all physical queries and terminal influence accounted')
            es=[interval(e) for e in charges]; booked=[max(F(0),b) for a,b in es]
            remaining=S0-sum(booked)
            ck(remaining>F(3,256),'SAME diminished original bank, BOTH positive bookings retained')
            ck(interval(ledger)[1]<4*rootI-F(3,256),'complete ledger below ORIGINAL rate4')
            rows.append({'w':w,'m':m,'d':d,'t':w-d,'eta':str(eta),'e1':[str(x) for x in es[0]],'e2':[str(x) for x in es[1]],'remaining_lower':str(remaining),'second_zero_reference_boundary':zero_boundary,'nonunit_Z':nonunit,'true_zero_fibers':zeros})
    return rows
rows=[];error=None
try:
    domain=[(4,0)] if 'pilot' in sys.argv else [(4,0),(4,1),(5,0)]
    for w,m in domain: rows+=fixture(w,m)
    for m in range(65):ck(16*m+17<=17*2**m,'padding induction diagnostic')
except Exception as exc: error=repr(exc)
result={'status':'FAIL_OR_INCOMPLETE' if error else 'PASS','error':error,'assertions':N,'runtime_seconds':perf_counter()-START,'histories':len(rows),'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'own_prior_helper_sha256':hashlib.sha256(LIB.read_bytes()).hexdigest()}
path=O/('PILOT.json' if 'pilot' in sys.argv else 'EXACT_RESULTS.json');path.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if error:raise SystemExit(1)
