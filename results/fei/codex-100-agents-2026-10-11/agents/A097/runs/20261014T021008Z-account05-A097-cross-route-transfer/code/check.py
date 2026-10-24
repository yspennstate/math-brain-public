from pathlib import Path
from fractions import Fraction as R
from functools import lru_cache
from collections import defaultdict
import json,time,sys

BASE=Path(__file__).resolve().parents[1]; COUNT=0; GRID=1<<90
def require(x):
    global COUNT
    assert x
    COUNT+=1
def lnunit(x):
    z=(x-1)/(x+1); zz=z*z; power=z; total=R(0)
    for j in range(32):
        total+=2*power/(2*j+1); power*=zz
    return total,total+2*power/(65*(1-zz))
L2,U2=lnunit(R(2))
@lru_cache(None)
def logs(x):
    require(x>0)
    j=x.numerator.bit_length()-x.denominator.bit_length()
    scale=R(2)**j
    if x<scale: j-=1; scale/=2
    y=x/scale; require(1<=y<2)
    lo,hi=lnunit(y); lo=R(j)+lo/U2; hi=R(j)+hi/L2
    lower=(lo*GRID).__floor__(); upper=(hi*GRID).__ceil__()
    return R(lower,GRID),R(upper,GRID)
def ce(p,q):
    groups=defaultdict(R)
    for a,b in zip(p,q):
        if a: require(b>0); groups[b]+=a
    lo=hi=R(0)
    for q,w in groups.items():
        a,b=logs(q); lo-=w*b; hi-=w*a
    return lo,hi
def ent_groups(groups):
    lo=hi=R(0)
    for p,mult in groups:
        if not p or not mult: continue
        a,b=logs(p); lo-=p*mult*b; hi-=p*mult*a
    return lo,hi
def walsh(t):
    w=list(t); step=1
    while step<len(w):
        for start in range(0,len(w),2*step):
            for j in range(start,start+step):
                a,b=w[j],w[j+step]; w[j],w[j+step]=a+b,a-b
        step*=2
    return [R(x,len(w)) for x in w]
def infl(t):
    return [R(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t)) for i in range((len(t)-1).bit_length())]
def tables(k,m):
    n=k+m
    g=[(-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2)) for x in range(1<<n)]
    h=list(g); h[0]=-h[0]
    return g,h,g+h
