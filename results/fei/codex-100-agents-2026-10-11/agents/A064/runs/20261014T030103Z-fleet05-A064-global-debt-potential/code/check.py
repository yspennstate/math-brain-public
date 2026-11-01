from pathlib import Path
import json,hashlib,time,sys
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261013T235917Z-fleet05-A064-global-debt-potential/code/check.py'
# Reuse only independently audited exact arithmetic primitives, not the old search.
exec(OLD.read_text(encoding='utf-8').split('allcores=')[0])
PILOT='--pilot' in sys.argv
LIMIT=58 if PILOT else 595
def deadline():
    if time.perf_counter()-START>LIMIT: raise TimeoutError('Frozen stage deadline')
def comp(ctrl,u,v):
    return tuple(u[a] if j==0 else v[b] if j==1 else 1 if j==2 else -1 for j in ctrl for b in range(len(v)) for a in range(len(u)))
def bank(ctrl,u,v,C):
    return plus(*[(F(ctrl.count(j),len(ctrl)),core_reserve(c,C)) for j,c in enumerate((u,v))],(1,rare(ctrl,u,v)))
def rare(ctrl,u,v):
    return plus(*[(1-core(c)[1]**2,phi(F(ctrl.count(j),len(ctrl)))) for j,c in enumerate((u,v))])
def cutctrl(ctrl,i,b): return child(ctrl,i,b)
def erasure(vals,i):
    cs=tuple(F(a,len(vals)) for a in fwht(vals)); out=[]
    for k,a in enumerate(cs):
        if not (k>>i)&1: out.append((1,Phi(a*a,cs[k|(1<<i)]**2)))
    return plus(*out)
def Id(ctrl,u,v):
    means=[core(u)[1],core(v)[1],F(1),F(-1)]; d=F(0)
    for i in range(len(ctrl).bit_length()-1):
        for z in range(len(ctrl)):
            j,k=ctrl[z],ctrl[z^(1<<i)]
            if j!=k: d+=(1-means[j]*means[k])/(2*len(ctrl))
    return d
