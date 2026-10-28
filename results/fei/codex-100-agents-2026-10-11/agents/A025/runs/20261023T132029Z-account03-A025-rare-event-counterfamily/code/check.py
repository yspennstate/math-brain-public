"""Frozen exact actual-controller histories; full phase and calibration KL."""
from pathlib import Path
from functools import lru_cache
import json,time,sys
import arith as A
F=A.F; add=A.add; mul=A.scale; c=A.c; mean=A.mean
ROOT=Path(__file__).resolve().parents[1]; count_nodes=0; positive_calibrations=0; receipts=[]
def eq(x,y,tag): A.ck(A.same(x,y),tag)
def fwht(f):
    f=list(f); step=1
    while step<len(f):
        for a in range(0,len(f),2*step):
            for j in range(a,a+step):
                u,v=f[j],f[j+step]; f[j],f[j+step]=u+v,u-v
        step*=2
    return f
@lru_cache(maxsize=2048)
def amplitudes(f): return tuple(F(v,len(f)) for v in fwht(f))
def law(f): return tuple(x*x for x in amplitudes(tuple(f)))
def cut(f,i,b): return tuple(v for x,v in enumerate(f) if (x>>i)&1==b)
def clamp(P,r):
    p,q=P[0],r[0]
    if p==1: return tuple([F(1)]+[F(0)]*(len(P)-1))
    A.ck(q<1,'finite child reference has nonempty support')
    return tuple([p]+[(1-p)*x/(1-q) for x in r[1:]])
def original(P,profile):
    p=P[0]; N=len(P)
    if p==1: return P
    nu=([F(1,N-1)]*(N-1)) if profile==0 else ([F(1)]+[F(0)]*(N-2))
    q=[p]+[(1-p)*x for x in nu]
    return tuple((x+y)/2 for x,y in zip(P,q))
def serial(e): return {str(k):str(v) for k,v in A.reduce_logs(e).items()}
def walk(f,r,prefix=()):
    global count_nodes,positive_calibrations
    P=law(f); D=A.divg(P,r); CE=A.cross(P,r)
    A.ge(D,'complete calibrated source KL')
    A.ck(P[0]==r[0],'EVERY actual leaf vacuum calibrated')
    n=len(f).bit_length()-1
    if n==0: return D,CE,{},{}
    i=0 if sum(prefix)%2==0 else n-1
    aa=amplitudes(f); pairs=[(s,s|(1<<i)) for s in range(len(f)) if not s&(1<<i)]
    pp=[P[s]+P[t] for s,t in pairs]; rr=[r[s]+r[t] for s,t in pairs]
    E=add(D,mul(A.divg(pp,rr),-1)); A.ge(E,'actual erasure E')
    rhos=[]; children=[]; Z=[]; inherited=[]
    for b in (0,1):
        joint=[]
        for s,t in pairs:
            den=aa[s]**2+aa[t]**2
            prob=(aa[s]+(-1)**b*aa[t])**2/(2*den) if den else F(1,2)
            joint.append((r[s]+r[t])*prob)
        rho=sum(joint); A.ck(rho>0,'actual positive reference outcome'); rhos.append(rho)
        fc=cut(f,i,b); pc=law(fc); rin=tuple(x/rho for x in joint); rc=clamp(pc,rin)
        z=A.divg([pc[0],1-pc[0]],[rin[0],1-rin[0]])
        di=A.divg(pc,rin); dc=A.divg(pc,rc)
        eq(di,add(z,dc),'KL disintegration with BOTH full child debts')
        A.ge(z,'vacuum calibration releases exact signed refund')
        positive_calibrations+=A.bounds(z)[0]>0
        children.append((fc,rc)); Z.append(z); inherited.append(di)
    O=A.divg([F(1,2)]*2,rhos); A.ge(O,'actual outcome O'); A.ck(sum(rhos)==1,'normalized propagated reference')
    nextD=mean([A.divg(law(fc),rc) for fc,rc in children]); credit=add(E,O,mean(Z))
    eq(D,add(credit,nextD),'full phase+calibration source contraction')
    DH=add(A.ent(P),mul(mean([A.ent(law(fc)) for fc,rc in children]),-1)); A.ge(DH,'actual controller entropy decrement')
    nextCE=mean([A.cross(law(fc),rc) for fc,rc in children]); sourcecredit=add(DH,credit)
    eq(CE,add(sourcecredit,nextCE),'single ORIGINAL source CE decrement')
    count_nodes+=1
    after=[walk(fc,rc,prefix+(b,)) for b,(fc,rc) in enumerate(children)]
    leafD=mean([x[0] for x in after]); leafCE=mean([x[1] for x in after]); spentD=add(credit,mean([x[2] for x in after])); spentCE=add(sourcecredit,mean([x[3] for x in after]))
    eq(D,add(spentD,leafD),'all adaptive terminal KLs + original mismatch credits')
    eq(CE,add(spentCE,leafCE),'all original entropy spend + full terminal CE')
    if len(receipts)<3 and A.bounds(mean(Z))[0]>0:
        receipts.append({'actual_function':list(f),'query_index':i,'reference_outcomes':list(map(str,rhos)),'vacuum_refunds':[serial(x) for x in Z],'both_inherited_KL':[serial(x) for x in inherited],'both_target_KL':[serial(A.divg(law(fc),rc)) for fc,rc in children]})
    return leafD,leafCE,spentD,spentCE