def save(name,out):
    (BASE/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
def cutoff(start):
    if time.perf_counter()-start>55: raise RuntimeError('Frozen internal cutoff reached; no completion credited')

def compressed():
    start=time.perf_counter(); results=[]; K=R(17,8)
    for k in (4,6,8,10):
        for m in range(33):
            cutoff(start); n=k+m; d=R(1,1<<n); e=R(1,1<<(k//2)); size=1<<k; total=1<<n
            gh=[]; gm=[]
            for sigma in (1,-1):
                count=(size+sigma*(1<<(k//2)))//2
                gh.append(((sigma*e-2*d)**2,count))
                gm.append(((sigma*e-d)**2,count))
            gh.append((4*d*d,total-size))
            gm.extend([(d*d,total),(d*d,total-size)])
            require(sum(p*c for p,c in gh)==1 and sum(p*c for p,c in gm)==1)
            hh=ent_groups(gh); hm=ent_groups(gm)
            avgI=R(k,2)+n*d; rootI=avgI+d
            delta=(hm[0]-(k+hh[1])/2,hm[1]-(k+hh[0])/2)
            bank=(K*avgI-(k+hh[1])/2,K*avgI-(k+hh[0])/2)
            require(delta[1]<=(n+2+3/U2)*d)
            require(hh[1]-k<=R(k,1)/(1<<k)+R(2,1)/(1<<k)+R(1,(1<<k))*1/L2)
            require(bank[0]>(delta[1]-K*d))
            require(K*rootI-hm[1]>R(1,64))
            if k==4 and n>=22:
                proof=d*(2*n-42-4*n*R(16,1<<n))
                require(proof>0 and hm[0]-2*rootI>=proof)
            if k in (4,6) and m<=2:
                g,h,t=tables(k,m); a,b,c=walsh(g),walsh(h),walsh(t)
                require(all(y==x-2*d for x,y in zip(a,b)))
                require(sum(infl(g))==R(k,2))
                require(sum(infl(h))==R(k,2)+2*n*d)
                require(sum(infl(t))==rootI)
                # Compare probability multisets to independently derived four count types.
                actual=defaultdict(int); expected=defaultdict(int)
                for x in c: actual[x*x]+=1
                for p,cnt in gm: expected[p]+=cnt
                require(dict(actual)==dict(expected))
            results.append(dict(k=k,m=m,n=n,root_I=str(rootI),H_interval=[str(x) for x in hm],price17over8_margin_interval=[str(K*rootI-hm[1]),str(K*rootI-hm[0])],price2_margin_interval=[str(2*rootI-hm[1]),str(2*rootI-hm[0])]))
    require(len(results)==132)
    out=dict(status='PASS',cases=132,assertions=COUNT,seconds=time.perf_counter()-start,results=results)
    save('COMPRESSED_RESULTS.json',out)
    print(json.dumps({k:v for k,v in out.items() if k!='results'}))

def composition():
    start=time.perf_counter(); cases=refs=actrefs=0
    for m in (0,1,2):
        g,h,mt=tables(4,m); pm=[x*x for x in walsh(mt)]; im=sum(infl(mt)); muM=R(sum(mt),len(mt))
        for label in range(16):
            cutoff(start)
            qt=[1 if label>>j&1 else -1 for j in range(4)]
            pq=[x*x for x in walsh(qt)]; iq=sum(infl(qt)); muq=R(sum(qt),4)
            tt=[qt[j&3]*mt[j>>2] for j in range(4*len(mt))]
            pg=[x*x for x in walsh(tt)]; ig=sum(infl(tt)); mu=muq*muM
            require(ig==iq+im and R(sum(tt),len(tt))==mu)
            require(all(pg[j]==pq[j&3]*pm[j>>2] for j in range(len(pg))))
            hg=ce(pg,pg); hq=ce(pq,pq); hm=ce(pm,pm)
            require(hg[0]<=hq[1]+hm[1] and hg[1]>=hq[0]+hm[0])
            activations={}; N=len(pg); c=1-mu
            for r in (1,2):
                cutoff(start); p=R(1,1<<r)
                ft=[tt[j&(N-1)] if j//N==0 else 1 for j in range(N*(1<<r))]
                pf=[x*x for x in walsh(ft)]
                require(sum(infl(ft))==p*(iq+im+r*c))
                require(all(pf[j]==((1-p*c)**2 if not j else (p*p*c*c if not j%N else p*p*pg[j%N])) for j in range(len(pf))))
                for T in range(1,N): require(sum(pf[T+U*N] for U in range(1<<r))==p*pg[T])
                activations[r]=(p,pf)
            for mode in range(3):
                cutoff(start)
                rq=pq if mode==0 else ([R(1,4)]*4 if mode==1 else [R(j+1,10) for j in range(4)])
                rg=[rq[j&3]*pm[j>>2] for j in range(len(pg))]
                require(sum(rg)==1)
                for j,x in enumerate(pg):
                    if x: require(rg[j]/x==rq[j&3]/pq[j&3])
                cq=ce(pq,rq); cg=ce(pg,rg)
                require(cg[1]<cq[0]+R(17,8)*im)
                r0=[mu*mu]+[(1-mu*mu)*x/(1-rg[0]) for x in rg[1:]]
                require(sum(r0)==1)
                c0=ce(pg,r0)
                require(r0==rg or c0[1]<=cg[0])
                refs+=1
                for r in (1,2):
                    cutoff(start); p,pf=activations[r]
                    qf=[]
                    for j in range(len(pf)):
                        U=j//N; T=j%N
                        qf.append((1-p*c)**2 if not U and not T else (p*p*c*c if not T else p*p*r0[T]))
                    require(sum(qf)==1)
                    # Actual spectrum formula was verified for every U once above;
                    # this exact nonempty-row ratio therefore holds for every U.
                    for T in range(1,N):
                        if pg[T]: require(pf[T]/qf[T]==pg[T]/r0[T])
                    cf=ce(pf,qf)
                    require(cf[1]<p*cq[0]+R(17,8)*p*im+6*r*p*c)
                    actrefs+=1
            cases+=1
    require((cases,refs,actrefs)==(48,144,288))
    out=dict(status='PASS',cases=cases,tensor_reference_cases=refs,activation_reference_cases=actrefs,assertions=COUNT,seconds=time.perf_counter()-start,arithmetic='exact Fraction FWHT/edges and likelihood ratios; outward 32-term atanh log intervals rounded to 2^-90')
    save('COMPOSITION_RESULTS.json',out); print(json.dumps(out))

if __name__=='__main__':
    {'compressed':compressed,'composition':composition}[sys.argv[1]]()
