"""A025: actual control query after nonflat data prefix; exact signed resets."""
from pathlib import Path
from itertools import product
import json,sys,time
from exact import *
from a022_source import qdata
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'
count=0
def ck(ok,tag):
    global count
    count+=1
    assert ok,(count,tag)
def eq(a,b,tag): ck(a==b,tag)
def ge(a,tag): ck(bounds(a)[0]>=0,tag)
def avg(xs): return mul(plus(*xs),Q(1,len(xs)))
def kl(p,q): return plus(ce(p,q),mul(entropy(p),-1))
def Rlaw(a,delta):
    r=[delta*x for x in spectrum(a)]; r[0]+=1-delta
    return r
def G(s,delta):
    return plus(phi(1-delta+delta*s*s),mul(phi(s*s),-delta),mul(lg(1/delta),delta*(1-s*s)))
def exact_phase(f,ref,idx,ptarget):
    """Retain every reference row, true zero-pair branches and actual rho."""
    w=fwht(f); n=len(f); P=[Q(x*x,n*n) for x in w]
    pairs=[(s,s|(1<<idx)) for s in range(n) if not s&(1<<idx)]
    pp=[P[s]+P[t] for s,t in pairs]; rr=[ref[s]+ref[t] for s,t in pairs]
    E=plus(kl(P,ref),mul(kl(pp,rr),-1)); ge(E,'actual physical erasure refund')
    ds=[]; dtarget=[]; rhos=[]; kappas=[]
    for b in (0,1):
        joint=[]
        for s,t in pairs:
            den=w[s]*w[s]+w[t]*w[t]
            k=Q((w[s]+(-1)**b*w[t])**2,2*den) if den else Q(1,2)
            joint.append((ref[s]+ref[t])*k)
        rho=sum(joint); ck(rho>0,'actual reference branch normalizer positive'); rhos.append(rho)
        p=spectrum(restrict(f,idx,b)); inh=[r/rho for r in joint]
        di=kl(p,inh); dt=kl(p,ptarget[b]); ds.append(di); dtarget.append(dt)
        kappas.append(plus(dt,mul(di,-1)))
        ge(di,'full inherited child KL'); ge(dt,'full prescribed child KL')
    O=kl([Q(1,2)]*2,rhos); ge(O,'actual outcome refund')
    eq(plus(E,O,avg(ds)),kl(P,ref),'physical KL chain retains BOTH children')
    sigma=plus(avg(dtarget),mul(kl(P,ref),-1))
    eq(plus(avg(kappas),mul(E,-1),mul(O,-1)),sigma,'signed reset less actual refunds')
    return sigma,avg(kappas),E,O