cores=[tuple(1 if (t>>a)&1 else -1 for a in range(4)) for t in range(16)]
named=[cores[t] for t in (0,15,7,6)]
ctrls=list(product((1,2,3),repeat=4))
if PILOT: ctrls=ctrls[:9]
localcases=0
for s in ((1,2) if PILOT else (1,2,3)):
    p=F(1,2**s)
    for fallback in ctrls:
        for u,v in product(named,repeat=2):
            # A is the all-zero point; the queried bit is its first physical bit.
            ctrl=tuple(0 if a==0 else j for j in fallback for a in range(2**s))
            full=comp(ctrl,u,v); h=spectrum_H(full)
            c0,c1=(cutctrl(ctrl,0,b) for b in (0,1))
            full0,full1=comp(c0,u,v),comp(c1,u,v)
            D=plus((1,h),(-F(1,2),spectrum_H(full0)),(-F(1,2),spectrum_H(full1)))
            B=erasure(full,4); kap=plus((1,rare(ctrl,u,v)),(-F(1,2),rare(c0,u,v)),(-F(1,2),rare(c1,u,v)))
            y=core(u)[1]; mv=core(v)[1]; gj=tuple(mv if j==1 else F(1) if j==2 else F(-1) for j in fallback)
            x=sum(gj,F(0))/4; delta=tuple(g-y for g in gj)
            gh=tuple(a/4 for a in fwht(gj)); dh=tuple(a/4 for a in fwht(delta))
            e2=sum((z*z for z in delta),F(0))/4
            prof=plus((p-2*p*p,{2:e2}),*[(1,Phi((a-p*b)**2,p*p*b*b)) for a,b in zip(gh,dh)])
            W=F(fallback.count(1),4)*(1-mv*mv)
            cp=plus((1,{2:p-2*p*p}),(1,Phi((1-p)**2,p*p)))
            kp=plus((1,phi(1-p)),(-F(1,2),phi(1-2*p)))
            check(plus((1,B),(-1,kap))==plus((1,prof),(W,cp),(-W,kp)),'exact repeated-fallback erasure')
            check(nonnegative(kap),'owned release nonnegative')
            check(nonnegative(plus((2*p,{2:F(1)}),(-1,cp))),'complement packet <=2p')
            d=p*(1-x*y)
            check(core(full)[3][4]==d,'actual independent u/G mismatch')
            check(nonnegative(plus((8*d,{2:F(1)}),(-1,B),(1,kap))),'B-kappa <=8d')
            check(nonnegative(plus((11*d,{2:F(1)}),(-1,D),(1,kap))),'D-kappa <11d except zero')
            localcases+=1
        deadline()
    (R/'out/CHECKPOINT.json').write_text(json.dumps({'phase':'LOCAL','s_finished':s,'cases':localcases,'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START},indent=2)+'\n')
    spectrum_H.cache_clear();core.cache_clear();bounds_tuple.cache_clear()

TREES=0; STATES=0; sharednodes=0; interruptednodes=0; grows=0
@lru_cache(None)
def tree(ctrl,u,v,order,C):
    global STATES,sharednodes,interruptednodes,grows
    STATES+=1
    q=bank(ctrl,u,v,C); h=spectrum_H(comp(ctrl,u,v))
    if not order:
        check(not h and not q,'actual full terminal H=Q=0')
        return {},F(0),F(0),{}
    typ,idx=order[0]; args=[]
    if typ=='c':
        c0,c1=(cutctrl(ctrl,idx,b) for b in (0,1)); args=[(c0,u,v),(c1,u,v)]
        full=comp(ctrl,u,v); d=core(full)[3][(len(u).bit_length()-1)+(len(v).bit_length()-1)+idx]
        rate=F(11)
        kap=plus((1,rare(ctrl,u,v)),(-F(1,2),rare(c0,u,v)),(-F(1,2),rare(c1,u,v)))
        check(nonnegative(kap),'controller release at actual history')
        if len(ctrl)==16: sharednodes+=1
        if len(ctrl)==4 and len(u)==2: interruptednodes+=1
    else:
        cur=u if typ=='u' else v; j=0 if typ=='u' else 1
        for b in (0,1): args.append((ctrl,child(u,idx,b),v) if typ=='u' else (ctrl,u,child(v,idx,b)))
        d=F(ctrl.count(j),len(ctrl))*core(cur)[3][idx]; rate=C+F(11,2)
    qs=[bank(*a,C) for a in args]; hs=[spectrum_H(comp(*a)) for a in args]
    D=plus((1,h),(-F(1,2),hs[0]),(-F(1,2),hs[1]))
    check(nonnegative(plus((rate*d,{2:F(1)}),(1,q),(-F(1,2),qs[0]),(-F(1,2),qs[1]),(-1,D))),'whole interleaved candidate drift')
    if typ=='c': check(nonnegative(plus((11*d,{2:F(1)}),(-1,D),(1,kap))),'shared/repeated/one-sided controller price')
    else:
        check(nonnegative(plus((1,q),(C*d,{2:F(1)}),(-F(1,2),qs[0]),(-F(1,2),qs[1]))),'expected reserve growth rate C')
    for qc in qs:
        if nonnegative(plus((1,qc),(-1,q))) and qc!=q: grows+=1
    results=[tree(*a,order[1:],C) for a in args]
    alpha=max(C+F(11,2),F(11))
    snell=positive(plus((1,D),(-alpha*d,{2:F(1)}),(F(1,2),results[0][0]),(F(1,2),results[1][0])))
    check(nonnegative(plus((1,q),(-1,snell))),'least nonnegative full reserve dominated')
    pd=(d if typ!='c' else F(0))+sum((z[1] for z in results),F(0))/2
    pc=(d if typ=='c' else F(0))+sum((z[2] for z in results),F(0))/2
    eh=plus((F(1,2),results[0][3]),(F(1,2),results[1][3]))
    check(nonnegative(plus(((C+F(11,2))*pd+11*pc,{2:F(1)}),(1,q),(1,eh),(-1,h))),'actual stopped/completed payment')
    return snell,pd,pc,eh

# Initial physical controller bits are X,A0,A1,B, lowest index first.
# A positive orientation event is live at shared X=0. Private events are zero points.
order=(('c',0),('c',0),('u',0),('c',0),('c',0),('v',0),('u',0),('v',0))
rootcores=named if PILOT else cores
for ori in (0,1):
    ctrl=tuple(0 if (z&1)==0 and (z&6)==0 else 1 if (z&1)==ori and (z&8)==0 else 2 for z in range(16))
    for u,v in product(rootcores,repeat=2):
        check(nonnegative(plus((2*Id(ctrl,u,v),{2:F(1)}),(-1,rare(ctrl,u,v)))),'initial single-edge rarity funding')
        for C in (F(0),F(4)):
            ans=tree(ctrl,u,v,order,C); TREES+=1
            check(ans[1]+ans[2]==sum(core(comp(ctrl,u,v))[3],F(0)),'single influence partition actual complete tree')
        deadline()
    (R/'out/CHECKPOINT.json').write_text(json.dumps({'phase':'TREES','orientation_finished':ori,'trees':TREES,'states':STATES,'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START},indent=2)+'\n')
    tree.cache_clear();core.cache_clear();spectrum_H.cache_clear();bounds_tuple.cache_clear()

out={'status':'PASS','pilot':PILOT,'local_repeated_fallback_cases':localcases,'complete_interleaved_trees':TREES,'distinct_tree_states':STATES,'shared_X_nodes':sharednodes,'actual_interrupted_private_nodes':interruptednodes,'branch_growth_occurrences':grows,'exact_assertions':ASSERTIONS,'certified_sign_decisions':SIGNS,'runtime_seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_source_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'maximum_dimension':9}
(R/'out'/('PILOT.json' if PILOT else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
