"""Signed complete-reference ledger through already converted blocks."""
from pathlib import Path
from functools import lru_cache
import json,time,sys,hashlib
from exact import *
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
count=0
def ck(ok,tag):
    global count
    count+=1
    assert ok,(count,tag)
def eq(a,b,tag): ck(a==b,tag)
def ge(a,x=0): ck(bounds(a)[0]>=x,'certified lower bound')
L3=lg(3); L13=lg(13); L15=lg(15)
h=plus(const(4),mul(L3,-Q(9,8)))
c1=plus(const(3),mul(L13,-Q(1,2)))
c2=plus(const(4),mul(L15,-1))
CONTROLS=((0,0,0,0),(1,1,1,1),(0,1,0,1),(0,0,1,1),(0,0,0,1),(0,1,1,1))
def J(v): return mul(L3,-Q(7,4) if v==0 else Q(5,4))
@lru_cache(None)
def qdata(t,labels,fixed):
    fixed=dict(fixed); out=[]
    for s in range(2**len(labels)):
        p=Q(1)
        for block in range(t):
            bits=[i for i in range(3*block,3*block+3) if i in labels]
            sf=sum(((s>>labels.index(i))&1)<<j for j,i in enumerate(bits))
            j=3-len(bits)
            if j==0: p*=Q(9 if sf==0 else 1,16)
            elif j==1:
                value=next(fixed[i] for i in range(3*block,3*block+3) if i in fixed)
                p*=Q(1,4) if value==0 else Q(13 if sf==0 else 1,16)
            elif j==2:
                main=1 if all(fixed[i]==0 for i in range(3*block,3*block+3) if i in fixed) else 0
                p*=Q(15 if sf==main else 1,16)
        out.append(p)
    assert sum(out)==1 and all(out)
    return out
