import sys,time,json,itertools
from pathlib import Path
from functools import lru_cache
import exact as x
Q=x.Q; ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); pilot='--pilot' in sys.argv
counts={}; cases=0; CAP=60 if pilot else 600; evaluated={}
def check(ok,label):
    assert ok,label
    counts[label]=counts.get(label,0)+1
    if time.monotonic()-START>CAP:
        (ROOT/'out'/'timeout_checkpoint.json').write_text(json.dumps({'completed_cases':cases,'counts':counts,'elapsed_seconds':time.monotonic()-START,'cap':CAP},indent=2)+'\n',encoding='utf-8')
        raise RuntimeError('frozen amended runtime cap')
@lru_cache(None)
def point(r): return tuple(-1 if t==0 else 1 for t in range(1<<r))
@lru_cache(None)
def G(r,d): return x.add((d,x.Hplus(point(r))),(1,x.R(Q(1,1<<r),d)))
def orders(m,r):
    core=list(range(m)); ctrl=list(range(m,m+r))
    a=[j for pair in itertools.zip_longest(core,ctrl) for j in pair if j is not None]
    b=[j for pair in itertools.zip_longest(ctrl,core) for j in pair if j is not None]
    return [ctrl+core,core+ctrl,a,b,[0]+ctrl+core[1:],[m]+core+ctrl[1:]]
def evaluate(u,r,nextquery,label):
    global cases
    m=len(u).bit_length()-1; n=m+r; p=Q(1,1<<r); F=x.activate(u,point(r))
    def shape(fixed):
        active=all(b==0 for i,b in fixed.items() if i>=m)
        query=nextquery(fixed); rem=sum(i not in fixed for i in range(m))
        if not active or query is None or (query<m and rem==1): return None
        return (query,shape(fixed|{query:0}),shape(fixed|{query:1}))
    key=(u,r,shape({}))
    if key in evaluated:
        check(evaluated[key],'duplicate actual physical tree certificate reused by identical shape')
        counts[label]=counts.get(label,0)+1; cases+=1
        return
    root_d=x.neg(u); projectedH={}; leafH={}; endpoint=G(r,root_d)
    projectedI=terminalI=projection_mass=Q(0); qcore=qctrl=qlive=Q(0)
    core_base={}; correction_core={}; correction_ctrl={}; nodeH={}; active_leaves=inactive_leaves=0
    def walk(fixed,w):
        nonlocal projectedH,leafH,endpoint,projectedI,terminalI,projection_mass,qcore,qctrl,qlive,core_base,correction_core,correction_ctrl,nodeH,active_leaves,inactive_leaves
        physical=x.restrict(F,tuple(sorted(fixed.items())))
        active=all(b==0 for i,b in fixed.items() if i>=m)
        corefixed=tuple(sorted((i,b) for i,b in fixed.items() if i<m))
        core=x.restrict(u,corefixed); remcore=[i for i in range(m) if i not in fixed]
        remctrl=[i for i in range(m,n) if i not in fixed]; rr=len(remctrl); pp=Q(1,1<<rr)
        if active: check(physical==x.activate(core,point(rr)),'actual active function including r=0 endpoint')
        else: check(set(physical)=={1},'inactive constant actual leaf')
        query=nextquery(fixed)
        if not active or query is None or (query<m and len(remcore)==1):
            leafH=x.add((1,leafH),(w,x.H(physical))); terminalI+=w*x.I(physical)
            check(len(remcore)>=1,'proper physical core terminal')
            if active:
                v=w*pp/p; projection_mass+=v; projectedH=x.add((1,projectedH),(v,x.H(core))); projectedI+=v*x.I(core)
                endpoint=x.add((1,endpoint),(-w,G(rr,x.neg(core))))
                check(v==Q(1,1<<len(corefixed)),'conditional projected actual core weight')
                active_leaves+=1
            else: inactive_leaves+=1
            return
        check(query not in fixed,'physical coordinate queried once')
        free=[i for i in range(n) if i not in fixed]; index=free.index(query)
        children=[x.restrict(physical,((index,b),)) for b in [0,1]]
        delta=x.add((1,x.H(physical)),(-Q(1,2),x.H(children[0])),(-Q(1,2),x.H(children[1])))
        bill=x.inf(physical,index); nodeH=x.add((1,nodeH),(w,delta))
        if query<m:
            ci=remcore.index(query); cc=[x.restrict(core,((ci,b),)) for b in [0,1]]
            base=x.add((1,x.H(core)),(-Q(1,2),x.H(cc[0])),(-Q(1,2),x.H(cc[1])))
            check(bill==pp*x.inf(core,ci),'core node physical scaled query influence')
            qcore+=w*bill; qlive+=w*bill if rr else 0
            core_base=x.add((1,core_base),(w*pp,base))
            correction_core=x.add((1,correction_core),(w,delta),(-w*pp,base))
        else:
            check(bill==2*pp*x.neg(core),'control node physical influence')
            qctrl+=w*bill; correction_ctrl=x.add((1,correction_ctrl),(w,delta))
        for bit in [0,1]: walk(dict(fixed,**{})|{query:bit},w/2)
    walk({},Q(1))
    projected_drop=x.add((1,x.H(u)),(-1,projectedH))
    drop=x.add((1,x.H(F)),(-1,leafH)); error=x.add((1,drop),(-p,projected_drop))
    check(projection_mass==1,'conditional active leaf normalization')
    check(qcore==p*(x.I(u)-projectedI),'single projected core influence account')
    check(core_base==x.add((p,projected_drop)),'exact projected signed core entropy account')
    check(x.I(F)==qcore+qctrl+terminalI,'single full physical influence partition')
    check(drop==nodeH,'actual signed tree entropy telescope')
    check(error==endpoint,'single signed root-to-terminal correction')
    check(error==x.add((1,correction_core),(1,correction_ctrl)),'signed correction decomposition no reserve reset')
    lo,hi=x.bounds(correction_core)
    check(max(abs(lo),abs(hi))<=22*qlive,'core correction paid only while controls remain')
    lo,hi=x.bounds(correction_ctrl)
    check(lo>=0 and hi<=6*qctrl,'entire actual control entropy payment')
    lo,hi=x.bounds(error)
    check(lo>=-22*qlive and hi<=22*qlive+6*qctrl,'full two-sided interleaved transport')
    evaluated[key]=True; counts[label]=counts.get(label,0)+1; cases+=1