def main(mode):
    start=time.perf_counter(); roots=0
    for table in range(16 if mode=='pilot' else 256):
        f=tuple(1-2*((table>>x)&1) for x in range(8)); P=law(f)
        for profile in (0,1):
            r=original(P,profile); D=A.divg(P,r); var=1-P[0]; infl=sum(A.physical(f,i) for i in range(3))
            A.ge(add(c(var),mul(D,-1)),'one ORIGINAL mismatch <=Var')
            A.ck(var<=infl,'actual Boolean Poincare by physical edges')
            walk(f,r); roots+=1
            if time.perf_counter()-start>(60 if mode=='pilot' else 300): raise RuntimeError('frozen runtime cap')
    A.ck(roots==(32 if mode=='pilot' else 512),'frozen roots')
    A.ck(count_nodes==(224 if mode=='pilot' else 3584),'frozen phase query nodes')
    result={'status':'PASS','mode':mode,'roots':roots,'query_nodes':count_nodes,'positive_calibrations':positive_calibrations,'assertions':A.count,'seconds':time.perf_counter()-start,'receipts':receipts}
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in result.items() if k!='receipts'}))
def family():
    start=time.perf_counter(); rows=[]
    for k in range(1,5):
        N=4**k; f=tuple((-1)**sum(((z>>(2*j))&3)==3 for j in range(k)) for z in range(N)); P=law(f)
        A.ck(P==tuple([F(1,N)]*N),'actual bent tensor Fourier law')
        infl=sum(A.physical(f,i) for i in range(2*k)); A.ck(infl==k,'actual bent tensor physical influence')
        eq(A.ent(P),c(2*k),'actual H/I=2')
        r=tuple(F(1,N) if s<2 else (F(3,4*N) if s%2==0 else F(5,4*N)) for s in range(N))
        A.ck(sum(r)==1 and r[0]==P[0],'calibrated normalized dominated source')
        A.ck(all(y>=x/2 for x,y in zip(P,r)),'original half-smoothing admissibility')
        D=A.divg(P,r); formula=mul(A.logq(F(16,15)),F(N-2,2*N)); eq(D,formula,'parameterized exact mismatch')
        for eta in (F(1,64),F(1,512),F(1,8),F(1)):
            mp=[eta*x for x in P]; mr=[eta*x for x in r]; mp[0]+=1-eta; mr[0]+=1-eta
            output=A.divg(mp,mr); eq(output,mul(D,eta),'nonempty mismatch ENTIRELY survives selector erasure')
            A.ge(add(D,mul(A.logq(F(16,15)),-F(1,4))),'uniform positive profile mismatch')
            rows.append({'k':k,'eta':str(eta),'D_source':serial(D),'D_output':serial(output),'selector_refund':{}})
    result={'status':'PASS','cases':len(rows),'assertions':A.count,'seconds':time.perf_counter()-start,'witnesses':rows}
    (ROOT/'out/family.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in result.items() if k!='witnesses'}))
if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('pilot','main','family'): raise SystemExit('usage: check.py pilot|main|family')
    family() if sys.argv[1]=='family' else main(sys.argv[1])