def case(t,v,A,order,maxdepth):
    k=3*t; N=2**k; delta=Q(1,N); alpha=Q(sum(A),4)
    pa=spectrum([1-2*z for z in A]); L=mul(entropy(pa),delta)
    R=[1-4*delta*alpha*(1-alpha)]+[delta*p for p in pa[1:]]; HR=entropy(R)
    f=[(1-2*int(x==v and A[z]))*__import__('math').prod(g((x>>(3*b))&7) for b in range(t)) for z in range(4) for x in range(N)]
    labels=tuple(range(k)); nodes=[(f,())]; C=[]; H=[]; D=[]; B=[]; Is=[]; pivs=[]
    U=Q(t,64)
    for depth in range(maxdepth+1):
        M=2**len(labels); Cs=[]; Hs=[]; ids=[]; avgR=[Q(0)]*4
        for ff,fixed in nodes:
            P=spectrum(ff); pdata=[sum(P[z*M+s] for z in range(4)) for s in range(M)]
            pr=[sum(P[z*M:(z+1)*M]) for z in range(4)]
            ref=qdata(t,labels,fixed)
            Cs.append(plus(ce(pdata,ref),ce(pr,R))); Hs.append(entropy(P))
            ids.append(sum((p*s.bit_count() for s,p in enumerate(pdata)),Q(0)))
            for z in range(4): avgR[z]+=pr[z]/len(nodes)
        C.append(mul(plus(*Cs),Q(1,len(nodes))))
        H.append(mul(plus(*Hs),Q(1,len(nodes))))
        D.append(plus(C[-1],mul(H[-1],-1))); Is.append(sum(ids,Q(0))/len(nodes))
        B.append(plus(const(4*Is[-1]-U),L,mul(C[-1],-1)))
        eq(avgR,R,'same original R at every cut')
        ge(D[-1])
        r,j=divmod(depth,3); intact=[]
        for b in range(t):
            if all(i in labels for i in range(3*b,3*b+3)): intact.append(b)
        expectedC=plus(HR,mul(h,len(intact)),mul(plus(*(J((v>>(3*b))&7) for b in intact)),4*delta*alpha))
        if j:
            block=order[3*r]//3; first=order[3*r]
            extra=mul(L13,3) if (v>>first)&1 else {}
            expectedC=plus(expectedC,c1 if j==1 else c2,mul(extra if j==1 else mul(L15,2),delta*alpha))
        eq(C[-1],expectedC,'exact complete terminal reference, old R retained')
        sigma=lambda i:g((v>>(3*(i//3)))&7)*g(((v>>(3*(i//3)))&7)^(1<<(i%3)))
        eq(Is[-1],Q(len(labels),4)+2*delta*alpha*sum(sigma(i) for i in labels),'actual data influence all prefixes')
        if depth<=3*(t//2)+2: ge(B[-1],Q(13*t,576))
        if depth:
            ell=plus(const(4*pivs[-1]),mul(C[-2],-1),C[-1])
            eq(B[-1],plus(B[-2],mul(ell,-1)),'no restored source bank')
            Da=plus(H[-2],mul(H[-1],-1))
            eq(Da,plus(C[-2],mul(C[-1],-1),D[-1],mul(D[-2],-1)),'both full terminal KLs')
            if depth%3==2:
                block=order[depth-1]//3; fi=order[depth-2]; se=order[depth-1]
                w1=mul(L13,3) if (v>>fi)&1 else {}
                expected=plus(const(2),mul(L13,Q(1,2)),mul(L15,-1),
                              mul(plus(const(8*sigma(se)),mul(w1,-1),mul(L15,2)),delta*alpha))
                eq(ell,expected,'second already converted coordinate exact loss')
                ck(bounds(ell)[1]<Q(1,4),'second query pays from old reserve')
                if t>=3: ck(bounds(ell)[1]<0,'second query earns reference capacity for t>=3')
        if depth==maxdepth: break
        i=order[depth]; pos=labels.index(i)
        piv=sum((inf(ff,pos) for ff,_ in nodes),Q(0))/len(nodes); pivs.append(piv)
        new=[]
        for ff,fixed in nodes:
            for val in (0,1): new.append((restrict(ff,pos,val),tuple(sorted(fixed+((i,val),)))))
        nodes=new; labels=tuple(j for j in labels if j!=i)
    for d,piv in enumerate(pivs): eq(Is[d]-Is[d+1],piv,'physical influence telescoping')
    E=plus(*(plus(const(4*pivs[d]),mul(H[d],-1),H[d+1]) for d in range(len(pivs))))
    eq(plus(B[-1],D[-1],E),plus(B[0],D[0]),'complete signed accumulated history')
    if maxdepth==k:
        eq(H[-1],L,'all-data terminal entropy exact')
        eq(C[-1],HR,'all-data ORIGINAL R terminal cross entropy exact')
        eq(B[-1],plus(L,mul(HR,-1),const(-U)),'final CE-only obstruction')
    return {'t':t,'v':v,'alpha':str(alpha),'depth':maxdepth,'bank_at_five_lower':str(bounds(B[min(5,maxdepth)])[0])[:80]}
def main(mode):
    start=time.perf_counter(); rows=[]
    limit=120 if mode=='main' else 60
    if mode=='pilot': domain=[(2,v,A,tuple(range(6)),6) for v in range(4) for A in CONTROLS]
    elif mode=='targeted': domain=[(3,v,A,tuple(range(9)),5) for v in [0,511] for A in CONTROLS]
    else: domain=[(2,v,A,o,6) for v in range(64) for A in CONTROLS for o in [tuple(range(6)),(2,0,1,4,5,3)]]
    for args in domain:
        rows.append(case(*args))
        if len(rows)%32==0:
            (OUT/(mode+'.json')).write_text(json.dumps({'status':'RUNNING','cases':len(rows),'assertions':count,'seconds':time.perf_counter()-start})+'\n',encoding='utf-8',newline='')
        if time.perf_counter()-start>limit-1: raise RuntimeError('frozen runtime cap; completed count checkpoint preserved')
    out={'status':'PASS','mode':mode,'cases':len(rows),'assertions':count,'seconds':time.perf_counter()-start,
         'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
    (OUT/(mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps({k:v for k,v in out.items() if k not in ['rows','helper_sha256']}))
if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else 'main')
