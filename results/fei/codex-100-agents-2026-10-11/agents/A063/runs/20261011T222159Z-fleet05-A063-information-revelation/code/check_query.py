"""Independent direct-Walsh / rational symbolic-entropy reconstruction."""
import itertools, json, time
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(ok):
    global checks
    checks+=1
    assert ok
def fac(n):
    ans={}; d=2
    while d*d<=n:
        while n%d==0: ans[d]=ans.get(d,0)+1; n//=d
        d+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def add(*terms):
    out=defaultdict(F)
    for scale,vec in terms:
        for p,c in vec.items(): out[p]+=scale*c
    return {p:c for p,c in out.items() if c}
def ent(dist):
    out=defaultdict(F)
    for v in dist:
        if not v: continue
        for p,e in fac(v.numerator).items(): out[p]-=v*e
        for p,e in fac(v.denominator).items(): out[p]+=v*e
    return {p:c for p,c in out.items() if c}
def spectrum(vals,coords):
    # Direct character sum: distinct from the existing FWHT checker.
    N=len(vals); out={}
    for t in range(N):
        mask=sum(1<<coords[j] for j in range(len(coords)) if t>>j&1)
        out[mask]=F(sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(vals)),N)
    return out
def restrict(vals,coords,i,z):
    j=coords.index(i)
    return tuple(v for x,v in enumerate(vals) if (x>>j&1)==z),tuple(k for k in coords if k!=i)
def sq(a): return {k:v*v for k,v in a.items() if v}
def marg(dist,fun):
    out=defaultdict(F)
    for k,p in dist.items():
        if p: out[fun(k)]+=p
    return dict(out)

def tree(vals,coords,order=None,stop=None):
    root=sq(spectrum(vals,coords)); totalB={}; totalJ={}; leafEH={}; leafRootH={}
    final={}; nodecount=0
    def visit(v,c,joint,h):
        nonlocal totalB,totalJ,leafEH,leafRootH,nodecount
        pi=sum(joint.values()); current=marg(joint,lambda s:s&sum(1<<k for k in c))
        pn={s:p/pi for s,p in current.items()}
        ck(pn==sq(spectrum(v,c)))
        if (order is not None and len(h)==len(order)) or (order is None and (not c or (stop is not None and len(c)<=stop))):
            leafEH=add((1,leafEH),(pi,ent(pn.values())))
            leafRootH=add((1,leafRootH),(pi,ent((p/pi for p in joint.values()))))
            key=tuple(sorted(h))
            for s,p in joint.items():
                if p: final[(s,key)]=p
            return
        if order is not None: i=order[len(h)]
        else:
            # Cheapest positive influence; query an irrelevant coordinate only if all are irrelevant.
            inf={i:sum(p for s,p in pn.items() if s>>i&1) for i in c}
            i=min(c,key=lambda i:(inf[i]==0,inf[i],i))
        children=[restrict(v,c,i,z) for z in (0,1)]
        ps=[sq(spectrum(cv,cc)) for cv,cc in children]
        q=marg(pn,lambda s:s&~(1<<i))
        ck(q=={s:(ps[0].get(s,0)+ps[1].get(s,0))/2 for s in q})
        B=add((1,ent(pn.values())),(-1,ent(q.values())))
        J=add((1,ent(q.values())),(-F(1,2),ent(ps[0].values())),(-F(1,2),ent(ps[1].values())))
        totalB=add((1,totalB),(pi,B)); totalJ=add((1,totalJ),(pi,J))
        nodecount+=1
        nextj=[defaultdict(F),defaultdict(F)]
        for s,p in joint.items():
            if not p: continue
            t=s&sum(1<<k for k in c if k!=i)
            kernel=[ps[z].get(t,0)/(2*q[t]) for z in (0,1)]
            ck(sum(kernel)==1)
            for z in (0,1): nextj[z][s]+=p*kernel[z]
        for z in (0,1):
            clean={s:p for s,p in nextj[z].items() if p}
            ck(sum(clean.values())==pi/2)
            visit(*children[z],clean,h+((i,z),))
    visit(vals,coords,root,())
    H=ent(root.values())
    ck(add((1,H),(-1,totalB),(-1,totalJ),(-1,leafEH))=={})
    ck(add((1,H),(-1,totalJ),(-1,leafRootH))=={})
    ck(add((1,leafRootH),(-1,totalB),(-1,leafEH))=={})
    if order is not None:
        A=sum(1<<i for i in order)
        w=marg(root,lambda s:s&~A)
        z=marg(final,lambda k:k[1])
        wz=marg(final,lambda k:(k[0]&~A,k[1]))
        Hjoint=ent(final.values()); Hz=ent(z.values()); Hwz=ent(wz.values())
        ck(z=={k:F(1,1<<len(order)) for k in z})
        blockB=add((1,H),(-1,ent(w.values())))
        blockJ=add((1,ent(w.values())),(1,Hz),(-1,Hwz))
        refund=add((1,H),(1,Hwz),(-1,ent(w.values())),(-1,Hjoint))
        ck(add((1,totalJ),(-1,blockJ),(-1,refund))=={})
        ck(add((1,totalB),(-1,blockB),(1,refund))=={})
        # Zero refund iff exact conditional independence, established without evaluating logs.
        independent=True
        for (s,h),p in final.items():
            ww=s&~A
            if p*w[ww]!=root[s]*wz[(ww,h)]: independent=False
        ck((refund=={})==independent)
        return totalB,totalJ,refund,nodecount,final
    return totalB,totalJ,None,nodecount,final

