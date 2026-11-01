"""Exact selective DATA query after one active-only physical CONTROL split."""
from pathlib import Path
from functools import lru_cache
import time,json,sys,math
import arith as A
from exact import fwht
from a022_source import qdata
F=A.F; ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'
ck=A.ck; ge=A.ge; same=A.same; add=A.add; mul=A.scale; const=A.c; mean=A.mean
L3=A.logq(3); L13=A.logq(13); L15=A.logq(15)
def eq(a,b,tag): ck(same(a,b),tag)
@lru_cache(maxsize=2048)
def law(f):
    n=len(f); return tuple(F(w*w,n*n) for w in fwht(f))
def Rlaw(a,d):
    r=[d*p for p in law(tuple(a))]; r[0]+=1-d; return tuple(r)
def J(s,d,w): return add(A.overhead(s,d),mul(A.logq(1-d+d*s*s),1-w))
def stats(f,nd,q,R):
    p=law(tuple(f)); M=2**nd; pd=[sum(p[z*M+s] for z in range(len(R))) for s in range(M)]; pc=[sum(p[z*M:(z+1)*M]) for z in range(len(R))]
    C=add(A.cross(pd,q),A.cross(pc,R)); H=A.ent(p)
    I=sum((p[s]*(s&(M-1)).bit_count() for s in range(len(p))),F(0))
    ge(add(C,mul(H,-1)),'COMPLETE terminal KL, including full joint dependence')
    return C,H,I
def ell_formula(t,v,d,alpha,rho):
    r,j=divmod(d,3); delta=F(1,8**t); w=F(1,2**d); u=(v>>(3*r))&7; pos=j
    sigma=(-1 if u==0 else 1)*(-1 if (u^(1<<pos))==0 else 1)
    c2=add(const(4),mul(L15,-1))
    w1=mul(L13,3) if u&1 else {}
    if j==0:
        base=add(mul(L3,F(9,8)),mul(L13,-F(1,2)))
        jv=mul(L3,-F(7,4) if u==0 else F(5,4))
        first=mul(L13,3) if u&1 else {}
        T=add(const(8*sigma),mul(jv,-4),first)
    elif j==1:
        base=c2 if not u&1 else add(L13,mul(L15,-1))
        T=add(const(8*sigma),mul(w1,-1),mul(L15,2))
    else:
        character=int(u&3==0); base=add(const(4*character),mul(c2,-1))
        T=add(const(8*sigma),mul(L15,-2))
    return mul(add(mul(base,w),mul(T,delta*alpha)),rho)
def loss_bound(t,d):
    r,j=divmod(d,3)
    return F(6,8**t) if j==0 else (F(1,6) if j==1 else (F(1,2) if r==0 else F(1,16)))
def floor_bound(t,d):
    r,j=divmod(d,3)
    if j==0: return F(121*t,576)-F(3,128)
    if j==2 and r==0: return F(139*t,288)+F(17,1152)
    return F(121*t,576)+F(17,1152)
