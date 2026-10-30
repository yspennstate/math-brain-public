from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
import exact as e

RUN=Path(__file__).resolve().parents[1]
ROOT=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
def save(name,x):
    (RUN/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def ck(x):e.ck(x)
@lru_cache(None)
def coeff(v):return e.fw(v)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def truth(a,h,s):return tuple(x+s*(1-x*x)*y for y in h for x in a)
def coherent(a,h,r,s):
    A=coeff(a);B=coeff(tuple(1-x*x for x in a));m=F(sum(h),len(h))
    ck(r[0]==m*m)
    q=tuple((A[u]+s*m*B[u])**2 if t==0 else B[u]**2*r[t] for t in range(len(h)) for u in range(len(a)))
    ck(sum(q)==1 and min(q)>=0)
    return q
def cal(r,z):
    if z==1:return (F(1),)+(F(0),)*(len(r)-1)
    ck(r[0]<1)
    return (z,)+tuple((1-z)*v/(1-r[0]) for v in r[1:])
def coarse(p,N):return p[:N]+(sum(p[N:]),)
def profile(N):
    if N==0:return ()
    return tuple(F(i+1,N*(N+1)//2) for i in range(N))
def references(h):
    p=e.spec(h);a=1-p[0]
    if not a:return [p]*3
    return [p]+[(p[0],)+tuple((p[t]+a*w)/2 for t,w in enumerate(v,1)) for v in [tuple(F(1,len(p)-1) for _ in p[1:]),profile(len(p)-1)]]

def review(a,h,r,s,j,logs):
    A=coeff(a);B=coeff(tuple(1-v*v for v in a));beta=dot(B,B)
    C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B));E=sum(y**4 for y in B)
    Gamma=C-D*D/E if E else F(0)
    ck(Gamma>=0)
    m=F(sum(h),len(h));d=coeff(h)[1<<j];delta=r[1<<j]-d*d
    fm=sum(y*y*(s*x+m*y)**2 for x,y in zip(A,B))
    ck(fm>=Gamma)
    x=Gamma*d*d+(E+beta*beta)*delta*delta/4
    xe=d*d*(fm+beta*beta*m*m)+(E+beta*beta)*delta*delta/4
    v=truth(a,h,s);p=e.spec(v);q=coherent(a,h,r,s)
    J=len(a).bit_length()-1+j;qb=e.marginal(q,J);pb=e.marginal(p,J)
    cq=coarse(qb,len(a));coarses=[];ces=[];refunds=[]
    for bit in (0,1):
        hh=e.restrict(h,j,bit);vv=truth(a,hh,s);pp=e.spec(vv)
        ck(vv==e.restrict(v,J,bit))
        z=F(sum(hh),len(hh))**2;rr=cal(e.marginal(r,j),z);qq=coherent(a,hh,rr,s)
        cp=coarse(pp,len(a));coarses.append(cp)
        for k,(mass,old) in enumerate(zip(cp,cq)):
            if mass:ck(old>0)
        ck(all((coarses[0][k]+cp[k])/2==coarse(pb,len(a))[k] for k in range(len(cp))) if bit else True)
        # Verify full calibration by multiplying old atoms blockwise.
        expect=tuple(cp[t]/cq[t]*qb[t] if t<len(a) and cq[t] else F(0) if t<len(a) else cp[-1]/cq[-1]*qb[t] if cq[-1] else F(0) for t in range(len(qb)))
        ck(expect==qq)
        tail=beta*(1-z);eps=x/(tail+x) if tail and x else F(0)
        if tail and eps:
            tar=profile(len(hh)-1);old=tuple(w/(1-z) for w in rr[1:]);new=tuple((1-eps)*w+eps*t for w,t in zip(old,tar))
            ck(sum(new)==1 and all(vv>0 for vv,w in zip(new,old) if w))
            ck(tail*eps/(1-eps)==x)
        if logs:
            k=e.KL(cp,cq)
            ck(e.add((1,e.CE(pp,qb)),(-1,e.CE(pp,qq)))==k)
            refunds.append(k);ces.append(e.CE(pp,qq))
    direct=sum(sum((u-vv)**2 for u,vv in zip(cp,cq)) for cp in coarses)/2
    ck(direct==4*xe and direct>=4*x)
    if logs:
        rho=e.add((1,e.KL(p,q)),(-1,e.KL(pb,qb)))
        inc=e.add((1,e.B(p,J)),*[(F(1,2),v) for v in ces],(-1,e.CE(p,q)))
        ck(inc==e.add((-1,rho),*[(F(-1,2),k) for k in refunds]))
        ck(not inc or e.bounds(inc)[1]<=0)
    return x

def nullstep(h,r,j):
    p=e.spec(h);c=coeff(h);m=c[0];a0=1-m*m
    ck(c[1<<j]==0 and r[1<<j]==0)
    ck(all(c[e.insert(t,j)]*c[e.insert(t,j)|(1<<j)]==0 for t in range(len(h)//2)))
    pb=e.marginal(p,j);rb=e.marginal(r,j)
    ck(pb[0]==rb[0]==m*m and a0>0)
    pi=tuple(z/a0 for z in pb[1:]);M=tuple(z/a0 for z in rb[1:])
    delta=sum(abs(x-y) for x,y in zip(pi,M))/2
    W=F(0)
    for t,pt in enumerate(pb):
        if pt:
            ck(rb[t]>0)
            v=e.insert(t,j)|(1<<j)
            W+=pt*(p[v]/pt-r[v]/rb[t])**2
    eta=delta*delta+W/a0
    ck((eta==0)==(r==p))
    bins=[tuple(k for k in range(len(pi)) if pi[k]>M[k]),tuple(k for k in range(len(pi)) if pi[k]<=M[k])]
    Pmass=tuple(sum(pi[k] for k in b) for b in bins);Rmass=tuple(sum(M[k] for k in b) for b in bins)
    ck(Pmass[0]-Rmass[0]==delta)
    out=[F(0)]*len(pi)
    for b,pa,ra in zip(bins,Pmass,Rmass):
        if pa:
            ck(ra>0)
            for k in b:out[k]=pa*M[k]/ra
    rc=(m*m,)+tuple(a0*x for x in out)
    ck(sum(rc)==1)
    rho=e.add((1,e.KL(p,r)),(-1,e.KL(pb,rb)))
    kk=e.add((1,e.CE(pb,rb)),(-1,e.CE(pb,rc)))
    ck(kk==e.add((a0,e.KL(Pmass,Rmass))))
    return eta,W,delta,rc,rho,kk

def run(pilot):
    start=time.perf_counter();before=e.COUNT
    seeds=[tuple(1 if mask>>t&1 else -1 for t in range(1<<n)) for n in range(3) for mask in range(1<<(1<<n))]
    if not pilot:
        seeds += [tuple((-1)**((s&t).bit_count()) for t in range(8)) for s in range(8)]
        seeds += [tuple(-1 if t==0 else 1 for t in range(8)),tuple(1 if t.bit_count()<=1 else -1 for t in range(8))]
        seeds += [tuple(-1 if t in (0,1,2,4) else 1 for t in range(16))]
    controllers=[ROOT,e.restrict(ROOT,0,0),(1,),(-1,),(0,)]
    if pilot:controllers=[ROOT,(1,),(-1,),(0,)]
    wrappers=queries=logqueries=0
    for h in seeds:
        # Independent direct character sums, not a second FWHT.
        direct=tuple(F(sum(v*(-1)**((u&t).bit_count()) for t,v in enumerate(h)),len(h)) for u in range(len(h)))
        ck(direct==coeff(h))
        p=e.spec(h);ck(sum(p)==1)
        ck(e.inf(h)==sum(F(t.bit_count())*v for t,v in enumerate(p)))
        Hplus=e.add(*[(-v,e.logq(v)) for v in p[1:] if v]);vac=e.add((-p[0],e.logq(p[0]))) if p[0] else {}
        ck(e.H(p)==e.add((1,Hplus),(1,vac)))
        for a in controllers:
            for r in references(h):
                for s in (-1,1):
                    wrappers+=1
                    for j in range(len(h).bit_length()-1):
                        logs=len(a)==1
                        review(a,h,r,s,j,logs);queries+=1;logqueries+=int(logs)
                    ck(time.perf_counter()-start<55)
    # Fixed-strength new target, both physically nonconstant terminals.
    h=tuple((-1)**t.bit_count() for t in range(8));p=e.spec(h);rows=[]
    for atom in (7,6,3):
        r=tuple((p[t]+F(t==atom))/2 for t in range(8))
        eta,W,delta,rc,rhoseed,kseed=nullstep(h,r,0)
        ck(eta==(0 if atom==7 else F(1,4)))
        ck(W==(F(1,4) if atom==6 else 0))
        ck(delta==(F(1,2) if atom==3 else 0))
        for s in (-1,1):
            v=truth(ROOT,h,s);P=e.spec(v);Q=coherent(ROOT,h,r,s);J=4
            marg=e.marginal(Q,J);pm=e.marginal(P,J)
            rho=e.add((1,e.KL(P,Q)),(-1,e.KL(pm,marg)))
            beta=F(3,8);ck(rho==e.add((beta,rhoseed)))
            targets=[tuple(F(i==k) for i in range(1,4)) for k in range(1,4)]+[profile(3)]
            for target in targets:
                ces=[];costs=[];kk=[]
                for bit in (0,1):
                    hh=e.restrict(h,0,bit);PP=e.spec(truth(ROOT,hh,s));calQ=coherent(ROOT,hh,rc,s)
                    ck(e.spec(hh)==e.marginal(p,0))
                    k=e.add((1,e.CE(PP,marg)),(-1,e.CE(PP,calQ)))
                    ck(k==e.add((beta,kseed)));kk.append(k)
                    rn=(F(0),)+tuple(F(63,64)*rc[t]+F(1,64)*target[t-1] for t in range(1,4))
                    Qn=coherent(ROOT,hh,rn,s);ces.append(e.CE(PP,Qn))
                    costs.append(e.add((1,e.CE(PP,Qn)),(-1,e.CE(PP,calQ))))
                inc=e.add((1,e.B(P,J)),*[(F(1,2),ce) for ce in ces],(-1,e.CE(P,Q)))
                ck(inc==e.add((-1,rho),*[(F(-1,2),k) for k in kk],*[(F(1,2),z) for z in costs]))
                ck(e.B(P,J)=={})
                disjoint=target[2]==0
                if atom!=7:ck(e.bounds(inc)[1]<-F(93,256))
                elif disjoint:ck(e.bounds(inc)[0]>0)
                else:ck(e.bounds(inc)[0]>=0)
                rows.append({'reference_extra_atom':atom,'sigma':s,'target':[str(t) for t in target],'eta':str(eta),'W':str(W),'delta':str(delta),'occupancy_refund':e.rec(rho),'calibration_refund':e.rec(kk[0]),'complete_increment':e.rec(inc),'criterion_fixed_1_64':eta>=F(1,63)})
    ck(64**32<2*63**32)
    # Guard positive and negative controls are really visited.
    ck(len(rows)==24 and sum(r['criterion_fixed_1_64'] for r in rows)==16)
    A=coeff(ROOT);B=coeff(tuple(1-v*v for v in ROOT));E=dot(tuple(v*v for v in B),tuple(v*v for v in B));C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B))
    ck(E==F(21,512) and C-D*D/E==F(9,3584) and (E+F(3,8)**2)/4==F(93,2048))
    out={'status':'PASS','pilot':pilot,'assertions':e.COUNT-before,'seconds':time.perf_counter()-start,'seeds':len(seeds),'wrappers':wrappers,'query_cases':queries,'exact_log_ledger_cases':logqueries,'new_fixed_strength_histories':len(rows),'funded_histories':16,'unfunded_exact_source_controls':8,'rows':rows,'scope':'Independent A003 reconstruction and new all-dimensional written proof; finite validation not FEI or kernel certification.'}
    save('PILOT.json' if pilot else 'CHECK.json',out)
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':run('--pilot' in sys.argv)
