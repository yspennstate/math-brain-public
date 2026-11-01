import sys,json,time
from pathlib import Path
from functools import lru_cache
import exact as x
Q=x.Q; ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); pilot='--pilot' in sys.argv
counts={}; cases=0; prices={str(c):{'admitted':0,'rejected_or_unresolved':0,'negative_actual_child_slack':0} for c in [2,3,4,5,9,10]}
def check(ok,label):
    assert ok,label
    counts[label]=counts.get(label,0)+1
    if time.monotonic()-START>(60 if pilot else 180): raise RuntimeError('frozen runtime cap')
@lru_cache(None)
def point(r): return tuple(-1 if t==0 else 1 for t in range(1<<r))
def constant(c): return {2:c} if c else {}
for m in ([2] if pilot else [2,3]):
    for mask in range(1<<(1<<m)):
        u=tuple(1 if (mask>>t)&1 else -1 for t in range(1<<m))
        for r in [1,2,3]:
            p=Q(1,1<<r); F=x.activate(u,point(r)); delta=x.neg(u)
            for i in range(m):
                g=x.restrict(u,((i,0),)); h=x.restrict(u,((i,1),))
                fg=x.restrict(F,((i,0),)); fh=x.restrict(F,((i,1),)); product=tuple(a*b for a,b in zip(g,h)); fp=tuple(a*b for a,b in zip(fg,fh))
                eps=Q(sum(a!=b for a,b in zip(g,h)),len(g)); q=p*eps
                Bdata=p*x.I(product)/2; Bfuture=r*p*eps
                Tdata=p*(x.I(g)+x.I(h))/2; Tctrl=2*r*p*delta
                rho=eps/(2*delta) if delta else Q(0)
                check(fg==x.activate(g,point(r)) and fh==x.activate(h,point(r)),'actual shared-controller children')
                check(fp==x.activate(product,point(r)),'actual product retains same point controls')
                check(x.I(fp)==p*x.I(product)+2*r*p*eps,'product influence data/future-control decomposition')
                check(x.inf(F,i)==q,'actual core query influence')
                check(Bdata<=Tdata and 0<=rho<=1 and Bfuture==rho*Tctrl,'one-use sharp owner capacities')
                check(x.I(F)==q+Tdata+Tctrl,'complete physical query and terminal influence partition')
                leafH=x.add((Q(1,2),x.H(fg)),(Q(1,2),x.H(fh)))
                drop=x.add((1,x.H(F)),(-1,leafH))
                check(x.bounds(drop)[1]<=Bdata+Bfuture+Q(9,2)*q,'full entropy local sufficient price 9/2')
                for C in [2,3,4,5,9,10]:
                    sg=x.add((1,constant(C*x.I(fg))),(-1,x.H(fg)))
                    sh=x.add((1,constant(C*x.I(fh))),(-1,x.H(fh)))
                    surplus=x.add((Q(1,2),sg),(Q(1,2),sh))
                    root=x.add((1,constant(C*x.I(F))),(-1,x.H(F)))
                    check(root==x.add((1,surplus),(1,constant(C*q)),(-1,drop)),'exact signed child slack identity')
                    requirement=Bdata+Bfuture+(Q(9,2)-C)*q
                    s_lo,s_hi=x.bounds(surplus); root_lo,root_hi=x.bounds(root)
                    if s_lo>=requirement:
                        check(root_lo>=0,'certified sufficient admission has no false positive'); prices[str(C)]['admitted']+=1
                    else: prices[str(C)]['rejected_or_unresolved']+=1
                    if x.bounds(sg)[1]<0 or x.bounds(sh)[1]<0: prices[str(C)]['negative_actual_child_slack']+=1
                # A whole terminal rate gap one suffices, from the owner capacities.
                check(Bdata+Bfuture<=Tdata+Tctrl,'single terminal rate unit covers both distinct owners')
                cases+=1
assert cases==(96 if pilot else 2400)
out={'status':'PASS','pilot':pilot,'cases':cases,'assertions':sum(counts.values()),'counts':counts,'prices':prices,'elapsed_seconds':time.monotonic()-START,'max_dimension':5 if pilot else 6,'arithmetic':'exact Fraction prime-log equality and rational log enclosures','memory_peak':'unmeasured; estimated160MB'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