def run(mode):
    start=time.perf_counter(); cases=roots=positive=negative=0; receipts=[]
    vs=range(2) if mode=='pilot' else range(64); depths=(1,2,5) if mode=='pilot' else range(6)
    cap=60 if mode=='pilot' else 600
    t=2; k=6; delta=F(1,64); U=F(t,64); labels0=tuple(range(k))
    seed=[math.prod(-1 if ((x>>(3*b))&7)==0 else 1 for b in range(t)) for x in range(2**k)]
    for v in vs:
        for table in range(16):
            a=tuple(1-2*((table>>z)&1) for z in range(4)); R=Rlaw(a,delta); L=mul(A.ent(law(a)),delta)
            original=tuple(seed[x]*(a[z] if x==v else 1) for z in range(4) for x in range(2**k)); nodes=[(original,())]
            for d in range(6):
                if d in depths:
                    roots+=1; nd=k-d; labels=tuple(range(d,k)); w=F(1,2**d)
                    st=[]; active=None
                    for n,(f,fixed) in enumerate(nodes):
                        q=qdata(t,labels,fixed); st.append(stats(f,nd,q,R))
                        if all(((v>>i)&1)==b for i,b in fixed): active=n
                    Cp=mean([z[0] for z in st]); Hp=mean([z[1] for z in st]); Ip=sum(z[2] for z in st)/len(st)
                    Bp=add(const(4*Ip-U),L,mul(Cp,-1)); ge(add(Bp,const(-floor_bound(t,d))),'stronger SAME unused source floor')
                    parent,fixed=nodes[active]; q=qdata(t,labels,fixed); C0,H0,I0=st[active]
                    for i in ((0,) if mode=='pilot' else (0,1)):
                        ac=[A.cut(a,i,b) for b in (0,1)]; Rs=[Rlaw(ab,delta) for ab in ac]
                        fc=[A.cut(parent,nd+i,b) for b in (0,1)]; sc=[stats(fc[b],nd,q,Rs[b]) for b in (0,1)]
                        Cctl=add(Cp,mul(add(mean([z[0] for z in sc]),mul(C0,-1)),w))
                        Hctl=add(Hp,mul(add(mean([z[1] for z in sc]),mul(H0,-1)),w)); Ictl=Ip+w*(sum(z[2] for z in sc)/2-I0)
                        Lctl=mul(mean([A.ent(law(ab)) for ab in ac]),delta)
                        Bctl=add(const(4*Ictl-U),Lctl,mul(Cctl,-1)); Gamma=add(Bctl,mul(Bp,-1))
                        gamma=add(J(F(sum(a),4),delta,w),mul(mean([J(F(sum(ab),2),delta,w) for ab in ac]),-1))
                        eq(Gamma,gamma,'original A021 Jensen gain retained'); ge(Gamma,'old actual control credit')
                        ck(Ictl==Ip,'control step preserves remaining DATA influence')
                        Ectl=add(L,mul(Lctl,-1),mul(Hp,-1),Hctl)
                        for b in ((0,) if mode=='pilot' else (0,1)):
                            childfixed=[tuple(sorted(fixed+((d,val),))) for val in (0,1)]
                            fd=[A.cut(fc[b],0,val) for val in (0,1)]
                            sd=[stats(fd[val],nd-1,qdata(t,tuple(range(d+1,k)),childfixed[val]),Rs[b]) for val in (0,1)]
                            reach=w/2; Ca=add(Cctl,mul(add(mean([z[0] for z in sd]),mul(sc[b][0],-1)),reach))
                            Ha=add(Hctl,mul(add(mean([z[1] for z in sd]),mul(sc[b][1],-1)),reach)); Ia=Ictl+reach*(sum(z[2] for z in sd)/2-sc[b][2])
                            Ba=add(const(4*Ia-U),Lctl,mul(Ca,-1)); ell=add(Bctl,mul(Ba,-1))
                            expected=ell_formula(t,v,d,F(1,2)-F(sum(ac[b]),4),F(1,2))
                            eq(ell,expected,'exact selected-leaf local capacity charge')
                            ge(add(const(loss_bound(t,d)),mul(ell,-1)),'local phase-dependent charge bound')
                            ge(add(Ba,mul(Gamma,-1),const(-F(13*t,576))),'SAME original reserve plus prior Gamma retained')
                            piv=reach*A.physical(fc[b],0); ck(Ictl-Ia==piv,'actual selective physical edge influence')
                            Edata=add(const(4*piv),mul(Hctl,-1),Ha)
                            eq(add(Ba,Ca,mul(Ha,-1),Ectl,Edata),add(Bp,Cp,mul(Hp,-1)),'old source spend and BOTH full terminal KL/history')
                            lo,hi=A.bounds(ell); positive+=lo>0; negative+=hi<0
                            if v==0 and table==10 and i==0 and b==0 and d==2:
                                eq(ell,mul(L15,F(1,8)),'constant-cost rare-event family witness')
                                receipts.append({'t':t,'v':v,'depth':d,'control_table':table,'selected_outcome':b,'rho':str(F(1,2)),'w':str(w),'charge':{str(p):str(x) for p,x in A.reduce_logs(ell).items()}})
                            cases+=1
                    if roots%64==0:
                        (OUT/(mode+'_checkpoint.json')).write_text(json.dumps({'roots':roots,'cases':cases,'assertions':A.count,'seconds':time.perf_counter()-start}),encoding='utf-8')
                    if time.perf_counter()-start>cap: raise RuntimeError('frozen cap')
                if d<5: nodes=[(A.cut(f,0,b),fixed+((d,b),)) for f,fixed in nodes for b in (0,1)]
    out={'status':'PASS','mode':mode,'roots':roots,'cases':cases,'assertions':A.count,'positive_charges':positive,'negative_charges':negative,'seconds':time.perf_counter()-start,'constant_family_receipts':receipts}
    (OUT/(mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='constant_family_receipts'}))
if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('pilot','main'): raise SystemExit('usage: check.py pilot|main')
    run(sys.argv[1])
