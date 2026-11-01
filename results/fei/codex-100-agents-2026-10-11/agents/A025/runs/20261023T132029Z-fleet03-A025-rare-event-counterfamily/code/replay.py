"""Independent global-frontier reconstruction: direct characters, no production imports."""
from functools import lru_cache
from pathlib import Path
import json,time
import arith as A
F=A.F; add=A.add; mul=A.scale; mean=A.mean; start=time.perf_counter(); queries=0; strict=0
def eq(x,y,s): A.ck(A.same(x,y),s)
@lru_cache(maxsize=2048)
def spectrum(f):
    return tuple(F(sum(f[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(len(f))),len(f)) for s in range(len(f)))
def prob(f): return tuple(x*x for x in spectrum(tuple(f)))
def restriction(f,i,b): return tuple(x for k,x in enumerate(f) if k//2**i%2==b)
def ext(P,kind):
    if P[0]==1:return P
    non=[F(1,len(P)-1)]*(len(P)-1) if kind==0 else [F(1)]+[F(0)]*(len(P)-2)
    return tuple([P[0]]+[(P[j]+(1-P[0])*non[j-1])/2 for j in range(1,len(P))])
def cal(P,r):
    if P[0]==1:return tuple([F(1)]+[F(0)]*(len(P)-1))
    return tuple([P[0]]+[(1-P[0])*q/(1-r[0]) for q in r[1:]])
def one(f,kind):
    global queries,strict
    P=prob(f); r=ext(P,kind); initialD=A.divg(P,r); initialCE=A.cross(P,r)
    frontier=[(F(1),tuple(f),r)]; refundD={}; spendCE={}; snapshots=0
    while any(len(set(ff))>1 for w,ff,rr in frontier):
        idx=next(j for j,(w,ff,rr) in enumerate(frontier) if len(set(ff))>1)
        w,ff,rr=frontier.pop(idx); n=len(ff).bit_length()-1; i=n-1; p=prob(ff); amps=spectrum(ff)
        # Assemble the entire joint phase output over remaining label and physical bit.
        labels=[s for s in range(len(ff)) if s//2**i%2==0]
        pairP=[]; pairR=[]; output=[[],[]]
        for s in labels:
            t=s+2**i; x,y=amps[s],amps[t]; den=x*x+y*y
            pairP.append(p[s]+p[t]); pairR.append(rr[s]+rr[t])
            for b in (0,1):
                channel=F(1,2) if not den else (x+(-1)**b*y)**2/(2*den)
                output[b].append((rr[s]+rr[t])*channel)
        E=add(A.divg(p,rr),mul(A.divg(pairP,pairR),-1)); A.ge(E,'independent erased KL')
        masses=[sum(row) for row in output]; O=A.divg([F(1,2)]*2,masses); A.ge(O,'independent outcome KL')
        Z=[]; Dc=[]; Di=[]; Cc=[]; Hc=[]; children=[]
        for b in (0,1):
            fc=restriction(ff,i,b); pc=prob(fc); rin=tuple(q/masses[b] for q in output[b]); rc=cal(pc,rin)
            A.ck(sum(rc)==1 and rc[0]==pc[0],'independent normalized calibrated child')
            zi=A.divg([pc[0],1-pc[0]],[rin[0],1-rin[0]]); A.ge(zi,'independent vacuum refund')
            strict+=A.bounds(zi)[0]>0
            di=A.divg(pc,rin); dc=A.divg(pc,rc)
            eq(add(dc,zi),di,'independent full child inherited/target KL difference')
            Z.append(zi); Di.append(di); Dc.append(dc); Cc.append(A.cross(pc,rc)); Hc.append(A.ent(pc)); children.append((w/2,fc,rc))
        eq(A.divg(p,rr),add(E,O,mean(Di)),'independent phase chain, no off-support mass dropped')
        chargeD=add(E,O,mean(Z)); eq(A.divg(p,rr),add(chargeD,mean(Dc)),'independent source mismatch debit')
        chargeCE=add(chargeD,A.ent(p),mul(mean(Hc),-1)); eq(A.cross(p,rr),add(chargeCE,mean(Cc)),'independent entropy-source debit')
        refundD=add(refundD,mul(chargeD,w)); spendCE=add(spendCE,mul(chargeCE,w)); frontier.extend(children)
        leafD=add(*(mul(A.divg(prob(ff),rr),w) for w,ff,rr in frontier)); leafCE=add(*(mul(A.cross(prob(ff),rr),w) for w,ff,rr in frontier))
        eq(initialD,add(refundD,leafD),'EVERY changed unequal frontier uses ORIGINAL mismatch')
        eq(initialCE,add(spendCE,leafCE),'EVERY changed unequal frontier uses ORIGINAL CE')
        queries+=1; snapshots+=1
        if time.perf_counter()-start>180: raise RuntimeError('frozen independent cap')
    return snapshots
roots=0; snapshots=0
for table in range(16):
    f=tuple(1-2*((table>>x)&1) for x in range(4))
    for kind in (0,1): snapshots+=one(f,kind); roots+=1
extra=[tuple(-1 if z==0 else 1 for z in range(2**m)) for m in (3,4,5)]
extra += [tuple((-1)**sum(((z>>(2*j))&3)==3 for j in range(k)) for z in range(4**k)) for k in (2,3)]
for f in extra:
    for kind in (0,1): snapshots+=one(f,kind); roots+=1
A.ck(roots==42,'frozen independent roots')
family_cases=0
for k in (1,2,3):
    N=4**k; f=tuple((-1)**sum(((z>>(2*j))&3)==3 for j in range(k)) for z in range(N)); P=prob(f)
    A.ck(all(x==F(1,N) for x in P),'independent actual bent spectrum')
    r=tuple(F(1,N) if s in (0,1) else F(3 if s%2==0 else 5,4*N) for s in range(N))
    D=A.divg(P,r); eq(D,mul(A.logq(F(16,15)),F(N-2,2*N)),'independent parameterized exact mismatch')
    for eta in (F(1,64),F(1,512)):
        q=[eta*x for x in P]; rr=[eta*x for x in r]; q[0]+=1-eta; rr[0]+=1-eta
        eq(A.divg(q,rr),mul(D,eta),'independent ZERO selector refund despite positive mismatch')
        family_cases+=1
out={'status':'PASS','roots':roots,'family_cases':family_cases,'query_nodes':queries,'frontier_snapshots':snapshots,'positive_calibrations':strict,'assertions':A.count,'seconds':time.perf_counter()-start,'independence':'direct character sums and global-frontier accounting; shared pinned rational-log algebra only; author code, not independent person'}
(Path(__file__).resolve().parents[1]/'out/replay.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
