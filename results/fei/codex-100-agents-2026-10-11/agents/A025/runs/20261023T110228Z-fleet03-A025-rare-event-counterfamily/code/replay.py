"""Independent direct DFT, physical edges, explicit two-step phase channels.

No production search/formula/reference imports. Shared pinned rational log algebra only.
"""
from functools import lru_cache
from pathlib import Path
import time,json,math
import arith as A
F=A.F; add=A.add; mul=A.scale; c=A.c; mean=A.mean
start=time.perf_counter(); receipts=[]; phases=0
def eq(a,b,label): A.ck(A.same(a,b),label)
@lru_cache(maxsize=2048)
def amps(f):
    return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f)))
def law(f): return tuple(v*v for v in amps(tuple(f)))
def cut(f,i,b): return tuple(v for x,v in enumerate(f) if (x>>i)&1==b)
def physical(f,i): return F(sum(v!=f[x^(1<<i)] for x,v in enumerate(f)),len(f))
def ref(a,delta):
    q=[delta*p for p in law(a)]; q[0]+=1-delta; return tuple(q)
def qdata(t,d,h):
    out=[]
    for s in range(2**(3*t-d)):
        q=F(1)
        for k in range(t):
            fixed=[(h>>i)&1 for i in range(3*k,min(d,3*k+3))]
            free=list(range(max(d,3*k),3*k+3)); mark=sum(((s>>(i-d))&1)<<j for j,i in enumerate(free))
            if len(fixed)==0: q*=F(9 if mark==0 else 1,16)
            elif len(fixed)==1: q*=F(1,4) if fixed[0]==0 else F(13 if mark==0 else 1,16)
            elif len(fixed)==2: q*=F(15 if mark==int(not any(fixed)) else 1,16)
        out.append(q)
    return tuple(out)
def target(q,R): return tuple(r*v for r in R for v in q)
def stat(f,nd,T):
    p=law(f); H=A.ent(p); C=A.cross(p,T); I=sum(physical(f,i) for i in range(nd))
    A.ge(add(C,mul(H,-1)),'independent complete terminal KL')
    return C,H,I
def phase(f,i,T,targets,label):
    global phases
    aa=amps(f); P=law(f); pairs=[(s,s|(1<<i)) for s in range(len(f)) if not (s>>i)&1]
    pp=[P[s]+P[t] for s,t in pairs]; rr=[T[s]+T[t] for s,t in pairs]
    E=add(A.divg(P,T),mul(A.divg(pp,rr),-1)); A.ge(E,'actual erasure refund')
    rhos=[]; inh=[]; tar=[]; kap=[]
    for b in (0,1):
        jj=[]
        for s,t in pairs:
            den=aa[s]**2+aa[t]**2
            prob=(aa[s]+(-1)**b*aa[t])**2/(2*den) if den else F(1,2)
            jj.append((T[s]+T[t])*prob)
        rho=sum(jj); A.ck(rho>0,'reference actual branch normalization'); rhos.append(rho)
        child=law(cut(f,i,b)); inh.append(A.divg(child,[x/rho for x in jj])); tar.append(A.divg(child,targets[b])); kap.append(add(tar[-1],mul(inh[-1],-1)))
    A.ck(sum(rhos)==1,'complete phase reference including off true support')
    O=A.divg([F(1,2)]*2,rhos); A.ge(O,'actual outcome refund')
    eq(A.divg(P,T),add(E,O,mean(inh)),'both inherited KLs exact physical phase chain')
    eq(add(mean(kap),mul(E,-1),mul(O,-1)),add(mean(tar),mul(A.divg(P,T),-1)),'signed conversion with BOTH target debts')
    phases+=1
    return {'query':label,'reference_outcomes':list(map(str,rhos)),'erasure':serial(E),'outcome_refund':serial(O),'both_inherited_KL':[serial(x) for x in inh],'both_target_KL':[serial(x) for x in tar],'net_conversion':serial(add(mean(kap),mul(E,-1),mul(O,-1)))}