def case(t,v,A,depth):
    k=3*t; delta=Q(1,2**k); U=Q(t,64); a=tuple(1-2*x for x in A)
    original=[(1-2*int(x==v and A[z]))*__import__('math').prod(g((x>>(3*b))&7) for b in range(t)) for z in range(4) for x in range(2**k)]
    nodes=[(original,())]; labels=tuple(range(k))
    for i in range(depth):
        nodes=[(restrict(f,0,b),fixed+((i,b),)) for f,fixed in nodes for b in (0,1)]
        labels=labels[1:]
    nd=k-depth; M=2**nd; R=Rlaw(a,delta); L=mul(entropy(spectrum(a)),delta)
    Cs=[]; Hs=[]; ids=[]; pref=[]; Fs=[]; ragg=[Q(0)]*4
    for f,fixed in nodes:
        p=spectrum(f); q=qdata(t,labels,fixed); ref=[r*x for r in R for x in q]
        Cs.append(ce(p,ref)); Hs.append(entropy(p)); pref.append(ref); Fs.append(f)
        ids.append(sum((p[s]*(s&(M-1)).bit_count() for s in range(len(p))),Q(0)))
        for z in range(4): ragg[z]+=sum(p[z*M:(z+1)*M])/len(nodes)
    eq(ragg,R,'all original reached data siblings preserve exact R')
    Cp=avg(Cs); Hp=avg(Hs); Ip=sum(ids,Q(0))/len(ids)
    Bp=plus(const(4*Ip-U),L,mul(Cp,-1)); ge(plus(Bp,const(-Q(13*t,576))),'source A022 reserve at requested prefix')
    ge(plus(Cp,mul(Hp,-1)),'parent COMPLETE KL')
    for i in (0,1):
        ach=[tuple(restrict(a,i,b)) for b in (0,1)]
        Rs=[Rlaw(ab,delta) for ab in ach]; Ls=[mul(entropy(spectrum(ab)),delta) for ab in ach]
        sm=Q(sum(a),4); sch=[Q(sum(ab),2) for ab in ach]
        gamma=plus(G(sm,delta),mul(avg([G(s,delta) for s in sch]),-1)); ge(gamma,'rare overhead concavity')
        childCs=[]; childHs=[]; childids=[]; sigmas=[]; raw=[]; refunds=[]; raggc=[[Q(0)]*2 for _ in (0,1)]
        for (f,fixed),rp in zip(nodes,pref):
            q=qdata(t,labels,fixed); target=[[r*x for r in Rb for x in q] for Rb in Rs]
            si,ka,er,ou=exact_phase(f,rp,nd+i,target)
            sigmas.append(si); raw.append(ka); refunds.append(plus(er,ou))
            for b in (0,1):
                fc=restrict(f,nd+i,b); pc=spectrum(fc)
                childCs.append(ce(pc,target[b])); childHs.append(entropy(pc))
                childids.append(sum((pc[s]*(s&(M-1)).bit_count() for s in range(len(pc))),Q(0)))
                for z in range(2): raggc[b][z]+=sum(pc[z*M:(z+1)*M])/len(nodes)
        for b in (0,1): eq(raggc[b],Rs[b],'target equals actual conditional marginal after all data siblings')
        Cc=avg(childCs); Hc=avg(childHs); Ic=sum(childids,Q(0))/len(childids)
        eq(Ic,Ip,'actual remaining data influence is preserved')
        Bc=plus(const(4*Ic-U),avg(Ls),mul(Cc,-1))
        eq(plus(Bc,mul(Bp,-1)),gamma,'SAME actual bank gain; original U retained')
        ge(plus(Bc,const(-Q(13*t,576))),'no new source admission after actual control')
        dHa=plus(L,mul(avg(Ls),-1)); dHf=plus(Hp,mul(Hc,-1))
        eq(plus(Cp,mul(Cc,-1)),plus(dHa,gamma),'full original source entropy spent exactly once')
        eq(avg(sigmas),plus(dHf,mul(dHa,-1),mul(gamma,-1)),'actual net physical conversion paid')
        eq(plus(Bc,Cc,mul(Hc,-1),dHa,mul(dHf,-1)),plus(Bp,Cp,mul(Hp,-1)),'B+D+signed old/new history conserved')
    return 2
def main(mode):
    start=time.perf_counter(); cases=0
    if mode=='pilot': domain=[(2,v,tuple((a>>z)&1 for z in range(4)),d) for v in range(4) for a in range(16) for d in (1,2,5)]
    elif mode=='targeted': domain=[(3,v,tuple((a>>z)&1 for z in range(4)),d) for v in (0,511) for a in range(16) for d in (1,2,5,6)]
    else: domain=[(2,v,tuple((a>>z)&1 for z in range(4)),d) for v in range(64) for a in range(16) for d in (1,2,5)]
    cap=60 if mode=='pilot' else (600 if mode=='main' else 120)
    for args in domain:
        cases+=case(*args)
        if cases%128==0:
            (OUT/(mode+'_checkpoint.json')).write_text(json.dumps({'cases':cases,'assertions':count,'seconds':time.perf_counter()-start}),encoding='utf-8')
        if time.perf_counter()-start>cap: raise RuntimeError('frozen runtime cap')
    out={'status':'PASS','cases':cases,'assertions':count,'seconds':time.perf_counter()-start,'mode':mode}
    (OUT/(mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__': main(sys.argv[1])