def serial(v): return {str(p):str(c) for p,c in sorted(v.items())}
def main():
    started=time.perf_counter(); cases=trees=0; witness=None; nodes=0
    for n in range(4):
        coords=tuple(range(n))
        for code in range(1<<(1<<n)):
            vals=tuple(-1 if code>>x&1 else 1 for x in range(1<<n))
            for stop in (None,1):
                result=tree(vals,coords,stop=stop); nodes+=result[3]; trees+=1
            for k in range(1,n+1):
                for block in itertools.combinations(coords,k):
                    reference=None; reforder=None
                    for order in itertools.permutations(block):
                        B,J,R,nn,_=tree(vals,coords,order); nodes+=nn; cases+=1
                        if reference is not None and reference!=J and witness is None:
                            witness={'n':n,'truth_code':code,'values':vals,'block':block,'orders':[reforder,order], 'information':[serial(reference),serial(J)],'erasure_second':serial(B),'refund_second':serial(R)}
                        if reference is None: reference=J; reforder=order
    # Near-identical point-defect branches: constant versus one defect, r=2..8.
    near=[]
    for r in range(2,9):
        p=F(1,1<<r)
        parent=(1-2*p)**2
        # Query one coordinate; dominant fiber has a=1-2p,b=-2p; other fibers |a|=|b|=2p.
        a=1-2*p; b=-2*p; q=a*a+b*b
        er=add((1,ent([a*a,b*b])),(-1,ent([q])))
        raremass=((1<<(r-1))-1)*8*p*p
        er=add((1,er),(raremass,{2:F(1)}))
        ck(q+raremass==1)
        # Child distributions: one constant and one (r-1)-dimensional defect.
        child=[(1-4*p)**2]+[16*p*p]*((1<<(r-1))-1)
        avg=ent([q]+[8*p*p]*((1<<(r-1))-1))
        info=add((1,avg),(-F(1,2),ent(child)))
        near.append({'r':r,'influence':str(2*p),'erasure':serial(er),'information':serial(info)})
    # Single split with two different admissible classical couplings, same physical/residual marginal.
    # Dominant point-defect3 fiber: q=5/8, B marginal=1/10, Z+ marginal=1/5 (sign convention).
    q=F(5,8); beta=F(1,10); rho=F(1,5)
    canonical=[(1-beta)*(1-rho),(1-beta)*rho,beta*(1-rho),beta*rho]
    t=beta
    alternate=[1-beta-rho+t,rho-t,beta-t,t]
    ck(sum(canonical)==sum(alternate)==1)
    ck(canonical[2]+canonical[3]==alternate[2]+alternate[3]==beta)
    ck(canonical[1]+canonical[3]==alternate[1]+alternate[3]==rho)
    injected=add((q,ent([beta,1-beta])),(q,ent([rho,1-rho])),(-q,ent(alternate)))
    ck(injected!={})
    result={'status':'PASS','exact_assertions':checks,'truth_tables':278,'fixed_block_order_cases':cases,'adaptive_trees':trees,'nodes':nodes,'runtime_seconds':time.perf_counter()-started,'first_order_dependence_witness':witness,'near_identical_point_defect_controls':near,'nonunique_kernel_injection':serial(injected),'arithmetic':'Fraction and rational prime-log maps; no numerical entropy comparison'}
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['near_identical_point_defect_controls']},indent=2))
if __name__=='__main__': main()