def serial(e): return {str(k):str(v) for k,v in A.reduce_logs(e).items()}
def fixture(t,v,d,a,b,keep=False):
    delta=F(1,8**t); w=F(1,2**d); nd=3*t-d; R=ref(a,delta); L=mul(A.ent(law(a)),delta)
    rows=[]; root=[]
    for h in range(2**d):
        f=[]
        for z in range(len(a)):
            for y in range(2**nd):
                x=h+(y<<d); seed=(-1)**sum(((x>>(3*k))&7)==0 for k in range(t))
                f.append(seed*(a[z] if x==v else 1))
        f=tuple(f); T=target(qdata(t,d,h),R); rows.append((f,T)); root.append(stat(f,nd,T))
    C,H=mean([x[0] for x in root]),mean([x[1] for x in root]); I=sum(x[2] for x in root)/len(root)
    B=add(c(4*I-F(t,64)),L,mul(C,-1)); h=v%2**d; f,T=rows[h]; cp,hp,ip=root[h]
    ac=[cut(a,0,u) for u in (0,1)]; fc=[cut(f,nd,u) for u in (0,1)]; Rc=[ref(x,delta) for x in ac]
    Tc=[target(qdata(t,d,h),r) for r in Rc]; sc=[stat(fc[u],nd,Tc[u]) for u in (0,1)]
    CC=add(C,mul(add(mean([x[0] for x in sc]),mul(cp,-1)),w)); HC=add(H,mul(add(mean([x[1] for x in sc]),mul(hp,-1)),w))
    IC=I+w*(sum(x[2] for x in sc)/2-ip); LC=mul(mean([A.ent(law(x)) for x in ac]),delta)
    BC=add(c(4*IC-F(t,64)),LC,mul(CC,-1)); Gamma=add(BC,mul(B,-1)); A.ge(Gamma,'old active-only controller gain')
    Ectl=add(L,mul(LC,-1),HC,mul(H,-1))
    td=[target(qdata(t,d+1,h+(u<<d)),Rc[b]) for u in (0,1)]; fd=[cut(fc[b],0,u) for u in (0,1)]; sd=[stat(fd[u],nd-1,td[u]) for u in (0,1)]
    reach=w/2; CA=add(CC,mul(add(mean([x[0] for x in sd]),mul(sc[b][0],-1)),reach)); HA=add(HC,mul(add(mean([x[1] for x in sd]),mul(sc[b][1],-1)),reach))
    IA=IC+reach*(sum(x[2] for x in sd)/2-sc[b][2]); BA=add(c(4*IA-F(t,64)),LC,mul(CA,-1)); ell=add(BC,mul(BA,-1))
    A.ge(add(BA,mul(Gamma,-1),c(-F(13*t,576))),'independent same original reserve')
    piv=reach*physical(fc[b],0); A.ck(IC-IA==piv,'independent physical selective DATA influence')
    Edata=add(c(4*piv),HA,mul(HC,-1))
    eq(add(BA,CA,mul(HA,-1),Ectl,Edata),add(B,C,mul(H,-1)),'all terminal debts and full signed history retained')
    oldphase=phase(f,nd,T,Tc,'CONTROL'); newphase=phase(fc[b],0,Tc[b],td,'selected DATA')
    if v==0 and d==2 and all(x==1 for x in ac[b]):
        eq(ell,mul(A.logq(15),F(1,8)),'constant charge exact independent reconstruction')
    if keep: receipts.append({'t':t,'v':v,'depth':d,'controller':list(a),'selected_outcome':b,'leaf_reach':str(reach),'child_reaches':[str(reach/2)]*2,'charge':serial(ell),'old_control':oldphase,'new_DATA':newphase})
controllers=[tuple(1 for _ in range(8)),tuple(-1 for _ in range(8)),tuple(-1 if z==0 else 1 for z in range(8)),tuple(-1 if z.bit_count()>=2 else 1 for z in range(8)),tuple((-1)**z.bit_count() for z in range(8)),tuple(-1 if z in (0,2,3,7) else 1 for z in range(8))]
cases=0
for v in (0,63):
    for d in (1,2,5):
        for a in controllers:
            for b in (0,1):
                fixture(2,v,d,a,b,keep=(v==0 and d==2)); cases+=1
                if time.perf_counter()-start>180: raise RuntimeError('frozen replay cap')
for a in (controllers[2],controllers[4]):
    for b in (0,1): fixture(3,0,5,a,b,keep=True); cases+=1
A.ck(cases==76,'frozen independent domain')
out={'status':'PASS','cases':cases,'phase_queries':phases,'assertions':A.count,'seconds':time.perf_counter()-start,'receipts':receipts}
(Path(__file__).resolve().parents[1]/'out/replay.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='receipts'}))