def adaptive(pair,mode,m,r):
    def policy(fixed):
        if not fixed: return 0
        if len(fixed)==1: return 1 if pair[fixed[0]] else m
        if len(fixed)>=3 or mode==0: return None
        candidates=range(m,m+r) if mode==1 else range(m)
        return next((i for i in candidates if i not in fixed),None)
    return policy
for m in ([2] if pilot else [2,3]):
    for mask in range(1<<(1<<m)):
        u=tuple(1 if (mask>>t)&1 else -1 for t in range(1<<m))
        for r in [1,2]:
            for order in orders(m,r):
                for depth in range(1,m+r+1):
                    evaluate(u,r,lambda fixed,order=order,depth=depth:order[len(fixed)] if len(fixed)<depth else None,'ordered prefix')
            if m==3:
                for pair in itertools.product([False,True],repeat=2):
                    for mode in range(3): evaluate(u,r,adaptive(pair,mode,m,r),'adaptive interleaved prefix')
out={'status':'PASS','pilot':pilot,'cases':cases,'distinct_verified_actual_trees':len(evaluated),'assertions':sum(counts.values())-cases,'counts':counts,'elapsed_seconds':time.monotonic()-START,'arithmetic':'exact Fraction canonical prime-log identities and rigorous rational intervals','maximum_dimension':4 if pilot else 5,'memory_peak':'unmeasured; refined estimate180MB','no_automatic_escalation':True}
assert cases==(672 if pilot else 20640)
(ROOT/'out'/('pilot_refined.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
