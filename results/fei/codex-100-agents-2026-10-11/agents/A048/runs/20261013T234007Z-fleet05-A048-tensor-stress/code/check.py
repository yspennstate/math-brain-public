"""Exact actual-leaf schedule-injection verifier; frozen v1."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import runpy, json, time, sys
ROOT=Path(__file__).resolve().parents[1]
U=runpy.run_path(str(ROOT.parent/'20261011T221822Z-fleet05-A048-tensor-stress'/'code'/'check.py'))
add,scale,entropy,hb,walsh,influence=[U[k] for k in ('add','scale','entropy','hb','walsh','influence')]
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def ser(v): return {str(k):str(x) for k,x in sorted(v.items())}
def marg(joint,indices):
    out=defaultdict(F)
    for key,p in joint.items(): out[tuple(key[i] for i in indices)]+=p
    return dict(out)
def H(j,indices): return entropy(marg(j,indices).values())
def MI(j,a,b): return add(H(j,a),H(j,b),scale(H(j,a+b),-1))
def defect(k): return [(-1 if x==(1<<k)-1 else 1) for x in range(1<<k)]
def j_formula(k):
    p=F(1,1<<(k-1)); v=4*p*(1-p)
    return add(hb(v/2),scale(hb(v),F(-1,2)))
def direct(r,k,adaptive):
    m=1<<r; n=r*k+m; allmask=(1<<n)-1
    def f(x):
        val=(-1)**((x>>(r*k)).bit_count())
        for a in range(r):
            if (x>>(a*k))&((1<<k)-1)==(1<<k)-1: val=-val
        return val
    table=[f(x) for x in range(1<<n)]
    @lru_cache(None)
    def node(hist):
        used=sum(1<<i for i,b in hist); inds=[i for i in range(n) if not (used>>i&1)]
        base=sum(b<<i for i,b in hist)
        tab=[f(base+sum(((z>>a)&1)<<i for a,i in enumerate(inds))) for z in range(1<<len(inds))]
        coeff=walsh(tab)
        law={sum(((s>>a)&1)<<i for a,i in enumerate(inds)):p*p for s,p in enumerate(coeff) if p}
        return law,influence(tab),sum(tab,F(0))/len(tab)
    rootlaw,rootI,rootmean=node(())
    eq(rootI,F(m)+r*k*F(1,1<<(k-1)))
    eq(entropy(rootlaw.values()),scale(entropy(U['law'](defect(k))),r))
    # Root/retained-frequency/transcript states, propagated through the actual reveal kernel.
    states={(s,s,()):p for s,p in rootlaw.items()}
    for depth in range(r+1):
        nxt=defaultdict(F)
        for (s0,s,hist),mass in states.items():
            address=sum(b<<a for a,(i,b) in enumerate(hist))
            i=depth*k if depth<r else r*k+(address if adaptive else 0)
            T=s&~(1<<i); plaw,_,_=node(hist)
            q=plaw.get(T,F(0))+plaw.get(T|(1<<i),F(0))
            eq(q>0,True)
            for b in (0,1):
                child=hist+((i,b),); cl=node(child)[0]
                prob=cl.get(T,F(0))/(2*q)
                if prob: nxt[(s0,T,child)]+=mass*prob
        states=dict(nxt); eq(sum(states.values()),1)
    # Add output Y to the coherent joint using actual balanced leaf output law.
    joint={}
    leaves=defaultdict(lambda:defaultdict(F))
    for (s0,w,h),mass in states.items():
        leaves[h][w]+=mass
        eq(node(h)[2],0)
        for y in (0,1): joint[(s0,h,w,y)]=mass/2
    for hist,law in leaves.items():
        eq(sum(law.values()),F(1,1<<(r+1)))
        eq({s:p*2**(r+1) for s,p in law.items()},node(hist)[0])
    expectedI=sum((node(h)[1]*F(1,1<<(r+1)) for h in leaves),F(0))
    R=rootI-expectedI; eq(R,1+r*F(1,1<<(k-1)))
    hleaf=add(*(scale(entropy(node(h)[0].values()),F(1,1<<(r+1))) for h in leaves))
    eq(hleaf,scale(entropy(U['law'](defect(k-1))),F(r,2)))
    j0=MI(joint,(0,),(1,)); jw=MI(joint,(2,),(1,)); oy=MI(joint,(3,),(1,))
    injection=add(H(joint,(0,2)),scale(H(joint,(0,)),-1))
    eq(j0,scale(j_formula(k),r)); eq(oy,{})
    if adaptive:
        eq(jw,{2:F(r)}); eq(injection,add({2:F(r)},scale(j0,-1)))
        for s0,w,h in states:
            missing=((1<<m)-1)^((w>>(r*k))&((1<<m)-1))
            eq(missing.bit_count(),1)
            eq(missing.bit_length()-1,sum(b<<a for a,(i,b) in enumerate(h[:r])))
    else: eq(injection,{})
    result={'r':r,'k':k,'n':n,'policy':'adaptive' if adaptive else 'fixed','R':str(R),'root_MI':ser(j0),'leaf_MI':ser(jw),'injection':ser(injection),'root_entropy':ser(entropy(rootlaw.values())),'expected_terminal_entropy':ser(hleaf),'terminal_influence':str(expectedI),'joint_atoms':len(joint),'checks_so_far':checks}
    (ROOT/'out'/f'case_r{r}_k{k}_{result["policy"]}.json').write_text(json.dumps(result,indent=2)+'\n')
    return joint,result
def main():
    start=time.perf_counter(); results=[]; saved=None
    cases=[(1,2)] if '--pilot' in sys.argv else [(1,2),(1,3),(1,4),(2,2),(2,3),(3,2)]
    for r,k in cases:
        for adaptive in (True,False):
            joint,result=direct(r,k,adaptive); results.append(result)
            if (r,k,adaptive)==(1,3,True): saved=joint
    if '--pilot' not in sys.argv:
        # Tensor products of complete coherent joint laws, with disjoint labels.
        for t in (1,2,3):
            jt={(((),(),(),())):F(1)}
            for _ in range(t):
                nt={}
                for ka,pa in jt.items():
                    for kb,pb in saved.items(): nt[tuple(ka[i]+(kb[i],) for i in range(4))]=pa*pb
                jt=nt
            eq(MI(jt,(0,),(1,)),scale(MI(saved,(0,),(1,)),t))
            eq(MI(jt,(2,),(1,)),{2:F(t)})
            eq(add(H(jt,(0,2)),scale(H(jt,(0,)),-1)),scale(add({2:F(1)},scale(j_formula(3),-1)),t))
        formula=[]
        for r in range(1,17):
            k=2*r+2; R=1+r*F(1,1<<(k-1))
            eq(R<1+F(1,4),True)
            formula.append({'r':r,'k':k,'n':r*k+(1<<r),'R':str(R),'conversion':str(F(r,2)),'conversion_over_R':str(F(r,2)/R)})
        # ln2=2(1/3+1/(3^3*3)+...)>2/3; hence R/ln2<3R/2.
        r,k=4,10; R=1+r*F(1,1<<(k-1)); eq(R,F(129,128)); eq(F(r,2)>F(3,2)*R,True)
        certificate={'r':r,'k':k,'n':r*k+(1<<r),'R':str(R),'actual_conversion':str(F(r,2)),'strict_upper_on_root_compatible_allowance':str(F(3,2)*R),'proof_of_log_bound':'ln2=2*sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3'}
        (ROOT/'out'/'FORMULA_AND_VIOLATION.json').write_text(json.dumps({'grid':formula,'certificate':certificate},indent=2)+'\n')
    summary={'status':'PASS','mode':'pilot' if '--pilot' in sys.argv else 'full','frozen_case_count':2 if '--pilot' in sys.argv else 32,'assertions':checks,'seconds':time.perf_counter()-start,'direct':results}
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='direct'}))
if __name__=='__main__': main()
